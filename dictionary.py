def get_student_marks():
    student_marks = {
        "Shaurya": 85,
        "Sachin": 90,
        "Shreya": 78,
        "Aaruhi": 92
    }

    student_name = input("Enter the student's name: ")

    marks = student_marks.get(student_name)
    if marks is not None:
        print("student_name's marks: ",marks)
    else:
        print(f"Student '{student_name}' not found in records.")

get_student_marks()
