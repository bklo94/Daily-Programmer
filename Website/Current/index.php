<?php
  /**
   * index.php
   *
   * Currant Pi - Raspberry Pi Status
   *
   * @author     Colin Waddell
   * Edited to personal uses by Brandon Lo
   * @license    https://opensource.org/licenses/MIT  The MIT License (MIT)
   * @link       https://github.com/ColinWaddell/CurrantPi
   */

   /*
    * Libraries and helper function
   */
  include ('lib/string_helpers.php');
?>

<!DOCTYPE html>
<html lang="en">
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
<meta charset="utf-8">

  <head>
    <!-- Header -->
    <?php include ('content/header.php'); ?>
  </head>

<div class="container-fluid">
  <ul class="nav navbar-nav navbar-right">
    <li><a href="../index.html" class="navigation whitelink">Home</a></li>
    <li><a href="../about.html" class="navigation whitelink">About Me</a></li>
    <li><a href="../projects.html" class="navigation whitelink">Projects</a></li>
    <li><a href="Current/index.php" class="navigation whitelink">Raspberry Status</a></li>
    <li><a href="../contact.html" class="navigation whitelink">Contact</a></li>
  </ul>
</div>

  <body>

    <div class="container">
        <!-- Banner -->
      <div class="header clearfix title-area">
        <?php include ('content/banner.php'); ?>
      </div>

      <div class="row">
        <!-- Hardware -->
        <div class="col-lg-6 widget-padding">
          <?php include ('content/hardware.php'); ?>
        </div>
        <!-- Network -->
        <div class="col-lg-6 widget-padding">
          <?php include ('content/network.php'); ?>
        </div>
      </div>

      <div class="row">
        <!-- Load Average -->
        <div class="col-lg-6 widget-padding">
          <?php include ('content/load_average.php'); ?>
        </div>
        <div class="col-lg-6 widget-padding">
          <!-- Memory -->
          <?php include ('content/memory.php'); ?>
        </div>
      </div>

      <div class="row">
        <!-- Storage -->
        <div class="col-lg-12 widget-less-padding">
          <?php include ('content/storage.php'); ?>
        </div>
      </div>

      <hr />

      <!-- Footer -->
      <footer class="footer">
        <?php include ('content/footer.php'); ?>
      </footer>

    </div> <!-- /container -->

  </body>
</html>
<!--
<style type="text/css">
body {
  background-image: url(../Images/wallpaper.jpg);
  background-repeat: no-repeat;
  background-position: center;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}
</style>
-->
