#!python3
import wave, struct


file = open('source.txt', 'r', encoding='utf8')
data = file.read()
file.close()


obj = wave.open('serialized.wav', 'w')
obj.setnchannels(1)
obj.setsampwidth(2)
obj.setframerate(44100.0)

for char in data:
    obj.writeframesraw(struct.pack('<h', ord(char)))

obj.close()
