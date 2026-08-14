

    #1. What is software testing?
        #Testing is checks wheather your program behaves as expected.

def add(a,b):
    return a+b
add(2,5)

#Insteaad of manually checking
print(add(2,3))

#You can create a test:
assert add(2,3)==5


    #2.What is a unit test?
"""     A Unit checks one small part of a program ,such as :
    -- One function
    -- One method
    -- One validation rule
    """
    
def is_valid_port(port):
    return 1 <= port <= 65535
is_valid_port(80)


    #3.Assertions
        #An assertion an expected result with the actual result..
assert 2+ 2 == 4
#More Examples

assert "admin" .upper()=="ADMIN"
assert len([1,2,3])==3
assert 5>2


    #4.Testing with unittest
        #Create a file named calculator.py
            #create test_calculator.py
            
            
    #5.Common unit test Assertions
"""     Assertion                Assertions
        assertEqual(a,b)         Values should be equal
        assertNotEqual(a,b)      Values should differ
        assertTrue(value)	     Value should be true
        assertFalse(value)	    Value should be false
        assertIn(a, b)	        a should exist inside b
        assertRaises()	        Code should raise an exception
        """
        
def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by Zero")
    return a/b

#Test
def test_divide_by_zero(self):
    with self.assertraises(ValueError):
        divide(10,0)
#
#
#
#
#