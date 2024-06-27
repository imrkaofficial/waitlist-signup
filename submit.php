<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
    if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $file = 'waitlist.txt';
        file_put_contents($file, $email . PHP_EOL, FILE_APPEND);
        echo "Thank you for joining the waitlist!";
    } else {
        echo "Invalid email address.";
    }
} else {
    echo "Invalid request.";
}
?>