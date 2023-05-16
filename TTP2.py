import random

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

    def is_prime(self, n):
        """
        Check if a number is prime using trial division.
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
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
        for g in range(2, self.prime):
            if all(pow(g, t, self.prime) != 1 for t in range(1, self.prime)):
                self.generator = g
                break

    def generate_key_pairs(self):
        # Get the private keys for TTP-A and TTP-B
        self.private_key_a = int(input("Enter TTP-A's private key: "))
        self.private_key_b = int(input("Enter TTP-B's private key: "))

        # Check if the inputs are valid
        if self.private_key_a < 1 or self.private_key_a >= self.prime:
            raise ValueError("Invalid private key for TTP-A")
        if self.private_key_b < 1 or self.private_key_b >= self.prime:
            raise ValueError("Invalid private key for TTP-B")

        # Generate the public keys for TTP-A and TTP-B
        self.public_key_a = pow(self.generator, self.private_key_a, self.prime)
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
        print("Shared key A:", self.shared_key_a)

    def run_ttpB(self):
        # Step 3: Exchange public keys
        self.shared_key_b = self.calculate_shared_key(self.private_key_b, self.public_key_a)
        print("Shared key B:",self.shared_key_b)

# Create an instance of the TTP system
key_size = 10
ttp = TTP(key_size)

# Run the TTP system
ttp.run_ttpA()
ttp.run_ttpB()

# Step 4: Verify that the shared keys match
if ttp.shared_key_a == ttp.shared_key_b:
    print("Key exchange successful")
else:
    print("Key exchange failed. Shared keys do not match.")
