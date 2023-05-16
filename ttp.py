import random
import math

class TTP:
    def __init__(self, key_size):
        self.key_size = key_size
        self.prime = None
        self.generator = None
        self.private_key_a = None
        self.private_key_b = None
        self.public_key_a = None
        self.public_key_b = None
        self.shared_key_a = None
        self.shared_key_b = None

    def is_prime(self, n, k=10):
        """
        Check if a number is prime using the Miller-Rabin primality test.
        """
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False

        # Find s and d such that n-1 = 2^s * d with d odd
        s = 0
        d = n - 1
        while d % 2 == 0:
            s += 1
            d //= 2

        # Perform k rounds of the Miller-Rabin test
        for i in range(k):
            a = random.randrange(2, n - 1)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for j in range(s - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    def generate_prime_and_generator(self):
        """
        Generate a prime number and generator value for the key exchange.
        """
        while True:
            # Generate a random prime number of the specified size
            p = random.getrandbits(self.key_size)
            if self.is_prime(p):
                self.prime = p
                break

        # Find a generator g of the prime field
        while True:
            g = random.randrange(2, self.prime - 1)
            if pow(g, (self.prime - 1) // 2, self.prime) != 1:
                self.generator = g
                break

    def generate_key_pairs(self):
        """
        Generate public and private key pairs for the two users.
        """
        self.private_key_a = random.randrange(1, self.prime - 1)
        self.public_key_a = pow(self.generator, self.private_key_a, self.prime)

        self.private_key_b = random.randrange(1, self.prime - 1)
        self.public_key_b = pow(self.generator, self.private_key_b, self.prime)

    def calculate_shared_key(self, private_key, other_public_key):
        """
        Calculate the shared key using the private key and the other user's public key.
        """
        return pow(other_public_key, private_key, self.prime)

    def run_ttpA(self):
        # Step 1: Generate a prime number and generator value
        self.generate_prime_and_generator()

        # Step 2: Generate public and private key pairs for the two users
        self.generate_key_pairs()

        # Step 3: Exchange public keys
        self.shared_key_a = self.calculate_shared_key(self.private_key_a, self.public_key_b)
        # self.shared_key_b = self.calculate_shared_key(self.private_key_b, self.public_key_a)
        print("Shared key A:", self.shared_key_a)

        # Step 4: Verify that the shared keys match
        # if self.shared_key_a == self.shared_key_b:
        #   # print("Key exchange successful")
        #   # print("Shared key A:", self.shared_key_a)
        #   # print("Shared key B:",self.shared_key_b)
        #   print("Key exchange successful")
        #   return self.shared_key_a
        #   return self.shared_key_b





        # else:
        #     print("Key exchange failed. Shared keys do not match.")
    def run_ttpB(self):
        # # Step 1: Generate a prime number and generator value
        # self.generate_prime_and_generator()
        #
        # # Step 2: Generate public and private key pairs for the two users
        # self.generate_key_pairs()

        # Step 3: Exchange public keys

        self.shared_key_b = self.calculate_shared_key(self.private_key_b, self.public_key_a)
        print("Shared key B:",self.shared_key_b)

        # # Step 4: Verify that the shared keys match
        # if self.shared_key_a == self.shared_key_b:
        #   # print("Key exchange successful")
        #   # print("Shared key A:", self.shared_key_a)
        #   # print("Shared key B:",self.shared_key_b)
        #   print("Key exchange successful")
        #   return self.shared_key_a
        #
        #
        #
        #
        #
        #
        # else:
        #     print("Key exchange failed. Shared keys do not match.")

# Create an instance of the TTP system
key_size = 10
ttp = TTP(key_size)

# Run the TTP system


if ttp.run_ttpA() == ttp.run_ttpB():
     print("Key exchange successful")
else:
    print("Key exchange Not successful")
