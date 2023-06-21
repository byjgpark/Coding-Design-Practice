function libraryFine(d1, m1, y1, d2, m2, y2) {
    // Write your code here
    console.log("check d1",d1,"m1",m1,"y1",y1,"d2",d2,"m2",m2,"y2",y2)
    
    let number = 0;
    if( y1 > y2){
    number = (y1 - y2) * (10000)
        if( m1 > m2){
        number = (m1 - m2) * (500)
            if( d1 > d2){
            number = (d1 - d2) * (15)
                        }    
                    }
                }
    else{
         if( m1 > m2){
        number = (m1 - m2) * (500)
            if( d1 > d2){
            number = (d1 - d2) * (15)
                        }    
                    }
    }
    return number
}