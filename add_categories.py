from pathlib import Path
import json
import re


# ============================================================
# SETTINGS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "portfolio-data.json"


# ============================================================
# CATEGORY RULES
# ============================================================

CATEGORY_RULES = {

    "PHOTOGRAPHY": [
        "photography",
        "photo",
        "photos",
        "photographer",
        "stilllife",
        "portraitphotography",
        "streetphotography",
        "nikon",
        "camera",
        "photoshoot",
    ],

    "DRAWING": [
        "drawing",
        "draw",
        "sketch",
        "sketchbook",
        "doodle",
        "doodling",
        "pensketch",
        "pencilsketch",
        "pencil",
        "micron",
        "ink",
        "lineart",
        "drawingandsketching",
    ],

    "PAINTING": [
        "painting",
        "paint",
        "watercolor",
        "watercolour",
        "waterpainting",
        "acrylic",
        "acralyicpainting",
        "oilpastel",
        "colourpencil",
        "color",
        "colour",
        "canvaspainting",
    ],

    "DIGITAL ART": [
        "digital",
        "digitalart",
        "digitalartwork",
        "digitalartist",
        "digitaldrawing",
        "digitalpainting",
        "digitalillustration",
        "illustration",
        "illustrator",
        "photoshop",
        "adobe",
        "adobephotoshop",
        "adobeillustrator",
        "editing",
        "graphicdesign",
        "graphicposter",
        "posterart",
        "characterdesign",
    ],

    "3D / CGI": [
        "3d",
        "cgi",
        "unreal",
        "unrealengine",
        "blender",
        "render",
        "rendering",
        "photoscanning",
        "scanning",
        "environmentdesign",
    ],

    "VIDEO": [
        "video",
        "reel",
        "animation",
        "animated",
        "motion",
        "film",
    ],

    "DESIGN": [
        "design",
        "graphicdesign",
        "productdesign",
        "productsketch",
        "explodedview",
        "crosssection",
        "posterart",
        "graphicposter",
        "environmentdesign",
    ],

    "EXPERIMENTS": [
        "experiment",
        "experiments",
        "random",
        "creative",
        "creativity",
        "concept",
        "testing",
        "test",
        "process",
        "wip",
    ],
}


# ============================================================
# TEXT NORMALIZATION
# ============================================================

def normalize_text(text):

    if not text:
        return ""

    text = str(text).lower()

    # Remove # symbols
    text = text.replace("#", " ")

    # Remove punctuation
    text = re.sub(
        r"[^a-z0-9\s]+",
        " ",
        text
    )

    # Normalize whitespace
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# ============================================================
# GET SEARCH TEXT
# ============================================================

def get_post_text(post):

    parts = []

    caption = post.get(
        "caption",
        ""
    )

    parts.append(caption)


    hashtags = post.get(
        "hashtags",
        []
    )

    parts.extend(
        hashtags
    )


    # Also include media paths.
    # This can help identify video / 3D material.
    for media in post.get(
        "media",
        []
    ):

        parts.append(
            str(media)
        )


    return normalize_text(
        " ".join(parts)
    )


# ============================================================
# CATEGORY ONE POST
# ============================================================

def categorize_post(post):

    text = get_post_text(
        post
    )

    categories = []


    for category, keywords in CATEGORY_RULES.items():

        for keyword in keywords:

            keyword = normalize_text(
                keyword
            )

            if not keyword:
                continue


            # Word / phrase matching
            if keyword in text:

                categories.append(
                    category
                )

                break


    # --------------------------------------------------------
    # VIDEO DETECTION
    # --------------------------------------------------------

    for media in post.get(
        "media",
        []
    ):

        extension = (
            Path(str(media))
            .suffix
            .lower()
        )

        if extension in {
            ".mp4",
            ".mov",
            ".m4v"
        }:

            if "VIDEO" not in categories:

                categories.append(
                    "VIDEO"
                )

            break


    # --------------------------------------------------------
    # FALLBACK
    # --------------------------------------------------------

    if not categories:

        categories.append(
            "EXPERIMENTS"
        )


    return categories


# ============================================================
# MAIN
# ============================================================

def main():

    print()
    print("=" * 65)
    print("ADDING PORTFOLIO CATEGORIES")
    print("=" * 65)
    print()


    if not DATA_FILE.exists():

        print(
            "ERROR: portfolio-data.json was not found."
        )

        print()
        print(
            "Expected:"
        )

        print(
            DATA_FILE
        )

        return


    # --------------------------------------------------------
    # READ JSON
    # --------------------------------------------------------

    print(
        "Reading:"
    )

    print(
        DATA_FILE
    )

    print()


    with open(
        DATA_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(
            file
        )


    # --------------------------------------------------------
    # SUPPORT BOTH JSON STRUCTURES
    # --------------------------------------------------------

    if isinstance(
        data,
        dict
    ):

        posts = data.get(
            "posts",
            []
        )

    elif isinstance(
        data,
        list
    ):

        posts = data

    else:

        print(
            "ERROR: Unexpected JSON structure."
        )

        return


    print(
        "Posts found:",
        len(posts)
    )

    print()


    # --------------------------------------------------------
    # CATEGORIZE
    # --------------------------------------------------------

    category_counts = {}


    for post in posts:

        categories = categorize_post(
            post
        )

        post["categories"] = categories


        for category in categories:

            category_counts[
                category
            ] = (
                category_counts.get(
                    category,
                    0
                ) + 1
            )


    # --------------------------------------------------------
    # WRITE JSON
    # --------------------------------------------------------

    with open(
        DATA_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


    # --------------------------------------------------------
    # REPORT
    # --------------------------------------------------------

    print("=" * 65)
    print("CATEGORIES ADDED")
    print("=" * 65)
    print()

    print(
        "Total posts:",
        len(posts)
    )

    print()

    print(
        "CATEGORY COUNTS"
    )

    print(
        "-" * 65
    )


    for category in sorted(
        category_counts
    ):

        print(
            f"{category:<20} "
            f"{category_counts[category]}"
        )


    print()

    print(
        "JSON updated:"
    )

    print(
        DATA_FILE
    )

    print()

    print(
        "Done."
    )

    print()


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    main()