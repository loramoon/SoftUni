function extractAndConvertToUpperCase(str) {
    const words = str.match(/\w+/g);
    const upperCaseWords = words.map(word => word.toUpperCase());
    const result = upperCaseWords.join(', ');
    console.log(result);
  }
  
  extractAndConvertToUpperCase("This is a sample string with some words.");
  