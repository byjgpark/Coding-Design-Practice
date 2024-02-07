function getGCD(n1, n2) {
  return n2 === 0 ? n1 : getGCD(n2, n1 % n2);
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
    gcd = getGCD(gcd, num);
  }

  let count = 0;
  for (let multiple = lcm; multiple <= gcd; multiple += lcm) {
    if (gcd % multiple === 0) {
      count++;
    }
  }

  return count;
}