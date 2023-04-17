function spiceMustFlow(startingYield) {
    let totalSpice = 0;
    let days = 0;
  
    while (startingYield >= 100) {
      let dailySpice = startingYield - 26;
      totalSpice += dailySpice;
      startingYield -= 10;
      days++;
    }
  
    if (totalSpice >= 26) {
      totalSpice -= 26;
    }
  
    console.log(days);
    console.log(totalSpice);
  }
  
  spiceMustFlow(450)