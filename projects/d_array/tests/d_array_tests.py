from nose.tools import *
from d_array.d_array import DynamicArray as d

def setup():
    print "SETUP!"
   
def teardown():
    print "TEAR DOWN!"
 
def test_basic():
    print "I RAN!"
    
def test_array_len():
    gold = d()
    gold._append('w')
    gold._append(1000)
    assert_equal(gold._len(), 2)

    
def test_items():
    gold = d()
    gold._append('w')
    gold._append(1000)
    assert_equal(gold.get_item(0), 'w')
    assert_equal(gold.get_item(1), 1000)
    #assert_equal(gold.get_item(2), 'Index Error')