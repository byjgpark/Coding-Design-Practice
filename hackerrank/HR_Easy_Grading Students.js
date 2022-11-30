function gradeDiff(grade){
     
    let counter = 0
    while(grade % 5 != 0){
        grade++
        counter++
    }
   return counter
}

function gradingStudents(grades) {
   
   let answer = []
   // console.log("check grades", grades)    
   
   for(let i = 0; i< grades.length; i++){
       let difference = gradeDiff(grades[i])
       let nextNum = grades[i] + difference
       
       if( difference <3 && grades[i] ){
           answer.push(nextNum)
       }
   }
   
   