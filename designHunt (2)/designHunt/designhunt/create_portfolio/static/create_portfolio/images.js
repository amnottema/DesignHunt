document.querySelectorAll('.file input[type="file"]').forEach(inputFile => {
    inputFile.addEventListener('change', function () {
        const dt = new DataTransfer();
        const filesList = this.closest('label').nextElementSibling;

        if (filesList && filesList.classList.contains('file-list')) {
            filesList.innerHTML = '';

            if (this.files.length > 3) {
                alert("Нельзя загрузить более 3 файлов.");
                this.value = ''; 
                return;
            }

            Array.from(this.files).forEach(file => {
                dt.items.add(file);
                const reader = new FileReader();
                reader.readAsDataURL(file);

                reader.onloadend = () => {
                    const fileItem = document.createElement('div');
                    fileItem.classList.add('file-list-item');

                    const img = document.createElement('img');
                    img.classList.add('file-list-img');
                    img.src = reader.result;

                    const fileName = document.createElement('span');
                    fileName.classList.add('file-list-name');
                    fileName.textContent = file.name;

                    const removeBtn = document.createElement('a');
                    removeBtn.href = '#';
                    removeBtn.classList.add('file-list-remove');
                    removeBtn.textContent = 'x';

                    removeBtn.addEventListener('click', (event) => {
                        event.preventDefault();
                        removeFilesItem(file.name, inputFile, fileItem, dt);
                    });

                    fileItem.appendChild(img);
                    fileItem.appendChild(fileName);
                    fileItem.appendChild(removeBtn);

                    filesList.appendChild(fileItem);
                };
            });

            inputFile.files = dt.files;
        }
    });
});

function removeFilesItem(fileName, input, fileItem, dt) {
    fileItem.remove(); 

    for (let i = 0; i < dt.items.length; i++) {
        if (dt.items[i].getAsFile().name === fileName) {
            dt.items.remove(i);
            break;
        }
    }

    input.files = dt.files;
}