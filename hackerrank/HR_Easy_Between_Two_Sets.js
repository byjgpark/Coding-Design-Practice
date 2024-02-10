function getLCM(n1, n2){
    
  if( n1 ==0 | n2 == 0 ){
      return 0;
  }
  
  return Math.abs(n1 * n2) / getGCD(n1, n2);  
  
}

function getGCD(n1, n2){
  
  if(n2 == 0){
      return n1;
  }
  
  let remainder = n1 % n2;
  
  return getGCD(n2, remainder); 
}


function getTotalX(a, b) {
  // Write your code here
  
  console.log("check getLCM ", getLCM(2,4));
  
  console.log("check getGCD ", getGCD(16, 32));
  
  let result = 0;
  
  let lcm = a[0];
  
  for(let i = 0; i < a.length; i++){
      lcm = getLCM(lcm, a[i])
  }
  
  let gcd = b[0]
  
  for(let j = 0; j < b.length; j++){
      gcd = getGCD(gcd, b[j])
  }
  
  let multiple = 0;
  while(multiple <= gcd){
      multiple += lcm;
      
      if(gcd % multiple == 0){
          result++
      }
      
  }
  
  return result;
}
