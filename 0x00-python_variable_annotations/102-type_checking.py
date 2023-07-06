from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zoom array

    Args:
        lst (Tuple): tuple of elements
        factor (int, optional): int. Defaults to 2.

    Returns:
        List: list of zoomed elements
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x: List = zoom_array(array)

zoom_3x: List = zoom_array(array, 3)
