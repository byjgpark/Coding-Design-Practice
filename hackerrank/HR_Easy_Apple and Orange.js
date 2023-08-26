function countApplesAndOranges(s, t, a, b, apples, oranges) {
    // Write your code here
    
     // Write your code here
   
     let appleCount = 0;
     let organgeCount = 0;
     
     //console.log("check s",s,"t", t, "a",a, "b", b, "apple", apples, "oranges", oranges)
     
     for( let i = 0; i <= apples.length; i++){
             
         if( a + apples[i] >= s && a + apples[i] <= t){
             appleCount++
         }
     }
     
     
     for( let j =0; j <= oranges.length; j++){
         
         if( b + oranges[j] >= s && b + oranges[j] <= t){
             organgeCount++
         }
     }
 
     console.log(appleCount)
     console.log(organgeCount)

}