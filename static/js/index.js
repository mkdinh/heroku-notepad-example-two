
d3.json('/api/notes/postgres').then(data => {
    var list = d3.select('#notes')
    data.forEach(note => {
        var li = list.append('li')
        li.text(note.content)
    })
})