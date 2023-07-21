subject = int(input("How Many subject you have : "))
marks = []
def student():
    for i in range(1,subject+1):
        m = int(input(f"Subject {i} :"))
        marks.append(m)
    print(f"subject", marks)
def grade():
    sum_of_marks = sum(marks)
    average = sum_of_marks/subject
    print(average)
    if average >= 100:
        print("Try with valid marks..")
    elif average >= 71 and average <= 100:
        print("First Class")
    elif average >= 61 and average <= 70:
        print("Second Class")
    elif average >= 35 and average <= 60:
        print("Third Class")
    else:
        print("tRY next time...")


student()
grade()