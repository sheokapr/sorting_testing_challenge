#!python
import pytest
from code.quicksort import quick_sort
import random


'''TEST_CASE_1: Array of positive integers as input, quick_sort should sort this array in ascending order '''
@pytest.mark.parametrize(
    "items,expected",
    [
        ([2,1,9,0], [0,1,2,9]),  #Input array of positive integers, second array is the expected output
    ],
)
def test_quicksort_positive_int(items, expected):
    assert quick_sort(items)  == expected #input array is passed to quick_sort algorithm and output is compared with expected output given above



'''TEST_CASE_2: Empty array, quick_sort should return an empty array '''
@pytest.mark.parametrize(
    "items,expected",
    [
        ([], []),  #Input empty array, second array is the expected output
    ],
)
def test_quicksort_empty_list(items, expected):
    assert quick_sort(items)  == expected #input array is passed to quick_sort algorithm and output is compared with expected output given above



'''TEST_CASE_3: Array of repeated positive integers as input, quick_sort should sort this array in ascending order '''
@pytest.mark.parametrize(
    "items,expected",
    [
        ([2,1,9,0,2,9], [0,1,2,2,9,9]),  #Input array with repeated positive integers, second array is the expected output
    ],
)
def test_quicksort_repeated_int(items, expected):
    assert quick_sort(items)  == expected  #input array is passed to quick_sort algorithm and output is compared with expected output given above



'''TEST_CASE_4: Array of mix of positive and negative integers as input, quick_sort should sort this array in ascending order '''
@pytest.mark.parametrize(
    "items,expected",
    [
         ([2,-1,-9,0,9], [-9,-1,0,2,9]),  #Input array with mix of positive and negative integers
    ],
)
def test_quicksort_postive_negative_int(items, expected):
    assert quick_sort(items)  == expected  #input array is passed to quick_sort algorithm and output is compared with expected output given above



'''TEST_CASE_5: Array of only negative integers as input, quick_sort should sort this array in ascending order '''
@pytest.mark.parametrize(
    "items,expected",
    [
         ([-2,-1,-9,-6,-11], [-11,-9,-6,-2,-1]),  #Input array with all negative  integers, second array is the expected output
    ],
)
def test_quicksort_negative_int(items, expected):
    assert quick_sort(items)  == expected  #input array is passed to quick_sort algorithm and output is compared with expected output given above



'''TEST_CASE_6: Array of mix of floating points and integers as input, quick_sort should sort this array in ascending order '''
@pytest.mark.parametrize(
    "items,expected",
    [
        ([2.1,1.8,0.5,2,9], [0.5,1.8,2,2.1,9]),  #Input array with float and int mix
    ],
)
def test_quicksort_float_int_mixed(items, expected):
    assert quick_sort(items)  == expected #input array is passed to quick_sort algorithm and output is compared with expected output given above


'''TEST_CASE_7: Array of mix of floating points,positive and negative integers as input, quick_sort should sort this array in ascending order '''
@pytest.mark.parametrize(
    "items,expected",
    [
        ([2.1,-1.8,.5,2,-9,6], [-9,-1.8,.5,2,2.1,6]),  #Input array with positive/negative integers and float mix, second array is the expected output
    ],
)
def test_quicksort_float_int_negative_positive_mixed(items, expected):
    assert quick_sort(items)  == expected #input array is passed to quick_sort algorithm and output is compared with expected output given above



'''TEST_CASE_8: Array of characters as input, quick_sort should sort this array in ascending order '''
@pytest.mark.parametrize(
    "items,expected",
    [
        (['c','d','a','f'],['a','c','d','f']), #characters array as input, second array is the expected output
    ],
)
def test_quicksort_strings(items, expected):
    assert quick_sort(items)  == expected #input array is passed to quick_sort algorithm and output is compared with expected output given above



'''TEST_CASE_9: Array of characters with repeated elements as input, quick_sort should sort this array in ascending order '''
@pytest.mark.parametrize(
    "items,expected",
    [
        (['c','a','d','a','d','f'],['a','a','c','d','d','f']), #characters array with repeated elements as input, second array is the expected output
    ],
)
def test_quicksort_repeated_strings(items, expected):
    assert quick_sort(items)  == expected #input array is passed to quick_sort algorithm and output is compared with expected output given above



'''TEST_CASE_10: Array of words as input, quick_sort should sort this array in ascending order '''
@pytest.mark.parametrize(
    "items,expected",
    [
       (['apple','drum','arm','foil'],['apple','arm','drum','foil']), #first array is input, second array is expected output
    ],
)
def test_quicksort_strings_words(items, expected):
    assert quick_sort(items)  == expected #input array is passed to quick_sort algorithm and output is compared with expected output given above



'''TEST_CASE_11: Immutable Tuple test: This test takes in random tuple as input type generated by random function, 
number of elements in the array is defined by the range function and run them against sorting algorithm. 
As this Sorting Algortithm assumes input should be ONLY mutable object, since Tuple objects are immutable so this test should FAIL'''
@pytest.mark.xfail(raises=AttributeError) #As we expect an exception, Pytest will register this test an 'expected failure'
def test_quicksort_on_random_tuple():
    items1 = tuple(random.randint(-10,20) for i in range(50)) #random function to generate tuple of integers
    sorted_items = quick_sort(items1)  #sort() function trying to sort the immutable tuple object
    with pytest.raises(AttributeError): #we expect above line of code will raise an exception, pytest handles this exception here
         raise_exception()



'''TEST_CASE_12: Immutable String test: This test takes in random string as input types generated by random function, 
number of elements in the array is defined by the range function and run them against sorting algorithm. 
As this Sorting Algortithm assumes input should be ONLY mutable object, since Strings objects are immutable so this test should FAIL'''
@pytest.mark.xfail(raises=AttributeError) #As we expect an exception, Pytest will register this test an 'expected failure'
def test_sort_on_random_string():
    items1 = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(7)) #random choice function generates mix of uppercase and lowercase strings, range function dictates the size of the string
    print(items1)
    sorted_items = sort(items1)  #sort() function trying to sort the immutable string object
    with pytest.raises(AttributeError):  #we expect code will raise an exception, pytest handles this exception here
        raise_exception()



'''TEST_CASE_13: Non-Comparable Collection test: This test takes in array of mix of ints and strings as input types, 
and run them against sorting algorithm. 
As this Sorting Algortithm assumes input should have ONLY comparable items, since array has mix of ints and strings so this test should FAIL'''
@pytest.mark.xfail(raises=TypeError) #As we expect an exception, Pytest will register this test an 'expected failure'
def test_sort_on_mix_elements():
    items1 = ['b',2,'c',1,'a']
    sorted_items = quick_sort(items1) #sort() function trying to sort non-comparable array
    with pytest.raises(TypeError):  #we expect code will raise an exception, pytest handles this exception here
        raise_exception()


