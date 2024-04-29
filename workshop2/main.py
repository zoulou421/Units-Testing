def add(a, b):
    if isinstance(a,str) or isinstance(b,str):
        return None #this will fail the test:test failure(test_add_two_letters method)
    return a + b
