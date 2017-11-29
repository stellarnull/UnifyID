
import requests
from path import Path

RANDOM_ORG_QUOTA_API = 'https://www.random.org/quota/'
RANDOM_ORG_INTEGER_API = 'https://www.random.org/integers/'

class Failure(Exception):
    pass

class RandomOrg(object):
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'user-agent': 'stelminator@gmail.com'})

    def get_integers(self, num = 1, min_int = 1, max_int = 2, col = 1, base = 16, format_return='plain', rnd='1'):
        #TODO: deal with exponential backoff when trying to get data
        ints = self.session.get(RANDOM_ORG_INTEGER_API, params = {
            'num' : str(num),
            'min' : str(min_int),
            'max' : str(max_int),
            'col' : str(col),
            'base' : str(base),
            'format' : str(format_return),
            'rnd' : str(rnd)
            })
        # break into pieces, filter empties, parse as hex
        if 200 != ints.status_code:
            raise Failure(ints)
        try:
            vals = [int(y, base) for y in [x.strip() for x in ints.content.strip().split()] if len(y)]
        except Exception as _e:
            return ints
        return vals

    def get_and_save_bytes(self, num_bytes, directory='.'):
        #TODO: validate all filenames are ints
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
        retval = []
        files = sorted(int(pth.basename().split('.')[0]) for pth in Path(directory).files('*.rawbytes'))
        for i in files:
            retval.append((Path(directory) / str(i) + '.rawbytes').open('rb').read())
        return ''.join(retval)

    def quota_remaining(self):
        resp = self.session.get(RANDOM_ORG_QUOTA_API, params=dict(format='plain'))
        return int(resp.content.strip())

def main():
    random_org = RandomOrg()
    random_org.get_and_save_bytes(10000)

if __name__ == "__main__":
    main()
