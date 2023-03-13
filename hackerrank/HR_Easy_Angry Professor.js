function angryProfessor(k, a) {
    
    console.log("check k ", k, "check a", a)
    // Write your code here
    
    let count = 0
    
    for (let i = 0; i< a.length; i++){
        if(a[i] <= 0){
            count++
            
            
            // if( count === k){
            //     return "YES"
            // }else{
            //     return "NO"
            // }
        }
    }
    
    if( count === k){
        return "NO"
    }else{
        return "YES"
    }

}