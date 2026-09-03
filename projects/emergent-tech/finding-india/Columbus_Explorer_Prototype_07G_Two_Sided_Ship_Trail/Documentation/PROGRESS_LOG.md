# COLUMBUS EXPLORER — PROGRESS LOG

## Project Started

**20 August 2026**

---

# 20 AUGUST 2026 — PROJECT FOUNDATION

## Completed

* Created the project folder: `Columbus_Explorer`
* Decided to build the game as a browser-based experience.
* Decided to use VS Code as the development environment.
* Decided to use JavaScript + p5.js.
* Established that the first version will be single-player.
* Established the pixel-art visual direction.
* Established the core Columbus exploration concept.
* Established the "player does not know where they are" mechanic.
* Established player-created geographical naming.
* Established the concept of a player-created / potentially incorrect map.
* Established that incorrect geographical assumptions can affect navigation.
* Established interaction with local peoples as an important part of exploration.
* Established that local peoples should use their own names and geographical understanding rather than modern geopolitical labels.
* Established the idea of incomplete communication / language as a possible mechanic.
* Established India → spices → return to Europe as the primary objective.
* Established ocean hazards such as storms, wind and currents.
* Established the need for project documentation that can be handed to other AIs.

## Files Created

* `PROJECT_MASTER.md`
* `PROGRESS_LOG.md`
* `AI_HANDOFF.md`

## Current Status

**Pre-production / Prototype setup**

---

# 20 AUGUST 2026 — PROTOTYPE 01

## Completed

* Established the existing `Game/` and `ui/` implementation folders as the active project structure.
* Added shared gameplay constants to `Game/GAME_SETTINGS.js`.
* Connected `GAME_SETTINGS.js` to `Game/index.html` before `sketch.js`.
* Created a playable p5.js ocean prototype.
* Added a large ocean world measuring 6000 × 4000 world units.
* Added a temporary pixel-style ship marker.
* Added ship movement using WASD and Arrow Keys.
* Normalized diagonal movement so diagonal travel is not faster.
* Added north/south map limits for the top and bottom of the world map.
* Added east/west horizontal world wrapping so sailing does not end at an artificial map edge.
* Added a camera that follows the ship.
* Added a simple repeating ocean-wave pattern for visual orientation.
* Added temporary ship coordinates and controls as prototype debug information.
* Kept land, NPCs, navigation systems, hazards, map, journal and identification systems out of this prototype as required by the development order.

## Changed

* `Game/index.html` now loads `GAME_SETTINGS.js` before `sketch.js`.
* `Game/sketch.js` changed from the original title screen into Prototype 01.
* `Game/style.css` now preserves the pixelated canvas rendering.

## Added

* `GAME_SETTINGS` configuration object.
* Ocean world.
* Ship movement.
* Camera following.
* Basic world boundary.
* Temporary prototype ship graphic.

## Removed

* Original static "Project successfully started" screen.

## Bugs Found

* None identified during implementation.

## Bugs Fixed

* None required.

## Current State

**Prototype 01 is playable:** the player can move a temporary ship around a bounded ocean world while the camera follows the ship.

The world currently contains ocean only. This is intentional. No land, exploration, local peoples, map, journal, hazards or India systems have been implemented yet.

The map is treated as an Earth-style world map rather than a closed rectangular level: east/west travel wraps continuously around the globe. North/south travel is limited by the polar extent of the map.

## Next Task

**Prototype 02: establish the first basic world/landmass system without implementing advanced exploration mechanics.**

The next implementation should preserve the separation between the actual world and the player's understanding of it.

Before adding land, verify the world-wrap behavior and keep the Earth-style map continuous east/west.

## Important Decisions

* The project folder structure remains unchanged.
* `GAME_SETTINGS.js` is the shared location for prototype tuning values.
* The first playable prototype intentionally uses placeholder pixel-style art; visual polish is deferred.
* The world is treated as an Earth-style map rather than a closed rectangular level. East/west travel wraps continuously around the globe.
* The north/south limits represent the polar extent of the map.
* No artificial visible rectangular world boundary should be used for the Earth map.
* Advanced systems remain deferred until the basic world foundation is stable.

---

---

# 20 AUGUST 2026 — PROTOTYPE 03 — FULL WORLD WRAP

## Completed

* Changed north/south movement from hard map limits to continuous wrapping.
* The ship now wraps from the northern edge to the southern edge and vice versa.
* East/west wrapping remains active.
* The prototype world therefore has no artificial stopping edge in any direction.
* Updated project documentation to record full four-direction world wrapping as an established decision.

