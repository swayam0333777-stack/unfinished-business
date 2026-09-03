# COLUMBUS EXPLORER — AI HANDOFF

> This document is intended to be given to another AI so it can understand and continue development of the project.

---

# 1. PROJECT

**Name:** Columbus Explorer

**Type:** Single-player browser-based exploration game

**Technology:** HTML + CSS + JavaScript + p5.js

**Development Environment:** VS Code

**Visual Style:** Pixel art

**Current Stage:** Prototype 06B — Isometric world + eight-direction ship sprites

---

# 2. GAME IN ONE PARAGRAPH

The player takes the role of Columbus during an era when European knowledge of the wider world is incomplete. The player sails through a largely unknown world, initially spawning in a highly zoomed-in area so their location is not obvious. They explore oceans and land, observe terrain and environmental clues, interact with local peoples, learn local names and geographical information, and construct their own map of the world. The player's map can be incorrect, and incorrect assumptions can lead to incorrect navigation. The ultimate objective is to find India, obtain spices, and successfully return to Europe.

---

# 3. CORE EXPERIENCE

The player should feel:

> "I genuinely don't know where I am."

The game should create uncertainty and discovery.

The player should have to combine:

* Observation
* Exploration
* Local knowledge
* Environmental clues
* Navigation
* Memory
* Personal deduction

The game should NOT feel like a conventional geography quiz.

---

# 4. CORE GAME LOOP

EXPLORE
→ OBSERVE
→ LAND
→ INTERACT
→ LEARN
→ GUESS
→ MAP
→ NAVIGATE
→ DISCOVER / GET LOST
→ FIND INDIA
→ GET SPICES
→ RETURN TO EUROPE
→ WIN / FAIL

---

# 5. MOST IMPORTANT MECHANIC

There are two separate realities:

### Actual World

The game knows the player's true location.

### Player's Map

The player only knows what they have discovered or inferred.

These must remain separate.

Example:

Actual location:
`Caribbean`

Player believes:
`Unknown island near Africa`

The player can therefore create an incorrect geographical understanding.

---

# 6. PLAYER MAP

The map should gradually fill as the player explores.

The player can:

* Record locations.
* Name places.
* Record observations.
* Mark directions.
* Record local information.
* Make guesses.

Wrong information can remain on the player's map and influence future navigation.

Do not simply tell the player "WRONG."

Let the consequences emerge through gameplay.

---

# 7. LOCAL PEOPLES

Local peoples are an important part of the game.

They should NOT simply function as NPCs that give the player the correct geographical answer.

They already understand their own environment.

They may provide:

* Local place names
* Directions
* Information about rivers
* Information about mountains
* Information about neighboring peoples
* Trade information
* Weather knowledge
* Stories
* Rumours
* Local resources

The player is the outsider.

---

# 8. HISTORICAL APPROACH

The setting represents an era when the entire world had not been mapped or standardized from the European perspective.

Do NOT automatically use modern country names, modern borders, or modern geopolitical terminology as though they existed in their current form.

The player should encounter:

* Local peoples
* Communities
* Regions
* Geographical features
* Local names
* Indigenous names
* Trade networks

The world should feel inhabited and understood by the people who live there.

---

# 9. EXPLORATION CLUES

Possible clues include:

* Terrain
* Vegetation
* Animals
* Climate
* Mountains
* Rivers
* Coastlines
* Architecture
* Crops
* Weather
* Local information
* Trade
* Settlement patterns

The player should combine clues rather than receiving direct answers.

---

# 10. OCEAN

The ocean is an active gameplay environment.

Potential systems:

* Wind
* Opposing wind
* Currents
* Storms
* Fog
* Rough seas
* Directional drift
* Visibility

These should affect navigation.

---

# 11. INDIA

Primary objective:

**Find India → obtain spices → return to Europe.**

Finding India should be a significant discovery.

The exact implementation of the spice system is still undecided.

---

# 12. FAILURE

The player can fail the expedition.

The intended thematic failure involves the player being punished / burned for failing.

Exact implementation is undecided.

---

# 13. CURRENT TECH

Use:

* VS Code
* JavaScript
* p5.js
* HTML
* CSS

The project should remain free to develop.

---

# 14. CURRENT FILES

```text
Columbus_Explorer/
├── PROJECT_MASTER.md
├── PROGRESS_LOG.md
└── AI_HANDOFF.md
```

