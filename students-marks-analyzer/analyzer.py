import numpy as np
import pandas as pd

try:
    data = pd.read_csv('grades.csv')
except FileNotFoundError:
    print("The file 'grades.csv' was not found.")
    exit()
df = pd.DataFrame(data)
math_mean = df['Math'].mean()
science_mean = df['Science'].mean()
english_mean = df['English'].mean()

print(f"Average Math Score: {math_mean}")
print(f"Average Science Score: {science_mean}")
print(f"Average English Score: {english_mean}")


def return_grade(df,name):
    student_data = df[df['Name'] == name]
    subjects = ['Math', 'Science', 'English']
    if student_data.empty:
        print("Student not found.")
        return
    row = student_data.iloc[0]
    print(f"Grades for {row['Name']}:")
    for subject in subjects:
        grade = row[subject]
        if grade >= 90:
            print(f"{subject}: A")
        elif grade >= 60:
            print(f"{subject}: B")
        elif grade >= 40:
            print(f"{subject}: C")
        else:
            print(f"{subject}: F")


def return_avg(df,name1):
    student_data = df[df['Name']==name1]
    if student_data.empty:
        print("Student not found.")
        return
    row=student_data.iloc[0]
    print(f"{row['Name']}'s average score is {row[['Math','Science','English']].mean():.2f}")


def return_topper(df):
    new_df = df.copy()
    new_df['Average'] = new_df[['Math', 'Science', 'English']].mean(axis=1)
    topper = new_df.loc[new_df['Average'].idxmax()]
    print(f"The topper is {topper['Name']} with an average score of {topper['Average']}")

def return_failures(df):
    failures = df[df[['Math', 'Science', 'English']].mean(axis=1).lt(40)]
    if failures.empty:
        print("No students have failed.")
    else:
        print("Students who have failed:")
        for name in failures['Name']:
            print(name)

def return_leaderboard(df):
    leaderboard=df.copy()
    leaderboard['Average']=leaderboard[['Math','Science','English']].mean(axis=1)
    leaderboard=leaderboard.sort_values(by='Average',ascending=False)
    print("Leaderboard:")
    rank=0
    for index,row in leaderboard.iterrows():
        rank+=1
        print(f"rank {rank}: { row['Name']}: {row['Average']:.2f}")

while True:
    print("\nMenu:")
    print("1. Get a student's grades")
    print("2. Get a student's average score")
    print("3. Get the class topper")
    print("4. Get the list of students who have failed")
    print("5. Get the leaderboard")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    match choice:
        case '1':
            name = input("Enter the name of the student to get their grades: ")
            return_grade(df, name)
        case '2':
            name1 = input("Enter the name of the student to get their average score: ")
            return_avg(df, name1)
        case '3':
            return_topper(df)
        case '4':
            return_failures(df)
        case '5':
            return_leaderboard(df)
        case '6':
            print("Exiting the program.")
            break        
        case _:
            print("Invalid choice. Please try again.")

 
print(f"DataFrame after dropping the English column: {df.drop(columns=['English'])}")