## Current State

**Prototype 03 is playable with continuous four-direction world wrapping.** The player can sail across any edge of the prototype world and continue from the opposite side.

This is intentionally a world-continuity foundation only. Land, actual geography, projection behavior, exploration discovery, map/journal systems and navigation consequences remain deferred.

## Important Decision

The game world should not behave like a closed rectangular level. For the current prototype, crossing the map boundary in **east, west, north or south** wraps the ship to the opposite side. This decision should be preserved when land and actual world geography are introduced.

## Next Task

**Prototype 04: establish the first basic world/landmass system while preserving continuous world wrapping.**

# FUTURE LOG ENTRIES

For each development session, record:

## Date

### Completed

*

### Changed

*

### Added

*

### Removed

*

### Bugs Found

*

### Bugs Fixed

*

### Current State

*

### Next Task

*

### Important Decisions

*

## Prototype 04 — Physical World Geography Foundation

### Implemented

- Added a physical geography rendering system.
- Added simplified continent and major-island polygons.
- Added longitude/latitude to game-world coordinate conversion.
- Added repeated geography tiles so land remains visible across all four world seams.
- Kept physical geography separate from political geography and player knowledge.

### Important Decision

Modern country borders are not part of the physical world layer.

The current polygons are a lightweight prototype representation. They are not final historical cartography and will be refined before final navigation and map systems.

### Current State

- Continuous ocean
- Ship movement
- Four-direction world wrapping
- Camera following
- Physical land geography

### Next Step

Refine the physical geography and then introduce the historical geography layer: period-appropriate regions, polities, settlements, ports, place names and trade centres.


# 21 AUGUST 2026 — PROTOTYPE 05 — HIGH-DETAIL PIXEL-ART VISUAL FOUNDATION

## Completed

* Selected high-detail modern pixel art as the project's visual direction.
* Reworked the ocean from a flat blue field into a layered pixel-art surface.
* Added multiple ocean texture scales and wave patterns.
* Reworked the ship into a detailed caravel-style pixel-art presentation.
* Added hull, deck, masts, sails, rigging, flag, shadow and wake details.
* Added ship orientation based on movement direction.
* Improved land rendering with beach, coastline, texture and terrain accents.
* Added a nautical-style HUD with compass, voyage information and navigation bar.
* Preserved four-direction world wrapping.
* Preserved the existing camera behavior.

## Changed

* `Game/GAME_SETTINGS.js` now contains the visual palette and visual tuning values.
* `Game/sketch.js` now contains the high-detail pixel-art presentation layer.
* `Game/WORLD_GEOGRAPHY.js` now adds visual treatment without changing the established prototype geography coordinates.
* `Game/style.css` now presents the game as a dark, polished game viewport.

## Important Decision

The project is no longer targeting a basic primitive-rendered prototype as its visual endpoint. The selected direction is high-detail modern pixel art.

## Current State

* Four-direction world wrapping: WORKING
* Camera follow: WORKING
* Physical geography: PRESENT, still prototype-level
* Ship: REWORKED visual foundation
* Ocean: REWORKED visual foundation
* HUD: FIRST visual foundation

## Deferred

* Final production ship sprite/animation set
* Accurate historical coastline data
* Detailed terrain biomes
* Historical political geography
* Settlements and ports
* Player discovery map

## Next Task

Review the new visual foundation in-game. If the visual direction is accepted, refine the physical geography and replace the simplified continent polygons with a more accurate historical-period physical geography layer.
## 21 AUGUST 2026 — SHIP ORIENTATION CORRECTION

### Changed

* Ship rotation is no longer based on the exact movement vector.
* The ship now has only two visual orientations.
* The base presentation remains at 90 degrees.
* Moving left flips the ship 180 degrees.
* Moving right flips the ship back 180 degrees.
* Moving up or down does not rotate the ship.
* Diagonal movement does not introduce arbitrary ship rotation.

### Design Decision

The ship should read as a controlled sailing-vessel sprite rather than continuously rotating toward every movement vector. This decision is part of the visual direction and should be preserved unless explicitly changed.

### Ship Orientation Decision

- The ship uses a fixed upright visual orientation.
- It does not continuously rotate with movement direction.
- Left/right movement changes the ship orientation by exactly 180 degrees.
- Up/down movement does not rotate the ship.
- Diagonal movement does not introduce intermediate angles.



