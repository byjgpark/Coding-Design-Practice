function staircase(n){
    
    // N = 4
    // 0123
    // SSS# i = 0, S = 3, #=1
    // SS## i = 1, S = 2, #=2 
    // S### i = 2, S = 1, #=3
    // #### i = 3, S = 0, #=4
    
    // S= n-i-1
    // #= i+1
    
    // Looping through n
    for(let i = 0; i< n; i++){
        
        // Initialzing an empty string
        let string = ""
        
        // Looping through and Assigning empty spaces times 
        // if J is smaller than S= n-i-1 
        for(let j = 0; j< n - i - 1; j++){
            string += " "
        }
        
        // Looping through and Assigning # 
        // if J is smaller than #= i+1
        for(let k = 0; k< i + 1; k++ ){
            string += "#"
        }
        
        // printout string that meets the given conditions
        console.log(string)
    }
    
}