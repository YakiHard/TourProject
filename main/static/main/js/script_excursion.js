const btnOpen = document.getElementById('btnOpen')
const closeExit = document.getElementById('id_close')
const directionSelect = document.getElementById('id_direction')
const id_mountains = document.getElementById('id_mountains')
const applicationBlock = document.getElementById('id_arrange')
const parisBlock = document.getElementById('id_paris_excursion')
const romeBlock = document.getElementById('id_rome_excursion')
const istanbulBlock = document.getElementById('id_istanbul_excursion')
const saintBlock = document.getElementById('id_saint_excursion')

// Блок заявки
applicationBlock.style.display = 'none'

btnOpen.onclick = function() {
    if(applicationBlock.style.display === 'none') {
        applicationBlock.style.display = 'flex';
    } else {
        applicationBlock.style.display = 'none'
    }
}

closeExit.onclick = function() {
    applicationBlock.classList.add('outputApp')
    setTimeout(() => {
        applicationBlock.style.display = 'none'
        applicationBlock.classList.remove('outputApp')
        const exitError = document.querySelector('.error_message')
        if(exitError)  {
            exitError.remove()
            document.querySelectorAll('.error-input').forEach(e => {
                e.classList.remove('error-input')})
        }  
    }, 1000)
}

// Навпраление
function showMountains() {
    if(parisBlock) { 
        parisBlock.style.display = 'none'
    }
    if(romeBlock) {
        romeBlock.style.display = 'none'
    }
    if(istanbulBlock) {
        istanbulBlock.style.display = 'none'
    }
    if(saintBlock) {
        saintBlock.style.display = 'none'
    }

    if(directionSelect.value === 'Paris') {
        id_mountains.style.display = 'block';
        parisBlock.style.display = 'block'
    } else if(directionSelect.value === 'Rome') {
        id_mountains.style. display = 'block';
        romeBlock.style.display = 'block';
    } else if(directionSelect.value === 'Istanbul') {
        id_mountains.style.display = 'block';
        istanbulBlock.style.display = 'block';
    } else if(directionSelect.value === 'Saint-Petersburg') {
        id_mountains.style.display = 'block'
        saintBlock.style.display = 'block'
    } 
}

// Уведомление об ошибке
const scrollOpenError = document.querySelector('.error_message')

if(scrollOpenError) {
    document.querySelector('.tour').scrollIntoView({behavior : 'smooth'})
    applicationBlock.style.display = 'flex'
}

directionSelect.addEventListener('change', showMountains)

showMountains()