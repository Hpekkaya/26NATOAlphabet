student_dict = {
    "student" : ["Hakan", "Alev", "Kerem", "Mehmet", "Hatice", "Fatih"],
    "scores" : [75, 85, 90, 78, 79, 81]
}

# [print(value) for (key, value) in student_dict.items()]

import pandas

student_df = pandas.DataFrame(student_dict)

# print(student_df)

# [print(value) for (key, value) in student_df.items()]

# Loop through rows of data frame
# [print(f"{index+1}. {row.student} : {row.scores}") for (index, row) in student_df.iterrows()]

print("SNu-Name  Score ")
for (index, row) in student_df.iterrows():
    if row.scores >= 80:
        print(f"{index+1}. {row.student} : {row.scores}")


