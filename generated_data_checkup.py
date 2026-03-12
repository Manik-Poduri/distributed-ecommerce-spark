# this script isn't necessary for data generation. It merely goes over the generated data to check its correctness and proivde some statistics.
# It's a good idea to run this script after running data_generation.py to learn a few stats about the generated data.

from tqdm import tqdm
import csv

# read the people_dict from the people_with_handshake_info.csv file
people_with_handshake_info = {}
with open("Task1/output/people_with_handshake_info.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in tqdm(reader):
        id = int(row[0])
        x = float(row[1])
        y = float(row[2])
        first_name = row[3]
        last_name = row[4]
        age = int(row[5])
        email = row[6]
        occupation = row[7]
        home_city = row[8]
        activated = row[9] == "True"
        
        people_with_handshake_info[id] = {
            "id": id,
            "x": x,
            "y": y,
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "email": email,
            "occupation": occupation,
            "home_city": home_city,
            "activated": activated
        }
        
print("people_with_handshake_info.csv was read successfully.")
print("\n")
print("\n")
print("\n")

# print the number of people in the people_with_handshake_info dictionary
print(f"Number of people: {len(people_with_handshake_info)}")

# print the number of activated people
activated_count = 0
for id in people_with_handshake_info:
    if people_with_handshake_info[id]["activated"]:
        activated_count += 1
print(f"Number of activated people: {activated_count}")
print("\n")

# print number of people in 6 unit manhattan distance to activated people.
def manhattan_distance_check(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2) <= 6
    
people = []
activated = []

sum_of_contacts = 0

for entry in tqdm(people_with_handshake_info):
    if people_with_handshake_info[entry]["activated"]:
        activated.append(people_with_handshake_info[entry])
    else:
        people.append(people_with_handshake_info[entry])
        
for zombie in tqdm(activated):
    for person in people:
        if manhattan_distance_check(zombie["x"], person["x"], zombie["y"], person["y"]):
            sum_of_contacts += 1
            
print(f"Number of contacts with activated people: {sum_of_contacts}")
print("\n")




# make a few stats about x and y, like how often people are in the same location and print the most common locations
x_y_dict = {}
for id in people_with_handshake_info:
    x = people_with_handshake_info[id]["x"]
    y = people_with_handshake_info[id]["y"]
    if (x, y) in x_y_dict:
        x_y_dict[(x, y)] += 1
    else:
        x_y_dict[(x, y)] = 1
        
print(f"Number of unique locations: {len(x_y_dict)}")

# print the most common locations with the number of people in each location
sorted_x_y_dict = sorted(x_y_dict.items(), key=lambda x: x[1], reverse=True)
print("Most common locations:")

for i in range(10):
    print(f"{sorted_x_y_dict[i][0]}: {sorted_x_y_dict[i][1]}")
    

print("\n")
    
# print the number of people in each age group
age_dict = {}
for id in people_with_handshake_info:
    age = people_with_handshake_info[id]["age"]
    if age in age_dict:
        age_dict[age] += 1
    else:
        age_dict[age] = 1
        
print("Number of people in each age group:")
for age in age_dict:
    print(f"{age}: {age_dict[age]}")
    

print("\n")

# print the number of people who are activated and not activated in each age group
activated_age_dict = {}
not_activated_age_dict = {}

for id in people_with_handshake_info:
    age = people_with_handshake_info[id]["age"]
    activated = people_with_handshake_info[id]["activated"]
    if activated:
        if age in activated_age_dict:
            activated_age_dict[age] += 1
        else:
            activated_age_dict[age] = 1
    else:
        if age in not_activated_age_dict:
            not_activated_age_dict[age] += 1
        else:
            not_activated_age_dict[age] = 1
            
print("Number of activated people in each age group:")
for age in activated_age_dict:
    print(f"{age}: {activated_age_dict[age]}")
    
    
print("\n")

# print the top 10 most common occupations
occupation_dict = {}

for id in people_with_handshake_info:
    occupation = people_with_handshake_info[id]["occupation"]
    if occupation in occupation_dict:
        occupation_dict[occupation] += 1
    else:
        occupation_dict[occupation] = 1
    
sorted_occupation_dict = sorted(occupation_dict.items(), key=lambda x: x[1], reverse=True)
print("Most common occupations:")
for i in range(10):
    print(f"{sorted_occupation_dict[i][0]}: {sorted_occupation_dict[i][1]}")


print("\n")

# print the top ten most common occupations for activated people
activated_occupation_dict = {}

for id in people_with_handshake_info:
    occupation = people_with_handshake_info[id]["occupation"]
    activated = people_with_handshake_info[id]["activated"]
    if activated:
        if occupation in activated_occupation_dict:
            activated_occupation_dict[occupation] += 1
        else:
            activated_occupation_dict[occupation] = 1
            
sorted_activated_occupation_dict = sorted(activated_occupation_dict.items(), key=lambda x: x[1], reverse=True)
print("Most common occupations for activated people:")
for i in range(10):
    print(f"{sorted_activated_occupation_dict[i][0]}: {sorted_activated_occupation_dict[i][1]}")
    
    
print("\n")

# print the top 10 most common home cities
home_city_dict = {}

for id in people_with_handshake_info:
    home_city = people_with_handshake_info[id]["home_city"]
    if home_city in home_city_dict:
        home_city_dict[home_city] += 1
    else:
        home_city_dict[home_city] = 1
        
sorted_home_city_dict = sorted(home_city_dict.items(), key=lambda x: x[1], reverse=True)

print("Most common home cities:")
for i in range(10):
    print(f"{sorted_home_city_dict[i][0]}: {sorted_home_city_dict[i][1]}")
    

print("\n")

# print the top ten most common home cities for activated people
activated_home_city_dict = {}

for id in people_with_handshake_info:
    home_city = people_with_handshake_info[id]["home_city"]
    activated = people_with_handshake_info[id]["activated"]
    if activated:
        if home_city in activated_home_city_dict:
            activated_home_city_dict[home_city] += 1
        else:
            activated_home_city_dict[home_city] = 1
            
sorted_activated_home_city_dict = sorted(activated_home_city_dict.items(), key=lambda x: x[1], reverse=True)
print("Most common home cities for activated people:")
for i in range(10):
    print(f"{sorted_activated_home_city_dict[i][0]}: {sorted_activated_home_city_dict[i][1]}")
    
    
print("\n")

# print the top ten most used email domains
email_domain_dict = {}

for id in people_with_handshake_info:
    email = people_with_handshake_info[id]["email"]
    domain = email.split("@")[1]
    if domain in email_domain_dict:
        email_domain_dict[domain] += 1
    else:
        email_domain_dict[domain] = 1
        
sorted_email_domain_dict = sorted(email_domain_dict.items(), key=lambda x: x[1], reverse=True)
print("Most common email domains:")
for i in range(10):
    print(f"{sorted_email_domain_dict[i][0]}: {sorted_email_domain_dict[i][1]}")
    

print("\n")

# print the top ten most common email domains for activated people
activated_email_domain_dict = {}

for id in people_with_handshake_info:
    email = people_with_handshake_info[id]["email"]
    domain = email.split("@")[1]
    activated = people_with_handshake_info[id]["activated"]
    if activated:
        if domain in activated_email_domain_dict:
            activated_email_domain_dict[domain] += 1
        else:
            activated_email_domain_dict[domain] = 1
            
sorted_activated_email_domain_dict = sorted(activated_email_domain_dict.items(), key=lambda x: x[1], reverse=True)
print("Most common email domains for activated people:")
for i in range(10):
    print(f"{sorted_activated_email_domain_dict[i][0]}: {sorted_activated_email_domain_dict[i][1]}")
    
    
print("\n")
    
print("Data checkup complete.")

