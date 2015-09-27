import random

def calc_modulus(p, q):
  return p*q

def calc_totient(p, q):
  return (p-1)*(q-1)

def gen_pub_key_exponent(p, q):
  totient = calc_totient(p, q)
  rand_index = random.randrange(1, totient)

  while not is_prime(rand_index):
    rand_index -= 1
  return rand_index

# TODO start at n/2
def is_prime(n, index=None):
  if not index: index = n-1

  if index == 1 or index == 0: return True
  if n % index == 0: return False

  return is_prime(n, index-1)


