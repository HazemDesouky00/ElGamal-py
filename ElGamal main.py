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

def mod_exp(base, exp, mod):  # Function to perform modular exponentiation
    result = 1   #initializing result 
    while exp > 0:
        if exp % 2 == 1: #if exp is odd, multiply base with result 
            result = (result * base) % mod
        base = (base * base) % mod   #square the base 
        exp = exp // 2   
    return result

def is_prime(num):      # Function to check if a number is prime
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime(min_value=10000):   # function to generate a random prime number
    while True:
        num = random.randint(min_value, min_value * 10)  #generating random number from this range min,max
        if is_prime(num):
            return num


def is_primitive_root(g, p):    # function to check if a number is a primitive root modulus p
    required_set = set(num for num in range(1, p))
    actual_set = set(pow(g, powers, p) for powers in range(1, p)) 
    return required_set == actual_set


def find_primitive_root(p):   #function to find the primitive root, looping from 2 to p-1 
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    raise ValueError("No primitive root found")


def generate_keys(p, g):    #function to generate the keys (public and private)
    x = random.randint(1, p - 2)  # Private key
    h = mod_exp(g, x, p)  # Public key
    return (p, g, h), x  # Public and private keys returned 

def encrypt(public_key, m):   #function to encrypt a message using the public key
    p, g, h = public_key
    k = random.randint(1, p - 2) #random ephemeral key 
    c1 = mod_exp(g, k, p)
    c2 = (m * mod_exp(h, k, p)) % p
    return c1, c2

def decrypt(private_key, p, c1, c2): #to decrypt the message 
    s = mod_exp(c1, private_key, p)
    s_inv = pow(s, -1, p)    #compute the modular inverse of s
    m = (c2 * s_inv) % p
    return m

def get_integer_input(prompt):    #function to ensure integer value entered to decrypt
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")




# Example

# Generate a random prime number for p
p = generate_prime()
print("Generated prime number (p): ", p)

# Generate a random base generator that is a primitive root
g = find_primitive_root(p)
print("Generated primitive root base generator (g): ", g)


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
