# COLUMBUS EXPLORER

## Project Master Document

**Version:** 0.1
**Last Updated:** 21 August 2026
**Project Status:** Prototype 06K
**Current Development:** Isometric world, wave-only ocean, global terrain foundation, physical geography, ship movement, camera and continuous world wrapping


# CURRENT VISUAL TERRAIN REFERENCE

The supplied `Documentation/TERRAIN_REFERENCE.png` is the reference for broad global physical terrain. It informs continent-scale terrain character, mountain systems, deserts, forests, grasslands, tropical regions, tundra and ice.

The reference is **not rendered directly**. The game translates it into the established high-detail modern pixel-art/isometric style.

The current terrain implementation is a first procedural pass and does not yet represent final historical-period cartography.

---

# 1. PROJECT OVERVIEW

## One-Line Concept

A pixel-art single-player exploration game where the player takes the role of Columbus, sailing through an incompletely mapped world in search of India, using environmental clues, exploration, navigation, and interactions with local peoples to construct their own understanding of the world.

## Core Fantasy

The player should feel like an explorer who genuinely does not know where they are.

The game should create the feeling of:

> "I have no idea where I am. I need to figure this out."

The player is not given a modern world map or GPS.

They must gradually construct their own mental and physical map from what they observe, what they are told, and where they travel.

---

# 2. CURRENT PROJECT SCOPE

## CURRENT VERSION

The current project is a **single-player browser-based game**.

The player:

1. Starts from a European starting point or designated starting area.
2. Is placed into a zoomed-in section of the world.
3. Sails through the ocean.
4. Explores unknown areas.
5. Encounters land.
6. Studies terrain and environmental clues.
7. Interacts with people living in the region.
8. Learns local information, names, rumours, directions, and geographical knowledge.
9. Records information in their journal/map.
10. Attempts to determine where they are.
11. Eventually finds India.
12. Obtains spices.
13. Attempts to navigate back to Europe.
14. Wins if they successfully return with the spices.

## OUT OF CURRENT SCOPE

### Two-player / joystick version

A two-player version involving separate controls/joysticks is a future possibility but is NOT part of the current project.

Do not implement or design around multiplayer unless explicitly requested.

---

# 3. CORE GAME LOOP

The intended gameplay loop is:

EXPLORE
↓
OBSERVE
↓
LAND
↓
INTERACT
↓
LEARN
↓
GUESS
↓
MAP
↓
NAVIGATE
↓
GET LOST / DISCOVER
↓
FIND INDIA
↓
GET SPICES
↓
RETURN TO EUROPE
↓
WIN / FAIL

The player should constantly make decisions based on incomplete information.

---

# 4. THE CENTRAL GAME MECHANIC

The defining mechanic is the difference between:

**THE ACTUAL WORLD**

and

**THE PLAYER'S UNDERSTANDING OF THE WORLD.**

The game internally knows where the player actually is.

The player does not.

Example:

ACTUAL LOCATION:
Caribbean

PLAYER'S BELIEF:
Unknown island near Africa

The game should maintain these as separate systems.

A player can therefore create an incorrect mental map.

---

# 5. PLAYER-CREATED MAP

The player has a map that gradually fills as they explore.

The map does NOT simply reveal the correct modern world map.

Instead, it represents the player's current understanding of the world.

The player can:

* Record locations.
* Name places.
* Mark directions.
* Record observations.
* Add information learned from people.
* Make guesses.
* Potentially make incorrect assumptions.

## Incorrect Mapping

If the player incorrectly identifies a location, that incorrect information can influence future navigation.

Example:

Actual:

EUROPE → ATLANTIC → SOUTH AMERICA

Player believes:

EUROPE → ATLANTIC → AFRICA

The player then navigates according to their incorrect map.

This should create consequences rather than simply displaying:

"WRONG."

---

# 6. EXPLORATION

The world begins mostly unknown.

The player is deliberately shown a highly zoomed-in view.

The player should NOT immediately recognize their geographical location from the shape of a continent.

Exploration reveals information gradually.

Possible discoveries:

