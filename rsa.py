import random

def generate_keys(p, q):
  n = calc_modulus(p, q)
  totient = calc_totient(p, q)
  e = gen_pub_key_exponent(totient)
  d = gen_priv_key_exponent(n, totient, e)

  return {"public": [e, n], "private": [d, n]}

def calc_modulus(p, q):
  return p*q

def gen_pub_key_exponent(totient):
  rand_index = random.randrange(1, totient)

  while not is_prime(rand_index):
    rand_index -= 1
  return rand_index

def gen_priv_key_exponent(n, totient, e):
  d = 1
  while not calc_mod((d*e), totient) == 1:
    d += 1
  return d

def calc_mod(a, b):
  return a % b

def calc_totient(p, q):
  return (p-1)*(q-1)

def is_prime(n, index=None):
  if not index: index = n//2

  if index == 1 or index == 0: return True
  if n % index == 0: return False

  return is_prime(n, index-1)

def encrypt(message, e, n):
  ciphertext = crypt(to_ascii(message), e, n)
  return ciphertext

def decrypt(ciphertext, d, n):
  message = ""
  for block in ciphertext:
    m = dcrypt(block, d, n)
    message += from_ascii(m)
  return message

def dcrypt(ciphertext, d, n):
    return ((ciphertext ** d) % n)

def crypt(m, e, n):
  return ((m**e) % n)

def to_ascii(message, value=0):
  if len(message) == 1:
    value += ord(message)
    return value

  value += (ord(message[0]) << 8) 
  return to_ascii(message[1:], value)

def from_ascii(c):
  return chr(c)
