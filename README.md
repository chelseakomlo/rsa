# RSA 

## Why RSA? 

Can be used for both encrypting and signing messages

## Background

### Chinese Remainder Theorum

1. The theorum

With the following linear system:

n is modular equivilant to to n1 (mod y)

and

n is modular equivilant to n2 (mod z)

This system is only solvable for n when n1 = n2 (mod gcd(y, z))

Another way of solving the CRT:

x = (((a−b)(q^−1 mod p)) mod p)·q+b

2. Why is the CRT useful? 

If you have to do a lot of computations mod n, using this is more efficient. 

3. In conclusion: 

A number x (mod n) can be represented as a pair, x (mod p), x (mod q) when n == pq.

And

The CRT representation is useful if you have to do many multiplications modulo a composite number that you know the factorization of. 

### Multiplication mod N

How does x (mod n), where n is a composite number, behave under multiplication, as opposed to x (mod p), where p is a prime number?

When n is a composite number, for 0 < x < n, the equation x^(p-1) = 1 (mod n) doesn't hold.  

Instead, we need to find an exponent t such that x^t=1 (mod n) for almost every x. (it is easy to do this using CRT).  

Also, this doesn't hold when x^t=0


## What is RSA?

### Calculating inputs
1. Start by randomly choosing two different primes, p and q
2. Compute n=pq
3. Use e and d as exponents, where ed = 1 (mod t), t = lcm(p-1, q-1)

### Encrypting Messages

1. Encryption

ciphertext = message ^ e (mod n)

However, this is expensive and almost never done. Instead, we do this: 

a. Choose a random number k
b. Encrypt k using the RSA secret key
c. Encrypt m with k using a block or stream cipher

2. Decryption 

message = ciphertext ^ d (mod n)

### RSA Public and Private Keys

The pair (n, e) form the public key. 

The values (p, q, t, d) form the private key. 

## Attacks on RSA

todo

## Sources

1. https://www.cs.utexas.edu/~mitra/honors/soln.html
