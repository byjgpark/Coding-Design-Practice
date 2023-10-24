 // Write your code here
    
  console.log("check s", s, "d", d, "m", m)
    
  let count = 0;
  let sum = 0;

  for(let index = 0; index < m; index++) {
    sum += s[index]
  }

  if (sum === d) {
    count++;
  }

  for(let i = m; i < s.length; i++) {
    console.log("check i :",i, "m :",m)
    console.log("check s[i] :",s[i] , "s[i -m] :", s[i - m])
    console.log("sum in for-loop", sum)
    sum += s[i] - s[i - m];

    if (sum === d) {
      count++;
    }
  }

  return count;