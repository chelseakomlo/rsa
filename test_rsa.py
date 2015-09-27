from nose.tools import *

from rsa import *

class TestRSA():

  def test_creation_modulus_n(self):
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
    expected_pub_key_exponent = [1]

    actual = gen_pub_key_exponent(2, 3)
    assert_true(actual in expected_pub_key_exponent)

    expected_pub_key_exponent = [1, 2, 3]

    actual = gen_pub_key_exponent(2, 5)
    assert_true(actual in expected_pub_key_exponent)

  def test_generate_priv_key_exponent(self):
    p = 3
    q = 11
    e = 7

    expected = 3
    actual = gen_priv_key_exponent(p, q, e)
    assert_equals(actual, expected) 

  def test_generate_keys(self):
    p = 2
    q = 3

    expected_public = [1, 6]
    expected_private = [1, 6]
    actual_keys = generate_keys(p, q)

    assert_equals(actual_keys["public"], expected_public)
    assert_equals(actual_keys["private"], expected_private)


