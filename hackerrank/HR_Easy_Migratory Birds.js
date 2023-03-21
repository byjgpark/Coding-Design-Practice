function migratoryBirds(arr) {
    let max = 0;
    let max_id = 6;
    let store = new Array(6).fill(0);
    
    console.log("check store", store)
    
    for(const num of arr){
        // store[num]++;
        // console.log("check num", store[num]++)
        console.log("check num", store[num]++)   
        // console.log("check num", store[num]++)
        
        // if(store[num] > max){
        //     max = store[num]
        //     max_id = num;
        // }else if(store[num] === max && num < max_id){
        //     max_id = num;
        // }
    }
    return max_id;
}