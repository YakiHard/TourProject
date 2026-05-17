const btnOpen = document.getElementById('btnOpen')
const applicationBlock = document.getElementById('id_arrange');
const directionSelect = document.getElementById('id_direction');
const closeExit = document.getElementById('id_close');
const id_mountains = document.getElementById('id_mountains');
const phuhetBlock = document.getElementById('id_phuket_mountains');
const hurghadaBlock = document.getElementById('id_hurghada_mountains');
const baliBlock = document.getElementById('id_bali_mountains');
const maleBlock = document.getElementById('id_male_mountains');

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
        applicationBlock.style.display = 'none'
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

// Направление
function showMountains() {
    if(id_mountains)id_mountains.style.display = 'none';
    if(phuhetBlock)phuhetBlock.style.display = 'none';
    if(hurghadaBlock)hurghadaBlock.style.display = 'none';
    if(baliBlock)baliBlock.style.display = 'none';
    if(maleBlock)maleBlock.style.display = 'none';

    if (directionSelect.value === "Phuket") {
        id_mountains.style.display = 'block';
        phuhetBlock.style.display = 'block';
    } else if (directionSelect.value === "Hurghada") {
        id_mountains.style.display = 'block';
        hurghadaBlock.style.display = 'block';
    } else if (directionSelect.value === "Bali") {
        id_mountains.style.display = 'block';
        baliBlock.style.display = 'block';
    } else if (directionSelect.value === "Male") {
        id_mountains.style.display = 'block';
        maleBlock.style.display = 'block';
    }
}

// Ошибка
const hasError = document.querySelector('.error_message')

if(hasError) {
    document.querySelector('.tour').scrollIntoView({behavior: 'smooth'})
    applicationBlock.style.display = 'flex'
}

directionSelect.addEventListener('change', showMountains);   
// Вызываем сразу, чтобы скрыть поля при загрузке
showMountains();