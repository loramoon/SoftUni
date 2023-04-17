function factorialDivision(num1, num2) {
    let factorial1 = 1;
    let factorial2 = 1;
    
    for (let i = 1; i <= num1; i++) {
      factorial1 *= i;
    }
    
    for (let j = 1; j <= num2; j++) {
      factorial2 *= j;
    }
    
    let result = factorial1 / factorial2;
    
    return result.toFixed(2);
  }
  