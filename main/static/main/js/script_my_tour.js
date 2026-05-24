const aboutUs = document.getElementById('id_aboutUs')

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