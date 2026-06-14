const reviews = document.getElementById('id_reviews')
const aboutUs = document.getElementById('id_aboutUs')
const contacts = document.getElementById('contacts')

contacts.onclick = function() {
    window.location.href = "/#footer"
}

reviews.onclick = function() {
    window.location.href = "/#reviews"
}

aboutUs.onclick = function() {
    window.location.href = '/#biografy'
}

// Уведомление
setTimeout(() => {
            const thanks = document.querySelectorAll('.messages_thanks');
            thanks.forEach(e=> {
                e.classList.add('output')
                setTimeout(() => thanks.remove(), 1000);
            })
        },3000)