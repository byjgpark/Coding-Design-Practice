function countingValleys(steps, path){
    // Write your code here
    
    console.log("check step", steps, "check path", path)
    
    let valley = 0;
    let elevation = 0;
    for(let i =0; i < steps; i++){
        if( path[i] == 'D'){
            elevation--;
        }else{
            if(elevation == -1){
                valley++;
            }
            elevation++
        }
    }
    return valley;
}