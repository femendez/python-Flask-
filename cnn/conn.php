<?php
session_start();
// include('/conn.php');
$conn = mysqli_connect('localhost', 'root', '', 'maryproduct');
// $conn = mysqli_connect('host17.latinoamericahosting.com', 'dbwebsof_fmendez', '5O]#{V1b{oS(', 'dbwebsof_development');
if (!$conn) {
    echo 'no se pudo conectar a la base de datos';
} 
?>