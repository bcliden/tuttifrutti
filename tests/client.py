import io
from base64 import b64decode, b64encode
from pathlib import Path
from signal import SIG_DFL, SIGINT, signal
from typing import Any

import zmq
from PIL import Image as im
from PIL.Image import Image

"""
Tests to write...
- invalid hex colors values
- valid hex colors
    - # prefixed
    - non-# prefixed
    - mixed prefices
- missing one color/property
"""

# assuming we're at the project root
# test_image = Path.cwd() / "tests" / "last_recieved_test_image.png"
test_image = Path.cwd() / "tests" / "good_dog.png"


def main() -> None:
    # maybe use argparser or something for host, port, etc

    host = "localhost"
    port = "8672"

    # please exit when someone presses ctrl+C
    signal(SIGINT, SIG_DFL)

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://{host}:{port}")

    print(f"reading image file: {test_image}")
    with open(test_image, "rb") as f:
        data = f.read()
        b64data = b64encode(data).decode("ascii")
        print(f"sending {str(b64data[0:10])}... image")
        socket.send_json({"image": b64data, "intensity": 1})

    response: Any = socket.recv_json()

    # print("recieved response: ", response)

    if response["status"] == "ok":
        img = response["image"]
        img_bytes = b64decode(img)

        parent_folder = Path(__file__).parent.resolve()
        with open(parent_folder / "last_recieved_test_image.png", "wb") as f:
            f.write(img_bytes)

        b = io.BytesIO(img_bytes)
        i: Image = im.open(b)
        i.show()
    elif response["status"] == "error":
        print(response)


if __name__ == "__main__":
    main()
