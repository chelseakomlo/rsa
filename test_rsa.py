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
    assert_equals(1632, ciphertext)

    m = "aa"
    ciphertext = encrypt(m, e, n)
    assert_equals(2894, ciphertext)

  def test_crypt(self):
    m = 9
    e = 17
    n = 3233

    ciphertext = crypt(m, e, n)
    assert_equals(1972, ciphertext)

  def test_decrypt(self):
    d = 2753
    n = 3233

    ciphertext = 1632
    message = decrypt(ciphertext, 1, d, n)
    assert_equals("a", message)

    ciphertext_2 = 2069
    message = decrypt(ciphertext_2, 2, d, n)
    assert_equals("ab", message)

  def test_to_ascii(self):
    message_one = ["a"]
    assert_equals(97, to_ascii(message_one))

    message_two = ["a", "a"]
    assert_equals(24929, to_ascii(message_two))

    message_three = ["a", "b"]
    assert_equals(24930, to_ascii(message_three))

  def test_from_ascii(self):
    assert_equals("a", from_ascii(97, 1))
    assert_equals("ab", from_ascii(24930, 2))

  def test_sanity__integration(self):
    e = 17
    d = 2753
    n = 3233

    message = "aa"
    ciphertext = encrypt(message, e, n)
    received_message = decrypt(ciphertext, len(message), d, n)
    assert_equals(received_message, "aa")

  def signature(self):
    #TODO
    pass