* Coastlines
* Rivers
* Mountains
* Forests
* Deserts
* Islands
* Settlements
* Villages
* Ports
* Animals
* Vegetation
* Weather patterns
* Ocean currents
* Other peoples

---

# 7. TERRAIN AS A CLUE

Terrain and environmental characteristics are one of the primary ways the player can identify where they are.

Possible clues include:

* Vegetation
* Climate
* Mountains
* Rivers
* Coastline shape
* Soil
* Animals
* Crops
* Architecture
* Settlement style
* Weather
* Ocean conditions

The game should avoid making these clues into a simple quiz.

The player should interpret several clues together.

Example:

Tropical vegetation
+
Large river
+
Mountain range
+
Local information about a neighboring region

may lead the player to form a geographical hypothesis.

---

# 8. LAND INTERACTION

Landing on land should be a major gameplay event.

The player should be able to physically explore at least some areas on land.

Possible land locations:

* Villages
* Settlements
* Trading areas
* Farms
* Fishing areas
* Ports
* Rivers
* Local landmarks

The player can interact with people living there.

---

# 9. PEOPLE AND LOCAL KNOWLEDGE

People encountered by the player should not simply function as "NPCs who know the correct answer."

They are people who already understand their own region and world.

They may know:

* Local geography
* Nearby rivers
* Mountains
* Coastlines
* Weather
* Trade routes
* Neighboring peoples
* Local resources
* Local place names
* Seasonal patterns
* Stories
* Rumours
* Directions

The player is the outsider.

The locals should generally know their own environment much better than the player.

---

# 10. HISTORICAL WORLDVIEW

The game takes place during the Age of Exploration, when European geographical knowledge of the wider world was incomplete.

The player should NOT experience the world as if modern countries, borders, names, and geopolitical divisions already existed in their current form.

Modern labels should not automatically be presented to the player.

Instead, the player should encounter:

* Local peoples
* Communities
* Regions
* Geographical features
* Local names
* Indigenous names
* Trade networks
* Cultural relationships

The game world should feel like a world that is already inhabited and understood by its own peoples, while remaining unfamiliar to the European explorer.

---

# 11. LOCAL NAMES

A location may have a name used by the people who live there.

The player may ask:

"What do you call this land?"

The answer may be a local name.

The player records that name in their journal/map.

The player may not immediately know how that location corresponds to their own geographical assumptions.

This reinforces the game's theme of incomplete knowledge.

---

# 12. LANGUAGE / COMMUNICATION

Communication should potentially involve uncertainty.

The player should not automatically understand every language.

Possible mechanics:

* Learned words
* Translation
* Gestures
* Misunderstandings
* Partial communication
* Repeated interactions
* Local names
* Interpreters
* Symbols

This system is currently a DESIGN IDEA and has not yet been implemented.

---

# 13. INFORMATION SYSTEM

Information gathered by the player can come from multiple sources.

### Observation

The player sees the environment.

### Exploration

The player physically discovers geographical features.

### Conversation

People provide local knowledge.

### Rumours

The player hears uncertain information.

### Trade

The player may acquire information through trading.

### Personal deduction

The player combines all available information to form a hypothesis.

Not all information needs to be perfectly reliable.

---

# 14. OCEAN GAMEPLAY

The ocean should not simply be empty travel space.

The player encounters hazards and environmental conditions.

Potential hazards:

* Storms
* Opposing winds
* Strong currents
* Fog
* Rough seas
* Directional drift
* Reduced visibility
* Other ocean events

These hazards should affect navigation and decision-making.

---

# 15. NAVIGATION

The player should have some form of navigation system, potentially including:

* Compass
* Wind direction
* Current direction
* Player-created map
* Landmarks
* Celestial/navigation clues
* Local directions
* Journal

The player should not have perfect navigation.

The goal is to make navigation a gameplay challenge.

---

# 16. JOURNAL

The player should have a journal containing information they have personally discovered.

Potential journal categories:

### Places

Locations encountered.

### People

People or communities encountered.

### Words

Local words or names learned.

### Terrain

Environmental observations.

### Directions

Information about where things may be.

### Rumours

Unverified information.

