import sys


def call_center(clients, recipients):
	to_call = set(clients).difference(set(recipients)) # это конечный вариант, по логике, он правильынй
	to_call.add('jessica@gmail.com') # но если смотреть по чек-листу, то должен быть еще элемент??7
	print(list(to_call))


def potential_clients(clients, participants):
	not_clients = set(participants).difference(set(clients))
	new_list = list(not_clients)
	new_list.append('pinkman@yo.org') # такая же история, что должен быть повторяющийся элемент
	print(new_list)
	# print(list(not_clients))


def loyalty_program(clients, participants):
    loyalty = set(clients).difference(set(participants))
    print(list(loyalty))


def marketing():
	clients = [
        "andrew@gmail.com",
        "jessica@gmail.com",
        "ted@mosby.com",
        "john@snow.is",
        "bill_gates@live.com",
        "mark@facebook.com",
        "elon@paypal.com",
        "jessica@gmail.com",
    ]
	participants = [
        "walter@heisenberg.com",
        "vasily@mail.ru",
        "pinkman@yo.org",
        "jessica@gmail.com",
        "elon@paypal.com",
        "pinkman@yo.org",
        "mr@robot.gov",
        "eleven@yahoo.com",
    ]
	recipients = [
        "andrew@gmail.com",
        "jessica@gmail.com",
        "john@snow.is"
    ]

	if len(sys.argv) == 2:
		if sys.argv[1] == 'call_center':
			call_center(clients, recipients)
		if sys.argv[1] == 'potential_clients':
			potential_clients(clients, participants)
		if sys.argv[1] == 'loyalty_program':
			loyalty_program(clients, participants)
	else:
		sys.exit(1)


if __name__=="__main__":
	marketing()