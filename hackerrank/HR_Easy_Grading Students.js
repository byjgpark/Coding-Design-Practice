function multipleOfFive(x) {

    // i = 0 => x = grades[0] = 73
    // i = 1 => x = grades[1] = 67
    // i = 2 => x = grades[2] = 38
    // i = 3 => x = grades[3] = 33
    let counter = 0;
    while (x % 5 != 0) {
        x++;
        // i = 0 => x = 74
        // i = 0 => x = 75
        
        // i = 1 => x = 68
        // i = 1 => x = 69
        // i = 1 => x = 70
        counter++;
        // i = 0 => counter = 1
        // i = 0 => counter = 2

        // i = 1 => counter = 1
        // i = 1 => counter = 2
        // i = 1 => counter = 3
    }
    return counter;
    // return i = 0 => counter = 75
    // return i = 1 => counter = 70
}

function gradingStudents(grades) {
    // Write your code here
    let roundedGrades = [];
    for (let i = 0; i < grades.length; i++) {
        
        let difference = multipleOfFive(grades[i]);
        // i = 0 => grades[0] = 73, difference = 2
        // i = 1 => grades[1] = 67, difference = 3
        
        let finalGrade = difference + grades[i];
        // i = 0 => finalGrade = 2 + 73
        // i = 1 => finalGrade = 3 + 67
        
        if ((difference < 3) && (finalGrade >= 40)) {
            roundedGrades.push(finalGrade);
            // i = 0, roundedGrades = [75, ]
            // i = 2, roundedGrades = [75, 67, 40]
        } else {
            roundedGrades.push(grades[i]);
            // i = 1, roundedGrades = [75, 67]
            // i = 3, roundedGrades = [75, 67, 40, 33]
        }
    }
    return roundedGrades;
}