// Columbus Explorer - Physical World Geography
// Prototype 06K - Global Terrain Foundation
//
// The physical world remains separate from historical/political geography.
// This pass uses the supplied global terrain reference to establish broad
// terrain character: ice, tundra, mountains, forests, grasslands and deserts.
//
// The satellite reference is NOT rendered directly. Terrain is translated into
// the game's high-detail modern pixel-art language.

const WORLD_LAND = [
    [[-168,72],[-150,70],[-135,72],[-125,70],[-115,68],[-105,62],[-95,58],[-85,52],[-75,48],[-66,46],[-60,50],[-63,56],[-75,60],[-82,66],[-92,70],[-105,73],[-125,75],[-145,74],[-168,72]],
    [[-97,26],[-90,24],[-86,20],[-84,16],[-87,12],[-91,14],[-94,18],[-97,26]],
    [[-81,12],[-74,8],[-68,10],[-60,8],[-52,4],[-45,0],[-40,-8],[-35,-18],[-38,-28],[-44,-35],[-50,-42],[-58,-50],[-66,-55],[-72,-50],[-75,-40],[-77,-28],[-78,-15],[-80,-2],[-81,12]],
    [[-73,83],[-50,84],[-25,80],[-18,72],[-30,64],[-45,60],[-58,64],[-70,72],[-73,83]],
    [[-11,36],[-5,43],[3,43],[10,46],[18,45],[25,48],[35,55],[32,62],[22,64],[14,60],[7,58],[2,53],[-5,50],[-10,44],[-11,36]],
    [[5,58],[10,64],[18,70],[25,71],[30,66],[25,60],[18,57],[10,56],[5,58]],
    [[-17,15],[-10,22],[0,28],[12,32],[25,31],[35,30],[43,18],[50,8],[48,-5],[42,-15],[35,-25],[25,-34],[15,-35],[5,-30],[-2,-20],[-8,-5],[-12,8],[-17,15]],
    [[27,36],[35,42],[45,45],[55,50],[70,55],[85,58],[100,65],[120,62],[140,55],[150,45],[145,35],[135,30],[125,25],[120,18],[110,15],[100,8],[90,8],[82,15],[75,20],[68,25],[60,25],[52,30],[45,28],[38,32],[27,36]],
    [[68,25],[76,30],[84,27],[88,22],[86,16],[82,10],[76,8],[72,12],[70,18],[68,25]],
    [[95,20],[105,18],[112,12],[116,4],[110,-5],[103,-2],[98,6],[95,20]],
    [[130,33],[137,39],[145,43],[146,37],[140,32],[134,30],[130,33]],
    [[114,-21],[120,-16],[130,-12],[140,-14],[151,-25],[154,-35],[146,-39],[135,-36],[124,-34],[115,-28],[114,-21]],
    [[43,-12],[50,-16],[50,-24],[46,-26],[43,-20],[43,-12]]
];

const TERRAIN = {
    ice: [224, 226, 214],
    tundra: [146, 157, 126],
    highland: [105, 103, 88],
    mountain: [88, 82, 69],
    forest: [48, 91, 49],
    forestLight: [69, 112, 58],
    grass: [101, 128, 67],
    grassLight: [128, 145, 77],
    dryGrass: [157, 143, 76],
    desert: [194, 158, 91],
    desertLight: [213, 181, 112],
    tropical: [43, 107, 66],
    tropicalLight: [66, 132, 72]
};

function longitudeToWorldX(longitude) {
    return ((longitude + 180) / 360) * GAME_SETTINGS.world.width;
}

function latitudeToWorldY(latitude) {
    return ((90 - latitude) / 180) * GAME_SETTINGS.world.height;
}

function drawWorldGeography() {
    // Land is rendered in repeated tiles so the physical world remains
    // continuous across every world seam.
    for (let tileY = -1; tileY <= 1; tileY++) {
        for (let tileX = -1; tileX <= 1; tileX++) {
            drawLandTile(
                tileX * GAME_SETTINGS.world.width,
                tileY * GAME_SETTINGS.world.height
            );
        }
    }
}

function drawLandTile(offsetX, offsetY) {
    for (let i = 0; i < WORLD_LAND.length; i++) {
        drawLandPolygon(WORLD_LAND[i], offsetX, offsetY, i);
    }
}

function drawLandPolygon(polygon, offsetX, offsetY, index) {
    // Base terrain is deliberately muted. The detail marks carry the biome
    // information so the continents do not look like flat coloured blobs.
    fill(...GAME_SETTINGS.geography.landColor);
    stroke(...GAME_SETTINGS.geography.coastlineColor);
    strokeWeight(GAME_SETTINGS.geography.coastlineWeight);
    drawProjectedPolygon(polygon, offsetX, offsetY);

    drawTerrainDetail(polygon, offsetX, offsetY, index);
}

function drawProjectedPolygon(polygon, offsetX, offsetY) {
    beginShape();

    for (const coordinate of polygon) {
        const wx = longitudeToWorldX(coordinate[0]) + offsetX;
        const wy = latitudeToWorldY(coordinate[1]) + offsetY;
        const p = projectWorldPoint(wx, wy);
        vertex(Math.round(p.x), Math.round(p.y));
    }

    endShape(CLOSE);
}

