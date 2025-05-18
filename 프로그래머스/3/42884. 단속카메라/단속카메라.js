function solution(routes) {
    let result = 0;
    let camera = -30001;
    
    routes.sort((a, b) => a[1] - b[1]);
    for (let i in routes) {
        if (routes[i][0] <= camera) {
            continue;
        } else {
            result++;
            camera = routes[i][1];
        }
    }
    
    return result;
}