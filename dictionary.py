students={"name" : "meet" , "age" : 20 , "course" : "datascience"}
print(students["name"])

print(students.get("age"))

students["course"]="data science"
print(students)

students.pop("age")
print(students)

print(students.keys())

print(students.values())

print(students.items())

