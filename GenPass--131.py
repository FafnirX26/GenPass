import string, random

print("Welcome to GenPass\n")

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
    print('It is recommend to use 8+ characters in a password, but it is up to you')
    dl = int(input('How many letters do you need in your password: '))
    if dl < 8:
        confirmed = input('You have selected a length below the recommended length. Are you sure you want to continue? [y/n]: ')
        if confirmed.lower().strip() == 'n':
            quit()
            
except ValueError:
    print('Enter an integer value!')
    quit()

print("\nHere are 5 possible passwords!\n")
print("Thanks for using GenPass")
