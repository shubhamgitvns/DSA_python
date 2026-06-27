# Dictionary (dist) is a collection of data type which store the data in the form of key & value

Student ={
    'name': 'shubham',
    'age': 22
}
print(type(Student))

# Add new data 

Student['city']='Varanasi'

# Uupdate the data
Student['age']=25

# Access the data

print(Student['name'])

# Access the data usning get()

print(Student.get('age'))

# Pop the data

Student.pop('age')
print(Student)

# Delete the data 

del Student['city']
print(Student)

# Acces the key 
print(Student.keys())

# clear the dist
Student.clear()
print(Student)
