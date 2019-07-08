# def numbers_of_evens(numbers):
#     evens = 0
#     for num in numbers:
#         if num % 2 == 0:
#             evens += 1
#     return evens


# Tests
# def test_are_equal(actual, expeted):
#     assert expeted == actual, "Expected {0}, got {1}".format(expeted, actual)


def test_not_equal(a, b):
    assert a != b, 'Did not expect {0} but got {1}'.format(a, b)


def test_is_in(collection, item):
    assert item in collection, '{0} does not contain {1}'.format(
        collection, item)


def test_not_in(numbers, item):
    assert item not in numbers, '{0} is in the list{1}'.format(
        item, numbers)


def test_between(number, top, bottom):
    test = True
    if number in range(bottom, top):
        test = True
    else:
        test = False

        assert test, '{0} is not in range between {1} and {2}'.format(
            number, bottom, top)


# test_are_equal(numbers_of_evens([1, 2, 3, 4, 5]), 2)
test_not_equal(2, 1)
test_is_in([1, 2, 3, 4, 5], 2)
test_not_in([1, 2, 4, 5, 6], 10)
test_between(8, 10, 0)


print('test passed')
