function cutTheSticks(arr) {
    
    // Write your code here
    
    console.log("check arr", arr)
    
    let sizeOfArray = []
    
    // console.log('check minValue', minValue)
    
    sizeOfArray.push(arr)
    
    while(arr != 0){
        
        let minValue = Math.min(...arr)
        
        for(let i = 0; i < arr.length; i++){
            
            let sub = arr[i] - minValue
            
            if(sub == 0){
               arr.splice(i, 1)
               i -= 1
            }else{
                arr[i] = sub
            }
            console.log("check i", i)
        }
    }
    return sizeOfArray
}