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

print(Student)

# Access the data

print(Student['name'])

# Access the data usning get()

print(Student.get('age'))

# Delete the data 

del Student['city']
print(Student)

# clear the dist
Student.clear()
print(Student)
