// script.js


// Import the getLastDetectionImagePath function
import { getLastDetectionImage, getLastOriginalImage,getNextAlbumImg,getPrevAlbumImg } from './imageFunctions.js';

// Call the async function
async function updateDetectionImage() {
    try {
        const imageBlob = await getLastDetectionImage();
        if (imageBlob) {
            const detectionImage = document.getElementById('detectionImage');
            detectionImage.src = URL.createObjectURL(imageBlob);
        }
    } catch (error) {
        console.error('Error updating detection image:', error);
    }
}

// Call the async function
async function updateOriginalImage() {
    try {
        const imageBlob = await getLastOriginalImage();
        if (imageBlob) {
            const detectionImage = document.getElementById('detectionImage');
            detectionImage.src = URL.createObjectURL(imageBlob);
        }
    } catch (error) {
        console.error('Error updating detection image:', error);
    }
}

const buttonLeftArrow = document.getElementById("buttonLeftArrow");
const buttonRightArrow = document.getElementById("buttonRightArrow");





buttonLeftArrow.addEventListener("click", async () => {
    
    try {
        const imageBlob = await getNextAlbumImg();
        if (imageBlob) {
            const albumImage = document.getElementById('albumImage');
            albumImage.src = URL.createObjectURL(imageBlob);
            console.log("click");
        }
    } catch (error) {
        console.error('Error updating album prev image:', error);
    }
    
});

buttonRightArrow.addEventListener("click", async () => {
    
    try {
        const imageBlob = await getPrevAlbumImg();
        if (imageBlob) {
            const albumImage = document.getElementById('albumImage');
            albumImage.src = URL.createObjectURL(imageBlob);
            console.log("click");
        }
    } catch (error) {
        console.error('Error updating album next image:', error);
    }
});
// Call the updateDetectionImage function every 500 milliseconds
// updateDetectionImage();
setInterval(updateDetectionImage, 200);

