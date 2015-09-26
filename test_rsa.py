from nose.tools import *

from rsa import *

class TestRSA():

  def test_calculate_creation_modulus_n(self):
    p = 3
    q = 11
    actual_n = calc_modulus(p, q)
    expected_n = p*q
    assert_equals(expected_n, actual_n)

  def test_calculate_totient(self):
    totient = calc_totient(5)
    assert_equals(3, totient)

    totient = calc_totient(7)
    assert_equals(4, totient)

  def test_is_prime(self):
    result = is_prime(7)
    assert_true(result)

    result = is_prime(4)
    assert_false(result)



