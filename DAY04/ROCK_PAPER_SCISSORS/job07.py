import rock_paper_scissors
import random   

igrac = int(input("Unesite 0 za kamen, 1 za papir i 2 za makaze: "))

print("Igrac je odabrao: " + rock_paper_scissors.rock_paper_scissors_list[igrac] + "\n")

computer = random.randint(0,2)

print("Racunar je odabrao: " + rock_paper_scissors.rock_paper_scissors_list[computer] + "\n")

if igrac == computer:
    print("Nerešeno!")
elif (igrac == 0 and computer == 2) or (igrac == 1 and computer == 0) or (igrac == 2 and computer == 1):
    print("Pobedio je igrač!")
else:
    print("Pobedio je računar!")