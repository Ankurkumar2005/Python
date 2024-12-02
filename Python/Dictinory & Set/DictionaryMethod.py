
student = {
    "name" : "Ankur Kumar",
    "Subject" : {
        "Phy" : 89,
        "Che" : 91,
        "Math" : 98
    }
}
# print(list(student.keys()))   #{returns all keys}

# print(list(student.values()))  #{returns all values}

# print(list(student.items()))   #{returns all pairs as tuples}

# print(student.get("key"))    #{returns the key according to value}

student.update({"city" : "Delhi"})
print(student)