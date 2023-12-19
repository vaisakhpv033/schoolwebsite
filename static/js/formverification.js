$(document).ready(function () {
    // Add custom validation methods
    $.validator.addMethod("positiveIntegerMax100", function (value, element) {
        // Check if the value is a positive integer less than or equal to 100
        return /^[1-9]\d*$/.test(value) && parseInt(value, 10) <= 100;
    }, "Please enter a valid age.");

    $.validator.addMethod("positiveInteger", function (value, element) {
        // Check if the value is a positive integer
        return /^[1-9]\d*$/.test(value);
    }, "Please enter a valid  mobile number.");

    $("#register-form").validate({
        rules: {
            email: {
                email: true
            },
            age: {
                positiveIntegerMax100: true
            },
            phone_number: {
                maxlength: 10,
                minlength: 10,
                positiveInteger: true
            },
            address: {
                required: true
            },
            department: {
                required: true,
                notEqual: "choose option........."
            },
            course: {
                required: true,
                notEqual: "choose option........."
            },
            gender: {
                required: true
            },
            purpose: {
                required: true
            }
        }
    })
});
