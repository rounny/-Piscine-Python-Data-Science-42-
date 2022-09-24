def	data_types():
	data = [1, "", 0.0, True, [], {1: '2'}, (), {1, 2}]
	# print(list(map(str, lambda x: type(x).__name__, b)))
	print("[{0}]".format(', '.join(map(lambda x: type(x).__name__, data))))

if __name__  == '__main__':
	data_types()


def	data_types():
	print("somer")
	new_data = []
	data = [1, "", 0.0, True, [], {1: '2'}, (), {1, 2}]
	for i in data:
		new_data.append(type(i).__name__)
	print('[%s]' % ', '.join(map(str, new_data)))

if __name__  == '__main__':
	data_types()

