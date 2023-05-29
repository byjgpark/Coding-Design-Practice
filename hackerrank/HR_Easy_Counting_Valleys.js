function countingValleys(steps, path){
    // Write your code here
    
    console.log("check steps", steps, "path", path)
    
    let strArr = path.split('')
    
    console.log("hey check strArr", strArr)
    
    let count = 0
    let result = 0
    for(let step=0; step<steps; step++){
        
        console.log('check here', strArr[step].toLowerCase())
        
        if(count == 0 && strArr[step].toLowerCase() == 'd')
        {
            count -= 1
            console.log("hey check count", count)
            result += 1
            console.log("check result", result)
        }else if(strArr[step].toLowerCase() == 'd'){
            count -= 1
        }else {
            count += 1
        }
    }
    return result
}