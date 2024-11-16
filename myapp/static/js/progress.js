document.addEventListener('DOMContentLoaded', function () {
    // const progressItems = document.querySelectorAll('.v-progress-item'); // All progress items
    // const koala = document.querySelector('.progress-koala-image img'); // Koala image
    // const ladderHeight = document.querySelector('.ladder-image img').clientHeight; // Ladder height
    // const totalItems = progressItems.length; // Total progress items
    const currentJobStatus = document.querySelector('#status').textContent.trim();
    const progressItems = document.querySelectorAll('.v-progress-item'); // All progress items
    const koala = document.querySelector('.progress-koala-image'); // Koala image
    
    const vProgressMap = new Map([
        ['Offer', 0],
        ['Follow-Up', 1],
        ['Interviewing', 2],
        ['Applied', 3],
        ['Wishlist', 4]
    ]);

    function updateVProgress() {
        const currentInprogressIndex = vProgressMap.get(currentJobStatus);
        for (let index = 0; index < progressItems.length; index++) {
            if (index === currentInprogressIndex) {
                progressItems[index].classList.add('inprogress');
            } else if (index > currentInprogressIndex) {
                progressItems[index].classList.add('completed');
            }
        }    
    }
    // Calculate the koala's position based on completed items
    function updateKoalaPosition() {
        switch(currentJobStatus) {
            case "Wishlist":
                koala.style.top = '60%';
                break;
            case "Applied":
                koala.style.top = '40%';
                break;
            case "Interviewing":
                koala.style.top = '20%';
                break;
            case "Follow-Up":
                koala.style.top = '-2%';
                break;
            case "Offer":
                koala.style.top = '-20%';
                break;
            default:
                koala.style.top = '60%';

        }

    }

    updateVProgress();
    
    setTimeout(() => updateKoalaPosition(), 300);
    // Initialize koala position



});
