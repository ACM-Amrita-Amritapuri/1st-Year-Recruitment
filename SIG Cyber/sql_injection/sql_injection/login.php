<?php

$servername = "";
$username = ""; 
$password = ""; 
$dbname = ""; 



$conn = new mysqli($servername, $username, $password, $dbname);


if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    $user = $_POST['username'];
    $pass = $_POST['password'];


    echo "Username: $user<br>";
    echo "Password: $pass<br>";


    $sql = "SELECT * FROM users WHERE username = '$user' AND password = '$pass'";


    echo "SQL Query: $sql<br>";

    
    $result = $conn->query($sql);     

    if (!$result) {
        die("Query failed: " . $conn->error);
    }

    if ($result->num_rows > 0) {
        
        echo "Welcome, " . htmlspecialchars($user) . "!";
    } else {
        
        echo "Invalid login credentials.";
    }
}


$conn->close();
?>
