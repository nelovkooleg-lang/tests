import pytest
from main2 import perimeter_area

@pytest.mark.parametrize(
    'a, b, expected',
    [
        (5, 7,(24, 35),
        (4, 4, (16, 16)),
        (2.5, 4.0, (13.0, 10.0)),
        (0, 5, (10, 0)),
    ],
)
def test_perimeter_area(a, b, expected):
    assert perimeter_area(a, b) == expected
