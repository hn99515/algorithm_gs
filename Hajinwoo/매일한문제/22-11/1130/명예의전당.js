function solution(k, score) {
    var answer = []
    var res = []
    for (var x of score) {
        // console.log(x)
        if (answer.length < k) {
            answer.push(x)
            answer.sort(function (a, b){
                return b - a
            })
            // console.log(answer)
            res.push(answer[answer.length-1])
        } else {
            if (answer[k-1]>x){
                res.push(answer[answer.length-1])
            } else {
                answer.pop()
                answer.push(x)
                answer.sort(function (a, b){
                    return b - a
                })
                res.push(answer[answer.length-1])
            }
        }
    }
    return res
}


console.log(solution(3, [10, 100, 20, 150, 1, 100, 200]))