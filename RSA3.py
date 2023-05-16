import random
from typing import Tuple

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a: int, b: int) -> int:

    while b:
        a, b = b, a % b
    return a

def mod_inverse(a: int, m: int) -> int:

    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def generate_keypair(p: int, q: int) -> Tuple[Tuple[int,int], Tuple[int,int]]:

    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    d = mod_inverse(e, phi)
    public_key = (e, n)
    private_key = (d, n)
    return (public_key, private_key)

def encrypt_RSA(public_key: Tuple[int,int], message: str) -> str:
    """Encrypt a message using an RSA public key."""
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return ' '.join(map(str, cipher))

def decrypt_RSA(private_key: Tuple[int,int], cipher_text: str) -> str:
    """Decrypt a message using an RSA private key."""
    d, n = private_key
    cipher = cipher_text.split()
    message = [chr(pow(int(char), d, n)) for char in cipher]
    return ''.join(message)

# if _name_ == '_main_':
#     p = 61
#     q = 53
#     public_key, private_key = generate_keypair(p, q)
#
#     message = input("Enter a message to encrypt using RSA: ")
#     print(f'Original message: {message}')
#     cipher_text = encrypt_RSA(public_key, message)
#     print(f'Encrypted message: {cipher_text}')
#     decrypted_message = decrypt_RSA(private_key, cipher_text)
#     print(f'Decrypted message: {decrypted_message}')