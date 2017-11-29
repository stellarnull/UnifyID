import wave
import bits

random_org = bits.GenRand()
bites = random_org.get_bytes_from_local()
wf = wave.open('output.wav', 'wb')
wf.setparams((1, 1, 44100, 0, 'NONE', 'not compressed'))
samplelength = 44100*3
wf.writeframes(bites[:samplelength])
wf.close()