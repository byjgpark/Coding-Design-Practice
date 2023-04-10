function migratoryBirds(arr) {
    
    let max = 1;
    let counter = 1;
    // sorting the array in ascending order
    arr.sort()
    
    let type = 0
    

    
    
    
    arr.sort();
    
    
    console.log("check arr", arr)
    
    for (let i = 0; i < arr.length; i = arr.lastIndexOf(arr[i]) + 1 ) {

        
        // finding the difference between first index  
        // and last index of the array value 
        max = arr.lastIndexOf(arr[i]) - arr.indexOf(arr[i])
        
        // if max is bigger than counter
        // assign max to counter as well as arr[i] to type
        if( max > counter){
            counter = max;
            type = arr[i]
        }
    }
    return type
}