<!DOCTYPE html>
<html>
  <head>

    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <title> R1C website </title>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    
    <!-- Naš CSS -->
    <link rel="stylesheet" href="/css/base.css">

    <style>

      /*ta gavno je za iframe za urnik*/
      .skrij-se-prihaja-jujetova-koda{
        margin:50px;
        border-radius:15px;
        border-style: solid;
        border-color:#007BAC;
        border-width: 5px;
      }

    </style>
  </head>
  <body>


    <!--Ta koda zloada navbar.html file da nam ni treba za vsako spremembo pr navbaru editat vseh html filou-->
    <?php
      require 'templates/navbar.html';
    ?>

    <!--tale neurejena, complicated, napol ukradena koda zloada urink iz urnik.vegova.si in ga automatsko adjusta na screen size. probably. -->

    <div class="skrij-se-prihaja-jujetova-koda">
      <iframe src="https://www.easistent.com/urniki/30a1b45414856e5598f2d137a5965d5a4ad36826/razredi/424558" onload='javascript:(function(o){o.style.height=o.contentWindow.document.body.scrollHeight+"px";}(this));' style="height:600px;width:100%;border:none;overflow:hidden;"></iframe>
      <p><b>Opozorilo: </b>Ta urnik ni za vse! To je splošni urnik za naš razred! Možno je, da ma kdo rahlo drugačnega!</p>
    </div>


    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>

  </body>
</html>