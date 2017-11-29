
import requests
from path import Path

RANDOM_ORG_INTEGER_API = 'https://www.random.org/integers/'

class Failure(Exception):
    pass

class GenRand(object):
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'user-agent': 'xc2416@columbia.edu'})

    def get_integers(self, nums = 1, minRand = 1, maxRand = 2, col = 1, base = 16, format_return='plain', rnd='1'):
        ints = self.session.get(RANDOM_ORG_INTEGER_API, params = {
            'num' : str(nums),
            'min' : str(minRand),
            'max' : str(maxRand),
            'col' : str(col),
            'base' : str(base),
            'format' : str(format_return),
            'rnd' : str(rnd)
            })
        if 200 != ints.status_code:
            raise Failure(ints)
        try:
            vals = [int(y, base) for y in [x.strip() for x in ints.content.strip().split()] if len(y)]
        except Exception as _e:
            return ints
        return vals

    def get_and_save_bytes(self, num_bytes, directory='.'):
        files = sorted(int(pth.basename().split('.')[0]) for pth in Path(directory).files('*.rawbytes'))
        if files:
            nextbase = str(files[-1] + 1)
        else:
            nextbase = str(1)
        nextname = nextbase + '.rawbytes'
        ints = self.get_integers(num_bytes, 0, 0xFF, base = 16)
        value = ''.join(chr(i) for i in ints)
        with open(nextname, 'wb') as f:
            f.write(value)
        return value

    def get_bytes_from_local(self, directory='.'):
        res = []
        files = sorted(int(pth.basename().split('.')[0]) for pth in Path(directory).files('*.rawbytes'))
        for i in files:
            res.append((Path(directory) / str(i) + '.rawbytes').open('rb').read())
        return ''.join(res)

def main():
    random_org = GenRand()
    random_org.get_and_save_bytes(10000)

if __name__ == "__main__":
    main()
