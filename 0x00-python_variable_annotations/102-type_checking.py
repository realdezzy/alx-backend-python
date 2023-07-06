from typing import Tuple, List, Any

def zoom_array(lst: Tuple, factor: int = 2) -> Tuple[Any]:
    zoomed_in: Tuple[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x: Tuple[Any] = zoom_array(array)

zoom_3x: Tuple[Any] = zoom_array(array, 3)
print(zoom_3x)