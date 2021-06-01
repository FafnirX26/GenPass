import string, random, pyperclip

print("Welcome to GenPass\n")
should_be_copied = input("Would you like to use the copy feature? (It might not work) [y/n]: ")

def gen_password(length):
    password = ''
    for a in range(length):
        char_type = random.choice([1, 2, 3])
        if char_type == 1:
            password += random.choice(string.ascii_letters)
        elif char_type == 2:
            password += str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
        else:
            password += random.choice(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ">", "<", ',', '.', '`', '~', '?', '/'])
    return password
    
try:
    print('We recommend using 8+ characters in a password, but it is up to you')
    dl = int(input('How many letters do you need in your password: '))
    if dl < 8:
        confirmed = input('You have selected a length below our recommended length. Are you sure you want to continue? [y/n]: ')
        if confirmed.lower().strip() == 'n':
            quit()
            
except ValueError:
    print('Enter an integer value!')
    quit()

print("\nHere are 5 possible passwords!\n")

password_list = []

for i in range(10):
    pword_generated = gen_password(dl)
    print("Password", str(i + 1) + ':', pword_generated, "\n")
    password_list.append(pword_generated)
	
if should_be_copied.strip().lower() == 'y':
	pword_choice = int(input("Enter the number of the password you want to copy to your clipboard: "))
	pyperclip.copy(password_list[pword_choice - 1])



print("Thanks for using GenPass")