// Columbus Explorer
// Prototype 06J - Ocean Waves Only / Performance Pass
//
// Preserved systems:
// - Four-direction world wrapping
// - World-coordinate movement
// - Camera following
// - Physical world geography
// - Isometric projection
//
// New in this milestone:
// - The player ship uses the supplied pixel-art ship sprites.
// - Eight directional sprites are selected from movement direction.
// - The ship is never mathematically rotated.

let ship;
let cameraPosition;
let cameraIsoPosition;
let shipSprites = {};
let oceanBaseTexture;

// ------------------------------------------------------------
// ASSET LOADING
// ------------------------------------------------------------

function preload() {
    shipSprites.north = loadImage('assets/ships/ship_north.png');
    shipSprites.northeast = loadImage('assets/ships/ship_northeast.png');
    shipSprites.east = loadImage('assets/ships/ship_east.png');
    shipSprites.southeast = loadImage('assets/ships/ship_southeast.png');
    shipSprites.south = loadImage('assets/ships/ship_south.png');
    shipSprites.southwest = loadImage('assets/ships/ship_southwest.png');
    shipSprites.west = loadImage('assets/ships/ship_west.png');
    shipSprites.northwest = loadImage('assets/ships/ship_northwest.png');

    // The ocean is now a pre-rendered pixel-art texture assembled from
    // multiple base-water variations. Dynamic wave lines are intentionally
    // deferred to the next ocean pass.
    oceanBaseTexture = loadImage('assets/ocean/ocean_world_base.png');
}


// PROTOTYPE_07E_SHIP_TRAIL
// Visible, world-space ship trail. Uses the actual ship object and the
// existing isometric projection so it cannot disappear due to coordinate
// mismatch.

const shipTrail = [];
const SHIP_TRAIL_MAX = 44;
const SHIP_TRAIL_MIN_DISTANCE = 2.5;

function updateShipTrail() {
    const speed = getShipSpeed();

    if (speed < 0.02) {
        return;
    }

    const last = shipTrail.length
        ? shipTrail[shipTrail.length - 1]
        : null;

    if (
        !last ||
        Math.hypot(ship.x - last.x, ship.y - last.y) >=
            SHIP_TRAIL_MIN_DISTANCE
    ) {
        shipTrail.push({
            x: ship.x,
            y: ship.y
        });

        if (shipTrail.length > SHIP_TRAIL_MAX) {
            shipTrail.shift();
        }
    }
}

