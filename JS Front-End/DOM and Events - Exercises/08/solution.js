function solve() {
  const [generateTextarea, buyTextarea] = Array.from(document.getElementsByTagName("textarea"));
  const [generateBtn, buyBtn] = Array.from(document.getElementsByTagName('button'));
  const tbody = document.querySelector('.table > tbody');

  generateBtn.addEventListener('click', generateHandler);
  buyBtn.addEventListener('click', buyHandler);

  function generateHandler() {
    const data = JSON.parse(generateTextarea.value);

    for (const { img, name, price, decFactor } of data) {
      const tableRow = createElement('tr', '', tbody);
      const firstColumnId = createElement('td', '', tableRow);
      createElement('img', '', firstColumnId, '', '', { src: img });
      const secondColumnID = createElement('td', '', tableRow);
      createElement('p', name, secondColumnID);
      const thirdColumnID = createElement('td', '', tableRow);
      createElement('p', price, thirdColumnID);
      const fourthColumnID = createElement('td', '', tableRow);
      createElement('p', decFactor, fourthColumnID);
      const fifthColumnID = createElement('td', '', tableRow);
      createElement('input', '', fifthColumnID, '', '', { type: 'checkbox' });
    }
  }

  function createElement(type, content, parentNode, id, classes, attributes) {
    const htmlElement = document.createElement(type);

    if (content && type !== 'input') {
      htmlElement.textContent = content;
    }

    if (content && type === 'input') {
      htmlElement.value = content;
    }

    if (parentNode) {
      parentNode.appendChild(htmlElement);
    }

    if (id) {
      htmlElement.id = id;
    }

    if (classes) {
      htmlElement.classList.add(...classes);
    }

    if (attributes) {
      for (const key in attributes) {
        htmlElement.setAttribute(key, attributes[key]);
      }
    }

    return htmlElement;
  }

  function buyHandler() {
    const allCheckedInputs = Array.from(document.querySelectorAll('tbody tr input:checked'));
    const boughtFurniture = [];
    let totalPrice = 0;
    let totalDecFactor = 0;

    for (const input of allCheckedInputs) {
      const tableRow = input.parentElement.parentElement;
      const [firstColumn, secondColoumn, thirdColumn, fourthColumn] = Array.from(tableRow.children);
      const item = secondColoumn.children[0].textContent;
      boughtFurniture.push(item);
      const currentPrice = Number(thirdColumn.children[0].textContent);
      totalPrice += currentPrice;
      const currentDecFactor = Number(fourthColumn.children[0].textContent);
      totalDecFactor += currentDecFactor;
    }

    buyTextarea.value += `Bought furniture: ${boughtFurniture.join(", ")}\n`;
    buyTextarea.value += `Total price: ${totalPrice.toFixed(2)}\n`;
    buyTextarea.value += `Average decoration factor: ${totalDecFactor / allCheckedInputs.length}`;
  }
}
