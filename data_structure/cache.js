// https://school.programmers.co.kr/learn/courses/30/lessons/17680

function solution(cacheSize, cities) {
  const lowerCities = cities.map((city) => city.toLowerCase());
  const cache = new Map();

  let time = 0;
  for (let city of lowerCities) {
    if (cache.has(city)) {
      cache.set(city, time);
      time += 1;
    } else if (cacheSize === 0) {
      time += 5;
    } else if (cache.size < cacheSize) {
      cache.set(city, time);
      time += 5;
    } else {
      const oldest = [...cache.keys()].reduce((oldest, city) => {
        if (cache.get(oldest) < cache.get(city)) return oldest;
        return city;
      });
      cache.delete(oldest);
      cache.set(city, time);
      time += 5;
    }
  }
  return time;
}
