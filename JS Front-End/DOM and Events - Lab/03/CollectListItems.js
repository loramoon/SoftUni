function extractText() {
    const list = document.getElementById('items');
    const listItems = list.getElementsByTagName('li');
    const result = document.getElementById('result');
    
    for(let i = 0; i < listItems.length; i++) {
      result.value += listItems[i].textContent + '\n';
    }
  }
  