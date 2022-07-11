//catching all the required fields from the DOM
const profileImageContainer = document.querySelector('.profile-img__container');
const profileImageEdit = document.querySelector('.profile-img__edit')
const profileImage = document.querySelector('.profile-img')
const editBtn = document.querySelector('.edit-btn')
const cancelBtn = document.querySelector('.btn-cancel')
const confirmBtn = document.querySelector('.btn-confirm')
const profileImageFile = document.getElementById('profile-image-file')
const userId = document.getElementById('id-field').value
const url = 'http://localhost:8000/account/api/crop_and_save/'
let cropX, cropY, cropWidth, cropHeight, selectedProfileImage;



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}




//adding requeried class to profile image and edit button
const addHover = () => {
    profileImageEdit.classList.add('active')
    profileImage.classList.add('active')
}

//removing requeried class to profile image and edit button
const removeHover = () => {
    profileImageEdit.classList.remove('active')
    profileImage.classList.remove('active')
}

profileImageContainer.addEventListener('mouseover', addHover, true)
profileImageContainer.addEventListener('mouseout', removeHover, true)

//on the click on edit button we are programatically clicking the button of file input filed so that input file 
//type value get set automatically bcoz the field is hidden we have to take this approch
const handleSelection = () => {
    profileImageFile.click()
}

editBtn.addEventListener('click', handleSelection)

//reading the selected file and setting it to the profile image
const readURL = (input) => {
    console.log(input.files[0])
    if (input.files && input.files[0]) {
        let reader = new FileReader()

        reader.onload = (eve) => {
            selectedProfileImage = eve.target.result;
            profileImage.src = selectedProfileImage

            //cropper js code
            cropper = new Cropper(profileImage, {
                aspectRatio: 1 / 1,
                crop(eve) {
                    //hiding the edit button
                    profileImageEdit.classList.remove('active')
                    profileImageContainer.removeEventListener('mouseover', addHover, true)

                    //showing cancel and confirm btns
                    cancelBtn.classList.add('active')
                    confirmBtn.classList.add('active')

                    // console.log('Cropt Starts....');
                    // console.log('x: ' + eve.detail.x);
                    // console.log('x: ' + eve.detail.y);
                    // console.log('x: ' + eve.detail.width);
                    // console.log('x: ' + eve.detail.height);
                    cropX = eve.detail.x
                    cropY = eve.detail.y
                    cropWidth = eve.detail.width
                    cropHeight = eve.detail.height
                }
            })
        }

        reader.readAsDataURL(input.files[0])
    }
}

const validateImageSize = (image) => {
    const startIndex = image.indexOf('base64,') + 7                 //we are doing this to get image data without its information log the image for better understanding
    const base64Str = image.substr(startIndex)
    const decod = atob(base64Str)       //atob is native js function use for decoing images

    if (decod.length >= 10485760) {
        return null
    }
    return base64Str

}

const callApi = async (image, x, y, width, height) => {
    const base64String = validateImageSize(image)
    if (base64String !== null) {
        const token = getCookie('csrftoken')
        const data = {
            cropX: x,
            cropY: y,
            cropWidth: width,
            cropHeight: height,
            image: base64String,
            userId: userId

        }
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': token
                },
                body: JSON.stringify(data)
            })
            console.log(response.status === 200);
            if (response.status === 200) {
                const data = await response.json()
                console.log(data)
                location.reload();
            }

        } catch (err) {
            console.error(err)
        }
    }else{
        alert('Please upload the image of size less than 10MB')
    }
}

const postImage = () => {
    const data = {
        cropX: cropX,
        cropY: cropY,
        cropWidth: cropWidth,
        cropHeight: cropHeight
    }
    callApi(selectedProfileImage, cropX, cropY, cropWidth, cropHeight)

}

confirmBtn.addEventListener('click', postImage)

cancelBtn.addEventListener('click', ()=>{ location.reload() })




const handleAccept = (eve)=>{
    eve.preventDefault()
    console.log('working...');
}