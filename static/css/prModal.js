// Get modal elements
const addProjectBtn = document.getElementById('addProjectBtn');
const modalOverlay = document.getElementById('modalOverlay');
const closeModal = document.getElementById('closeModal');
const projectForm = document.getElementById('projectForm');
const successMessage = document.getElementById('successMessage');

// Hide modal by default on page load
modalOverlay.style.display = 'none';

// Function to open modal when clicking "Add Project"
addProjectBtn.addEventListener('click', (e) => {
    e.preventDefault(); // Prevent default link behavior
    modalOverlay.style.display = 'flex'; // Show the modal overlay
});

// Function to close modal when clicking the close button (cross)
closeModal.addEventListener('click', () => {
    modalOverlay.style.display = 'none'; // Hide the modal overlay
});

// Function to close modal when clicking outside the modal content
window.addEventListener('click', (event) => {
    if (event.target === modalOverlay) {
        modalOverlay.style.display = 'none'; // Hide the modal overlay
    }
});

// Handle form submission
projectForm.addEventListener('submit', (e) => {
    e.preventDefault(); // Prevent actual form submission

    // Show the success message
    successMessage.style.display = 'block';
    successMessage.style.opacity = '1'; // Set full opacity for the message initially

    // Fade out effect
    setTimeout(() => {
        successMessage.style.transition = 'opacity 1s ease-out';
        successMessage.style.opacity = '0'; // Gradually fade out the message
    }, 2000); // Wait for 2 seconds before starting the fade out

    // Hide the modal after submission
    modalOverlay.style.display = 'none';

    // Reset the form
    projectForm.reset();
});

