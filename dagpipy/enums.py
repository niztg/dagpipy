from enum import Enum

__all__ = (
    'ImageOptions'
    'Games'
)


class ImageOptions(Enum):
    wanted =            "wanted"
    tweet =             "tweet"
    quote =             "quote"
    thought_image =     "thoughtimage"
    obama =             "obama"
    bad =               "bad"
    hitler =            "hitler"
    angel =             "angel"
    trash =             "trash"
    satan =             "satan"
    sobel =             "sobel"
    hogend =            "hogend"
    paint =             "paint"
    night =             "night"
    polaroid =          "polaroid"
    solar =             "solar"
    edge =              "edge"
    evil =              "evil"
    blur =              "blur"
    invert =            "invert"
    pixel =             "pixel"
    ascii =             "ascii"
    deepfry =           "deepfry"
    sepia =             "sepia"
    wasted =            "wasted"
    triggered =         "triggered"
    jail =              "jail"
    gay =               "gay"
    colours =           "colors"
    colors =            "colors"
    rgb_data =          "rgbdata"
    whyareyougay =      "whyareyougay"
    five_guys_one_girl = "5g1g"

    def __str__(self):
        return self.value


class Games(Enum):
    whos_that_pokemon = "wtp"
    logo_guessing =     "logogame"
    roast =             "roast"
    yo_mama =           "yomama"
    pickupline =        "pickupline"
    waifu =             "waifu"
    joke =              "joke"

    def __str__(self):
        return self.value

