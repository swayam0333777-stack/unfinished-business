// Columbus Explorer - Shared game settings
// Prototype 06I - High-detail pixel-art visual foundation

const GAME_SETTINGS = {
    canvas: {
        width: 1200,
        height: 700
    },

    world: {
        width: 6000,
        height: 4000
    },

    ship: {
        startX: 3000,
        startY: 2000,
        // Cruise speed is reached gradually rather than instantly.
        cruiseSpeed: 4,
        acceleration: 0.14,
        bobSpeed: 0.11,
        bobAmount: 2,
        wakeSpeed: 0.28,
        sailSpeed: 0.16,
        sailFlutter: 0.018,
        size: 42,
        spriteSize: 180,
        spriteOffsetY: -14
    },

    camera: {
        followStrength: 1
    },

    isometric: {
        scaleX: 0.58,
        scaleY: 0.30,
        oceanTile: 120
    },

    ocean: {
        // Prototype 06L: the ocean base is a pre-rendered pixel-art texture
        // assembled from multiple approved water variations. No wave lines,
        // foam, coastal bands or glints are baked into the base.
        baseTexture: 'assets/ocean/ocean_world_base.png',
        tileSize: 240,
        baseColor: [7, 34, 61],

        // Reserved for the later dynamic wave-overlay pass.
        waveColor: [72, 143, 161],
        waveMidColor: [93, 174, 180],
        waveBrightColor: [151, 213, 207],
        glintColor: [222, 246, 226],
        glintAlpha: 72
    },

    geography: {
        landColor: [86, 117, 67],
        landLight: [111, 139, 79],
        landDark: [62, 88, 55],
        beachColor: [190, 164, 111],
        coastlineColor: [40, 59, 43],
        coastlineWeight: 4,
        shoreFoamWeight: 2
    },

    shipVisual: {
        shadow: [23, 39, 43],
        hullDark: [52, 32, 24],
        hullMid: [102, 57, 31],
        hullLight: [151, 87, 40],
        deck: [176, 128, 73],
        sail: [235, 221, 181],
        sailShadow: [195, 177, 132],
        mast: [67, 45, 29],
        rope: [48, 39, 28],
        flag: [143, 48, 39],
        wake: [180, 214, 211]
    },

    hud: {
        panel: [25, 31, 31, 220],
        panelEdge: [164, 132, 79, 230],
        text: [236, 222, 184],
        muted: [169, 163, 139]
    }
};