Game code has been started. The current prototype is in `Game/`.

---

# 15. CURRENT STATUS

**PROTOTYPE 01**

A basic playable ocean prototype exists. The player can move a temporary ship around a bounded ocean world while the camera follows the ship.

The concept and major design principles remain unchanged.

---

# 16. CURRENT TASK

Continue from the existing p5.js prototype.

Prototype 01 currently contains:

1. Canvas
2. Ocean
3. Ship
4. Ship movement
5. Camera
6. Basic world boundaries

The next prototype should establish the first basic landmass/world system. Do not implement advanced systems yet.

---

# 17. IMPORTANT CONSTRAINTS

* Keep the current version single-player.
* Do not implement the future two-player/joystick idea unless explicitly requested.
* Do not turn the game into a modern geography quiz.
* Do not automatically reveal the player's true location.
* Do not assume modern country names are the correct historical names.
* Keep local peoples as knowledgeable inhabitants of their own world, not exposition machines.
* Maintain the distinction between the actual world and the player's understanding of it.
* Prioritize gameplay before visual polish.
* Do not introduce paid software/services unless explicitly approved.
* Update the project documentation when major decisions change.

---

# 18. HOW TO CONTINUE THIS PROJECT

Before making changes:

1. Read `PROJECT_MASTER.md`.
2. Read the latest entries in `PROGRESS_LOG.md`.
3. Read this file.
4. Inspect the current codebase.
5. Determine what is actually implemented rather than assuming it is implemented.
6. Continue from the current task.

Do not assume ideas listed in the Master Document are already implemented.

---

# 19. DOCUMENT STATUS

**Last Updated:** 20 August 2026

**Current Phase:** Pre-production

**Next Phase:** Technical setup and first prototype


## Latest World Continuity Decision

Prototype 01 now treats the world as an Earth-style map. East/west movement wraps continuously around the world instead of stopping at a rectangular boundary. Do not reintroduce a visible closed-world boundary unless explicitly requested. North/south remains limited by the polar extent of the map.

## Current Development State — Prototype 04

The prototype now includes a first physical world-geography layer using simplified land polygons. The world remains continuous in all four directions.

Do not add modern political borders to the physical world layer. Historical political geography must remain a separate system.

The current geography is deliberately a lightweight prototype foundation and should be refined before final navigation, discovery and player-map systems are implemented.

# 31A. CURRENT VISUAL DIRECTION

The selected visual direction is **high-detail modern pixel art**.

The game should feel like a polished historical exploration game rather than a basic p5.js prototype. Visual quality should be built as a coherent system:

* Rich layered ocean texture
* Detailed but readable coastlines
* Natural terrain variation
* Period-appropriate sailing ship artwork
* Pixel-art lighting and shadows
* Nautical/historical interface styling
* Consistent pixel scale and palette

The generated visual concept in `Documentation/VISUAL_REFERENCE.png` is the current style reference. It is a direction reference, not final production art.

Do not return to flat placeholder shapes unless temporarily required for debugging.

# 31B. WORLD CONTINUITY DECISION

The current gameplay decision is that the ship wraps in all four directions:

* East → West
* West → East
* North → South
* South → North

This must be preserved. The camera currently follows the wrapped position without a noticeable teleporting effect and should not be changed unless a real visual problem appears.

# 31C. CURRENT PROTOTYPE STATE

Prototype 05 focuses on visual foundation only. It improves the ocean, land rendering, ship presentation and HUD while preserving the established movement, camera and four-direction wrapping systems.

The physical geography polygons are still a simplified prototype and are not final historical cartography.
### Ship Orientation Rule

The player ship must not continuously rotate toward movement direction. It uses two fixed visual orientations: a 90-degree base presentation and the opposite 180-degree-flipped presentation. Left/right movement changes between these two states. Up/down and diagonal movement do not create additional rotation angles.

### Ship Orientation Decision

- The ship uses a fixed upright visual orientation.
- It does not continuously rotate with movement direction.
- Left/right movement changes the ship orientation by exactly 180 degrees.
- Up/down movement does not rotate the ship.
- Diagonal movement does not introduce intermediate angles.



### Ship Orientation — Established Decision

The ship must remain upright during vertical movement. It has only two visual orientations: the default upright orientation for right-facing movement and an exact 180-degree flip for left-facing movement. Up/down and diagonal movement must never create arbitrary rotation angles.


