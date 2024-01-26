function fairRations(a) {
    
    let loave = 0, i, temp = a;

    for(i = 0; i < temp.length - 1 ; i++){
        
        if(temp[i] % 2 != 0){
            temp[i]++
            temp[i+1]++
            loave++;
        }
    }

    if ( temp[i] % 2 == 0){
        return loave * 2;
    }
    
    return "NO"
}