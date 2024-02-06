function getTotalX(a, b) {
    // Write your code here
    console.log("Check here gcd : ", gcd(75,25));
    
    console.log("Check here lcm : ", lcm(75,25));
    
    console.log("check % = ", 75%25)
}

function gcd(x, y) {
    
  x = Math.abs(x);
  y = Math.abs(y);
  
  while(y) {
    var t = y;
    y = x % y;
    x = t;
  }
  return x;
}

function lcm(x, y){
    return (x * y) / gcd(x, y); 
}

 // starts to understand the question day4