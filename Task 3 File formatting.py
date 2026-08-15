#RICHARD KAINUKU 
#Student ID: 270565532

#Task 3: File formatting

#reading and cleaning
with open("student_record_v1.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

#Extract data categories
student_ids = lines[0:5]
first_names = lines[5:10]
last_names = lines[10:15]
campuses = lines[15:20]
study_modes = lines[20:25]

#Generate email addresses
#Using .replace(' ', '') for people with multiple first names
emails = [
    f"{first.lower().replace(' ', '')}_{last.lower()}@yoobeecolleges.com"
    for first, last in zip(first_names, last_names)
]

#Create formatted student records
formatted_data = []
for i in range(5):
    student_info = (
        f"ID: {student_ids[i]}, "
        f"Name: {first_names[i]} {last_names[i]}, "
        f"Campus: {campuses[i]}, "
        f"Mode: {study_modes[i]}, "
        f"Email: {emails[i]}"
    )

    formatted_data.append(student_info)

#Write data to a new file
with open("student_record_v2.txt", "w") as file:
    for record in formatted_data:
        file.write(record + "\n")

#Test output file
with open("student_record_v2.txt", "r") as file:
    print(file.read())