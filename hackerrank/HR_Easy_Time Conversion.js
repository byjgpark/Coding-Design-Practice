function timeConversion(s) {
    // Write your code here
    
    console.log("check s", s)
    
    const time = s.slice(0,8).split(':');

    arr[0] = (s.indexOf('PM') > -1) ?
        (time[0] == 12 ? '12' : NUmber(time[0]) + 12) :
        (time[0] == 12 ? '00' : time[0]);
        
    // console.log("check arr[0]", arr[0] = (s.indexOf('PM') > -1) ?
    //     (time[0] == 12 ? '12' : Number(time[0]) + 12) :
    //     (time[0] == 12 ? '00' : time[0]))    
        

    

    return time.join(':');
}