## Prototype 05C — Ship Orientation Correction

### Fixed

- Corrected the ship's base orientation so the vessel remains upright.
- Right movement uses the default upright orientation.
- Left movement flips the ship exactly 180 degrees.
- Up/down movement does not change ship orientation.
- Diagonal movement does not introduce additional rotation.


# 21 AUGUST 2026 — PROTOTYPE 06A — ISOMETRIC WORLD FOUNDATION

## Completed

* Converted the world rendering from flat 2D presentation to an isometric projection.
* Kept the underlying world coordinates unchanged.
* Kept four-direction world wrapping unchanged.
* Converted the ocean into an isometric tile surface.
* Converted physical land polygons to the isometric projection.
* Kept the ship controlled by fixed orientation states rather than continuous rotation.
* Kept the existing HUD in screen space so it remains readable.

## Important Decision

The game uses an isometric presentation layer over the underlying world-coordinate system. Geography, navigation and wrapping continue to operate in world coordinates and are projected to the screen only for rendering.

## Current State

* Isometric world projection: IMPLEMENTED
* Four-direction wrapping: PRESERVED
* Camera follow: PRESERVED
* Ship movement: PRESERVED
* Ship orientation: PRESERVED
* Physical geography: PRESENT, prototype-level

## Next Task

Evaluate the isometric presentation in-game before adding detailed isometric terrain, ports, settlements or historical geography.

# 21 AUGUST 2026 — PROTOTYPE 06B — EIGHT-DIRECTION SHIP SPRITE SYSTEM

## Completed

* Adopted the user-supplied pixel-art ship sprite sheet as the game's ship artwork.
* Extracted eight transparent ship sprites from the supplied sheet.
* Added the eight ship directions:
  * North
  * North-East
  * East
  * South-East
  * South
  * South-West
  * West
  * North-West
* Replaced the procedural placeholder caravel drawing with PNG sprite rendering.
* Ship direction is selected from the player's movement direction.
* The ship is no longer mathematically rotated.
* The ship retains its last direction when the player stops moving.
* Preserved the isometric world projection.
* Preserved four-direction world wrapping.

## Asset Structure

`Game/assets/ships/` contains the eight directional PNG sprites and the original supplied sprite sheet.

## Important Design Decision

The game now uses eight authored ship sprites rather than rotating a single ship image.

Movement direction determines which sprite is displayed. No arbitrary rotation angles are introduced.

## Direction Mapping

World movement is mapped as follows:

* Up → North
* Up + Right → North-East
* Right → East
* Down + Right → South-East
* Down → South
* Down + Left → South-West
* Left → West
* Up + Left → North-West

## Current State

* Isometric world projection: IMPLEMENTED
* Four-direction wrapping: WORKING
* Camera follow: PRESERVED
* Physical geography: PRESENT, prototype-level
* Eight-direction ship sprites: IMPLEMENTED
* Procedural ship artwork: REMOVED

## Next Task

Evaluate the supplied ship sprites in the isometric game and then refine their scale/position if necessary before continuing with detailed isometric terrain and historical geography.

## Prototype 06B1 — Updated East Ship Asset

### Asset Update

* Replaced `Game/assets/ships/ship_east.png` with the user's edited East-facing ship artwork.
* Kept the existing eight-direction ship system unchanged.
* Kept the other seven directional ship assets unchanged.
* Kept the isometric projection, movement, wrapping and camera systems unchanged.

### Direction Mapping

* Up → North
* Up + Right → North-East
* Right → East (updated user-edited asset)
* Down + Right → South-East
* Down → South
* Down + Left → South-West
* Left → West
* Up + Left → North-West

# 21 AUGUST 2026 — PROTOTYPE 06C — STABLE ISOMETRIC CAMERA

## Completed

* Changed the isometric camera to track the projected isometric position rather than independently following raw world X/Y screen offsets.
* Kept the underlying world coordinates unchanged.
* Kept the physical geography unchanged.
* Kept four-direction world wrapping unchanged.
* Kept the eight authored ship sprites unchanged.
* Kept the user's edited East ship asset unchanged.

## Important Decision

The isometric camera is a presentation layer. It must not alter the underlying geographic coordinate system.

The ship remains centered through the isometric projection, while camera following is calculated in projected space.

## Current State

