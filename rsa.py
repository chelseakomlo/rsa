import random

def generate_keys(p, q):
  n = calc_modulus(p, q)
  totient = calc_totient(p, q)
  e = gen_pub_key_exponent(totient)
  d = gen_priv_key_exponent(n, totient, e)

  return {"modulus": n, "public": e, "private": d}

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
  m = to_ascii(list(message))
  return crypt(m, e, n)

def decrypt(ciphertext, length, d, n):
  m = dcrypt(ciphertext, d, n)
  message = from_ascii(m, length)
  return message

def dcrypt(ciphertext, d, n):
    return ((ciphertext ** d) % n)

def crypt(m, e, n):
  return int(((m**e) % n))

def to_ascii(letters, value=0):
  if len(letters) == 0: return value
  counter = len(letters)-1
  value = value | ord(letters[0]) << (8 * counter) 
  return to_ascii(letters[1:], value) 

def from_ascii(value, length, message=""):
  if length == 0: return message
  length = length-1
  letter = (value >> (length*8) & 0xFF)
  message += chr(letter)
  return from_ascii(value, length, message)
