function pickingNumbers(a) {

    // Write your code here
    console.log("check ", a)
    
    let sortedArray = a.sort(function(a,b){
    return(a - b);
    })
    
    console.log("check sortedArray", sortedArray)

    let currentArray = [];
    let longestArray = 0;
    let startNumber = 0;
    
    for(let i = 0; i < sortedArray.length; i++){
        
        let result = Math.abs(sortedArray[startNumber] - sortedArray[i]);
        // i = 0 => result = sortedArray[0] - sortedArray[0] => 1 - 1 = 0
        // i = 1 => result = sortedArray[0] - sortedArray[1] => 1 - 3 = 2
        
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
        
        if(currentArray.length > longestArray){
            longestArray = currentArray.length
        }
        
        
        
        currentArray = [];
        currentArray.push(sortedArray[i]);
    }
}
return longestArray;
}