* Isometric projection: IMPLEMENTED
* Stable projected camera follow: IMPLEMENTED
* Four-direction wrapping: PRESERVED
* Eight-direction ship sprites: PRESERVED
* User-edited East ship: PRESERVED

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


# 21 AUGUST 2026 — PROTOTYPE 06E — OCEAN VISUAL FOUNDATION

## Completed

* Reworked the isometric ocean rendering.
* Removed the visible diamond/tile-board appearance from the water.
* Kept the ocean as one continuous visual field.
* Added soft depth variation without hard tile boundaries.
* Added irregular isometric wave groups.
* Added subtle animated wave drift.
* Added occasional water glints for surface variation.
* Preserved the existing isometric projection and camera.
* Preserved the established screen-oriented movement controls.
* Preserved the eight-direction ship sprite system and user-edited East ship.

## Visual Direction

The ocean should read as a continuous, detailed pixel-art sea rather than a repeating isometric tile grid.

Wave patterns are intentionally irregular and sparse. They should provide motion and texture without becoming a repetitive checkerboard.

## Current State

* Isometric controls: WORKING
* Eight-direction ship: WORKING
* Stable isometric camera: WORKING
* Ocean: REWORKED for continuous visual treatment
* Physical geography: PRESERVED

## Next Ocean Work

Further ocean refinement can include:

* Coastal shallow-water color transition
* Shore foam
* Larger wave bands in stormy conditions
* Current/wind effects
* Weather-dependent sea states
* Animated wake interaction around the ship


## Prototype 06F — Coastal Water & Ocean Cleanup

### Implemented

- Removed the previous noise-based dark circular ocean patches.
- Kept the ocean visually continuous rather than tiled.
- Added a shallow-water band around land.
- Added a subtle continuous shoreline-foam treatment.
- Preserved the existing isometric projection.
- Preserved the corrected isometric W/A/S/D controls.
- Preserved the 8-direction ship sprite system.

### Design Decision

Suddenly appearing dark circles are not part of the visual language and must not be reintroduced into the ocean. Ocean depth should be represented through broad, continuous tonal changes, while coastlines use shallow water, beach and restrained foam transitions.

### Next

Continue refining coastal geography and ocean behavior, including better beaches, islands, wake interaction and environmental water effects.

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



## Prototype 06H — Pixelated Coastal Water

### Ocean correction

- Removed continuous light/dark coastal border bands.
- Coastal depth is now represented by irregular, broken pixel clusters.
- Water becomes progressively lighter toward land without forming clean outlines.
- Added stepped vertical variation to coastal wave clusters to create a hand-pixelled shoreline rhythm.
- Added broken foam pixels directly at the shore.
- Increased wave density using multiple scales of pixel wave fragments.
- Kept the deep open ocean dark and continuous.
- Preserved ship, 8-direction controls, isometric projection, camera and world wrapping.

### Visual rule

The ocean should read as textured water with natural depth variation, not as concentric coloured borders around land.


## Prototype 06I — Ocean Performance Optimization

The pixelated coastal ocean remains visually layered, but the renderer was optimized after frame-rate degradation appeared.

- Replaced high-frequency per-frame Perlin-noise sampling in the ocean with deterministic hash sampling.
- Reduced the number of wave/glint samples while retaining multi-scale wave texture.
- Reduced coastal sampling density and shoreline foam sampling without reverting to continuous color borders.
- Reduced decorative land texture sampling.
- Preserved the 8-direction ship system, isometric controls, world wrapping and ocean visual direction.
- This is an implementation optimization only; the established visual target remains the layered, irregular, pixelated ocean.


# 21 AUGUST 2026 — PROTOTYPE 06J — OCEAN WAVES ONLY

## Implemented

* Removed the coastal water effect entirely for the current performance pass.
* Removed coastal layer rendering, shoreline pixel clusters and coastal foam.
* Kept the ocean as a continuous deep-water field with pixel-art waves.
* Reduced overall wave density to improve frame rate.
* Reduced secondary wave and glint frequency.
* Preserved the dark deep-ocean color direction.
* Preserved the eight-direction ship, isometric controls, camera and world wrapping.

## Current Ocean Direction

For now the ocean is intentionally simple: deep ocean plus restrained pixel-art wave texture. Coastal water effects are deferred until the base ocean performance is stable.

# 21 AUGUST 2026 — PROTOTYPE 06K — GLOBAL TERRAIN FOUNDATION

## Completed

