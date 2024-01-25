function fairRations(a) {
    
    let temp = a, loaves = 0, i;
    
    console.log("check i", i)
    
    console.log("check a", a);
    
    console.log("check temp", temp);
    
    for (i = 0; i < temp.length - 1; i++) {
        
        console.log("Check temp[i]", temp[i]);
        
        console.log("check modules ",  temp[i] % 2);        
        
        if (temp[i] % 2 != 0) {
            temp[i]++;
            temp[i + 1]++;
            loaves++;
        }
        
        console.log("check i inside of the for-loop", i)
    }
    
    console.log("check i after for-loop", i);

    if (temp[i] % 2 === 0) {
        
        console.log("check loaves : ", loaves);
        
        return loaves * 2;
    }

    temp = [];
    loaves = 0;
    i = 0;

    for (i = temp.length - 1; i > 0; i--) {
        
        if (temp[i] % 2 != 0) {
            temp[i]++;
            temp[i - 1]++;
        }
        
        console.log("check temp.length", temp.length);
    }

    if (temp[i] % 2 === 0) {
        return loaves * 2;
    }

    return 'NO';
}