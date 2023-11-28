<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    // SQL injection vulnerability
    $sql = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";

    echo "SQL IS: ".$sql."<br>";

    // Simulate database connection
    $dbConnection = mysqli_connect("mysql", "root", "root", "working");

    $result = mysqli_query($dbConnection, $sql);

    if ($result && mysqli_num_rows($result) > 0) {
        // Successful login
        echo "<h1>Welcome, $username!</h1><br>";
    } else {
        echo "Invalid username or password.";
    }

    mysqli_close($dbConnection);
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
</head>
<body>

<h2>Login</h2>
<form method="post">
    <div>
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
    </div>
    <div>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
    </div>
    <div>
        <input type="submit" value="Login">
    </div>
</form>

</body>
</html>
