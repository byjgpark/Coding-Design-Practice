function gradeDiff(grade){
     
    let counter = 0
    while(grade % 5 != 0){
        grade++
        counter++
    }
   return counter
}

function gradingStudents(grades) {
   
   // upload comments
   let answer = []
   // console.log("check grades", grades)    
   
   for(let i = 0; i< grades.length; i++){
       let difference = gradeDiff(grades[i])
       let nextNum = grades[i] + difference
       
       console.log("check difference", difference)
       
       // difference < 3 
       if( difference < 3 && grades[i] >= 38){
           answer.push(nextNum)
       }
       else if ( difference >= 3 && grades[i] >= 38){
           answer.push(grades[i])
       }
       else if ( grades[i] <= 38){
           answer.push(grades[i])   
       }
   }
   
   console.log('check grades', answer)
   
   return answer
}