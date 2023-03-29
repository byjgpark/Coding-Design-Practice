function cutTheSticks(arr) {
    // Write your code here
    
    console.log("check arr", arr)
    
    console.log("check min value", Math.min(...arr))
    
    let minNum = Math.min(...arr)
    
    console.log("check minNum in the array", arr.map( element => element - minNum))
}