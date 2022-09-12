const titleInput = document.getElementById("title-input")
const noteInput = document.getElementById("note-input")
const deleteIndexInput = document.getElementById("delete-index-input")
const submitBtn = document.getElementById("submit-btn")
const deleteAllBtn = document.getElementById("delete-all-btn")
const deleteIndexBtn = document.getElementById("delete-index-btn")
const notesUl = document.getElementById("notes-ul")

let notes = []

const notesFromLocalStorage = JSON.parse(localStorage.getItem("notes"))

if(notesFromLocalStorage) {
    notes = notesFromLocalStorage
    render(notes)
}
 
submitBtn.addEventListener("click", function() {
    notes.push({title: titleInput.value, note: noteInput.value})
    localStorage.setItem("notes", JSON.stringify(notes))
    render(notes)
    titleInput.value = ""
    noteInput.value = "" 
})

deleteIndexBtn.addEventListener("dblclick", function() {
    notes.splice(deleteIndexInput.value-1, 1)
    localStorage.setItem("notes", JSON.stringify(notes))
    render(notes)
    deleteIndexInput.value = "" 
})

deleteAllBtn.addEventListener("dblclick", function() {
    notes = []
    localStorage.clear()
    render(notes)
})

function render(arr) {
    arr.forEach((item) => {
        item.note = item.note.replace(/\n\r?/g, '<br />')
    })
    let listItems = ""
    for (let i = 0; i < arr.length; i++)
        listItems += `
        <li class="left-text">
        <p>${i+1}</p>
            <h1>${arr[i].title}</h1>
            <p>${arr[i].note}</p>
        </li>`
        notesUl.innerHTML = listItems
}