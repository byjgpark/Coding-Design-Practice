function cutTheSticks(arr) {
    let output = [];
    
    console.log("check arr", arr)
    
    while (arr.length != 0) {
        
        let minVal = Math.min(...arr);
        
        console.log("check minVal", minVal)
        
        output.push(arr.length);
        
        for (let i = 0; i < arr.length; i++) {
            
            let sub = arr[i] - minVal;
            
            console.log("check sub", sub)

            if (sub === 0) {
                console.log("check i ", i) 
                arr.splice(i, 1);
                i -= 1;
                
                console.log("check i", i)
                
            } else {
                arr[i] = sub;
            }
         }
    }
    return output;
}