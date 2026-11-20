import pytest
from main import square_params

@pytest.mark.parametrize(
    'side, expected',
    [
        (6, (24, 36)),
        (1, (4, 1)),
        (2.5, (10.0, 6.25))
        (0, (0, 0))
    ]
)
def test_square_params(side, expected):
    assert square_params(side) == expected
