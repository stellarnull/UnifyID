from Crypto.PublicKey import RSA
import bits

random_org = bits.GenRand()

class ByteGen(object):
    bites = random_org.get_bytes_from_local()
    def __init__(self):
        self.i = 0
    def __call__(self, N):
        retval = self.bites[self.i:self.i+N]
        self.i += N
        return retval

byte_gen = ByteGen()

key = RSA.generate(1024, byte_gen)
pubkey = key.publickey()

with open('private_key.pem', 'wb') as f:
    f.write(key.exportKey(passphrase='UnifyID'))

with open('public_key.pub', 'wb') as f:
    f.write(pubkey.exportKey())
