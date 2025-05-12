import pytest

def test_btestample_one():
    print("Hiii")

def test_cample_two():
    a=10
    b=10
    assert a==b

@pytest.mark.skip(reason="sample")
def test_three():   #not considered whn not started with test
    a=20
    b=10
    assert a>b

@pytest.mark.regression
def test_ample_4():
    a="arun"
    b="aruns"
    assert a.__eq__(b)
    print("laks")

@pytest.mark.xfail(reason="expected to fail")
def test_sample5():
    a=10
    b=10
    assert a!=b

@pytest.mark.xfail(reason="expected to pass")
def test_sample6():
    a=10
    b=10
    assert a==b