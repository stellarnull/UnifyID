from Crypto.PublicKey import RSA
import requests
import json
import util

# f304ca94-0185-41f9-bfdc-13e966e3ff83
api_key = 'f304ca94-0185-41f9-bfdc-13e966e3ff83'
url = "https://api.random.org/json-rpc/1/invoke"
headers = {'content-type': 'application/json'}

def gen_blobs(num_bits):
	global api_key 
	params = {
			"jsonrpc": "2.0",
			"method": "generateBlobs",
			"params": {
				"apiKey": api_key,
				"n": 1,
				"size": num_bits,
				"format": "hex"
			},
			"id": 4
		}
	
	response = requests.post(url, data = json.dumps(params), headers = headers).json()
	result = None
	try:
		result = response['result']['random']['data']
	except:
		print(response)
	# print result
	return result

def gen_rand(n):
	return gen_blobs(n * 8)[0].decode('hex')

def generate_rsa_key(bits):
	if bits%256 != 0 or bits < 1024:
		return
	keys = RSA.generate(bits, randfunc = gen_rand) 
	public_key = keys.publickey().exportKey("PEM") 
	private_key = keys.exportKey("PEM") 
	return private_key, public_key

def write_rsa_key(priv, pub):
	f = open('private_key.pem','wb')
	f.write(priv)
	f.close()
	f = open('public_key.pub','wb')
	f.write(pub)
	f.close()

def main():
	bits = 1024
	priv, pub = generate_rsa_key(bits)
	write_rsa_key(priv, pub)

if __name__ == "__main__":
    main()