function pickingNumbers(a) {
    
    // Write your code here
    console.log("check ", a)
    
    let sortedArray = a.sort(function(a,b){
    return(a - b);
    })
    
    console.log("check sortedArray", sortedArray)

    let currentArray = [];
    // i = 1 => currentArray = [3]
    let longestArray = 0;
    // i = 0 => longestArray = 1
    let startNumber = 0;
    
    for(let i = 0; i < sortedArray.length; i++){
        let result = Math.abs(sortedArray[startNumber] - sortedArray[i]);
        // i = 0 => result = sortedArray[0] - sortedArray[0] => 1 - 1 = 0
        // i = 1 => result = sortedArray[0] - sortedArray[1] => 1 - 3 = 2
        // i = 2 => result = sortedArray[0] - sortedArray[2] => 1 - 3 = 2
        // i = 3 => result = sortedArray[0] - sortedArray[3] => 1 - 4 = 3
        // i = 4 => result = sortedArray[0] - sortedArray[4] => 1 - 5 = 4
        // i = 5 => result = sortedArray[0] - sortedArray[5] => 1 - 6 = 5
        console.log("check result", result)
        
        if (result <= 1){
        currentArray.push(sortedArray[i]);
        // i = 0 => currentArray = [1] 

        if(currentArray.length > longestArray){
            longestArray = currentArray.length
        };
        // i = 1 > 0
        // longestArray = 1
            
        }else {
        startNumber = i;
        // i = 1 => startNumber = 1
        // i = 2 => startNumber = 2
        // i = 3 => startNumber = 3
        // i = 4 => startNumber = 4
        // i = 5 => startNumber = 5
        
        if(currentArray.length > longestArray){
        // i = 0 => 1 > 1
        // i = 2 => 1 > 1
        // i = 3 => 1 > 1
        // i = 4 => 1 > 1
        // i = 5 => 1 > 1
            longestArray = currentArray.length
            // longestArray = 1
            // longestArray = 2
        }
        
        currentArray = [];
        console.log("check currentArray before currentArray.push ", currentArray)
        currentArray.push(sortedArray[i]);
        // i = 1 => currentArray = [3]
        // i = 2 => currentArray = [3]
        // i = 3 => currentArray = [4]
        // i = 4 => currentArray = [5]
        // i = 5 => currentArray = [6] 
        console.log("check currentArray after currentArray.push ", currentArray)
    }
}
return longestArray;
}