function colorize() {
    const rows = document.getElementsByTagName('tr');
    for (let i = 1; i < rows.length; i += 2) {
      const row = rows[i];
      if (!row.style.backgroundColor.includes('teal')) {
        row.style.backgroundColor = 'teal';
      } else {
        console.error('Row was erroneously colorized: expected \'teal\' to not include \'teal\'');
      }
    }
  }
  