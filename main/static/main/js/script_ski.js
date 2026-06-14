const btnOpen = document.getElementById('btnOpen')
const aboutUs = document.getElementById('id_aboutUs')
const applicationBlock = document.getElementById('id_arrange');
const closeExit = document.getElementById('id_close')
const directionSelect = document.getElementById('id_direction');
const id_mountains = document.getElementById('id_mountains');
const zermattBlock = document.getElementById('id_zermatt_mountains');
const grindelwaldBlock = document.getElementById('id_grindelwald_mountains')
const chamonixBlock = document.getElementById('id_chamonix_mountains');
const caruisoBki = document.getElementById('id_caruiso_ski')

function aboutScroll() {
    window.location.href = '/#biografy';
}
aboutUs.onclick = aboutScroll

// Блок заявки
applicationBlock.style.display = 'none'

btnOpen.onclick = function () {
    if(applicationBlock.style.display === 'none') {
        applicationBlock.style.display = 'flex';
    } else {
        applicationBlock.style.display = 'none'
    }
} 

closeExit.onclick = function() {
    applicationBlock.classList.add('outputApp')
    setTimeout(() => {
        applicationBlock.style.display = 'none';
        applicationBlock.classList.remove('outputApp')
        const exitError = document.querySelector('.error_message')
        if(exitError) {
            exitError.remove()
            document.querySelectorAll('.error-input').forEach(e => {
                e.classList.remove('error-input')
            })
        }

    },1000)
}

// Навпраление
function showMountains() {
    if(id_mountains)id_mountains.style.display = 'none';
    if(zermattBlock)zermattBlock.style.display = 'none';
    if(grindelwaldBlock)grindelwaldBlock.style.display = 'none';
    if(chamonixBlock)chamonixBlock.style.display = 'none';
    if(caruisoBki)caruisoBki.style.display = 'none;'
    if (directionSelect.value === 'Zermatt') {
        id_mountains.style.display = 'block';
        zermattBlock.style.display = 'block';
    } else if (directionSelect.value === 'Grindelwald') {
        id_mountains.style.display = 'block';
        grindelwaldBlock.style.display = 'block';
    } else if (directionSelect.value === 'Chamonix') {
        id_mountains.style.display = 'block';
        chamonixBlock.style.display = 'block';
    } else if (directionSelect.value === 'Caruiso') {
        id_mountains.style.display = 'block';
        caruisoBki.style.display = 'block';
    }
}

// Уведомление об ошибке
const hasError = document.querySelector('.error_message')
if(hasError) {
    document.querySelector('.tour').scrollIntoView({behavior: 'smooth'});
    applicationBlock.style.display = 'flex';
}

// Вешаем событие на изменение выбора
directionSelect.addEventListener('change', showMountains);
    
// Вызываем сразу, чтобы скрыть поля при загрузке
showMountains();
