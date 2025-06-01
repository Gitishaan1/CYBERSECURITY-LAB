<?php

$conn = new mysqli("localhost", "root", "", "demo");

$user = $_GET['username'];
$pass = $_GET['password'];

$result = $conn->query("SELECT * FROM users WHERE username='$user' AND password='$pass'");

if ($result->num_rows > 0) {
    echo "Login success!";
} else {
    echo "Access denied.";
}

?>