function drawShipTrail() {
    if (shipTrail.length < 2 || getShipSpeed() < 0.02) {
        return;
    }

    push();
    noStroke();
    rectMode(CENTER);

    const count = shipTrail.length;

    for (let i = 0; i < count - 1; i++) {
        const p = shipTrail[i];
        const next = shipTrail[i + 1];

        // Project BOTH trail points first. This is important for the
        // isometric game: world X/Y are not the same as screen X/Y.
        const a = projectWorldPoint(p.x, p.y);
        const b = projectWorldPoint(next.x, next.y);

        // Direction from the newer point toward the older point.
        let dx = a.x - b.x;
        let dy = a.y - b.y;
        const len = Math.hypot(dx, dy);

        if (len < 0.01) {
            continue;
        }

        dx /= len;
        dy /= len;

        // Screen-space perpendicular. This makes the trail expand
        // to BOTH sides of the ship regardless of sailing direction.
        const sideX = -dy;
        const sideY = dx;

        const t = i / (count - 1);

        // Much larger than the previous version.
        const halfWidth = 3.5 + t * 11;
        const alongLength = 5 + t * 12;
        const alpha = 60 + t * 125;

        // Main central trail.
        fill(218, 244, 238, alpha);

        rect(
            Math.round(a.x + dx * alongLength * 0.25),
            Math.round(a.y + dy * alongLength * 0.25 + 5),
            Math.round(alongLength),
            Math.round(halfWidth * 0.75)
        );

        // LEFT side of the wake.
        fill(183, 229, 220, Math.round(alpha * 0.82));

        rect(
            Math.round(a.x + sideX * halfWidth + dx * 2),
            Math.round(a.y + sideY * halfWidth + dy * 2 + 6),
            Math.round(5 + t * 9),
            Math.round(3 + t * 5)
        );

        // RIGHT side of the wake.
        rect(
            Math.round(a.x - sideX * halfWidth + dx * 2),
            Math.round(a.y - sideY * halfWidth + dy * 2 + 6),
            Math.round(5 + t * 9),
            Math.round(3 + t * 5)
        );

        // Second pair farther out gives the trail a broad V shape.
        if (i % 2 === 0) {
            const outer = halfWidth * 1.55;

            fill(165, 218, 211, Math.round(alpha * 0.58));

            rect(
                Math.round(a.x + sideX * outer),
                Math.round(a.y + sideY * outer + 7),
                Math.round(3 + t * 7),
                Math.round(2 + t * 4)
            );

            rect(
                Math.round(a.x - sideX * outer),
                Math.round(a.y - sideY * outer + 7),
                Math.round(3 + t * 7),
                Math.round(2 + t * 4)
            );
        }

        // Bright small broken pixels along the center.
        if (i % 3 === 0) {
            fill(235, 250, 246, Math.round(alpha * 0.75));

            rect(
                Math.round(a.x + dx * 3),
                Math.round(a.y + dy * 3 + 5),
                Math.round(4 + t * 7),
                Math.round(3 + t * 4)
            );
        }
    }

    pop();
}

function setup() {
    createCanvas(
        GAME_SETTINGS.canvas.width,
        GAME_SETTINGS.canvas.height
    );

    pixelDensity(1);
    noSmooth();

    ship = {
        x: GAME_SETTINGS.ship.startX,
        y: GAME_SETTINGS.ship.startY,
        direction: 'north',
        moving: false,

        // Cruise physics.
        velocityX: 0,
        velocityY: 0,
        targetVelocityX: 0,
        targetVelocityY: 0,

        // Visual sailing motion.
        bobTime: 0,
        wakePhase: 0,
        sailPhase: 0
    };

    cameraPosition = {
        x: ship.x,
        y: ship.y
    };

    cameraIsoPosition = worldToIsoRaw(
        ship.x,
        ship.y
    );
}

function draw() {
    updateShipTrail();
updateShip();
    updateCamera();

    drawIsometricOcean();
    drawWorldGeography();
    drawShipWake();
    drawShipTrail();
drawShip();
    drawHud();
}

// ------------------------------------------------------------
// MOVEMENT + CRUISE PHYSICS
// ------------------------------------------------------------

