function calculateDistance(x1, y1, x2, y2) {
    const distance1 = Math.sqrt(Math.pow(x1, 2) + Math.pow(y1, 2));
    const distance2 = Math.sqrt(Math.pow(x2, 2) + Math.pow(y2, 2));
  
    if (Number.isInteger(distance1)) {
      console.log(`{${x1}, ${y1}} to {0, 0} is valid`);
    } else {
      console.log(`{${x1}, ${y1}} to {0, 0} is invalid`);
    }
  
    if (Number.isInteger(distance2)) {
      console.log(`{${x2}, ${y2}} to {0, 0} is valid`);
    } else {
      console.log(`{${x2}, ${y2}} to {0, 0} is invalid`);
    }
  
    const distance3 = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
  
    if (Number.isInteger(distance3)) {
      console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`);
    } else {
      console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`);
    }
  }
