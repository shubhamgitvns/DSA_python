# Dictionary (dist) is a collection of data type which store the data in the form of key & value

Student ={
    'name': 'shubham',
    'age': 22,
    'city': 'varanasi'
}

# Print key using loop
for key in Student:
    print(key)

# Print value using loop 
for value in Student.values():
    print(value)

for key, value in Student.items():
    print(key,value)


