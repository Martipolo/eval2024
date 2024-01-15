from devine_turing import *
import pytest

def test_divisible():
    assert(divisible(108)) == True
    assert(divisible(540)) == True
    assert(divisible(990)) == True
    assert(divisible(109)) == False
    assert(divisible(541)) == False
    assert(divisible(991)) == False


def test_somme():
    assert(somme(1,9,8)) == True
    assert(somme(5,7,2)) == True
    assert(somme(1,0,8)) == False
    assert(somme(5,4,0)) == False

def test_decomposer():
    assert(decomposer(111)) == (1,1,1)
    assert(decomposer(222)) == (2,2,2)