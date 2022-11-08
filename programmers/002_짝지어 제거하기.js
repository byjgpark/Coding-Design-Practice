function solution(s)
{
 // initializing an empty array for stack
 let stack = [];
 
 // looping through for looing
 for(let i=0;i< s.length; i++){
     // pushing all the alphabet of s
    stack.push(s[i]);
     // if last element and second to last are same 
     // pop the elements 
     if(stack[stack.length-1] === stack[stack.length-2]){
         stack.pop()
         stack.pop()
     }
 }
    // if stack is empty, return 1
    return (stack.length === 0 ? 1 : 0)
}