function migratoryBirds(arr) {

    let largest = 1;
    let counter = largest;
    
    console.log("check counter before for-loop", counter)
    
    let type = 0;
    
    arr.sort();
    
    
    console.log("check arr", arr)
    
    for (let i = 0; i < arr.length; i = arr.lastIndexOf(arr[i]) + 1 ) {
        
        
        largest = (arr.lastIndexOf(arr[i]) - arr.indexOf(arr[i]))+1;
        
        console.log("check i", i, "arr[i]", arr[i], " largest", largest, "counter", counter, "inside for-loop")
        // console.log("check largest inside for-loop", largest)
        
        if (largest > counter) {
            counter = largest;
            type = arr[i];
        }
    }
    return type;
    
}