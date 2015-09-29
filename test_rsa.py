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

    actual = gen_pub_key_exponent(2)
    assert_true(actual in expected_pub_key_exponent)

    expected_pub_key_exponent = [1, 2, 3]

    actual = gen_pub_key_exponent(5)
    assert_true(actual in expected_pub_key_exponent)

  def test_generate_priv_key_exponent(self):
    n = 33
    totient = 20
    e = 7

    expected = 3
    actual = gen_priv_key_exponent(n, totient, e)
    assert_equals(actual, expected) 

  def test_generate_keys(self):
    p = 2
    q = 3

    expected_public = [1, 6]
    expected_private = [1, 6]
    actual_keys = generate_keys(p, q)

    assert_equals(actual_keys["public"], expected_public)
    assert_equals(actual_keys["private"], expected_private)

  def test_encrypt_message(self):
    e = 3
    n = 7

    m = "a"
    ciphertext = encrypt(m, e, n)
    assert_equals(6, ciphertext)

    m = "b"
    ciphertext = encrypt(m, e, n)
    assert_equals(0, ciphertext)

    m = "ab"
    ciphertext = encrypt(m, e, n)
    assert_equals(60, ciphertext)

  def test_crypt(self):
    m = 9
    e = 7
    n = 143

    ciphertext = crypt(m, e, n)
    assert_equals(48, ciphertext)

  def test_to_ascii(self):
    actual = to_ascii("h")
    assert_equals(104, actual)

    actual = to_ascii("i")
    assert_equals(105, actual)

