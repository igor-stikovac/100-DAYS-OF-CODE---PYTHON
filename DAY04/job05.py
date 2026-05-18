import random

random_number_0_to_10 = random.random() * 10
print(random_number_0_to_10)

random_float = random.uniform(1,10)
print(random_float)


head_or_tail = random.randint(0,1)

if( head_or_tail == 0):
    print("Head")       
else:    
    print("Tail")