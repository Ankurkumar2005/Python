# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database")

# s1 = student("Ankur", 387)
# print(s1.name, s1.marks)

# s2 = student("Anmol", 398)
# print(s2.name,s2.marks)



class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
            print("hi", self.name, "Your average score is : ",sum/3)


s1 = student("Ankur",[98,97,87])        
s1.get_avg()