function updateShip() {
    const up =
        keyIsDown(UP_ARROW) || keyIsDown(87);

    const down =
        keyIsDown(DOWN_ARROW) || keyIsDown(83);

    const left =
        keyIsDown(LEFT_ARROW) || keyIsDown(65);

    const right =
        keyIsDown(RIGHT_ARROW) || keyIsDown(68);

    let screenX = 0;
    let screenY = 0;
    let direction = null;

    if (up && right) {
        screenX = 1;
        screenY = -1;
        direction = 'northeast';
    } else if (down && right) {
        screenX = 1;
        screenY = 1;
        direction = 'southeast';
    } else if (down && left) {
        screenX = -1;
        screenY = 1;
        direction = 'southwest';
    } else if (up && left) {
        screenX = -1;
        screenY = -1;
        direction = 'northwest';
    } else if (up) {
        screenY = -1;
        direction = 'north';
    } else if (right) {
        screenX = 1;
        direction = 'east';
    } else if (down) {
        screenY = 1;
        direction = 'south';
    } else if (left) {
        screenX = -1;
        direction = 'west';
    }

    ship.moving = direction !== null;

    // Keep the 8-direction control mapping exactly as established.
    // Only the acceleration model is new.
    if (ship.moving) {
        let worldX = screenX + screenY;
        let worldY = screenY - screenX;

        const magnitude = Math.hypot(worldX, worldY);

        if (magnitude > 0) {
            worldX /= magnitude;
            worldY /= magnitude;
        }

        ship.targetVelocityX =
            worldX * GAME_SETTINGS.ship.cruiseSpeed;

        ship.targetVelocityY =
            worldY * GAME_SETTINGS.ship.cruiseSpeed;

        ship.direction = direction;
    } else {
        ship.targetVelocityX = 0;
        ship.targetVelocityY = 0;
    }

    // Smoothly accelerate toward the desired cruise velocity.
    ship.velocityX = approach(
        ship.velocityX,
        ship.targetVelocityX,
        GAME_SETTINGS.ship.acceleration
    );

    ship.velocityY = approach(
        ship.velocityY,
        ship.targetVelocityY,
        GAME_SETTINGS.ship.acceleration
    );

    ship.x += ship.velocityX;
    ship.y += ship.velocityY;

    ship.x = wrapValue(
        ship.x,
        GAME_SETTINGS.world.width
    );

    ship.y = wrapValue(
        ship.y,
        GAME_SETTINGS.world.height
    );

    const speed = Math.hypot(
        ship.velocityX,
        ship.velocityY
    );

    // Visual motion only advances while the vessel is actually moving.
    if (speed > 0.02) {
        ship.bobTime +=
            GAME_SETTINGS.ship.bobSpeed;

        ship.wakePhase +=
            GAME_SETTINGS.ship.wakeSpeed *
            Math.min(speed / GAME_SETTINGS.ship.cruiseSpeed, 1);

        ship.sailPhase +=
            GAME_SETTINGS.ship.sailSpeed *
            Math.min(speed / GAME_SETTINGS.ship.cruiseSpeed, 1);
    }
}

function approach(current, target, amount) {
    if (Math.abs(target - current) <= amount) {
        return target;
    }

    return current + Math.sign(target - current) * amount;
}

function wrapValue(value, range) {
    return (
        (value % range) + range
    ) % range;
}

// ------------------------------------------------------------
// CAMERA
// ------------------------------------------------------------

function updateCamera() {
    // Track the camera in projected isometric space.
    // This prevents raw world X/Y following from introducing a
    // separate camera drift on the two projected axes.
    const target = worldToIsoRaw(
        ship.x,
        ship.y
    );

    cameraIsoPosition.x = lerp(
        cameraIsoPosition.x,
        target.x,
        GAME_SETTINGS.camera.followStrength
    );

    cameraIsoPosition.y = lerp(
        cameraIsoPosition.y,
        target.y,
        GAME_SETTINGS.camera.followStrength
    );

    // Keep the legacy world-space camera values synchronized for HUD/debug
    // systems that use the player's geographic coordinates.
    cameraPosition.x = ship.x;
    cameraPosition.y = ship.y;
}

// ------------------------------------------------------------
// ISOMETRIC PROJECTION
// ------------------------------------------------------------

function worldToIsoRaw(wx, wy) {
    return {
        x:
            wx *
            GAME_SETTINGS.isometric.scaleX -
            wy *
            GAME_SETTINGS.isometric.scaleX,

        y:
            wx *
            GAME_SETTINGS.isometric.scaleY +
            wy *
            GAME_SETTINGS.isometric.scaleY
    };
}

function worldToIso(wx, wy) {
    const projected = worldToIsoRaw(wx, wy);

    return {
        x:
            width / 2 +
            (projected.x - cameraIsoPosition.x),

        y:
            height / 2 +
            (projected.y - cameraIsoPosition.y)
    };
}

function projectWorldPoint(wx, wy) {
    return worldToIso(wx, wy);
}

// ------------------------------------------------------------
// OCEAN
// ------------------------------------------------------------

