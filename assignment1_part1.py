
def list_divide(numbers, divide=2):
    """
    list_divide function returns the number of elements in the 'numbers'
    list that are divisible by integer called 'divide'.
    """
    divisible = 0
    for n in numbers:
        if n % divide == 0:
            divisible += 1
    return divisible


def test_list_divide():
    """
    test_list_divide performs test on list_divide function
    If any of the tests fail, the function should raise the ListDivideException
    """
    try:
        assert list_divide([1,2,3,4,5]) == 2
        assert list_divide([2,4,6,8,10]) == 5
        assert list_divide([30, 54, 63,98, 100], divide=10) == 2
        assert list_divide([]) == 0
        assert list_divide([1,2,3,4,5], 1) == 5
    except:
        raise ListDivideException

class ListDivideException(Exception):
    """
    raise when the test fails
    """
    pass

if __name__ == "__main__":
    test_list_divide()