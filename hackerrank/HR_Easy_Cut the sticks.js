function cutTheSticks(arr) {
    // Write your code here
    
  // Write your code here
    
  console.log("check arr", arr)
    
  console.log("check min value", Math.min(...arr))
  
  let minNum = Math.min(...arr)
  
  let subtrack = arr.map(element => element - minNum)
  
  console.log("check subtrack in the array", subtrack)
  
  let i = 0;
  while(i < subtrack.length){
      if(subtrack[i] === 0){
          subtrack.splice(i,1)
      }else{
          ++i;
      }
  }
  
  console.log("check subtrack's length at the end ", subtrack.length)
}