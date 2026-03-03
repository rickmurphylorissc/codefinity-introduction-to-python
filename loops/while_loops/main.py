#First variable is and integer 
start_number = 5
#Second variable is a list []
countdown_values = []
#Third variable is to record steps
counter = start_number

while counter > 0:
    countdown_values.append(counter)
    print(f"Remaining time: {countdown_values} hours")    
    counter -= 1
    

print("Discount countdown complete!")
print(counter)