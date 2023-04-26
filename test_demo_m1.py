import pytest
@pytest.mark.smoke
@pytest.mark.skip
def test_firstprogram():
    a = 5
    b = 8
    assert a+3 == b
def test_secondprogram():
    a = 25
    b = 5**2
    assert a == b


