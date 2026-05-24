const topScroll = document.getElementById('id_top')
const contacts = document.getElementById('contacts')
const aboutUs = document.getElementById('id_aboutUs')
const reviews = document.getElementById('id_reviews')
const btnDirections = document.getElementById('id_directions')
const accordion1 = document.getElementById('id_column3')
const accordion2 = document.getElementById('id_column4')
const btnReviews = document.getElementById('btnReviews')
const applicationBlock = document.getElementById('id_arrange')
const closeExit = document.getElementById('id_close')
const buttonOpen = document.getElementById('id_button')

// Прокрутка
reviews.onclick = function() {
    document.querySelector('.reviews').scrollIntoView({'behavior': 'smooth'})
}

aboutUs.onclick = function() {
    document.querySelector('.biografy').scrollIntoView({
        'behavior': 'smooth'
    })
}

btnDirections.onclick = function() {
    document.querySelector('.tour').scrollIntoView({'behavior': 'smooth'})
}

contacts.onclick = function() {
    document.querySelector('.footer-full').scrollIntoView({'behavior': 'smooth'})
}
   

topScroll.onclick = function() {
    window.scrollTo({ 
        top: 0, behavior: 'smooth' 
    });
}

topScroll.style.display = 'none'
window.onscroll = () => {
    if(window.scrollY > 450){
        topScroll.style.display = 'flex'
    } else {
        topScroll.style.display = 'none'
    }
}

// Аккордеон
accordion1.style.display = 'none'
accordion2.style.display = 'none'

btnReviews.onclick = function() {
    if(accordion1.style.display === 'none') {
        accordion1.style.display = 'flex'; 
        accordion2.style.display = 'flex'; 
    } else {
        accordion1.style.display = 'none'
        accordion2.style.display = 'none'
    }
}

// Блок заявки
applicationBlock.style.display = 'none'

buttonOpen.onclick = function() {
    applicationBlock.style.display = 'flex'
}

closeExit.onclick = function(){
    applicationBlock.classList.add('outputApp')
    setTimeout(()=> {
        applicationBlock.style.display = 'none';
        applicationBlock.classList.remove('outputApp');
        const exitError = document.querySelector('.error_message')
        if(exitError) {
            exitError.remove()
            document.querySelectorAll('.error-input').forEach(e => {
                e.classList.remove('error-input')
            })
        }
    },1000)
}

// Уведомление
setTimeout(()=> {
    const thanks = document.querySelector('.messages_thanks')
    if(thanks) {
        thanks.classList.add('output')
        setTimeout(()=> {
            thanks.remove('output')
        }, 1000)
    }
},3000)

// Ошибка
const scrollOpenError = document.querySelector('.error_message')

if(scrollOpenError) {
    document.querySelector('.pdf').scrollIntoView({behavior : 'smooth'})
    applicationBlock.style.display = 'flex'
}


