from base64 import b64encode, b64decode
import io
import logging

from PIL import Image as im
from PIL.Image import Image

logger = logging.getLogger(__name__)


"""
Image to b64
"""

jpeg_options = {"optimize": True, "quality": 95}
png_options = {"optimize": True}


def encode(image: Image, format: str = "jpeg"):
    logger.info("encoding image with format %s", format)
    if format == "jpeg" or format == "jpg":
        return encode_jpeg(image)
    elif format == "png":
        return encode_png(image)
    else:
        raise ValueError("Unknown format")


def encode_jpeg(image: Image) -> str:
    img_bytes = io.BytesIO()
    image = image.convert("RGB")  # drop the alpha channel
    image.save(img_bytes, format="jpeg", **jpeg_options)
    return b64encode(img_bytes.getvalue()).decode("utf-8")


def encode_png(image: Image) -> str:
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="jpeg", **jpeg_options)
    return b64encode(img_bytes.getvalue()).decode("utf-8")


def decode(encoded_image: str) -> Image:
    img_bytes = b64decode(encoded_image)
    img_bio = io.BytesIO(img_bytes)
    image = im.open(img_bio)
    image.load()  # check to see if it's really usable
    return image
