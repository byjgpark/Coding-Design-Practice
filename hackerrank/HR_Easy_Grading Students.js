function gradeDiff(grade){
     
    // incrementing grade and counter 
    // until grdae is divisible by 5
    let counter = 0
    while(grade % 5 != 0){
        grade++
        counter++
    }
   return counter
}

function gradingStudents(grades) {
   
   // answer array
   let answer = []
   
   // looping though the number of grades
   for(let i = 0; i< grades.length; i++){

       // getting difference from the next multiple of 5
       let difference = gradeDiff(grades[i])

       // getting the next multiple of 5
       let nextNum = grades[i] + difference
           
       // if difference is less than 3 and grades[i] is greater than 38
       // push next number to answer
       if( difference < 3 && grades[i] >= 38){
           answer.push(nextNum)
       }

       // if difference is greater than & equal 3 and grades[i] is greater than 38
       // push grades[i] to answer
       else if ( difference >= 3 && grades[i] >= 38){
           answer.push(grades[i])
       }

       // if grades[i] is less than & equal to 38
       // push grades[i] to answer
       else if ( grades[i] <= 38){
           answer.push(grades[i])   
       }
   }
   
   return answer
}