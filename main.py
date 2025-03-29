"""
12/3/25 
Made By Sarvesh Thiagarajan
This program creates a password based on answers the user
gives to a few preference based questions.
"""
#Introduction
print("⣿⣿⣿⣿⣿⠟⠁⣠⣶⣦⣤⣶⣶⣶⣶⣤⣀⣀⣀⣈⠉⠁⣤⣤⣄")
print("⣿⣿⣿⡿⠁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢀⣼⣿⠿")
print("⣿⣿⣿⠁⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⢀⠐⠈⢁⣀")
print("⣿⣿⠇⢀⣿⡿⠿⠛⠋⠉⠉⠉⢀⢀⣀⣀⣠⣤⣼⣷⣾⣿⣿⡿")
print("⠿⠏⢀⡾⢀⢀⣀⣀⣠⣤⣶⡶⠞⣿⣿⣉⡟⣬⢙⠿⣿⣿⠏⠁⣰")
print("⣤⣤⡴⣷⠛⣿⣿⣿⣿⣿⣿⠇⢀⠙⠻⢿⣿⣧⡾⠶⢻⠛⢀⣼⣿")
print("⠘⠻⢶⣯⡝⢠⣍⣻⣿⣿⠋⢀⢀⢀⢀⢀⢀⢀⢀⢀⡿⢀⣼⣿⣿")
print("⢀⢀⢀⠙⣟⠋⠉⠉⢀⢀⠠⠴⠖⠛⠉⢀⢀⢀⢀⣼⠁⣰⣿⣿⣿")
print("⢀⢀⢀⢀⠈⢧⣀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⣠⠞⠁⣠⣿⣿⣿⣿")
print("⢀⢀⢀⢀⣠⣀⠈⠓⠦⣄⣀⣀⣀⣀⣤⣴⣾⠁⢠⣾⣿⣿⣿⣿⣿")
print("⢀⢀⢀⣸⣿⣿⣿⣦⣄⢀⢹⣿⣿⣿⣿⣿⣿⡆⠈⣿⣿⣿⣿⣿⣿")
print("⢀⢀⣼⣿⣿⣿⣿⣿⡏⢀⢸⣿⣿⣿⣿⣿⣿⣷⢀⢻⣿⣿⣿⣿⡟")
print("⢀⠘⠛⠛⠛⠛⠛⠛⢀⢀⠘⠛⠛⠛⠛⠛⠛⠛⠃⢀⠛⠛⠛⠛")
print("𝑺𝒂𝒓𝒗𝒆𝒔𝒉 𝑻𝒉𝒊𝒂𝒈𝒂𝒓𝒂𝒋𝒂𝒏 𝑷𝒓𝒆𝒔𝒆𝒏𝒕𝒔")
print("The ingenous password creator 😱")
print("--------------------------------------")

print("This program will create a password\nbased on your answers to the questions\nbelow!")
print("--------------------------------------")

#This function removes spaces in a user input and replaces it
#with and exclamation mark.
def remove_space(phrase):
    while " " in phrase:
        index = phrase.find(" ")
        new_phrase = phrase[:index] + "!" + phrase[index + 1:]
        phrase = new_phrase
    return phrase

#This function reverses a word it is given
def reverse(word):
    phrase = ""
    for i in range(len(word)):
        phrase = word[i] + phrase
    return remove_space(phrase)

#This function splits an input based on the length of the input
#and adds the split input to a capitalised version of the first
#letter of the input
def caps(word):
    new_word = word.lower()
    case = new_word[0].upper() 
    if round(len(new_word)/9) > 5:
        end = 4
    elif round(len(new_word)/9) < 4:
        end = 3
    else:
        end = round(len(new_word)/9)
    final = case + new_word[2:end]
    return final

#This function compiles all the inputs together to make a password
#It also calls the other functions to edit the inputs.
def password_creator(day,movie,num,president,car):
    day = day.upper()
    num = len(movie) * num
    new_num = str(num)[-1]
    updated_pres = caps(president)
    president = remove_space(updated_pres)
    new_car = remove_space(car)
    if len(car) > 15:
        symbol = "?"
    else:
        symbol = "$"
    return president + remove_space(day[:2]) + str(new_num) + reverse(movie)[:3] + symbol + reverse(new_car[-2:])

    
#This bit of code asks the user for their input and strips it to
#make sure the password can handle it properly. It also checks
#if the user entered value is valid, if not, it will just set the
#input value as a default value
date = input(str("1. What month were you born in? "))
new_date = date.strip()

if new_date == "" or len(new_date) < 2 :
    print("\n⛔  This isn't a valid input so a default value will be used!")
    new_date = "I was never born"

movie = input(str("\n2. What is your favourite movie? "))
new_movie = movie.strip()
if len(new_movie) < 2 or new_movie == "":
    print("\n⛔  This isn't a valid input so a default value will be used!")
    new_movie = "Terminator 2 judgement day"
    
president = input(str("\n3. Who is your favourite president? "))
new_president = president.strip()
if len(new_president) < 2 or new_president == "":
    print("\n⛔  This isn't a valid input so a default value will be used!")
    new_president = "John F Kennedy"
    
car = input(str("\n4. What is your favourite car? "))
new_car = car.strip()
if len(new_car) < 2 or new_car == "":
    print("\n⛔  This isn't a valid input so a default value will be used!")
    new_car = "2006 Honda Civic"
    
#This if statement checks the length of the movie input
#and feeds a number based on the input to the function
#that combines the password together.
if len(new_movie) > 6:
    num = 8
else:
    num = 3
    
#This final bit of code outputs the newly created password
print("--------------------------------------")
print("Your school password is: " + password_creator(new_date,new_movie,num,new_president,new_car))
