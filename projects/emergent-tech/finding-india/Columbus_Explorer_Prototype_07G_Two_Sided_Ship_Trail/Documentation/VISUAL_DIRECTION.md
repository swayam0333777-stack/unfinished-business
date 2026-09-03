# COLUMBUS EXPLORER — VISUAL DIRECTION

## DECIDED DIRECTION

**High-detail modern pixel art**

This is the selected visual direction for the project.

## Target Feel

The game should feel like a polished historical exploration adventure, not a generic p5.js prototype.

### World

* Rich layered ocean
* Visible wave rhythm
* Coastal shallows and beaches
* Detailed coastlines
* Terrain variation
* Forest and mountain cues
* Atmospheric depth

### Ship

* Late-15th-century sailing-vessel influence
* Recognizable hull
* Multiple sails
* Masts and rigging
* Flag
* Wake
* Fixed 90-degree ship presentation with a 180-degree flip for left/right movement

### Interface

* Nautical chart influence
* Dark wood / parchment influence
* Compact panels
* Compass
* Voyage information
* Map/journal/crew/cargo navigation

## RULE

Visual detail should improve readability and immersion. Do not add effects merely to make the screen busy.

## REFERENCE

`VISUAL_REFERENCE.png` is the current visual concept reference. It establishes the general quality, mood and composition direction. It is not final production artwork.

### Ship Orientation Decision

- The ship uses a fixed upright visual orientation.
- It does not continuously rotate with movement direction.
- Left/right movement changes the ship orientation by exactly 180 degrees.
- Up/down movement does not rotate the ship.
- Diagonal movement does not introduce intermediate angles.



## Isometric Direction — Prototype 06A

The high-detail modern pixel-art direction now uses an isometric world presentation. The isometric projection is a rendering layer, not a replacement for the geographic world-coordinate system.

The target is a polished exploration-game presentation with readable depth, terrain height cues and detailed nautical assets.

## Ship Visual System — Prototype 06B

The selected ship artwork is the user-supplied high-detail pixel-art sprite sheet.

The production direction for the player ship is now an eight-direction authored sprite system. The game will select one of eight PNG sprites from movement direction rather than rotating a single sprite.

This is specifically chosen to fit the isometric presentation.

### Eight Directions

- North
- North-East
- East
- South-East
- South
- South-West
- West
- North-West

### Rendering Rule

Do not apply arbitrary rotation to the ship sprite. Select the authored directional sprite directly.

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


### Current Ocean Rule — Prototype 06J

The current production direction for the ocean is a dark continuous deep sea with a reduced number of pixel-art wave clusters. Coastal effects are temporarily removed for performance and should not be reintroduced unless explicitly requested.


## Global Terrain Reference — Prototype 06K

A global satellite terrain image has been added as `Documentation/TERRAIN_REFERENCE.png`.

It is used to guide the broad physical character of the world:

- continent-scale terrain distribution
- mountain systems
- deserts
- forests
- grasslands
- tropical regions
- tundra
- snow and ice

The satellite image itself must **not** be used as the final game texture. It is a geographic reference. The final rendering remains high-detail modern pixel art in isometric presentation.

Terrain should use irregular pixel clusters, stepped silhouettes and local variation rather than smooth biome borders.

## Prototype 06M — Base Ocean Texture Direction

The ocean base is now a pre-rendered pixel-art texture assembled from multiple water variations derived from the user's approved water references.

### Base Water Rules

- Use multiple shades of blue and blue-green rather than one flat blue.
- Use irregular pixel texture and broad natural variation.
- Tessellate through multiple variations so repetition is not obvious.
- Do not bake white wave lines into the base texture.
- Do not bake foam or glints into the base texture.
- Dynamic wave lines will be a separate lightweight animated layer added later.
- The base ocean must remain performant and should not return to expensive per-frame procedural noise.

### Base Ocean — Seamless Composition

The base ocean must read as one continuous pixel-art water field. Individual source-water tiles may provide local variation, but their rectangular boundaries must never be visually apparent.

### Ocean Seam Rule

The approved base water must read as a continuous water surface. Tile assets are texture sources, not visible map cells; their large-scale color gradients must be normalized so no box-like patches appear.

## Prototype 06O — Ocean Seam Correction

- Rebuilt the rendered base-water texture with wrap-aware edge blending so opposite texture edges meet continuously.
- Eliminated the remaining dark edge/seam artifacts that could appear when the ocean texture repeats with camera movement.
- The ocean remains a static base texture with no white waves, foam, glints, or per-frame procedural generation.

## Ocean Base — Prototype 06P

The world ocean uses a single 6000×4000 pixel-art base texture derived from the approved water reference. The base contains broad blue/teal variation and block-level pixel texture only; white wave crests, foam, glints and animated effects are intentionally separate future layers.


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
