from student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)
student3 = Student("Oscar", "Accounting", 3.5, False)

print(student1.name)
student2.set_major("Finance")
print(student2.major)
print(student3.on_honor_roll())
