#Postive expectation:you test for positive result.If not,something went wrong
def add(a, b):
    if isinstance(a,str) or isinstance(b,str):
        return None #this will fail the test:test failure(test_add_two_letters method)
    return a + b

#Negative expectation:you test for negative result.If not, something wentwrong
def add_v2(a, b):
    if isinstance(a,str) or isinstance(b,str):
    #if a is None or b is None:#equal to above
        return None #this will fail the test:test failure(test_add_two_letters method)
    return a + b

