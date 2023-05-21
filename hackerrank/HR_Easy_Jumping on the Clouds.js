function jumpingOnClouds(c) {

    // Counter for jump
    let jump = 0
    // Looping though c    
    for(let i = 0; i < c.length; i++){
        // if the value of c[i] && c[i+2] are 0 & 1         
        if(c[i] == 0 && c[i+2] == 1){
            // increment the value of jump by 1
            jump += 1
        }
        // if the value of c[i] && c[i+2] are 0 & 0
        else if(c[i] == 0 && c[i+2] == 0){
             
            // increment the value of i by 1 
            i++
            // increment the value of jump by 1
            jump += 1
        }
        // if the value of c[i] && c[i+1] are 0 & 0
        else if(c[i] == 0 && c[i+1] == 0){
            // increment the value of jump by 1
            jump += 1
        }
    }
    // return jump
    return jump
}