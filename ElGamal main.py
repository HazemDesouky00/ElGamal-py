#finding if a number is a primitive root using prime factors 
# def prime_factors(n):
#     factors = set()
#     for i in range(2, int(n ** 0.5) + 1):
#         while n % i == 0:
#             factors.add(i)
#             n //= i
#     if n > 1:
#         factors.add(n)
#     return factors

# def is_primitive_root(g, p):
#     if g <= 1:
#         return False
#     phi = p - 1  
#     factors = prime_factors(phi)
#     for factor in factors:
#         if pow(g, phi // factor, p) == 1:
#             return False
#     return True 
#instead of function in line 50


import random

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp // 2
    return result

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime(min_value=10000):
    while True:
        num = random.randint(min_value, min_value * 10)
        if is_prime(num):
            return num


def is_primitive_root(g, p):
    required_set = set(num for num in range(1, p))
    actual_set = set(pow(g, powers, p) for powers in range(1, p)) 
    return required_set == actual_set



def generate_keys(p, g):
    x = random.randint(1, p - 2)  # Private key
    h = mod_exp(g, x, p)  # Public key
    return (p, g, h), x  # Public and private keys

def encrypt(public_key, m):
    p, g, h = public_key
    k = random.randint(1, p - 2)
    c1 = mod_exp(g, k, p)
    c2 = (m * mod_exp(h, k, p)) % p
    return c1, c2

def decrypt(private_key, p, c1, c2):
    s = mod_exp(c1, private_key, p)
    s_inv = pow(s, -1, p)
    m = (c2 * s_inv) % p
    return m

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_prime_input(prompt):
    while True:
        value = get_integer_input(prompt)
        if is_prime(value):
            return value
        else:
            print("The number entered is not prime. Please enter a prime number.")


# Example
# Prime number and base generator
# Generate a random prime number for p
p = generate_prime()
print("Generated prime number (p): ", p)

g = get_integer_input("Enter a base generator (g): ")


while not is_primitive_root(g, p):
     print("The base generator (g) is not a primitive root of the prime number (p). Please enter a valid primitive root.") 
     g = get_integer_input("Enter a base generator (g): ")

# Generate keys
public_key, private_key = generate_keys(p, g)
print("Public Key: ",public_key)
print("Private Key: ",private_key)

# Encrypt message
plaintext = get_integer_input("Enter a plaintext message to encrypt (as an integer less than {}): ".format(p))
while plaintext >= p:
    print("The message must be less than the prime number {}.".format(p))
    plaintext = get_integer_input("Enter a plaintext message to encrypt (as an integer less than {}): ".format(p))

ciphertext = encrypt(public_key, plaintext)
print("Ciphertext: ", ciphertext)
print("Ciphertext c1 is {}, and c2 is {}".format(ciphertext[0],ciphertext[1]))

# Decrypt message
decrypted_message = decrypt(private_key, p, ciphertext[0], ciphertext[1])
print("Decrypted Message: ",decrypted_message)
