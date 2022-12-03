#!python3
import pyaudio, wave, time, struct


obj = wave.open('recv.wav', 'w')
obj.setnchannels(1)
obj.setsampwidth(2)
obj.setframerate(44100.0)


p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
	obj.writeframesraw(struct.pack('<h', in_data))
	return (in_data, pyaudio.paContinue)

stream = p.open(
	format=p.get_format_from_width(2),
	channels=1,
	rate=44100,
	input=True,
	stream_callback=callback,
)

stream.start_stream()

while stream.is_active():
	time.sleep(0.1)

stream.stop_stream()
stream.close()

p.terminate()

obj.close()
