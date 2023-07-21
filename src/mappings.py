import math
from PIL import ImageColor


class ColorMapper:
    COLOR_MAP = {
        "#FF4500": 2,  # red
        "#FFA800": 3,  # orange T
        "#FFD635": 4,  # yellow T
        "#00A368": 6,  # dark green
        "#7EED56": 8,  # light green
        "#2450A4": 12,  # dark blue
        "#3690EA": 13,  # blue T
        "#51E9F4": 14,  # light blue
        "#811E9F": 18,  # dark purple
        "#B44AC0": 19,  # purple T
        "#FF99AA": 23,  # light pink
        "#9C6926": 25,  # brown
        "#000000": 27,  # black T
        "#898D90": 29,  # grey
        "#D4D7D9": 30,  # light grey
        "#FFFFFF": 31,  # white, T
    }

    # map of pixel color ids to verbose name (for debugging)
    NAME_MAP = {
        2: "Red",
        3: "Orange",
        4: "Yellow",
        6: "Green",
        8: "Light Green",
        12: "Dark Blue",
        13: "Blue",
        14: "Light Blue",
        18: "Dark Purple",
        19: "Purple",
        23: "Light Pink",
        25: "Brown",
        27: "Black",
        29: "Grey",
        30: "Light Grey",
        31: "White",
    }

    @staticmethod
    def rgb_to_hex(rgb: tuple):
        """Convert rgb tuple to hexadecimal string."""
        return ("#%02x%02x%02x" % rgb).upper()

    @staticmethod
    def color_id_to_name(color_id: int):
        """More verbose color indicator from a pixel color id."""
        if color_id in ColorMapper.NAME_MAP.keys():
            return "{} ({})".format(ColorMapper.NAME_MAP[color_id], str(color_id))
        return "Invalid Color ({})".format(str(color_id))

    @staticmethod
    def closest_color(
        target_rgb: tuple, rgb_colors_array: list, legacy_transparency: bool
    ):
        """Find the closest rgb color from palette to a target rgb color, as well as handling transparency"""

        # first check is for the alpha channel transparency in ex. png
        if target_rgb[3] == 0:
            return (69, 42, 0)
        # second check is for the legacy method of transparency using hex #452A00.
        if target_rgb[:3] == (69, 42, 0) and legacy_transparency:
            return (69, 42, 0)

        r, g, b = target_rgb[:3]
        color_diffs = []
        for color in rgb_colors_array:
            cr, cg, cb = color
            color_diff = math.sqrt((r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2)
            color_diffs.append((color_diff, color))
        return min(color_diffs)[1]

    @staticmethod
    def generate_rgb_colors_array():
        """Generate array of available rgb colors to be used"""
        return [
            ImageColor.getcolor(color_hex, "RGB")
            for color_hex in list(ColorMapper.COLOR_MAP.keys())
        ]
