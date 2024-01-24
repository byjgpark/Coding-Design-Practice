function fairRations(a) {
    let temp = a, loaves = 0, i;
    
    for (i = 0; i < temp.length - 1; i++) {
        if (temp[i] % 2 != 0) {
            temp[i]++;
            temp[i + 1]++;
            loaves++;
        }
    }

    if (temp[i] % 2 === 0) {
        return loaves * 2
    }

    temp = [];
    loaves = 0;
    i = 0;

    for (i = temp.length - 1; i > 0; i--) {
        if (temp[i] % 2 != 0) {
            temp[i]++;
            temp[i - 1]++;
        }
    }

    if (temp[i] % 2 === 0) {
        return loaves * 2;
    }

    return 'NO';
}