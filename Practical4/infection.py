# 1. Define initial variables:
#    - Total number of students in the class (total_students) = 91
#    - Initial number of infected students (initial_infected) = custom value (e.g. 5)
#    - Daily growth rate of infection (growth_rate) = custom value (e.g. 40% = 0.4)
#    - Counter for days elapsed (days) = 0
#
# 2. Print initial information to inform the user of simulation conditions
#
# 3. Loop to simulate daily infection spread until all students are infected:
#    a. Increment the day counter by 1
#    b. Calculate new infections = current infected * growth rate
#    c. Update total infected (ensure it does not exceed total students)
#    d. Print the day number and number of infected students
#
# 4. After loop ends, print the total number of days taken
total_students = 91 
initial_infected = 5  
growth_rate = 0.4     
infected = initial_infected 
days = 0 
print("=== IBI1 Class Infection Simulation ===")
print(f"Total number of students in class: {total_students}")
print(f"Initial number of infected students: {initial_infected}")
print(f"Daily infection growth rate: {growth_rate * 100}%")
print("----------------------------------------")

while infected < total_students:
    days += 1  
    new_infected = infected * growth_rate  
    infected += new_infected  
    if infected > total_students:
        infected = total_students
    
  
    print(f"Day {days}: Number of infected students = {infected}")
print("----------------------------------------")
print(f"Total days to infect all 91 students: {days} days")