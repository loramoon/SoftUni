function deleteByEmail() {
    const emailInput = document.querySelector('input[name="email"]');
    const email = emailInput.value.trim().toLowerCase();
    const rows = document.querySelectorAll("#customers tbody tr");
    let found = false;
    for (let i = 0; i < rows.length; i++) {
      const row = rows[i];
      const rowEmail = row.cells[1].textContent.trim().toLowerCase();
      if (rowEmail === email) {
        row.remove();
        emailInput.value = ''
        found = true;
      }
    }
    const result = document.querySelector("#result");
    result.textContent = found ? "Deleted" : "Not found.";
    
  }
  