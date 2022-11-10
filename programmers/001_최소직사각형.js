function solution(sizes) {
    
    // To find minimum area of a rectangle 
    // by comparing w and h, assign bigger number to
    // higher array => else to lower array
    const lower = [];
    const higher = [];
    
    // Looping thourgh 2d array
    sizes.map( ([w, h]) => {
        
        // if w is greater than h 
        // push w to higher number array
        // else push h to lower number array
        if(w > h) {  
            higher.push(w)
            lower.push(h) 
        }
        
                
        // if h is greater than equal to w 
        // push h to higher number array
        // else push w to lower number array
        if(h >= w) {
            higher.push(h)
            lower.push(w)
        }
    
    })
    
    // find max number from the two different arrays
    const maxHigher = Math.max(...higher)
    const maxLower = Math.max(...lower)
    
    // to find area of the wallet size
    return (maxHigher * maxLower)
}