function drawIsometricOcean() {
    // Base-water pass only.
    //
    // The texture is a large pre-composed atlas built from multiple
    // pixel-art water variations derived from the approved water references.
    // It contains no white wave crests, foam, glints or animated effects.
    // Those will be added later as a lightweight dynamic overlay.
    drawOceanBaseTexture();
}

function drawOceanBaseTexture() {
    if (!oceanBaseTexture) {
        background(7, 34, 61);
        return;
    }

    const texW = oceanBaseTexture.width;
    const texH = oceanBaseTexture.height;

    // Anchor the texture to projected camera space so the water belongs to
    // the world rather than behaving like a fixed screen overlay.
    const offsetX = ((-cameraIsoPosition.x % texW) + texW) % texW;
    const offsetY = ((-cameraIsoPosition.y % texH) + texH) % texH;

    imageMode(CORNER);
    noTint();

    // Four draws are enough to cover the viewport while preserving seamless
    // wrapping of the pre-composed base texture.
    image(oceanBaseTexture, offsetX, offsetY);
    image(oceanBaseTexture, offsetX - texW, offsetY);
    image(oceanBaseTexture, offsetX, offsetY - texH);
    image(oceanBaseTexture, offsetX - texW, offsetY - texH);
}

// ------------------------------------------------------------
// SHIP CRUISE VISUALS
// ------------------------------------------------------------

function getShipSpeed() {
    return Math.hypot(
        ship.velocityX,
        ship.velocityY
    );
}

function drawShipWake() {
    const speed = getShipSpeed();

    if (speed < 0.12) {
        return;
    }

    const screen = projectWorldPoint(ship.x, ship.y);
    const intensity = Math.min(
        speed / GAME_SETTINGS.ship.cruiseSpeed,
        1
    );

    // Wake trails behind the vessel. It remains screen-space so the
    // authored ship sprites are never mathematically rotated.
    const wakeDirections = {
        north: [0, 1],
        northeast: [-0.707, 0.707],
        east: [-1, 0],
        southeast: [-0.707, -0.707],
        south: [0, -1],
        southwest: [0.707, -0.707],
        west: [1, 0],
        northwest: [0.707, 0.707]
    };

    const wake = wakeDirections[ship.direction] || [0, 1];
    const side = [-wake[1], wake[0]];
    const pulse = Math.sin(ship.wakePhase) * 1.5;

    push();
    noStroke();

    for (let i = 0; i < 5; i++) {
        const t = i / 5;
        const distance = 16 + i * (8 + intensity * 7);
        const spread = 2 + i * 1.8;
        const fade = (1 - t) * (0.35 + intensity * 0.65);

        const centerX = screen.x + wake[0] * distance;
        const centerY = screen.y + wake[1] * distance;

        const wobble = Math.sin(ship.wakePhase * 0.8 + i * 1.7) * 1.2;

        fill(
            GAME_SETTINGS.shipVisual.wake[0],
            GAME_SETTINGS.shipVisual.wake[1],
            GAME_SETTINGS.shipVisual.wake[2],
            35 + fade * 75
        );

        const size = Math.max(2, 4 + intensity * 3 - i * 0.45);

        rect(
            Math.round(centerX + side[0] * (spread + pulse) + wobble),
            Math.round(centerY + side[1] * (spread + pulse)),
            size,
            size
        );

        if (i > 1) {
            fill(
                GAME_SETTINGS.shipVisual.wake[0],
                GAME_SETTINGS.shipVisual.wake[1],
                GAME_SETTINGS.shipVisual.wake[2],
                24 + fade * 55
            );

            rect(
                Math.round(centerX - side[0] * spread - wobble),
                Math.round(centerY - side[1] * spread),
                Math.max(2, size - 1),
                Math.max(2, size - 1)
            );
        }
    }

    pop();
}

