def gradingStudents(grades):
    #Every student receives a grade in the inclusive range from 0 to 100.
    #Any grade less than 40 is a failing grade.
    
    #If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of .
    #If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
    
    result = []

    for grade in grades:
        if grade >= 38:
            roundGrade = round(grade / 5) * 5
            if grade > roundGrade:
                roundGrade += 5
            if roundGrade - grade  < 3:
                grade = roundGrade
        result.append(grade)
    return result

gradingStudents([73, 67, 38, 33])
