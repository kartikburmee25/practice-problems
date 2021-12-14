x=3

def test_function(y,x):
	print (y)
	x+=100
	return y

if __name__ == '__main__':
	x=3
	print(x)
	print (test_function(7,x))
	print(x)