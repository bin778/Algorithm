function solution(fees, records) {
    // 기본 시간: fees[0], 기본 요금: fees[1], 추가 시간: fees[2], 추가 요금: fees[3]
    const hashMap = {};
    const result = [];
    
    // 차량 요금 HashMap 저장
    records.map((record, idx) => {
        const info = record.split(" ");
        const time = info[0].split(":");
        
        // 차량 입출고 정보
        const minutes = (Number(time[0]) * 60) + (Number(time[1]));
        const car_number = info[1];
        const details = info[2];
        
        if (details === "IN") {
            if (!Object.keys(hashMap).includes(car_number)) {
                hashMap[car_number] = -(minutes);
            } else {
                hashMap[car_number] -= minutes;
            }
        } else {
            hashMap[car_number] += minutes;
        }
    });
    
    // 차량 넘버 정렬
    const fee_arr = [];
    const carnum_arr = Object.keys(hashMap).sort();
    for (let i in carnum_arr) {
        const idx = Object.keys(hashMap).indexOf(carnum_arr[i]);
        if (Object.values(hashMap)[idx] > 0) {
            fee_arr.push(Object.values(hashMap)[idx]);
        } else {
            fee_arr.push(Object.values(hashMap)[idx] + 1439);
        }
    }
    
    // 요금 환산하기
    for (let i of fee_arr) {
        // 기본 요금 계산
        i -= fees[0];
        let fee = fees[1];
        
        // 추가 요금 계산
        while (i > 0) {
            i -= fees[2];
            fee += fees[3];
        }
        result.push(fee);
    }
    return result;
}