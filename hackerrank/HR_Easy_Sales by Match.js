function sockMerchant(n, ar) {
    // 1. find unique values
    // 2. filter out the unique values
    // 3. divide the array / 2
    // 4. increment the values 
    
    const uniqueValues = [...new Set(ar)];
    
    let count = 0;
    
    for(let i = 0; i< uniqueValues.length; i++){
        
        const filteredArr = ar.filter((element) => element == uniqueValues[i] )
        const roundedNum = Math.floor(filteredArr.length/2);
        count += roundedNum
    }
    
    return count;
}