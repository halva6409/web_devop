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
        newsList.appendChild(card)
    })
}
document.addEventListener('DOMContentLoaded', loadNews)
document.getElementById('refreshButton').addEventListener('click', loadNews)
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
