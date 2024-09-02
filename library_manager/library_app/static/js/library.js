
var addModal = document.getElementById("addBookModal");

var delModal = document.getElementById("delBookModal");

var addbtn = document.getElementById("openAddModalBtn");

var delbtn = document.getElementById("openDelModalBtn");

var closeBtns = document.getElementsByClassName("close");

addbtn.onclick = function() {
    addModal.style.display = "block";
}

delbtn.onclick = function () {
    delModal.style.display = "block";
}

 for (let btn of closeBtns) {
btn.onclick = function() {
    addModal.style.display = "none";
    delModal.style.display = "none";
};
}

window.onclick = function(event) {
        if (event.target == addModal) {
            addModal.style.display = "none";
        } else if (event.target == delModal) {
            delModal.style.display = "none";
        }
    };

function updateHiddenFields() {
    const dropdown = document.getElementById('bookDropdown');
    const selectedOption = dropdown.options[dropdown.selectedIndex];
    document.getElementById('hiddenBookName').value = selectedOption.getAttribute('data-name');
    document.getElementById('hiddenBookAuthor').value = selectedOption.getAttribute('data-author');
    document.getElementById('hiddenBookYear').value = selectedOption.getAttribute('data-year');
}