function updateCourses() {
    var selectElement = document.getElementById("departmentDropdown");
    var departmentId = document.getElementById('departmentDropdown').value;
    var courseDropdown = document.getElementById('courseDropdown');

    courseDropdown.innerHTML = '<option>choose option.........</option>';

    if (departmentId) {
        var selectElement = document.getElementById("departmentDropdown");
        var selectedOption = selectElement.options[selectElement.selectedIndex];
        dataUrlValue = selectedOption.getAttribute("data-url");

        var url = '/department/get-courses/' + dataUrlValue + '/';
        console.log('Constructed URL:', url);

        fetch(url)
            .then(response => response.json())
            .then(data => {
                data.forEach(course => {
                    var option = document.createElement('option');
                    option.value = course.id;
                    option.text = course.name;
                    courseDropdown.add(option);
                });
            })
            .catch(error => {
                console.error('Error fetching courses:', error);
            });
    }
}
