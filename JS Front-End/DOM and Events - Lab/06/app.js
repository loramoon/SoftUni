function addItem() {
    const newItemText = document.getElementById("newItemText").value;
    const itemsList = document.getElementById("items");

    if (newItemText === "") {
        alert("Please enter an item to add to the list");
    } else {
        const newItem = document.createElement("li");
        newItem.innerText = newItemText;

        const deleteLink = document.createElement("a");
        deleteLink.innerText = "[Delete]";
        deleteLink.href = "#";
        deleteLink.addEventListener("click", function() {
            this.parentNode.remove();
        });
        newItem.appendChild(deleteLink);

        itemsList.appendChild(newItem);
        document.getElementById("newItemText").value = "";
    }
}
