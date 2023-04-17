function printCharactersInRange(char1, char2) {
    let startCharCode = char1.charCodeAt(0);
    let endCharCode = char2.charCodeAt(0);
    let result = "";
  
    if (startCharCode > endCharCode) {
      for (let i = endCharCode + 1; i < startCharCode; i++) {
        result += String.fromCharCode(i) + " ";
      }
    } else {
      for (let i = startCharCode + 1; i < endCharCode; i++) {
        result += String.fromCharCode(i) + " ";
      }
    }
  
    console.log(result);
  }
  
  printCharactersInRange('a', 'd'); // Output: b c
  