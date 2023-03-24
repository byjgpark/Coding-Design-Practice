function migratoryBirds(arr) {

    console.log("check arr", arr)
   
    let max = 1;
    let counter = max
    
    console.log("this is sorted arr", arr.sort())
    
    for(let i = 0; i < arr.length; i++){
        
        max = arr.lastIndexOf(arr[i]) - arr.indexOf(arr[i])
        
        console.log("check first index of something", max)       
    }
    
    console.log("check counter", counter) 
    
}