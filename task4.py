input=input("Enter a value: ")
value = input.strip()


if value.isdigit():
    print("Integer!")
elif "." in value and value.replace(".","").isdigit():
    print("Float!")
else:
    print("String!")