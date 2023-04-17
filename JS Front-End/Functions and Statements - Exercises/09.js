function loadingBar(num) {
    let percentage = num / 10;
    let bar = Array(10).fill('.');
    for (let i = 0; i < percentage; i++) {
      bar[i] = '%';
    }
    if (percentage < 10) {
      console.log(`${num}% [${bar.join('')}]`);
      console.log('Still loading...');
    } else {
      console.log('100% Complete!');
      console.log(`[${bar.join('')}]`);
    }
  }
  