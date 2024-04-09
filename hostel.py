#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import pandas as pd

stu_database = 'Hostel_Student_Data.csv'
room_cap= 'Hostel_Room_Capacity.csv'
# try:
#     dc=pd.read_csv(stu_database)
# except pd.errors.EmptyDataError:
#     l=list(dc['RollNumber'])
# l=list()
rc = pd.read_csv(room_cap)
x = rc['Room Capacity'].tolist()
room_no = pd.read_csv(room_cap, index_col='Room NO')
stu_count = {i: 0 for i in room_no.index}

try:
    df = pd.read_csv(stu_database)
except pd.errors.EmptyDataError:
    df = pd.DataFrame(columns=['Name', 'RollNumber', 'AllocatedRoom'])
l=list(df['RollNumber'])
df.to_csv(stu_database,index=False)
# df.columns=['Name', 'RollNumber', 'AllocatedRoom']

def display_menu():
    print(" Hostel Management System")
    print("---------------------------")
    print("1. Allocate Room")
    print("2. Reallocate Room")
    print("3. Vacate Room")
    print("4. Search Resident")
    print("5. Quit")
def allocate_room():
    global df
    global stu_count
    global stu_database
    global l
    name = input("Name: ")
    roll_no= int(input("Roll number: "))
    allocated_room = int(input("Room number: "))
    df = pd.read_csv(stu_database)
    if name is None or roll_no is None or allocated_room is None:
        print("Enter data correctly")
        return
    if roll_no in l:
        print("student already exist")
        return
    if allocated_room not in stu_count:
        print("Invalid room number. Please choose another room.")
        return
    stu_count[allocated_room] += 1
    if stu_count[allocated_room] > room_no.loc[allocated_room, 'Room Capacity']:
        print("Room is full. Please choose another room.")
        stu_count[allocated_room] -= 1
        return
    df = pd.DataFrame({"Name": [name], "RollNumber": [roll_no], "AllocatedRoom": [allocated_room]})
    df.to_csv(stu_database,mode='a', index=False,header=False)
    l.append(roll_no)
    print("Room allocated successfully.")
#     print(df)

def reallocate_room():
    global df
    global stu_count
    global stu_database 
    global l
#     print(l)
    roll_no = int(input("Enter Roll Number to update: "))
    if roll_no is None:
        print("Enter data correctly")
        return
#     print(df[1])
    df = pd.read_csv(stu_database)
    if roll_no not in l:
        print("Student not found.")
        return
    
    new_allocated_room = int(input("Enter new Room number: "))
    
    if new_allocated_room not in stu_count:
        print("Invalid room number. df.to_csv(stu_database, index=False)Please choose another room.")
        return
        
    if stu_count[new_allocated_room] >= room_no.loc[new_allocated_room, 'Room Capacity']:
        print("Room is full. Please choose another room.")
        return
    y=l.index(roll_no)
#     print(y)
    allocated_room=df.loc[y][2]
    stu_count[allocated_room] -= 1
    stu_count[new_allocated_room] += 1
    df.loc[y, ['AllocatedRoom']] = new_allocated_room
    df.to_csv(stu_database, index=False)
    print("Room reallocated successfully.")
    
def vacate_room():
    global df
    global stu_count
    global stu_database 
    
    roll_no = int(input("Enter Roll Number to update: "))
    if roll_no is None:
        print("Enter data correctly")
        return
    if  roll_no not in l:
        print("Student not found.")
        return
    y=l.index(roll_no)
    confirmation = input(f"Are you sure you want to vacate the room for {roll_no} (y/n)? ").lower()
    vacating_room=df.loc[y][2]
    print(vacating_room)
    if confirmation == 'y':
        stu_count[vacating_room] -= 1
        df=df[df['RollNumber']!=roll_no]
        df.to_csv(stu_database, index=False)
#         df.drop(index=df[df['RollNumber']==roll_no].index)
        print(roll_no,'has vacated',vacating_room)
    elif confirmation == 'n':
        print("Vacation canceled.")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        
def search_by_roll_number(roll_number):
    result = df[df['RollNumber'] == int(roll_number)]

    if not result.empty:
        print(result)
    else:
        print(f"No resident found with Roll Number: {roll_number}")

def search_by_name(name):
    result = df[df['Name'].str.lower() == name.lower()]

    if not result.empty:
        print(result)
    else:
        print(f"No resident found with Name: {name}")

def search_resident():
    print("Search Resident:")
    print("1. Search by Roll Number")
    print("2. Search by Name")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        roll_no = int(input("Enter Roll Number: "))
        search_by_roll_number(roll_no)
    elif choice == "2":
        name = input("Enter Name: ")
        search_by_name(name)
    else:
        print("Invalid choice. Please enter 1 or 2.")
while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        allocate_room()
    elif choice == '2':
        reallocate_room()
    elif choice == '3':
        vacate_room()
    elif choice == '4':
        search_resident()
    elif choice == '5':
        break
    else:
        print("Invalid choice")


