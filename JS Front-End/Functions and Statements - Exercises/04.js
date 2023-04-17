function oddAndEvenSum(number) {
    let oddSum = 0;
    let evenSum = 0;
  
    while (number > 0) {
      let digit = number % 10;
      if (digit % 2 === 0) {
        evenSum += digit;
      } else {
        oddSum += digit;
      }
      number = Math.floor(number / 10);
    }
  
    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`);
  }
  
  oddAndEvenSum(1000435); // Output: Odd sum = 9, Even sum = 4
  