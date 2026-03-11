# 1. Define input variables: age (years), weight (kg), gender (string), creatinine concentration (µmol/l)
# 2. Validate input values against allowed ranges:
#    - age: must be < 100
#    - weight: must be > 20 kg and < 80 kg
#    - creatinine (Cr): must be > 0 µmol/l and < 100 µmol/l
#    - gender: must be either "male" or "female" (case-insensitive)
# 3. If any input is invalid, collect and report which variable(s) need correction
# 4. If all inputs are valid, calculate CrCl using Cockcroft-Gault equation:
#    CrCl = ((140 - age) * weight) / (72 * Cr)
#    If female, multiply result by 0.85
# 5. Print the final CrCl result or the error message for invalid inputs
age =int(input("Enter your age(year):"))         
weight =int(input("Enter your weight(kg):"))       
gender = input("Enter your gender:")
cr = float(input("Enter your creatinine(µmol/l):"))          
errors = []
if age >= 100:
    errors.append("Age must be less than 100 years.")

if weight <= 20 or weight >= 80:
    errors.append("Weight must be greater than 20 kg and less than 80 kg.")

if cr <= 0 or cr >= 100:
    errors.append("Creatinine concentration must be greater than 0 µmol/l and less than 100 µmol/l.")

if gender.lower() not in ["male", "female"]:
    errors.append("Gender must be either 'male' or 'female'.")

if len(errors) > 0:
    print("=== Error: Invalid Input Values ===")
    for error in errors:
        print("- " + error)
else:
    crcl = ((140 - age) * weight) / (72 * cr)
    if gender.lower() == "female":
        crcl *= 0.85
    print("=== Creatinine Clearance Calculation ===")
    print(f"Age: {age} years")
    print(f"Weight: {weight} kg")
    print(f"Gender: {gender}")
    print(f"Creatinine concentration: {cr} µmol/l")
    print("----------------------------------------")
# 1. Define input variables: age (years), weight (kg), gender (string), creatinine concentration (µmol/l)
# 2. Validate input values against allowed ranges:
#    - age: must be < 100
#    - weight: must be > 20 kg and < 80 kg
#    - creatinine (Cr): must be > 0 µmol/l and < 100 µmol/l
#    - gender: must be either "male" or "female" (case-insensitive)
# 3. If any input is invalid, collect and report which variable(s) need correction
# 4. If all inputs are valid, calculate CrCl using Cockcroft-Gault equation:
#    CrCl = ((140 - age) * weight) / (72 * Cr)
#    If female, multiply result by 0.85
# 5. Print the final CrCl result or the error message for invalid inputs
age =int(input("Enter your age(year):"))         
weight =int(input("Enter your weight(kg):"))       
gender = input("Enter your gender:")
cr = float(input("Enter your creatinine(µmol/l):"))          
errors = []
if age >= 100:
    errors.append("Age must be less than 100 years.")

if weight <= 20 or weight >= 80:
    errors.append("Weight must be greater than 20 kg and less than 80 kg.")

if cr <= 0 or cr >= 100:
    errors.append("Creatinine concentration must be greater than 0 µmol/l and less than 100 µmol/l.")

if gender.lower() not in ["male", "female"]:
    errors.append("Gender must be either 'male' or 'female'.")

if len(errors) > 0:
    print("=== Error: Invalid Input Values ===")
    for error in errors:
        print("- " + error)
else:
    crcl = ((140 - age) * weight) / (72 * cr)
    if gender.lower() == "female":
        crcl *= 0.85
    print("=== Creatinine Clearance Calculation ===")
    print(f"Age: {age} years")
    print(f"Weight: {weight} kg")
    print(f"Gender: {gender}")
    print(f"Creatinine concentration: {cr} µmol/l")
    print("----------------------------------------")
    print(f"Estimated Creatinine Clearance (CrCl): {crcl:.2f} ml/min")