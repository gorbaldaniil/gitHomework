angl = "abcdefghijklmnopqrstuvwxyz" # Англійський алфавіт
number = "123456789" # Цифри
ukr = "абвгдеєжзиіїйклмнопрстуфхцчшщьюя" # Український алфавіт
user_input = input("Введіть любий текст: ")
changed_user_input = ""
i=0 # лічильник #1
g=0 # лічильник #2

# Цикл, який провіряє чи є англійські букви в слові. Якщо є то міняє на наступні з алфавіту.
while i < len(user_input):
	while g < len(angl):
		if user_input[i] == angl[g]:
			changed_user_input = changed_user_input + angl[g+1]
			g=0
			break
		elif user_input[i] == angl[g].upper():
			changed_user_input = changed_user_input + angl[g+1].upper()
			g=0
			break
		g=g+1
	i=i+1

i=0
g=0

# Цикл, який провіряє чи є українські букви в слові. Якщо є то міняє на наступні з алфавіту.
while i < len(user_input):
	while g < len(ukr):
		if user_input[i] == ukr[g]:
			changed_user_input = changed_user_input + ukr[g+1]
			g=0
			break
		elif user_input[i] == ukr[g].upper():
			changed_user_input = changed_user_input + ukr[g+1].upper()
			g=0
			break
		g=g+1
	i=i+1

i=0
g=0

# Цикл, який провіряє чи є цифри в тексті. Якщо є то міняє на наступні.
while i < len(user_input):
	try:
		check = int(user_input[i])
		if check == int(user_input[i]):
			while g < len(number):
				if user_input[i] == number[g]:
					changed_user_input = changed_user_input + number[g+1]
					g=0
					break
				g=g+1
		i=i+1
	except:
		i=i+1
		
print(changed_user_input)	

