function jumpingOnClouds(c) {
    // Write your code here
    console.log("check c", c)
    let jump = 0;
     for(let i=0;i<c.length;i++){
         if(c[i]==0 && c[i+2]==0){
             console.log("first condition ", c[i],"&", c[i+2])
             jump+=1;
             i = i+1;
         }else if(c[i]==0 && c[i+2]==1){
             console.log("second condition ", c[i],"&", c[i+2])
             jump+=1;
             
         }else if(c[i]==0 && c[i+1]==0){
             console.log("third condition ", c[i],"&", c[i+2])
             jump+=1;

         }
     }
     return jump;
}