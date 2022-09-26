const createPostDiv = document.querySelector('.create-post')
const img = document.querySelector('#upload-img')


function createPostDivHandler(e){
    if (e.target.id === 'id_picture'){
        uploadInput = document.querySelector('#id_picture')

        uploadInput.addEventListener('change', ( e) => {
            if (!e.target.files.length){
                return
            }
            const file = e.target.files[0]
            const reader = new FileReader()
            reader.onload = function (ev) {
                const src = ev.target.result
                img.src = src
            }
            reader.readAsDataURL(file)
        })

    }

    if (e.target.id === 'close-upload-menu'){
        createPostDiv.classList.remove('active')
    }

    if(e.target.id === 'btn-save-mod'){
        const btnDefaultSavePost = document.querySelector('#btn-save-default')
        btnDefaultSavePost.click()
    }
}

createPostDiv.addEventListener('click', createPostDivHandler)