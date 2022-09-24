def	main():
    list_of_tuples = [
        ("Russia", "25"),
        ("France", "132"),
        ("Germany", "132"),
        ("Spain", "178"),
        ("Italy", "162"),
        ("Portugal", "17"),
        ("Finland", "3"),
        ("Hungary", "2"),
        ("The Netherlands", "28"),
        ("The USA", "610"),
        ("The United Kingdom", "95"),
        ("China", "83"),
        ("Iran", "76"),
        ("Turkey", "65"),
        ("Belgium", "34"),
        ("Canada", "28"),
        ("Switzerland", "26"),
        ("Brazil", "25"),
        ("Austria", "14"),
        ("Israel", "12"),
    ]
    data = {}
    for value, key in list_of_tuples:
        if key not in data.keys():
            data[key] = [value]
        else:
            data[key].append(value)
    for key in data.keys():
        for val in data[key]:
            print(f"'{key}' : '{val}'")


if __name__ == "__main__":
    main()




# def	reverse_in_dict():
# 	list_of_tuples = [
#         ("Russia", "25"),
#         ("France", "132"),
#         ("Germany", "132"),
#         ("Spain", "178"),
#         ("Italy", "162"),
#         ("Portugal", "17"),
#         ("Finland", "3"),
#         ("Hungary", "2"),
#         ("The Netherlands", "28"),
#         ("The USA", "610"),
#         ("The United Kingdom", "95"),
#         ("China", "83"),
#         ("Iran", "76"),
#         ("Turkey", "65"),
#         ("Belgium", "34"),
#         ("Canada", "28"),
#         ("Switzerland", "26"),
#         ("Brazil", "25"),
#         ("Austria", "14"),
#         ("Israel", "12"),
#     ]
# 	data = {}
# 	for val, key in list_of_tuples:
# 		data[key] = val
# 		print(f"'{key}' : '{val}'")

# if __name__=="__main__":
# 	reverse_in_dict()
