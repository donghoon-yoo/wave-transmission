#!python3
import wave


obj = wave.open('serialized.wav', 'r')

for byte in obj.readframes(obj.getnframes()):
    print(chr(byte), end='')
print()
