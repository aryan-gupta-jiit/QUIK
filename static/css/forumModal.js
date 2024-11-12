    console.log("hello")
    
// Get modal elements for forum functionality
const requestForumBtn = document.getElementById('requestForumBtn');
const forumModalOverlay = document.getElementById('forumModalOverlay');
const closeForumModal = document.getElementById('closeForumModal');
const forumForm = document.getElementById('forumForm');
const forumSuccessMessage = document.createElement('div');

// Set up success message for forum form
forumSuccessMessage.id = 'forumSuccessMessage';
forumSuccessMessage.className = 'success-message';
forumSuccessMessage.innerHTML = '<center> <i>&#10004;</i> Forum Request Submitted Successfully! </center>';
forumSuccessMessage.style.display = 'none';
document.body.appendChild(forumSuccessMessage);

// Hide forum modal overlay by default
forumModalOverlay.style.display = 'none';

// Function to open forum modal on clicking "Request For Forum"
requestForumBtn?.addEventListener('click', (e) => {
    e.preventDefault();
    forumModalOverlay.style.display = 'flex';
});

// Function to close forum modal on clicking close button (the "X" icon)
closeForumModal?.addEventListener('click', () => {
    forumModalOverlay.style.display = 'none';
});

// Function to close forum modal if clicking outside the content area
window.addEventListener('click', (event) => {
    if (event.target === forumModalOverlay) {
        forumModalOverlay.style.display = 'none';
    }
});

// Handle forum form submission
forumForm?.addEventListener('submit', (e) => {
    e.preventDefault();

    // Show the forum success message
    forumSuccessMessage.style.display = 'block';
    forumSuccessMessage.style.opacity = '1';

    // Fade out effect for forum success message
    setTimeout(() => {
        forumSuccessMessage.style.transition = 'opacity 1s ease-out';
        forumSuccessMessage.style.opacity = '0';

        // Hide the success message after the fade-out
        setTimeout(() => {
            forumSuccessMessage.style.display = 'none';
        }, 1000); // 1 second after opacity transition
    }, 2000);

    // Hide the forum modal after submission
    forumModalOverlay.style.display = 'none';

    // Reset the forum form
    forumForm.reset();
});