function drawShip() {
    const screen = projectWorldPoint(
        ship.x,
        ship.y
    );

    const sprite =
        shipSprites[ship.direction];

    if (!sprite) {
        return;
    }

    const speed = getShipSpeed();

    // Very subtle vertical bob. It is deliberately tiny so the ship
    // remains readable as a pixel-art game asset.
    const bob =
        speed > 0.05
            ? Math.sin(ship.bobTime) *
              GAME_SETTINGS.ship.bobAmount
            : 0;

    // Tiny sail-breathing motion: a very small horizontal scale change
    // makes the sail feel alive without rotating or replacing the sprite.
    const sailBreath =
        speed > 0.05
            ? 1 + Math.sin(ship.sailPhase) * GAME_SETTINGS.ship.sailFlutter
            : 1;

    push();

    imageMode(CENTER);

    image(
        sprite,
        Math.round(screen.x),
        Math.round(
            screen.y +
            GAME_SETTINGS.ship.spriteOffsetY +
            bob
        ),
        Math.round(GAME_SETTINGS.ship.spriteSize * sailBreath),
        GAME_SETTINGS.ship.spriteSize
    );

    pop();
}

// ------------------------------------------------------------
// HUD
// ------------------------------------------------------------

function drawHud() {
    drawCompass();
    drawPositionPanel();
    drawBottomBar();
}

function drawPanel(x, y, w, h) {
    fill(...GAME_SETTINGS.hud.panel);
    stroke(...GAME_SETTINGS.hud.panelEdge);
    strokeWeight(1);
    rect(x, y, w, h, 6);
    noStroke();
}

function drawCompass() {
    push();

    drawPanel(
        22,
        22,
        86,
        86
    );

    translate(65, 65);

    stroke(...GAME_SETTINGS.hud.panelEdge);
    strokeWeight(2);
    noFill();
    ellipse(0, 0, 52, 52);

    fill(...GAME_SETTINGS.hud.text);
    noStroke();

    triangle(
        0,
        -20,
        -5,
        7,
        0,
        3
    );

    triangle(
        0,
        20,
        5,
        -7,
        0,
        -3
    );

    textAlign(
        CENTER,
        CENTER
    );

    textSize(11);

    text('N', 0, -31);
    text('S', 0, 31);
    text('E', 31, 0);
    text('W', -31, 0);

    pop();
}

function drawPositionPanel() {
    drawPanel(
        width - 232,
        22,
        210,
        76,
        6
    );

    fill(...GAME_SETTINGS.hud.text);
    textAlign(LEFT, TOP);
    textSize(13);

    text(
        'VOYAGE',
        width - 214,
        34
    );

    fill(...GAME_SETTINGS.hud.muted);
    textSize(12);

    text(
        `Longitude  ${formatLongitude(ship.x)}`,
        width - 214,
        55
    );

    text(
        `Latitude   ${formatLatitude(ship.y)}`,
        width - 214,
        73
    );
}

function formatLongitude(value) {
    const normalized =
        value /
        GAME_SETTINGS.world.width;

    return `${(
        normalized * 360 - 180
    ).toFixed(1)}°`;
}

function formatLatitude(value) {
    const normalized =
        value /
        GAME_SETTINGS.world.height;

    return `${(
        90 - normalized * 180
    ).toFixed(1)}°`;
}

function drawBottomBar() {
    const h = 48;
    const y = height - h - 18;

    drawPanel(
        width / 2 - 250,
        y,
        500,
        h
    );

    fill(...GAME_SETTINGS.hud.text);
    textAlign(
        CENTER,
        CENTER
    );

    textSize(12);

    const labels = [
        'MAP',
        'JOURNAL',
        'CREW',
        'CARGO',
        'SHIP'
    ];

    const spacing = 100;

    for (
        let i = 0;
        i < labels.length;
        i++
    ) {
        text(
            labels[i],
            width / 2 - 200 + i * spacing,
            y + 24
        );
    }
}
