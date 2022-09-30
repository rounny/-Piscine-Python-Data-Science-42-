import	os

def main():
	print(os.environ['VIRTUAL_ENV']) # путь, где лежит виртуальальная среда, причем, отображается только в самой виртуальной среде


if __name__=="__main__":
	main()