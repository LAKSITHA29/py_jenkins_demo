import pytest

@pytest.mark.smoke
def test_one():
    print("haii")

@pytest.mark.regression
def test_two():
    print("hellopytest") 