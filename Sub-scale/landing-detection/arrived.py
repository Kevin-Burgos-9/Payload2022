# This script is for the arrival of the launch vehicle after launch


def stopped():
	"""This will send a signal that the launch vehicule has landed"""
	return False

def has_arrived(stop_param):
	"""This function waiting on the arrival of the launch vehicule"""
	while True:
		if acc == stop_param:
			stopped()
			break;

