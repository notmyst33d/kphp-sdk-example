<?php
if ($_SERVER["REQUEST_URI"] == "/") {
    header("Location: /index.php", $http_response_code = 302);
} elseif ($_SERVER["REQUEST_URI"] == "/index.php") {
    require("index.php");
} elseif ($_SERVER["REQUEST_URI"] == "/time.php") {
    header("Content-Type: text/plain");
    require("time.php");
    print(omskTime());
} else {
    header("Content-Type: text/plain", $http_response_code = 404);
    print("404 Not Found");
}
?>
