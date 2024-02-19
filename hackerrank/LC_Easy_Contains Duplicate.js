
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    
    const a = new Set(nums)

    const b = [...a]

    console.log("check nums", nums);
    console.log("check a", a.length);
    console.log("check b", b.length);

    console.log("check b.lenth == a.length :", b.length === a.length);

    if( b.length === nums.length){
        return false
    }else{
        return true
    }
};