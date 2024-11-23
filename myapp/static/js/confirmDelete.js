document.addEventListener('DOMContentLoaded', function() {
    // Select all delete buttons by class
    const deleteBtns = document.querySelectorAll('.saveJob-delete-btn');

    deleteBtns.forEach(function(deleteBtn) {
        // Extract the job ID from the button's ID
        const jobId = deleteBtn.id.split('-')[2];  // The ID format is "delete-btn-{job.id}"
        
        const modal = document.getElementById('confirmDeleteModal-' + jobId);
        const cancelBtn = document.getElementById('cancel-delete-' + jobId);
        const confirmDeleteLink = document.querySelector('.confirm-delete-btn[href="#"]');

        // Show modal when delete button is clicked
        deleteBtn.addEventListener('click', function() {
            modal.style.display = 'block';  // Show modal
        });

        // Close modal when cancel button is clicked
        if (cancelBtn) {
            cancelBtn.addEventListener('click', function() {
                modal.style.display = 'none';  // Hide modal
            });
        }

        // Attach event listener for the delete confirmation link
        const confirmDeleteBtn = document.querySelector('.confirm-delete-btn[href*="delete_job_listing"]');
        if (confirmDeleteBtn) {
            confirmDeleteBtn.addEventListener('click', function(event) {
                // Prevent default action, but you can proceed with the delete action
                event.preventDefault();  // Prevent link navigation

                // You can directly submit the form for deletion here or trigger a redirect
                window.location.href = confirmDeleteBtn.getAttribute('href');  // Trigger the delete URL
            });
        }

    });
});
