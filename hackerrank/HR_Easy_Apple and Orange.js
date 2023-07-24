function countApplesAndOranges(s, t, a, b, apples, oranges) {
    // Write your code here
    
    console.log("check s", s, "t", t, "a", a, "b", b, "apple", apples, "organes", oranges)
    
    
    let newApples = apples;
    let newOranges = oranges;
    
    for(let i = 0; i < apples.length; i++){
        newApples[i] += a;
    }
    
    for(let j = 0; j < oranges.length; j++){
        newOranges[j] += b;
    }
    
    console.log("check newApples", newApples)
    console.log("check newOranges", newOranges)
    
    let appleCount = 0;
    let oranges
    for (let k = s; k <= t; k++){
        if(newApples.includes(k)){
            appleCount++
        }
        
        if(newOranges.includes(k)){
            new
        }
    }
    
    let orangesCount = 0;
    for(let o = s;)

}