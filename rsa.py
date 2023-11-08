import random

class RSA:
    def __init__(self):
        #Generating p,q
        self.p = self.generatePrime()
        self.q = self.generatePrime()
        
        # Calculating n, m
        self.n = self.p*self.q
        self.m = (self.p-1)*(self.q-1)
        
        #Calculate e
        self.e = self.calculateE()
        self.public_key = (self.e, self.n)
        
        #Calcualte d
        self.d = self.calculateD()
        self.private_key = (self.d, self.n)
    def generatePrime(self):
        while(True):
            num = random.randint(100, 999)
            for i in range(2, num):
                if(num%i == 0):
                    break
            if(num%i != 0):
                return num
    def calculateE(self):
        for e in range(2, self.m):
            if(self.calculateGCD(self.m, e) == 1):
                return e
    def calculateGCD(self, x, y):
        while(y):
            tmp = y;
            y = x % y;
            x = tmp;
        return x;
    def calculateD(self):
        d = 0
        while(True):
            if((d*self.e)%self.m == 1):
                return d
            d += 1
    def encrypt(self, msg):
        return (msg**self.e) % self.n
    def decrypt(self, cipher):
        return (cipher**self.d) % self.n
        
plain_text = 55
rsa = RSA()
cipher = rsa.encrypt(plain_text)
plain_text_retrived = rsa.decrypt(cipher)

print("Original Text:", plain_text)
print("Cipher Text:", cipher)
print("Decrypted Text:", plain_text_retrived)
print("p:", rsa.p)
print("q:", rsa.q)
print("n:", rsa.n)
print("m:", rsa.m)
print("e:", rsa.e)
print("d:", rsa.d)
print("Public Key:", rsa.public_key)
print("Private Key:", rsa.private_key)
