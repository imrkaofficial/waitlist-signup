$(document).ready(function() {
    $('#waitlist-form').on('submit', function(event) {
        event.preventDefault();
        var email = $('#email').val();
        if (!validateEmail(email)) {
            $('#email').addClass('is-invalid');
            $('.invalid-feedback').show();
            return;
        }
        $('#email').removeClass('is-invalid');
        $('.invalid-feedback').hide();
        $('#spinner').show();
        $.ajax({
            url: '/',
            type: 'POST',
            data: { email: email },
            success: function(response) {
                $('#spinner').hide();
                $('#message').html('<div class="alert alert-success">' + response.message + '</div>');
                $('#email').val('');
            },
            error: function() {
                $('#spinner').hide();
                $('#message').html('<div class="alert alert-danger">There was an error. Please try again.</div>');
            }
        });
    });

    function validateEmail(email) {
        var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
});
