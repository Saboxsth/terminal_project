#Terminal project
#A day in the life of Moneky.D.Luffy
# Luffy is a young, ambitious pirate who dreams of being the Pirate King.
import random 
print("Welcome to the Day in a life of the Straw Hat Pirates!")
print()
print("You are Monkey.D.Luffy, a cheerful young pirate who wants to be the Pirate King by finding the legendary treasure One Piece.")
print()
print("You are in the sea continuing your journey with your crew members.")
print("")
print('You have an 100 hp and 100 energy\nIf your hp is 0, you die and your energy depletes every time you attack or defend!')
print()
print("You find an island to explore and you start your adventure!")
print()
print("You see someone in the distance and go in for a closer look.")
print()

luffy = 100
energy=150
crocodile=100

#Enounter 1
rng= random.randint(1,3)
if rng== 1:
    print("The shadow seems to be Crocodile!")
    print("He challenges you to a duel to take revenge on you for destroying his plan to take over Alabasta.")
    print("He uses his move 'Sand Storm!'")
    luffy-=16
    print("He caught you off guard and you took 16 damage!")
    print()

    while crocodile>0 and luffy>0:
        print("You have 3 move set! You use energy each time you use your moves")
        print("It's now your turn to attack, choose your move!")
        print("1)Gomu Gomu no: Pistol (30 Energy)\n2)Gomu Gomu no: Bazooka (45 Energy)\n3)Gomu Gomu no: Gattling Gun (50 Energy)")
        move = (int(input("Choose your move: ")))
        print()
    
        if move== 1 and energy>=30:
            energy-=30
            damage= random.randint(15,30)
            crocodile-=damage
            print(f"You hit Crocodile for {damage} damage!")
            print(f"Crocodile hp = {crocodile}")
            print(f"Your Energy = {energy}")

        elif move==2 and energy>=45:
            energy-=45
            damage= random.randint(20,45)
            crocodile-= damage
            print(f"You hit Crocodile for {crocodile}\nCrocodile hp= {crocodile}")
            print(f"Your Energy = {energy}")

        elif move==3 and energy>=50:
            energy-=50
            damage= random.randint(45,60)
            crocodile-=damage
            print(f"You hit Crocodile for {damage} damage!\nCrocodile hp ={crocodile}")
            print(f"Your Energy= {energy}")

        else:
            print("Insufficient Energy!")   

        if crocodile >=0:    
            damage= random.randint(30,50)
            luffy-=damage
            print(f'Crocodile hits you for {damage}damage!')
        print()
        if crocodile<=0:
            print("Congratulations! You have defeated Crocodile!")
            
        elif luffy<=0:
            print("You have been defeated! Better luck next time!")    
        print(f'Your hp =  {luffy}')



#Encounter 2
if rng==2:
    whitebeard= 150
    print("You meet the strongest man alive Whitebeard!")
    print('He wants to you to join his crew, if you refuse he is gonna fight you to death!')
    choice= int(input("What will you choose?:\n1)Accept his offer\n2)Refuse his offer"))

    if choice==1:
        print('You failed at being the pirate king and your crew hates you now.\nThe End')

    if choice==2:
        while whitebeard>=0 and luffy>=0:
            print('Whitebeard seems to be mad and he is getting ready for a fight!')
            print('Normal attacks will not work because his def is too high.\nYou can use enhanced attacks but it takes greater amount of energy to pull it off.')
            print('You have 3 moves set to fight Whitebeard. Each moves depletes your energy by certain amount.')
            print("1)Gomu Gomu no: Red hawk (40 Energy)\n2)Gomu Gomu no: Elephant Gun (60 Energy)\n3)Gomu Gomu no: Grizzly Magnum (70 Energy)")
            move = (int(input("Choose your move: ")))

            if move== 1 and energy>=40:
                energy-=40
                damage= random.randint(40,60)
                whitebeard-=damage
                print(f"You hit Whitebeard for {damage} damage!")
                print(f"Whitebeard hp = {whitebeard}")
                print(f"Your Energy = {energy}")

            elif move==2 and energy>=60:
                energy-=60
                damage= random.randint(60,75)
                whitebeard-= damage
                print(f"You hit Whitebeard for {damage}damage\nWhitebeard hp= {whitebeard}")
                print(f"Your Energy = {energy}")

            elif move==3 and energy>=70:
                energy-=70
                damage= random.randint(75,100)
                whitebeard-=damage
                print(f"You hit Whitebeard for {damage} damage!\nWhitebeard hp ={whitebeard}")
                print(f"Your Energy= {energy}")

            else:
                print("Insufficient Energy!")   

            if whitebeard >=0:    
                damage= random.randint(30,50)
                luffy-=damage
                print(f'Whitebeard hits you for {damage}damage!')
            print()
            if whitebeard<=0:
                print("Congratulations! You have defeated Whitebeard!")
            
            elif luffy<=0:
                print("You have been defeated! Better luck next time!")    
                print(f'Your hp =  {luffy}')
            