## PROTOTYPE 06A — ISOMETRIC FOUNDATION

The current visual architecture uses an isometric projection over the existing world-coordinate system. Do not replace the underlying world coordinates with screen coordinates. Movement, wrapping and geography remain world-space systems; rendering projects them into isometric screen space.

The ship orientation decision remains fixed: right-facing state and an exact 180-degree left-facing flip; up/down and diagonal movement do not introduce arbitrary rotation.


# CURRENT DEVELOPMENT STATE — PROTOTYPE 06B

## Visual Architecture

The game uses an isometric presentation layer over the underlying world-coordinate system. The world remains continuous and wraps in all four directions.

## Ship Asset Decision

The player ship uses the user-supplied high-detail pixel-art ship sprite sheet. The sheet has been separated into eight transparent PNG sprites.

The game selects a sprite based on movement direction:

* Up → North
* Up + Right → North-East
* Right → East
* Down + Right → South-East
* Down → South
* Down + Left → South-West
* Left → West
* Up + Left → North-West

The ship is NOT rotated mathematically. It uses authored directional sprites only.

When the player stops moving, the ship remains facing its last movement direction.

This eight-direction sprite decision supersedes the earlier fixed-orientation/180-degree ship decision because the user explicitly selected eight directional ship artwork for the isometric game.

# PROTOTYPE 06B1 — EAST SHIP ASSET UPDATE

The user supplied an edited East-facing ship PNG. It replaces the previous `Game/assets/ships/ship_east.png` asset.

Do not regenerate or mathematically rotate this asset. Continue using authored directional PNG sprites.

The remaining seven directional ship assets are unchanged.


# PROTOTYPE 06C — STABLE ISOMETRIC CAMERA

The camera now follows the ship in projected isometric space. Underlying world X/Y coordinates remain the source of truth for movement, geography, wrapping and navigation. Do not convert the world permanently into screen coordinates.

The eight-direction authored ship sprite system remains unchanged. The user's edited East-facing ship asset remains the active East sprite.

## Prototype 06D — Isometric Screen-Oriented Controls

The keyboard controls are screen/isometric oriented rather than raw world-axis oriented.

Established mapping:

- W / Up = North
- W + D = North-East
- D / Right = East
- S + D = South-East
- S / Down = South
- S + A = South-West
- A / Left = West
- W + A = North-West

The input direction is converted through the inverse isometric projection before updating the underlying world coordinates. This keeps the geographic world coordinate system intact while making player controls correspond to the visible isometric compass directions.


## Prototype 06E — Ocean Visual Foundation

The ocean rendering was redesigned to remove the visible isometric tile-board effect.

Established ocean rules:

* Ocean must visually read as one continuous sea.
* Do not add hard outlines around water tiles.
* Depth variation should be soft and irregular.
* Wave groups should be sparse and non-repeating.
* Small animated motion is acceptable, but the ocean must remain readable.
* Future coastal foam and shallow-water effects must integrate with the physical coastline.

The existing 8-direction ship controls and ship assets are unchanged.


## Current Milestone — Prototype 06F

The ocean was refined to remove sudden dark circular patches. The current visual direction uses continuous water, a shallow-water coastal band, beach transition and restrained shoreline foam. Do not reintroduce circular depth blobs. The 8-direction ship and isometric controls are established and should remain unchanged unless explicitly requested.

## Prototype 06G — Layered Ocean Depth and Wave Density

- Deep open ocean is now dark navy/blue rather than medium blue.
- Coastal water is represented by broad, overlapping depth layers around land.
- Water transitions continuously from deep ocean to mid water, coastal water, and shallow water.
- Removed the previous bright light-blue coastal outline treatment.
- Removed sudden dark circular/noise patches.
- Increased wave density with multiple scales of broken pixel-art wave crests.
- Added restrained animated highlights/glints.
- Ship, 8-direction sprites, isometric controls, wrapping, camera and geography data remain unchanged.
- The supplied coastal reference and the generated high-detail pixel-art ocean reference are now the visual targets for the ocean.



### Ocean Rendering Rule — Prototype 06H

Coastal water uses broken pixel clusters and stepped wave/foam variations. Continuous outline-like depth bands are not permitted. Water transitions from dark open ocean to lighter coastal water through irregular texture rather than borders.