# In[ ]:


import csv
import pandas as pd

stu_database = 'Hostel_Student_Data.csv'
room_cap= 'Hostel_Room_Capacity.csv'
# try:
#     dc=pd.read_csv(stu_database)
# except pd.errors.EmptyDataError:
#     l=list(dc['RollNumber'])
# l=list()
rc = pd.read_csv(room_cap)
x = rc['Room Capacity'].tolist()
room_no = pd.read_csv(room_cap, index_col='Room NO')
stu_count = {i: 0 for i in room_no.index}

try:
    df = pd.read_csv(stu_database)
except pd.errors.EmptyDataError:
    df = pd.DataFrame(columns=['Name', 'RollNumber', 'AllocatedRoom'])
l=list(df['RollNumber'])
df.to_csv(stu_database,index=False)
# df.columns=['Name', 'RollNumber', 'AllocatedRoom']

def display_menu():
    print(" Hostel Management System")
    print("---------------------------")
    print("1. Allocate Room")
    print("2. Reallocate Room")
    print("3. Vacate Room")
    print("4. Search Resident")
    print("5. Quit")
def allocate_room():
    global df
    global stu_count
    global stu_database
    global l
    name = input("Name: ")
    roll_no= int(input("Roll number: "))
    allocated_room = int(input("Room number: "))
    df = pd.read_csv(stu_database)
    if name is None or roll_no is None or allocated_room is None:
        print("Enter data correctly")
        return
    if roll_no in l:
        print("student already exist")
        return
    if allocated_room not in stu_count:
        print("Invalid room number. Please choose another room.")
        return
    stu_count[allocated_room] += 1
    if stu_count[allocated_room] > room_no.loc[allocated_room, 'Room Capacity']:
        print("Room is full. Please choose another room.")
        stu_count[allocated_room] -= 1
        return
    df = pd.DataFrame({"Name": [name], "RollNumber": [roll_no], "AllocatedRoom": [allocated_room]})
    df.to_csv(stu_database,mode='a', index=False,header=False)
    l.append(roll_no)
    print("Room allocated successfully.")
#     print(df)

def reallocate_room():
    global df
    global stu_count
    global stu_database 
    global l
#     print(l)
    roll_no = int(input("Enter Roll Number to update: "))
    if roll_no is None:
        print("Enter data correctly")
        return
#     print(df[1])
    df = pd.read_csv(stu_database)
    if roll_no not in l:
        print("Student not found.")
        return
    
    new_allocated_room = int(input("Enter new Room number: "))
    
    if new_allocated_room not in stu_count:
        print("Invalid room number. df.to_csv(stu_database, index=False)Please choose another room.")
        return
        
    if stu_count[new_allocated_room] >= room_no.loc[new_allocated_room, 'Room Capacity']:
        print("Room is full. Please choose another room.")
        return
    y=l.index(roll_no)
#     print(y)
    allocated_room=df.loc[y][2]
    stu_count[allocated_room] -= 1
    stu_count[new_allocated_room] += 1
    df.loc[y, ['AllocatedRoom']] = new_allocated_room
    df.to_csv(stu_database, index=False)
    print("Room reallocated successfully.")
    
def vacate_room():
    global df
    global stu_count
    global stu_database 
    
    roll_no = int(input("Enter Roll Number to update: "))
    if roll_no is None:
        print("Enter data correctly")
        return
    if  roll_no not in l:
        print("Student not found.")
        return
    y=l.index(roll_no)
    confirmation = input(f"Are you sure you want to vacate the room for {roll_no} (y/n)? ").lower()
    vacating_room=df.loc[y][2]
    print(vacating_room)
    if confirmation == 'y':
        stu_count[vacating_room] -= 1
        df=df[df['RollNumber']!=roll_no]
        df.to_csv(stu_database, index=False)
#         df.drop(index=df[df['RollNumber']==roll_no].index)
        print(roll_no,'has vacated',vacating_room)
    elif confirmation == 'n':
        print("Vacation canceled.")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        
def search_by_roll_number(roll_number):
    result = df[df['RollNumber'] == int(roll_number)]

    if not result.empty:
        print(result)
    else:
        print(f"No resident found with Roll Number: {roll_number}")

def search_by_name(name):
    result = df[df['Name'].str.lower() == name.lower()]

    if not result.empty:
        print(result)
    else:
        print(f"No resident found with Name: {name}")

def search_resident():
    print("Search Resident:")
    print("1. Search by Roll Number")
    print("2. Search by Name")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        roll_no = int(input("Enter Roll Number: "))
        search_by_roll_number(roll_no)
    elif choice == "2":
        name = input("Enter Name: ")
        search_by_name(name)
    else:
        print("Invalid choice. Please enter 1 or 2.")
while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        allocate_room()
    elif choice == '2':
        reallocate_room()
    elif choice == '3':
        vacate_room()
    elif choice == '4':
        search_resident()
    elif choice == '5':
        break
    else:
        print("Invalid choice")


# In[ ]:





# In[ ]:




