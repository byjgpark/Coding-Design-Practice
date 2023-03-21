function getMoneySpent(keyboards, drives, b) {
    // initialize -1 for maxNum
    let maxNum = -1
    // Iterate through all the combination from keyboard & drive
    for(const keyboard of keyboards){
        for(const drive of drives){
            // suming up all the combination from keyboard & drive
            let sum = keyboard + drive
            // if the sum is bigger than the maximum and the sum 
            // is bigger than & equal to the b
            if( sum > maxNum && sum <= b){
            // Assign sum to maxNum
                maxNum = sum
            }    
        }
    }
    // return maxNum
    return maxNum
}