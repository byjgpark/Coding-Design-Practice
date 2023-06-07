function countingValleys(steps, path){
    // Write your code here
    
    let valley = 0;
    let elevation = 0;
    for(let i =0; i < steps; i++){
        if( path[i] == 'D'){
            elevation--;
            console.log("check elevation in D :", elevation,"check valley :", valley)
        }else{
            if(elevation == -1){
                console.log("check elevation in elevation == -1 :", elevation)
                valley++;
                console.log("check valley in elevation == -1 :", valley)
            }
            elevation++
            console.log("check elevation in U :", elevation, "valley :", valley)
        }
    }
    return valley;
}