function drawTerrainDetail(polygon, offsetX, offsetY, seed) {
    const xs = polygon.map(p => longitudeToWorldX(p[0]));
    const ys = polygon.map(p => latitudeToWorldY(p[1]));
    const minX = Math.min(...xs);
    const maxX = Math.max(...xs);
    const minY = Math.min(...ys);
    const maxY = Math.max(...ys);

    // Sampling stays intentionally modest for performance. Terrain is detail,
    // not a full-resolution texture simulation.
    const sampleCount = (maxX - minX) * (maxY - minY) > 30000 ? 105 : 28;
    let state = (seed + 7) * 92821;

    noStroke();

    for (let i = 0; i < sampleCount; i++) {
        state = seededRandom(state);
        const px = minX + state * (maxX - minX);
        state = seededRandom(state);
        const py = minY + state * (maxY - minY);

        if (!pointInPolygon(px, py, xs, ys)) continue;

        const longitude = worldXToLongitude(px);
        const latitude = worldYToLatitude(py);
        const terrain = classifyTerrain(longitude, latitude, px, py, seed);
        const p = projectWorldPoint(px + offsetX, py + offsetY);

        drawTerrainMark(p.x, p.y, terrain, px, py, seed);
    }
}

function classifyTerrain(longitude, latitude, x, y, seed) {
    const noiseA = terrainNoise(x, y, seed, 1);
    const noiseB = terrainNoise(x, y, seed + 19, 2);

    // Polar regions.
    if (Math.abs(latitude) > 70) return 'ice';
    if (Math.abs(latitude) > 60) return noiseA > 0.42 ? 'tundra' : 'highland';

    // Major desert belts, shaped by longitude so they roughly follow the
    // broad real-world distribution visible in the terrain reference.
    const sahara = longitude > -18 && longitude < 52 && latitude > 12 && latitude < 34;
    const arabia = longitude > 35 && longitude < 75 && latitude > 15 && latitude < 32;
    const centralAsia = longitude > 55 && longitude < 110 && latitude > 32 && latitude < 48;
    const australia = longitude > 112 && longitude < 150 && latitude > -32 && latitude < -15;
    const atacama = longitude > -78 && longitude < -68 && latitude > -30 && latitude < -5;

    if (sahara || arabia || centralAsia || australia || atacama) {
        return noiseB > 0.30 ? 'desert' : 'dryGrass';
    }

    // Tropical belt.
    if (Math.abs(latitude) < 18) {
        return noiseA > 0.32 ? 'tropical' : 'forest';
    }

    // Temperate forest/grass distribution.
    if (Math.abs(latitude) < 50) {
        if (noiseA > 0.66) return 'forest';
        if (noiseB > 0.55) return 'grassLight';
        return 'grass';
    }

    return noiseA > 0.55 ? 'highland' : 'tundra';
}

function drawTerrainMark(x, y, terrain, worldX, worldY, seed) {
    const jitter = terrainNoise(worldX, worldY, seed + 77, 3);

    if (terrain === 'ice') {
        fill(...TERRAIN.ice);
        rect(Math.round(x), Math.round(y), 7, 4);
        if (jitter > 0.55) {
            fill(246, 247, 235);
            rect(Math.round(x + 4), Math.round(y - 3), 4, 3);
        }
        return;
    }

    if (terrain === 'tundra') {
        fill(...TERRAIN.tundra);
        rect(Math.round(x), Math.round(y), 5, 3);
        if (jitter > 0.72) {
            rect(Math.round(x - 3), Math.round(y + 2), 3, 2);
        }
        return;
    }

    if (terrain === 'mountain' || terrain === 'highland') {
        fill(...TERRAIN[terrain]);
        triangle(
            Math.round(x), Math.round(y - 7),
            Math.round(x - 7), Math.round(y + 5),
            Math.round(x + 7), Math.round(y + 5)
        );

        if (terrain === 'mountain' && jitter > 0.48) {
            fill(147, 139, 113);
            rect(Math.round(x - 1), Math.round(y - 3), 3, 3);
        }
        return;
    }

    if (terrain === 'desert' || terrain === 'dryGrass') {
        fill(...TERRAIN[terrain]);
        rect(Math.round(x), Math.round(y), 6, 3);
        if (jitter > 0.62) {
            fill(...TERRAIN.desertLight);
            rect(Math.round(x + 3), Math.round(y + 3), 5, 2);
        }
        return;
    }

    if (terrain === 'forest' || terrain === 'tropical') {
        fill(...TERRAIN[terrain]);
        rect(Math.round(x - 1), Math.round(y), 3, 6);
        rect(Math.round(x - 4), Math.round(y + 3), 9, 3);
        if (jitter > 0.52) {
            fill(...TERRAIN[terrain + 'Light']);
            rect(Math.round(x + 2), Math.round(y - 2), 4, 3);
        }
        return;
    }

    if (terrain === 'grassLight') {
        fill(...TERRAIN.grassLight);
        rect(Math.round(x), Math.round(y), 5, 3);
        return;
    }

    fill(...TERRAIN.grass);
    rect(Math.round(x), Math.round(y), 4, 3);
}

function seededRandom(state) {
    state = (state * 16807) % 2147483647;
    return state / 2147483647;
}

function terrainNoise(x, y, seed, scale) {
    const value = Math.sin(
        x * (0.0021 * scale) +
        y * (0.0017 * scale) +
        seed * 13.731
    ) * 43758.5453;

    return value - Math.floor(value);
}

function worldXToLongitude(x) {
    return (x / GAME_SETTINGS.world.width) * 360 - 180;
}

function worldYToLatitude(y) {
    return 90 - (y / GAME_SETTINGS.world.height) * 180;
}

function pointInPolygon(x, y, xs, ys) {
    let inside = false;

    for (let i = 0, j = xs.length - 1; i < xs.length; j = i++) {
        const intersect =
            ((ys[i] > y) !== (ys[j] > y)) &&
            (x < (xs[j] - xs[i]) * (y - ys[i]) / (ys[j] - ys[i]) + xs[i]);

        if (intersect) inside = !inside;
    }

    return inside;
}
