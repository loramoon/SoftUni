function addItem() {
    // Get the input values
    const newItemText = document.getElementById("newItemText").value;
    const newItemValue = document.getElementById("newItemValue").value;
  
    // Create a new option element
    const newOption = document.createElement("option");
    newOption.text = newItemText;
    newOption.value = newItemValue;
  
    // Add the new option to the select element
    const selectElement = document.getElementById("menu");
    selectElement.add(newOption);
  
    // Clear the input fields
    document.getElementById("newItemText").value = "";
    document.getElementById("newItemValue").value = "";
  }
  