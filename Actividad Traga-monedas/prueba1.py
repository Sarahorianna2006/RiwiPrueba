#import random
#random.randint (0, 100)



#Traga-Monedas 
import random

emojis= ["🍇","🍉","🍒"]


while True:
    n1 = random.choice(emojis)
    n2 = random.choice(emojis)
    n3 = random.choice(emojis)

    if n1 == n2 == n3:
        print("Lo lograste!💥💯")
        break
    elif n1 == n2 or n1 == n3 or n3 == n2:
        print("Casi lo logras🪄⭐")
    else:
        print("Sigue intentando🫣")
    
        
            
    input("")