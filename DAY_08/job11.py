def calculate_love_score(name1, name2):
    combined_names = name1.lower() + name2.lower()
    true_count = 0
    for letter in combined_names:
        if letter in "true":
            true_count += 1
    for letter in combined_names:
        if letter in "love":
            true_count += 1

    love_score = int(str(true_count)+str(true_count))
    print(f"{name1} and {name2} your love score is: {love_score}")

print("Welcome to the Love Calculator!")
name1 = input("What is his name? \n")
name2 = input("What is her name? \n")
calculate_love_score(name1, name2)