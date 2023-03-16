function miniMaxSum(arr) {
    // Write your code here
    
    // sort array ascending order 
    let sortedArr = arr.sort()
    
    // Adding up the number except for first index of array
    let MaxNum = 0
    for(let i = 1; i < arr.length; i++){
        MaxNum += arr[i]
    }
    
    // Adding up the number except for last index of array
    let MinNum = 0
    for(let j = 0; j < arr.length-1; j++){
        MinNum += arr[j]
    }
        
    // printing out the MinNum & MaxNum        
    console.log(MinNum, MaxNum)
}