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
    p = 3
    q = 11
    totient = calc_totient(p, q)
    assert_equals(20, totient)

  def test_generate_pub_key_exponent(self):
    expected_pub_key_exponent = [1, 2]

    actual = gen_pub_key_exponent(2, 3)
    assert_true(actual in expected_pub_key_exponent)

    expected_pub_key_exponent = [1, 2, 3]

    actual = gen_pub_key_exponent(2, 5)
    assert_true(actual in expected_pub_key_exponent)

  def generate_priv_key_exponent(self):
    # (d * e) % φ(n) = 1
    # the result should be (d*e) module the toitent of n should equal 1

    n = 33
    e = 7
    expected = 3
    actual = gen_priv_exponent(n, e)

    assert_equals(actual, expected) 


