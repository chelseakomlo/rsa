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
    e = 17
    n = 3233

    m = "a"
    ciphertext = encrypt(m, e, n)
    assert_equals([1632], ciphertext)

    m = "aa"
    ciphertext = encrypt(m, e, n)
    assert_equals([1632, 1632], ciphertext)

  def test_crypt(self):
    m = 9
    e = 17
    n = 3233

    ciphertext = crypt(m, e, n)
    assert_equals(1972, ciphertext)

  def test_decrypt(self):
    d = 2753
    n = 3233

    ciphertext = [1632]
    message = decrypt(ciphertext, d, n)
    assert_equals("a", message)

    ciphertext_2 = [1632, 1632]
    message = decrypt(ciphertext_2, d, n)
    assert_equals("aa", message)

  def test_to_ascii(self):
    message_one = "a"
    assert_equals(97, to_ascii(message_one))

  def test_from_ascii(self):
    assert_equals("a", from_ascii(97))

  def sanity_test_integration(self):
    e = 17
    d = 2753
    n = 3233

    ciphertext = encrypt("very secret", e, n)
    message = decrypt(ciphertext, d, n)
    assert_equals(message, "very secret")

  def signature(self):
    #TODO
    pass
