try:
	f = open("C:/Users/sande/Desktop/new.txt",'r')

except FileNotFoundError as e:
	print(e)

except Exception as e:
	print(e)

else:
	print(f.read())
	f.close()

finally:
	print('Executing...')

	
