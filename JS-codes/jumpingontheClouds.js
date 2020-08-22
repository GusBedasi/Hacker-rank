// Complete the jumpingOnClouds function below.
function jumpingOnClouds(c) {
    let jumps = 0;
    for(let i = 0; i < c.length; i++){
        if(c[i] == 0){
            jumps = jumps + 1;
            if(c[i + 1] == 0 && c[i + 2] == 0){
                c.shift();
            }
        }
    }
    return jumps - 1;
}

jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]); //4
jumpingOnClouds([0, 0, 0, 0, 1, 0]); //3