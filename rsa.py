
def calc_modulus(p, q):
  return p*q

def calc_totient(n, counter=0):
  if n == 1: return counter
  
  if is_prime(n): counter+=1
  return calc_totient(n-1, counter)

# TODO start at n/2
def is_prime(n, index=None):
  if not index: index = n-1

  if index == 1 or index == 0: return True
  if n % index == 0: return False

  return is_prime(n, index-1)


