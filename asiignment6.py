grade = [55,70,65,40,90,85,50,77]

passed_with_bonus = [grade * 1.05 for grade in grade if grade >= 60]
print("Grades after applying bonus for passing students:", passed_with_bonus)
