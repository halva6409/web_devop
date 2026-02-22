let allNews = []

async function loadNews() {
    const response = await fetch("/api/news")
    const news = await response.json()
    allNews = news
    const newsList = document.getElementById("newsList")
    newsList.innerHTML = ''

    news.forEach(item => {
        const card = document.createElement('div')
        card.className = 'news-card'
        card.innerHTML = `
            <h3>${item.title}</h3>
            <p class='source'> Источник: ${item.source}</p>
        `
        card.addEventListener('contextmenu' , function(event){
            event.preventDefault()
            deleteNews(item.id)
        })
        newsList.appendChild(card)
    })
}

async function addNews(){
    const title_pole = document.getElementById('title_new').value
    const source_pole = document.getElementById('source_new').value
    await fetch('/api/news', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            title: title_pole,
            source: source_pole
        })
    })
    await loadNews()
    document.getElementById('title_new').value = ''
    document.getElementById('source_new').value = ''
}
async function deleteNews(id) {
    await fetch(`/api/news/${id}`, { method: 'DELETE' })
    await loadNews()
}

async function uploadImage(){
    const file = document.getElementById('imageFile').files[0]
    const formdata = new FormData()
    formdata.append('image', file)
    const ans = await fetch('/api/upload', {
                method: 'POST',
                body: formdata
            })
    const result = await ans.json()
    document.getElementById('uploadResult').innerHTML = `<img scr="${result.url}>`
}

document.getElementById('post_new').addEventListener('click', addNews)
document.addEventListener('DOMContentLoaded', loadNews)
document.getElementById('refreshButton').addEventListener('click', loadNews)
document.getElementById('upload').addEventListener('click', uploadImage)

document.getElementById('SearchPole').addEventListener('input', function() {
    const searching = this.value.toLowerCase()
    const filtered = allNews.filter(item => item.title.toLowerCase().includes(searching))
    const reNewList = document.getElementById('newsList')
    reNewList.innerHTML = ''
    filtered.forEach(item => {
        const card = document.createElement('div')
        card.className = 'news-card'
        card.innerHTML = `
            <h3>${item.title}</h3>
            <p class='source'> Источник: ${item.source}</p>
        `
        reNewList.appendChild(card)
    })
})

