import random

def calc_modulus(p, q):
  return p*q

def calc_totient(n, counter=0):
  if n == 1: return counter
  
  if is_prime(n): counter+=1
  return calc_totient(n-1, counter)

def gen_pub_key_exponent(n):
  totient = calc_totient(n)
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