* Added the supplied global satellite terrain map as the physical-terrain reference.
* Established broad terrain character for the world: ice, tundra, highlands, mountains, forests, grasslands, dry grasslands, deserts and tropical vegetation.
* Added latitude-aware biome distribution with longitude-aware regional adjustments for major desert belts and tropical regions.
* Added pixel-art terrain marks rather than flat biome colour fills.
* Added stylized mountain, forest, desert, ice and vegetation details while preserving the existing physical land polygons.
* Added `Documentation/TERRAIN_REFERENCE.png` as the project's terrain reference asset.
* Kept the terrain reference separate from political geography and the player's discovered map.

## Important Decision

The supplied satellite map is a **terrain reference**, not a texture to be displayed directly in the game.

The final game should translate its broad geographic information into the established high-detail modern pixel-art/isometric style.

Terrain should communicate:

* Major mountain systems
* Desert regions
* Forest regions
* Grasslands
* Tropical regions
* Tundra
* Ice/snow
* Broad climatic differences

Terrain transitions should remain irregular and pixel-art based rather than appearing as smooth coloured bands.

## Current State

* Four-direction world wrapping: WORKING
* Isometric movement: WORKING
* 8-direction ship sprites: WORKING
* Ocean: simplified wave-only performance version
* Physical geography: prototype polygons with new global terrain foundation
* Terrain biomes: FIRST PASS

## Deferred

* Accurate historical-period coastlines
* Detailed mountain-range geometry
* Rivers and lakes
* Individual biome boundaries
* Forest clusters at production density
* Settlements and ports
* Historical political geography
* Player discovery map

# 21 AUGUST 2026 — PROTOTYPE 06M — PIXEL-ART BASE WATER

## Implemented

* Replaced the procedural ocean background with a pre-rendered pixel-art base-water system.
* Added 24 source water variations derived from the approved water references and organized as Deep, Tropical/Clear, Shallow/Light and Mixed/Transition groups.
* Built four randomized composite ocean textures from those variations to reduce obvious repetition when tessellated across the world.
* Built a larger wrapped `ocean_world_base.png` texture from the four composites for efficient rendering.
* The base water contains multiple blue/teal shades and natural pixel texture, but intentionally contains **no white wave crests, foam, animated glints or dynamic wave lines**.
* Dynamic wave lines are explicitly deferred to the next ocean pass.
* Preserved the 8-direction ship, isometric controls, world wrapping, camera and global terrain.

## Performance Decision

The base ocean is rendered from a pre-composed image instead of generating water texture procedurally every frame. This keeps the visual texture rich while avoiding the lag caused by the earlier per-frame coastal/noise systems.

## Prototype 06N — Merged Base Ocean

- Reworked the base-water atlas composition so individual rectangular tile boundaries are no longer visible.
- Source water variations are softly blended across tile seams while retaining pixel-art texture.
- No dynamic waves, foam, glints, or coastal effects added in this pass.

## Prototype 06N — Seamless Base Water Correction

- Rebuilt the base ocean so source tile color blocks are removed from the final composition.
- Individual water tiles now contribute high-frequency pixel texture only; broad color variation comes from a continuous global field.
- No visible rectangular tile boundaries should remain.

## Prototype 06O — Ocean Seam Correction

- Corrected the remaining dark edge artifacts in the repeated base ocean texture.
- Applied wrap-aware edge blending to the base texture so repeated copies merge continuously at all four boundaries.
- Kept the 06N visual direction unchanged: pixel-art blue/teal water, no white waves yet, no foam, no glints, and no expensive per-frame ocean calculations.

# 21 AUGUST 2026 — PROTOTYPE 06P — PIXEL-STYLE WORLD OCEAN BASE

## Implemented

* Replaced the photographic-looking 6000×4000 ocean base with a pixel-art conversion of the approved ocean reference.
* The final world ocean texture is exactly **6000 × 4000 pixels**, matching the logical world dimensions.
* Reduced the source image to a lower-resolution pixel field, quantized the palette, then restored it to 6000×4000 with nearest-neighbor scaling to create visible pixel-art structure without adding white wave crests.
* Preserved multiple shades of blue/teal and broad water variation.
* Dynamic wave lines remain deferred and will be rendered as a separate lightweight animated layer.

## Preserved

* 8-direction ship sprites and edited East ship.
* Isometric movement controls.
* Four-direction world wrapping.
* Existing global terrain foundation.
* No foam, glints, coastal effects, or dynamic wave lines in the base texture.


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
