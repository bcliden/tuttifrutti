from PIL.Image import Image
from pillow_lut import amplify_lut, transform_lut
from tuttifrutti.lut import get_lut


def vibrant_filter(image: Image, intensity: float) -> Image:
    """
    The image filtering for the "Vibrant" look
    """
    lut = get_lut("Teigen")
    if lut is None:
        raise SystemError("Lut 'Teigen' could not be found!")

    # double the lut effect on itself
    doubled = transform_lut(lut, lut)

    amplified = amplify_lut(doubled, intensity)
    image = image.filter(amplified)
    return image
