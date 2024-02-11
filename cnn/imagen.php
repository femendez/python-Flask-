<?php
session_start();
// if (isset($_POST['sql'])){
    $sql=$_POST['sql'];
    $conn = mysqli_connect('localhost', 'root', '', 'maryproduct');
    $result=mysqli_query($conn,$sql);
    $datos=array();
        if (mysqli_num_rows($result)>0){
            while($row=mysqli_fetch_assoc($result)){
                // $imagen = base64_dencode($row['imagen']);
                $imagen = base64_encode($row['imagen_1']);
                $imagen1 = base64_encode($row['imagen_2']);
                $imagen2 = base64_encode($row['imagen_3']);
                $imagen3 = base64_encode($row['imagen_4']);
                $txt_desc = $row['txt_desc'];
                $id=$row['cod_prod'];
                $imp_precio=$row['imp_precio'];
                $cant=$row['cant'];
                $descuento=$row['descuento'];
                $imp_descuento=$imp_precio*(1+$descuento/100);
                array_push($datos,array("txt_desc"=>$txt_desc,"cod_producto"=>$id,"imagen"=>$imagen,
                "imagen1"=>$imagen1,"imagen2"=>$imagen2,"imagen3"=>$imagen3,"imp_precio"=>$imp_precio,"cant"=>$cant,"descuento"=>$descuento,"imp_descuento"=>$imp_descuento));
            }
        }    
    echo json_encode($datos);
    mysqli_close($conn);
?>