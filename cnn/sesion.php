<?php
    session_start();
    if(isset($_GET['cod_producto'])){
        $_SESSION['cod_producto']=$_GET['cod_producto'];       
        echo $_SESSION['cod_producto'];
    } 
?>