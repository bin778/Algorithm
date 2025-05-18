function solution(genres, plays) {
    let result = [];
    const hashSong = {};
    const hashGenre = {};
    
    // 장르별 총 플레이수 집계
    genres.map((genre, idx) => {
        if (!hashSong[genre]) {
            hashSong[genre] = 0;
            hashGenre[genre] = [];
        }
        hashSong[genre] += plays[idx];
        hashGenre[genre].push([plays[idx], idx]);
    });
    
    // 가장 많이 돌린 장르를 내림차순으로 집계
    const genreRank = Object.entries(hashSong).sort((a, b) => b[1] - a[1]).map(([k, v]) => k);
    
    // 각 장르에서 가장 재생횟수 높은 상위 2곡을 선택
    for (let genre of genreRank) {
        let songs = hashGenre[genre];
        // 재생횟수 내림차순, 재생횟수가 같으면 인덱스 오름차순
        songs.sort((a, b) => b[0] - a[0] || a[1] - b[1]);
        
        // 상위 2곡의 인덱스만 result에 추가
        result.push(songs[0][1]);
        if (songs[1]) result.push(songs[1][1]);
    }
    
    return result;
}