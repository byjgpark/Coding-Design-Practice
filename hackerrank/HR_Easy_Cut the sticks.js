function cutTheSticks(arr) {
    
    let output = [];
    
    console.log("check arr", arr)
    
    while (arr.length != 0) {
        
        let minVal = Math.min(...arr);
        
        // console.log("check minVal", minVal)
        
        output.push(arr.length);
        
        for (let i = 0; i < arr.length; i++) {
            
            let sub = arr[i] - minVal;
            
            console.log("check sub", sub)
            
            // console.log("check i before decrement ", i) 

            
            if (sub === 0) {
                console.log("check i before decrement ", i) 
                arr.splice(i, 1);
                i -= 1;
            
                console.log("check i after decrement ", i)
                console.log("check arr inside loop", arr)
            } else {
                arr[i] = sub;
                // console.log("chech arr in the else loop", arr)
            }
        //  console.log("check i here after if statement ", i)
        
         }
    }
    return output;
}