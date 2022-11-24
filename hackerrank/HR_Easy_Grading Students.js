function multipleOfFive(x) {

    
    // i = 0 => x = grades[0] = 73
    let counter = 0;
    while (x % 5 != 0) {
        x++;
        // i = 0 => x = 74
        // i = 0 => x = 75
        counter++;
        // counter = 1
        // counter = 2
    }
    return counter;
    // return counter = 75
}

function gradingStudents(grades) {
    // Write your code here
    let roundedGrades = [];
    for (let i = 0; i < grades.length; i++) {
        
        let difference = multipleOfFive(grades[i]);
        // i = 0 => grades[0] = 73, counter = 2
        
        let finalGrade = difference + grades[i];
        // finalGrade = 2 + 73
        
        if ((difference < 3) && (finalGrade >= 40)) {
            roundedGrades.push(finalGrade);
            // i = 0, roundedGrades = [75, ]
        } else {
            roundedGrades.push(grades[i]);
        }
    }
    return roundedGrades;
}