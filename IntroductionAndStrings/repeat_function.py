# Defines a "repeat" function that takes 2 arguments

def repeat(s, exclaim):
	"""
	Returns the string 's' repeated 3 times.
	If exclaim is true, add exclamation marks.
	"""

	result = s * 3
	if exclaim:
		result = result + '!!!'
	return resul
t
def main():
	print repeat('Yay', False)
	print repeat('Woo Hoo', True)

if __name__ == '__main__':
	main()