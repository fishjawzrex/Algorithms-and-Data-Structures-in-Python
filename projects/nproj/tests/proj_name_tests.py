from nose.tools import *
import my_first_rename

def setup():
    print "SETUP!"
    
def teardown():
    print "TEAR DOWN!"
 
def test_basic():
    print "I RAN!"