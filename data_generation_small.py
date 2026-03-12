from random import randint, choice
from tqdm import tqdm

# define a few constants to be used in the data generation
PEOPLE_AMOUNT = 10_000
ACTIVATED_PROBABILITY = 25
AREA_LIMIT_X = 10_000
AREA_LIMIT_Y = 10_000

# load data lists from file for later use
first_names = []
with open("utilities/first_names.txt", "r") as f:
    first_names = f.read().splitlines()
    
last_names = []
with open("utilities/last_names.txt", "r") as f:
    last_names = f.read().splitlines()
    
mail_providers = []
with open("utilities/mail_providers.txt", "r") as f:
    mail_providers = f.read().splitlines()

occupations = []
with open("utilities/occupations.txt", "r") as f:
    occupations = f.read().splitlines()
    
places = []
with open("utilities/places.txt", "r") as f:
    places = f.read().splitlines()
    
usernames = []
with open("utilities/usernames.txt", "r") as f:
    usernames = f.read().splitlines()
    
    
# method that creates usernames of a good length by appending random usernames from the list
def nickname_generator(namestart):
    new_nickname = namestart + choice(usernames)
    if len(new_nickname) < 15:
        new_nickname = nickname_generator(new_nickname + "_" )
    if len(new_nickname) > 30:
        new_nickname = new_nickname[:20]
    return new_nickname


# method that creates a random email address
def create_email():
    return nickname_generator("") + "@" + choice(mail_providers)
    


if __name__ == '__main__':
    
    # Prepare variables to store generated data into
    people_dict = {}
    activated_dict = {}
    people_with_handshake_info = {}
    
    # start by generating the people dictionary, as the other dictionaries depend on it
    for i in tqdm(range(PEOPLE_AMOUNT)):
        id = i
        x = randint(0, AREA_LIMIT_X)
        y = randint(0, AREA_LIMIT_Y)
        first_name = choice(first_names)
        last_name = choice(last_names).capitalize()
        age = randint(18, 100)
        email = create_email()
        occupation = choice(occupations)
        home_city = choice(places)
        
        people_dict[id] = {"id": id, 
                           "x": x, 
                           "y": y, 
                           "first_name": first_name, 
                           "last_name": last_name, 
                           "age": age, 
                           "email": email, 
                           "occupation": occupation, 
                           "home_city": home_city}
        
    print("people_dict was generated successfully.")
    print()
    print()
    print()
    print()
        
    # generate the activated dictionary, which is a subset of the people dictionary
    for id in tqdm(people_dict):
        if randint(0, 100) < ACTIVATED_PROBABILITY:
            activated_dict[id] = people_dict[id]
            
    print("activated_dict was generated successfully.")
    print()
    print()
    print()
    print()
            
    # generate the people with handshake info dictionary, which is a combination of the people and activated dictionaries
    for id in tqdm(people_dict):
        if id in activated_dict:
            people_with_handshake_info[id] = people_dict[id]
            people_with_handshake_info[id]["activated"] = True
        else:
            people_with_handshake_info[id] = people_dict[id]
            people_with_handshake_info[id]["activated"] = False
        

    print("people_with_handshake_info was generated successfully.")
    print()
    print()
    print()
    print()
    print("Data generation complete.")
    print()
    print()
    print()
    print()
    
    # write each dictionary to a csv file
    with open("Task1/output/people_small.csv", "w") as f:
        f.write("id,x,y,first_name,last_name,age,email,occupation,home_city\n")
        for id in people_dict:
            person = people_dict[id]
            f.write(f"{person['id']},{person['x']},{person['y']},{person['first_name']},{person['last_name']},{person['age']},{person['email']},{person['occupation']},{person['home_city']}\n")
            
    print("people.csv saved successfully.")
    print()
    print()
    print()
    print()
            
    with open("Task1/output/activated_small.csv", "w") as f:
        f.write("id,x,y,first_name,last_name,age,email,occupation,home_city\n")
        for id in activated_dict:
            person = activated_dict[id]
            f.write(f"{person['id']},{person['x']},{person['y']},{person['first_name']},{person['last_name']},{person['age']},{person['email']},{person['occupation']},{person['home_city']}\n")
            
    print("activated.csv saved successfully.")
    print()
    print()
    print()
    print()
            
    with open("Task1/output/people_with_handshake_info_small.csv", "w") as f:
        f.write("id,x,y,first_name,last_name,age,email,occupation,home_city,activated\n")
        for id in people_with_handshake_info:
            person = people_with_handshake_info[id]
            f.write(f"{person['id']},{person['x']},{person['y']},{person['first_name']},{person['last_name']},{person['age']},{person['email']},{person['occupation']},{person['home_city']},{person['activated']}\n")  
            
    print("people_with_handshake_info.csv saved successfully.")
    print()
    print()
    print()
    print()
            
    print("Data written to csv files.")