## Prototype 06I — Ocean Performance Optimization

The pixelated coastal ocean remains visually layered, but the renderer was optimized after frame-rate degradation appeared.

- Replaced high-frequency per-frame Perlin-noise sampling in the ocean with deterministic hash sampling.
- Reduced the number of wave/glint samples while retaining multi-scale wave texture.
- Reduced coastal sampling density and shoreline foam sampling without reverting to continuous color borders.
- Reduced decorative land texture sampling.
- Preserved the 8-direction ship system, isometric controls, world wrapping and ocean visual direction.
- This is an implementation optimization only; the established visual target remains the layered, irregular, pixelated ocean.


## Prototype 06J — Current Ocean State

The coastal water effect is intentionally disabled after performance issues. Do not reintroduce coastal layers, foam clusters, or expensive shoreline sampling until requested. The current ocean should use only a dark continuous base with a restrained number of pixel-art waves and sparse glints.


# 13. GLOBAL TERRAIN REFERENCE — PROTOTYPE 06K

`Documentation/TERRAIN_REFERENCE.png` is the approved reference for broad physical terrain distribution.

Use it to guide:

* mountain systems
* deserts
* forests
* grasslands
* tropical vegetation
* tundra
* ice/snow

Do not render the satellite image directly. Translate the reference into high-detail modern pixel art.

The current implementation is a first procedural terrain pass over the existing prototype land polygons. It is not final geography.

## Prototype 06M — Ocean Base Texture

The current ocean foundation is a pre-rendered pixel-art water texture system. `Game/assets/ocean/ocean_world_base.png` is the large wrapped base texture assembled from multiple variations. The source atlas and water references are stored in `Documentation/`.

Do not add white wave crests, foam, glints or animated wave lines to the base texture. The next ocean milestone should add dynamic wave lines as a separate lightweight overlay only.

### Prototype 06N
- Base ocean texture replaced with a softly blended composition of the approved water variations.
- Do not reintroduce visible box/tile boundaries.
- Dynamic wave animation remains a separate future overlay.

### Base Water Correction
- `ocean_world_base.png` now uses normalized pixel texture detail from the water tile library over a continuous blue/teal color field.
- Do not compose visible rectangular source tiles directly into the world.

## Current Ocean State — Prototype 06O

The current base ocean uses a pre-rendered pixel-art texture with wrap-aware edge blending. The remaining dark seams from repeated texture boundaries were corrected in 06O. Do not reintroduce visible tile boundaries, hard rectangular patches, coastal border effects, or expensive per-frame procedural water generation. Dynamic white wave lines remain a separate future layer.

## 06P Ocean Handoff

The current ocean base asset is `Game/assets/ocean/ocean_world_base.png`, exactly 6000×4000 px. It is a pixel-art conversion of the approved water reference. Do not replace it with procedural ocean noise or photographic water; future work should add lightweight dynamic wave lines as a separate overlay.


# 21 AUGUST 2026 — PROTOTYPE 07A — SHIP CRUISE VISUALS

## Implemented

* Added subtle sail-breathing animation while cruising; the authored 8-direction ship sprites remain unrotated.
* Reworked the wake into a softer, speed-responsive trail with multiple staggered pixel clusters and gentle pulse variation.
* Preserved acceleration, deceleration, bobbing, 8-direction controls, world wrapping, camera and terrain.
* Cruise visuals remain intentionally lightweight for performance.


## Prototype 07B — Ship Trail
- Added a lightweight fading pixel-art trail behind the moving ship.
- Trail uses recent ship positions and does not change heading or movement controls.
- Existing acceleration, bobbing, sail animation and wake are preserved.


## Prototype 07E — Ship Trail Coordinate Fix
- Rebuilt the trail using the actual ship world coordinates and existing isometric projection.
- Increased trail dimensions and opacity for clearly visible water pixels.
- Trail is generated only while the ship is moving.
- Existing ship movement, heading, acceleration, wake and sail animation are preserved.


## Prototype 07G — Directional Ship Trail
- Reworked the trail width using screen-space perpendicular vectors.
- Trail now forms a broad two-sided V/wake instead of a single axis-aligned line.
- Works consistently for north, south, east, west and all diagonal directions.
- Existing 8-direction ship sprites, movement and cruise physics are unchanged.
