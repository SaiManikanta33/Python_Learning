

    #6. Testing with pytest
        #pip install pytest
    #Create test_calculator.py

from calculator import add , subtract
def test_add():
    assert add(2,3)==5
def test_subtract():
    assert subtract(5,2)==2
#pytest is popular because it require less boilerplate than unittest
#
#
#
#
#