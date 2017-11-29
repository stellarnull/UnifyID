
import wave

import bits


random_org = bits.RandomOrg()
#misspelled to not conflict with builtin 'bytes'
bites = random_org.get_bytes_from_local()

wavefile = wave.open('output.wav', 'wb')
wavefile.setparams((1, 1, 44100, 0, 'NONE', 'not compressed'))

samplelength = 44100*3

wavefile.writeframes(bites[:samplelength])

wavefile.close()