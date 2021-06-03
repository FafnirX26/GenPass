import string, random, sys, json
data = open("data.json", "W")
print("Welcome to GenPass\n")
print("You are currently using GenPass 1.3.7\n")

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
    dl = int(input('How many letters do you want in your password: ').strip())
    if dl < 8:
        confirmed = input('You have selected a length below the recommended length. Are you sure you want to continue? [y/n]: ')
        if confirmed.lower().strip() == 'n':
            sys.exit("Thanks for using GenPass.")
except ValueError:
    sys.exit("Enter an appropriate value!")
    
try: 
    num_of_pwords = int(input('How many passwords do you want: ').strip())
except: 
    sys.exit("Enter an appropriate value!")
print("\nHere are your possible passwords:\n")

passwords_generated = []
for i in range(num_of_pwords):
    pword = gen_password(dl)
    print("Password",str(i + 1),pword,'\n')
    passwords_generated.append(pword)

pword_choice = passwords_generated[int(input('Enter the number of your choice: '))]
site_name = input('Enter the site name where this password will be used: ')
uname = input('What username have you chose for this site: ')

curr_pword_full_details = {
    "un": uname,
    "pw": pword_choice,
    "sn": site_name
}
data.write(json.dumps(curr_pword_full_details))
print("Your data has been saved locally.")
print("Thanks for using GenPass.")
