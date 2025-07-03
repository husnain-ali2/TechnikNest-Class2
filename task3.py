# Declare variables of different types
name = "Ali"            # string
age = 25                # integer
height = 5.9            # float
is_student = True       # boolean
z = 2 + 3j              # complex

# Print values and types
print("Print Values and Data Types:")
print(f"name= {name}.......{type(name)}")
print(f"age= {age}..........{type(age)}")
print(f"height= {height}.......{type(height)}")
print(f"is_student= {is_student}.......{type(is_student)}")
print(f"z= {z}..........{type(z)}")

print("\nAfter Conversion:")
# Convert string to float (will fail)
try:
    name_float = float(name)
except ValueError:
    name_float = "Cannot convert string to float"
print(f"name to float= {name_float}     => {type(name_float)}")

# Convert integer to string
age_str = str(age)
print(f"age to str= {age_str}                                      => {type(age_str)}")

# Convert float to integer
height_int = int(height)
print(f"height to int= {height_int}                                     => {type(height_int)}")

# Convert boolean to string
is_student_str = str(is_student)
print(f"is_student to str= {is_student_str}                            => {type(is_student_str)}")
# Convert complex to float (will fail)
try:
    z_float = float(z)
except TypeError:
    z_float = "Cannot convert complex to float"
print(f"z to float={z_float}           => {type(z_float)}")
