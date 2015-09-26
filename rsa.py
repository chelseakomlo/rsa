

def calc_modulus(p, q):
  return p*q

def calc_totient(n):
  return 3

def is_prime(n, index):
  if index == 1: return True

  print("n %s" % n)
  print("n %s" % index)
  if n % index == 0: return False

  return is_prime(n, index-1)

  #for i in range(2, n):
  #  if n % i == 0:
  #    return False
  #return True


