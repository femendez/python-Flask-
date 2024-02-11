<?php
  session_start();
?>
<!DOCTYPE html>
<html>

    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- <script src="./jquery.min.js"></script> -->
        <script src="./js/jquery-3.7.1.min.js"></script>
        <script src="./js/functions.js"></script>
        <link rel="stylesheet" href="./css/styles.css">

    </head>

    <body onload="cargaDatos()">
        <div style="height: 3em;background-color: blueviolet;text-align: right;">
            <input type="text" class="text-margin-10" name="seek" id="seek" style="margin-top: 0.7rem;"
                placeholder="Ingrese articulo a buscar" />
        </div>

        </div>
        <br>
        <div id="lista">

        </div>
        <!-- <input name="acep" id="acep" class="btn--radius" type="button" value="Acceptar" onclick="cargaDatos();" /> -->
    </body>



</html>
<script>
</script>