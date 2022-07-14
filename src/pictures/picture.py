from typing import Any, Dict

import cv2


class PictureLoader:
    """An object that represent user's picture."""

    def __init__(
            self,
            path: str,
            name: str,
            width: int = 400,
            height: int = 300
    ) -> None:
        self.path = path
        self.name = f"resized_{name}"
        self.width = width
        self.height = height

    def initiate_image(self) -> Any:
        """
        Read the image from the filepath.

        :return: an object that represents local picture.
        :rtype: Any

        :Example:
        >>> pic = PictureLoader("../../Pictures/arrow2.png", "arrow2.png")
        >>> png = pic.initiate_image()
        >>> type(png)
        <class 'Any'>
        """
        return cv2.imread(self.path)

    @staticmethod
    def get_dimensions(image: Any) -> Dict[str, int]:
        """
        Return an dictionary-like object with dimensions.

        :param image: an object that represent local picture.
        :type image: Any
        :return: an output with dimensions.
        :rtype: dict

        :Example:
        >>> pic = PictureLoader("../../Pictures/arrow2.png", "arrow2.png")
        >>> png = pic.initiate_image()
        >>> dimensions = pic.get_dimensions(png)
        >>> dimensions
        {'height': 999, 'width': 1308}
        """
        try:
            height, width, _ = image.shape

        except BaseException:
            output = {}
        else:
            output = {"height": height, "width": width}
        finally:
            return output

    def save_image(self, img: Any) -> None:
        """
        Save the modified pictures.

        :param img: an object that represent local picture.
        :type img: Any
        """
        cv2.imwrite(self.name, img)


class PictureResizer(PictureLoader):
    """An object that changes the resolution of given picture."""

    def is_resolution_same(self, image: Any) -> bool:
        """
        Return a boolean value if the given object already has the right
        resolution.

        :param image: an object that represent local picture.
        :type image: Any
        :return: True if the dimensions are the same, else False
        :rtype: bool

        :Example:
        >>> modif = PictureResizer("../../Pictures/arrow2.png", "arrow")
        >>> png = modif.initiate_image()
        >>> same_dimension = modif.is_resolution_same(png)
        >>> same_dimension
        False
        """
        return image.shape[:2] == (self.width, self.height)

    def resize_image(self, image: Any) -> bool:
        """
        Change the resolution of the given picture.

        :param image: an object that represent local picture.
        :type image: Any
        :return: a boolean value True if the resizing works, else False.
        :rtype: bool

        :Example:
        """
        try:
            resized = cv2.resize(
                image,
                (self.width, self.height),
                interpolation=cv2.INTER_NEAREST
            )

        except ValueError:
            output = False
        else:
            output = True
            cv2.imwrite(f"static/upload/{self.name}", resized)
        finally:
            return output


if __name__ == "__main__":
    import doctest
    doctest.testmod()
