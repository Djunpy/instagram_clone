const header = document.querySelector('header')


function headerHandler(e) {
    if (e.target.id === 'create-post'){
        const createPostDiv = document.querySelector('.create-post')
        e.preventDefault()
        createPostDiv.classList.add('active')


    }
}

header.addEventListener('click', headerHandler)
