function solution(N, stages) {
    var answer = [];
    var fail_arr = [];
    var total = stages.length;

    for(var i=1; i<=N; i++){
        
        var cnt = 0;
        for(var j=0; j<stages.length; j++){
            // i=0 == stages[0] => 2
            // i=0 == stages[1] => 1
            // i=0 == stages[2] => 2
            // i=0 == stages[3] => 6
            
            // i=1 == stages[0] => 2
            // i=1 == stages[1] => 1 cnt =1
            // i=1 == stages[2] => 2 

            // i=2 == stages[0] => 2 cnt =2
            // i=2 == stages[1] => 1
            // i=2 == stages[2] => 2 cnt =3

            // i=3 == stages[0] => 2
            // i=3 == stages[1] => 3 cnt =4
            // i=4 == stages[2] => 1
            if(i == stages[j]){
                cnt++;                
            }
        }        
        
        // 실패율(per)순으로 정렬시키기 위해 json형태로 push
        fail_arr.push({per:cnt/total, idx:i});
        total -= cnt;
    }
    
    fail_arr.sort(function(a, b) { return b["per"] - a["per"]; });
    
    for(var i=0; i<fail_arr.length; i++){
        answer.push(fail_arr[i].idx);
    }

    return answer;
}