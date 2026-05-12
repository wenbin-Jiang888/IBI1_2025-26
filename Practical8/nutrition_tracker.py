class food_item:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat


def calculate_daily_nutrition(food_list):
    total_cal = 0
    total_pro = 0
    total_carbs = 0
    total_fat = 0

    for food in food_list:
        total_cal += food.calories
        total_pro += food.protein
        total_carbs += food.carbs
        total_fat += food.fat

    print("=== 24-Hour Nutrition Summary ===")
    print(f"Total calories: {total_cal} kcal")
    print(f"Total protein: {total_pro} g")
    print(f"Total carbohydrates: {total_carbs} g")
    print(f"Total fat: {total_fat} g")

    if total_cal > 2500:
        print("Warning: Calorie intake exceeds 2500 kcal!")
    if total_fat > 90:
        print("Warning: Fat intake exceeds 90 g!")

    return total_cal, total_pro, total_carbs, total_fat


food_database = {
    "apple": food_item("Apple", 60, 0.3, 15, 0.5),
    "rice": food_item("Rice", 130, 2.7, 28, 0.3),
    "chicken": food_item("Chicken breast", 165, 31, 0, 3.6),
    "cake": food_item("Cake", 400, 4, 50, 20)
    }

food_list = []
print("Enter food names (one per line, enter blank line to finish):")

while True:
    line = input().strip()
    if not line:
        break
    food_name = line.lower()
    if food_name not in food_database:
        print("ERROR")
    else:
        food_list.append(food_database[food_name])

calculate_daily_nutrition(food_list)