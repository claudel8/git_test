def factoriel(n): 
	if n==0: 
		return 1 
	return n*factoriel(n-1)

def main(): 
	print("Factoriel 10 est de: ", factoriel(10))
if __name__ == '__main__':
	main()