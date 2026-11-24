import pytest
from main3 import circle_area

@pytest.mark.parametrize(
    'r, expected_area, expected_lenght',
    [
        (5, 78.5, 31.4),
        (0, 0, 0),
        (2.5, 19.625, 15.7),
        (10, 314.0, 62,8),
    ],
)
def test_circle_area(r,expected_area, expected_lenght):
    area, lenght = circle_area(r)
    assert area == pytest.approx(expected_area, abs=1e-2)
    assert lenght == pytest.approx(expected_lenght, abs=1e-2)
