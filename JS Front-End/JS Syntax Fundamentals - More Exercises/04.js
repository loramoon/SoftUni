function calculateExpenses(numLostFights, helmetPrice, swordPrice, shieldPrice, armorPrice) {
    let expenses = 0;

  
    for (let i = 1; i <= numLostFights; i++) {
      if (i % 2 === 0) {
        expenses += helmetPrice;
      }
      if (i % 3 === 0) {
        expenses += swordPrice;
      }
      if (i % 2 === 0 && i % 3 === 0) {
        expenses += shieldPrice;
      }
      if (i % 4 === 0 && i % 6 === 0) {
        expenses += armorPrice;
      }
    }
  
    console.log(    `Gladiator expenses: ${expenses.toFixed(2)} aureus`);
  }
  
  calculateExpenses(7,
    2,
    3,
    4,
    5
     );
  