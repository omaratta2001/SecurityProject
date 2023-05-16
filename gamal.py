import random

def generate_prime():
    while True:
        p = random.randint(100000, 1000000)
        if is_prime(p):
            return p

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def generate_keys():
    p = generate_prime()
    g = random.randint(2, p-1)
    x = random.randint(1, p-2)
    y = pow(g, x, p)
    return (p, g, y, x)

def encrypt_str(p, g, y, message):
    message_num = [ord(c) for c in message]
    k = random.randint(1, p-2)
    a = pow(g, k, p)
    b_num = [(pow(y, k, p) * m) % p for m in message_num]
    return (a, b_num)

def decrypt_str(p, x, a, b_num):
    message_num = [(b * mod_inverse(pow(a, x, p), p)) % p for b in b_num]
    message = ''.join([chr(n) for n in message_num])  # convert numerical representation back to string
    return message


# Encrypt a message
def encrypt(p, g, y, message):
    k = random.randint(1, p-2)
    a = pow(g, k, p)
    b = (pow(y, k, p) * message) % p
    return (a, b)

# Decrypt a message
def decrypt(p, x, a, b):
    message = (b * mod_inverse(pow(a, x, p), p)) % p
    return message

# Generate keys
keys = generate_keys()
p, g, y, x = keys

