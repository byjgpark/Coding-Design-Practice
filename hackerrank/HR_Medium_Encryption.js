function encryption(s) {
    // Write your code here    
    const ceil = Math.ceil(Math.sqrt(s.length));
    // console.log("check s ", s, "check s length", s.length)
    console.log("check ceil", ceil)   

    let temp = s;
    let array = [];
    
    while(temp) {
         array = array.concat(temp.substring(0, ceil));
         console.log("check array", array)
         temp = temp.substring(ceil)
    }
 
    let result = [];
   
    for(let i = 0 ; i < ceil; i++) {
         result = result.concat(
             array.reduce((r, v) => {
                 return r + (v[i] || "")
         }, "")
     )
     
     
     
    };
    return result.join(' ');

}