import random
#clear()
from replit import clear
from game_data import data
import art

person_A = random.choice(data)

score = 0

def generate_person_B(random_person_A):
    
    while True:
        random_person_B = random.choice(data)
        if random_person_A != random_person_B:
            break
        
    return random_person_B

while True:
    clear()
    print(art.logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    
    print(f"Compare A: {person_A['name']}, a {person_A['description']}, from {person_A['country']}.")
    
    person_B = generate_person_B(person_A)
    
    print(art.vs)
    print(f"Against B: {person_B['name']}, a {person_B['description']}, from {person_B['country']}.")
        
    unser_type =  input("Who has more followers? Type 'A' or 'B': ").lower()
    
    print(score)
    
    if person_A['follower_count'] > person_B['follower_count'] and unser_type == 'a':
        score += 1
        person_A = person_B
        
    elif person_B['follower_count'] > person_A['follower_count'] and unser_type == 'b':
        score += 1
        person_A = person_B
        
    else:
        clear()
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break

