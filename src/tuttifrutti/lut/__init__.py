import logging
from importlib.resources import files
from typing import Optional

from PIL.ImageFilter import Color3DLUT
from pillow_lut import load_cube_file

logger = logging.getLogger(__name__)


luts: dict[str, Color3DLUT] = dict()


def get_lut(name: str) -> Optional[Color3DLUT]:
    if name in luts:
        logger.info("found %s LUT in cache", name)
        return luts[name]
    try:
        contents = files("tuttifrutti.lut").joinpath(f"{name}.cube").read_text()
        lut = load_cube_file(contents.splitlines())
        luts[name] = lut
        logger.info("loaded %s LUT from file", name)
    except FileNotFoundError:
        logger.warn("couldn't load LUT: %s", name)
        raise SystemError(f"Couldn't load filter named: {name}")
    return lut
