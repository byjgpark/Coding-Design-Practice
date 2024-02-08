
// function getGCD(n1, n2) {
    
// //   console.log("check getGCD n1", n1, "n2", n2)  
    
//   return n2 === 0 ? n1 : getGCD(n2, n1 % n2);
// }

// 1. n1 = 16, n2 = 16
// 1-1. n1 = 16, n2 = 0 return 16
// 2. n1 = 16, n2 = 32
// 2-1 n1= 16, n2 = 16
// 2-2 n1= 16, n2 = 0 return 16
// 3. n1 = 16, n2 = 96
function getGCD(n1, n2) {
    
  if (n2 === 0) {
    return n1;
  }
  
  // 1. remainder = 16 % 16 => 0 
  // 2. remainder = 16 % 32 => 16
  // 2-1. remainder = 16 % 16 => 0
  // 3. remainder = 16 % 96 => 
  const remainder = n1 % n2;
  
  // 1. return getGCD(16, 0)
  // 2. return getGCD(16, 16)
  // 2-1 return getGCD(16, 0)
  return getGCD(n2, remainder);
}


function getLCM(n1, n2) {
    
  return n1 === 0 || n2 === 0 ? 0 : Math.abs(n1 * n2) / getGCD(n1, n2);
  
}

function getTotalX(a, b) {
    
  let lcm = a[0];
  
  for (const num of a) {
    lcm = getLCM(lcm, num);
  }

  let gcd = b[0];
  
  for (const num of b) {
     
    console.log("check gcd", gcd, "num", num);  
    // 1. gcd = 16, num = 16 
    // 2. gcd = 16, num = 32
    // 3. gcd = 16, num = 96
    gcd = getGCD(gcd, num);
    
    // 1. gcd = 16
    // 2. gcd = 32
    
    console.log("check gcd after the var", gcd)
    
  }

  let count = 0;
  for (let multiple = lcm; multiple <= gcd; multiple += lcm) {
    if (gcd % multiple === 0) {
      count++;
    }
  }

  return count;
}