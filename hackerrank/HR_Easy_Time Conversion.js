function timeConversion(s) {

    // 1. 12 AM -> 00
    // 2. 1 AM to 12 PM -> do nothing
    // 3. 1 PM To 11 PM -> add 12 to hours
    
    let firstLetterHour = s.charAt(8)
    let militaryTIme = ''
    
    // AM
    if(firstLetterHour === 'A'){
    
        if(s.substring(0,2) === '12'){
            militaryTIme = '00'
        }
        else{
            militaryTIme = s.substring(0,2)
        }
    }
    // PM
    else{
        if(s.substring(0,2) === '12'){
              militaryTIme = s.substring(0,2)
        }
        else{
            militaryTIme = parseInt(s.substring(0,2), 10) + 12
        }
    }

    return militaryTIme + s.substring(2,8)
}