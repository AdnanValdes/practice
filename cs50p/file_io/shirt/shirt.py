import sys
from PIL import Image, ImageOps
from utils import count_args, is_valid_file


def main():
    if not valid_cli():
        sys.exit(1)

    overlay_image(sys.argv[1], "test.png")
    sys.exit(0)


def valid_cli() -> bool:
    return (
        count_args(2)
        and is_valid_file(sys.argv[1], ["jpeg", "jpg", "png"])
        and is_valid_file(sys.argv[2], ["jpeg", "jpg", "png"])
        and sys.argv[1][-4:] == sys.argv[2][-4:]
    )


def overlay_image(img_name: str, savefile: str) -> None:
    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Error: shirt.png not found")

    try:
        image = Image.open(img_name)
    except FileNotFoundError:
        sys.exit(f"Error: {img_name} not found")

    with image as img:
        img = ImageOps.fit(img, shirt.size)
        img.paste(shirt, shirt)
        img.save(sys.argv[2])


if __name__ == "__main__":
    main()