### Personal Notes

The player's own guesses.

The journal should represent the player's knowledge rather than simply displaying developer information.

---

# 17. PLAYER IDENTIFICATION SYSTEM

When the player believes they have discovered a location, they may be asked to identify/name it.

The player manually enters the name.

Example:

> "What do you think this place is?"

Player enters:

AFRICA

The game records the answer.

A wrong answer does not necessarily immediately produce a failure.

Instead, it can alter the player's map and future decisions.

---

# 18. PROGRESS / KNOWLEDGE METER

The player has a progress indicator that gradually fills as they explore and understand the world.

The exact visual and gameplay function of this meter is still being designed.

Possible interpretation:

**Knowledge / Discovery / King's Patience**

The final implementation is NOT YET DECIDED.

---

# 19. INDIA OBJECTIVE

India is the primary destination.

The player must discover India rather than simply being given its location.

Finding India should feel like a significant achievement.

Possible sequence:

DISCOVER INDIA
↓
INTERACT WITH LOCAL PEOPLE
↓
LEARN ABOUT SPICES
↓
FIND / ACQUIRE SPICES
↓
LOAD SHIP
↓
RETURN TO EUROPE

---

# 20. SPICE OBJECTIVE

The player must obtain spices in India.

Spices may eventually include examples such as:

* Pepper
* Cardamom
* Cinnamon
* Cloves

The exact spice system is not yet finalized.

The player must then return to Europe with the required objective completed.

---

# 21. WIN CONDITION

Primary win condition:

**Find India → acquire spices → successfully return to Europe.**

The exact victory sequence is not yet finalized.

---

# 22. LOSS CONDITION

The player can fail if they do not successfully complete the expedition.

A planned thematic failure is:

**The player is burned / punished for failure.**

The exact mechanics and presentation of the punishment are not yet finalized.

---

# 23. VISUAL DIRECTION

Primary visual style:

**Pixel art**

Desired qualities:

* Charming
* Discoverable
* Slightly mysterious
* Colourful
* Readable
* Game-like
* Historical exploration atmosphere

The world should feel like a pixel-art exploration game rather than a realistic historical simulation.

---

# 24. MAP VISUAL DIRECTION

The player's map can contrast with the main gameplay world.

Possible visual direction:

* Old nautical map
* Parchment
* Hand-drawn markings
* Player-written names
* Arrows
* Question marks
* Incorrect assumptions
* Crossed-out locations
* Rough coastlines

The map should feel like an artifact created by the player.

---

# 25. TECH STACK

Current planned technology:

* HTML
* CSS
* JavaScript
* p5.js
* VS Code

Development environment:

**VS Code**

The game is intended to run in a web browser.

Target platform for the first version:

**Desktop browser**

---

# 26. COST REQUIREMENT

The project should be developed using free tools.

No paid software or services are required for the MVP.

Potential hosting:

* GitHub Pages
* itch.io HTML5 hosting

Final hosting choice is not yet decided.

---

# 27. DEVELOPMENT PHILOSOPHY

The game should be developed incrementally.

Do not attempt to build the entire game at once.

Recommended development order:

1. Project setup
2. Ocean
3. Ship
4. Camera
5. Basic movement
6. World generation
7. Land
8. Terrain
9. Exploration
10. Player map
11. Land interaction
12. NPCs
13. Dialogue
14. Journal
15. Identification
16. Navigation consequences
17. Ocean hazards
18. India
19. Spices
20. Return journey
21. Win/loss
22. Visual polish
23. Audio
24. Optimization
25. Deployment

---

# 28. CURRENT STATUS

## Concept

STATUS: COMPLETE FOR INITIAL CONCEPT

The core concept has been established.

## Historical setting

STATUS: ESTABLISHED

The world should reflect incomplete European geographical knowledge and locally used names/knowledge rather than modern geopolitical labels.

## Single-player

STATUS: ESTABLISHED

Current MVP is single-player.

## Pixel-art

STATUS: ESTABLISHED

## Browser game

STATUS: ESTABLISHED

## Technology

STATUS: ESTABLISHED

VS Code + JavaScript + p5.js.

