function addItem() {
    const input = document.getElementById("newItemText");
    const list = document.getElementById("items");
    const text = input.value.trim();
    if (text) {
        const li = document.createElement("li");
        li.textContent = text;
        list.appendChild(li);
        input.value = "";
    }
}
