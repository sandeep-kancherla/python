x='global star'

def outer():
	x='outer star'

	def inner():
		x='inner star'
		print(x)
	inner()
	
	print(x)

outer()