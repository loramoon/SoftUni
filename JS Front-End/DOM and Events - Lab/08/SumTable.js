function sumTable() {
    const table = document.getElementsByTagName('table')[0];
    const rows = table.getElementsByTagName('tr');
    let sum = 0;
    for (let i = 1; i < rows.length - 1; i++) {
      const cells = rows[i].getElementsByTagName('td');
      const value = parseFloat(cells[cells.length - 1].textContent);
      sum += value;
    }
    document.getElementById('sum').textContent = sum.toFixed(2);
  }
  