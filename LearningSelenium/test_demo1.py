import pytest

@pytest.mark.smoke
def test_first_Program():
    msg= "Hello"
    assert msg == "Hi, test failed beacuse srtings do not match"

def test_SecondCreditCard():
    a= 4
    b= 6
    assert a+2 == 6, "Addtion do not match"

