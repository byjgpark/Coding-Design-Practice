function cutTheSticks(arr) {
    
    // Initializing empty array
    let emptyArr = []
        
    // Looping through array until arr.length hits 0    
    while(arr.length != 0){
    
    // Finding min value from arr
    let minValue = Math.min(...arr);
    
    // Pushing arr.length after breaking out of a for-loop
    emptyArr.push(arr.length)
    
    for(let i = 0; i< arr.length; i++){
        
        // Subtrackig minValue from each element of arr   
        let sub = arr[i] - minValue;
        
        // When sub is 0, remove element at index i
        if(sub === 0){
            arr.splice(i, 1)
            
            // decrementing i
            i -= 1
            
        // else assigning sub value to arr[i]    
        }else{
           arr[i] = sub 
        }
    }
    }
    // Returning each iteration of arr.length after breaking out of for-loop
    return emptyArr
}