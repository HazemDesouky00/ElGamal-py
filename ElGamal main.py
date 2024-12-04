import random

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp // 2
    return result

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

# Example usage
# Prime number and base generator
p = 23
g = 5

# Generate keys
public_key, private_key = generate_keys(p, g)
print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")

# Encrypt message
plaintext = 15
ciphertext = encrypt(public_key, plaintext)
print(f"Ciphertext: {ciphertext}")

# Decrypt message
decrypted_message = decrypt(private_key, p, ciphertext[0], ciphertext[1])
print(f"Decrypted Message: {decrypted_message}")
