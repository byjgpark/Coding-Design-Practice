function kangaroo(x1, v1, x2, v2) {
    
    // Assigning each kangaroo & kangaroo's position to k1 & k2
    let k1 = x1;
    let k2 = x2;
    
    // Iterating though 100000
    for(let i =0; i< 10000; i++){
        k1 += v1
        k2 += v2
        
        // if there is k1 is equal to k2, they meet at the same location of i
        if( k1 == k2){
            console.log("YES")
            return "YES"
        }
    }
    
    // if they dont meet, then return NO
    return "NO"
}