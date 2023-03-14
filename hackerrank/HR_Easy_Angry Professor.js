function angryProfessor(k, a) {
    
       // counter for the non-positive arrival times    
       let count = 0
    
       // looping through the a-array if there is a non-positive arriva times,
       // increment count 
       for (let i = 0; i< a.length; i++){
           if(a[i] <= 0){
               count++
           }
       }
       
       // if count is bigger than k return no
       // else return yes 
       if( count >= k){
           return "NO"
       }else{
           return "YES"
       }

}