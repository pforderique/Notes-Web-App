// personal js methods

// js func for deleting notes
function deleteNote(noteId) {
    fetch('/delete-note', {
        method:'POST',
        body:JSON.stringify({ noteId: noteId })
    }).then((_res) => {
        window.location.href = "/"; // redirect us to homepage
    })
}