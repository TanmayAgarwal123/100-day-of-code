import pandas
import random

student_dict = {
    "student": ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"],
    "score": [random.randint(1, 100) for student in range(6)]
}
student_dataframe = pandas.DataFrame(student_dict)
#print(student_dataframe)

# for (key,value) in student_dataframe.items():
#     print(value)

for (index, row) in student_dataframe.iterrows():
    #print(index)
    #print(row)
    #print(row.student, row.score)
    print(index, row.student, row.score)