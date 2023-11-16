/**
 * Fetches the latest detection image from the server.
 * @returns {Promise<Blob|null>} A Promise resolving to the image Blob or null if an error occurs.
 */
async function getLastDetectionImage() {
    try {
        const response = await fetch(`/images/detection/last`);
        
        if (!response.ok) {
            throw new Error('Response was not successful');
        }
        
        return await response.blob();
    } catch (error) {
        console.error('Error fetching last detection image:', error);
        return null;
    }
}

/**
 * Fetches the latest original image from the server.
 * @returns {Promise<Blob|null>} A Promise resolving to the image Blob or null if an error occurs.
 */
async function getLastOriginalImage() {
    try {
        const response = await fetch(`/images/original/last`);
        
        if (!response.ok) {
            throw new Error('Response was not successful');
        }
        
        return await response.blob();
    } catch (error) {
        console.error('Error fetching last original image:', error);
        return null;
    }
}


/**
 * Fetches the latest original image from the server.
 * @returns {Promise<Blob|null>} A Promise resolving to the image Blob or null if an error occurs.
 */
async function getNextAlbumImg() {
    try {
        const response = await fetch(`/images/album/next`);
        
        if (!response.ok) {
            throw new Error('Response was not successful');
        }
        
        return await response.blob();
    } catch (error) {
        console.error('Error fetching next image:', error);
        return null;
    }
}


/**
 * Fetches the latest original image from the server.
 * @returns {Promise<Blob|null>} A Promise resolving to the image Blob or null if an error occurs.
 */
async function getPrevAlbumImg() {
    try {
        const response = await fetch(`/images/album/prev`);
        
        if (!response.ok) {
            throw new Error('Response was not successful');
        }
        
        return await response.blob();
    } catch (error) {
        console.error('Error fetching next image:', error);
        return null;
    }
}


// Export the functions as named exports.
export { getLastDetectionImage, getLastOriginalImage,getPrevAlbumImg,getNextAlbumImg };
