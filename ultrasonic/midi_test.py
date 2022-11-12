from pythonosc import osc_message_builder
from pythonosc import udp_client
from time import sleep

sender = udp_client.SimpleUDPClient('10.0.0.31', 4560)


while True:
	for pitch in range(20,80,5):
		print(pitch)	
		sender.send_message('/play_this', pitch)
		sleep(0.5)