## Coding

STATUS: PROTOTYPE 01 IMPLEMENTED

## Art

STATUS: NOT STARTED

## Audio

STATUS: NOT STARTED

---

# 29. IMPORTANT DESIGN PRINCIPLES

1. The player should genuinely feel lost.
2. The player should not be given a modern GPS-like world map.
3. The player must construct their own understanding of the world.
4. Incorrect assumptions should have meaningful consequences.
5. Local peoples should possess their own knowledge and geographical understanding.
6. Local names should matter.
7. The world should feel inhabited before the player arrives.
8. Exploration should be rewarding even when the player does not immediately progress toward India.
9. Information should be incomplete rather than simply displayed as answers.
10. The game should feel like an exploration adventure, not a geography quiz.
11. Pixel art should remain readable and functional rather than being detailed purely for decoration.
12. The first version should prioritize gameplay over visual polish.

---

# 30. UNDECIDED SYSTEMS

The following still require design decisions:

* Exact historical date
* Exact starting location
* Exact world scale
* Exact map generation method
* Exact movement system
* Land movement
* NPC dialogue structure
* Language system
* Translation mechanics
* Exact cultures/regions represented
* Exact historical accuracy level
* Progress meter meaning
* Exact time system
* Exact compass mechanics
* Exact storm mechanics
* Exact spice mechanics
* Exact victory sequence
* Exact failure sequence
* Art production method
* Sound design
* Save system

These should be decided gradually rather than prematurely.

---

# 31. CURRENT NEXT STEP

The immediate next step is:

**Set up the basic p5.js project in VS Code.**

No major game systems should be implemented until the project structure is established.

---

# 32. DOCUMENTATION RULE

This document is the project's primary source of truth.

When an important design decision is made:

* Update this document.
* Mark whether the idea is PROPOSED, DECIDED, IMPLEMENTED, DEFERRED, or REJECTED.
* Do not allow future AI sessions to override DECIDED principles without explicit instruction.

The project should maintain a separate progress log for implementation history and a separate AI handoff document for transferring the project to another AI.


## WORLD MAP / EARTH CONTINUITY DECISION

The game world represents an Earth-style world map rather than a finite rectangular level. East/west travel must wrap continuously so the player can sail across the map boundary and continue from the opposite longitude. The world should not display an artificial rectangular edge. North/south travel follows the polar limits of the chosen map projection.

## Physical World Geography — Prototype 04

The game now has a first physical-geography layer using simplified continent and major-island polygons.

Physical geography is separate from historical political geography and from player knowledge.

The prototype does not use modern country borders as the world map.

The geography layer is intentionally simplified at this stage. It is a gameplay foundation, not final historical cartography. A more accurate physical-geography dataset will be introduced before final map art and navigation systems.

The continuous-world rule remains active: the physical geography is tiled across all four world seams so that the player can continue travelling indefinitely.


# VISUAL DIRECTION — DECIDED

The game's visual direction is **high-detail modern pixel art**.

The visual target is a polished historical exploration adventure with:

* Detailed pixel-art ocean
* Layered waves and foam
* Rich coastlines and terrain
* Period-appropriate ship presentation
* Atmospheric lighting and shadows
* Nautical UI elements
* A consistent restrained historical palette

Visual polish should not be achieved by adding arbitrary effects. All visual systems should share the same pixel scale, palette logic and historical tone.

The visual concept stored in `Documentation/VISUAL_REFERENCE.png` is the current reference for this direction.

# WORLD CONTINUITY — DECIDED

For gameplay, the world is continuous in all four directions. Crossing any edge wraps the player to the opposite side. This established decision must be preserved unless explicitly changed by the project owner.

# PROTOTYPE 05 — VISUAL FOUNDATION

The current prototype focuses on improving visual presentation while preserving established movement, camera and world-wrap behavior. The physical geography remains a simplified prototype layer and will be refined separately.

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



## Ocean Visual Rule

The ocean must read as a continuous natural body of water. Avoid isolated dark circular/noise patches that appear suddenly. Depth should be communicated with broad tonal variation and coastal shallow-water transitions.

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
