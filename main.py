def main():
	print("git config --local user.name")
	print("git config --local user.email", end="\n")
	print("git config --global user.name")
	print("git config --global user.email", end='\n')
	print("git config --system user.name")
	print("git config --system user.email", end='\n')

if __name__ == "__main__":
	main()
