function getMoneySpent(keyboards, drives, b) {
    
    console.log("check keyboards", keyboards)
    
    console.log("check drives", drives)
    
    let maxValue = -1;
    for (let drive of drives) {
        for(let keyboard of keyboards) {
            
            console.log("check drive ", drive, "check keyboard", keyboard)
            
            let cost = drive + keyboard;
            if(cost > maxValue && cost <= b) {
                maxValue = cost;
            }
        }
    }
    return maxValue;
}
