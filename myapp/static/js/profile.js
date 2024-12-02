document.addEventListener('DOMContentLoaded', () => {
    const saveBtn = document.getElementById('save-btn');
    const editBtn = document.getElementById('edit-btn');
    const formInputs = document.querySelectorAll('.profile-form input, .profile-form textarea');

    // Make fields readonly after the form is saved
    function setFieldsReadonly(isReadonly) {
        formInputs.forEach(input => {
            if (isReadonly) {
                input.setAttribute('readonly', 'readonly');
            } else {
                input.removeAttribute('readonly');
            }
        });

        const resumeInput = document.getElementById('resume');
        if (isReadonly) {
            resumeInput.setAttribute('disabled', 'disabled');
        } else {
            resumeInput.removeAttribute('disabled');
        }
    }

    // Initial state: Fields are readonly if the profile is already saved
    setFieldsReadonly(true);

    // Enable editing when Edit is clicked
    editBtn.addEventListener('click', () => {
        setFieldsReadonly(false);
        editBtn.style.display = 'none';
        saveBtn.style.display = 'inline-block';
    });

    // Automatically make fields readonly after Save button is clicked
    saveBtn.addEventListener('click', () => {
        setFieldsReadonly(true);
        saveBtn.style.display = 'none';
        editBtn.style.display = 'inline-block';
    });
});
