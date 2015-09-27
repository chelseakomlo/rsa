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

  def test_generate_pub_key_exponent(self):
    n = 7
    expected_pub_key_exponent = [1, 2, 3]

    actual = gen_pub_key_exponent(n)
    assert_true(actual in expected_pub_key_exponent)

    m = 11
    expected_pub_key_exponent = [1, 2, 3, 5]

    actual = gen_pub_key_exponent(m)
    assert_true(actual in expected_pub_key_exponent)

  def generate_priv_key_exponent(self):
    # (d * e) % φ(n) = 1

    n = 7
    e = 2
    actual = gen_priv_exponent(n, e)
    totient = calc_totient(n)
    priv_key_exponent_result = (actual *e) % totient

    assert_equals(priv_key_exponent_result, 1) 


