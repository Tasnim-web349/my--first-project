name = input("Enter student name:")
python_mark = float(input("Enter Python mark:"))
java_mark = float(input("Enter Java mark:"))
english_mark = float(input("Enter English mark:"))
average = (python_mark + java_mark + english_mark) /3
print("Average:",average)
if average >= 60:
    print("Pass")
else:
    print("Fail")