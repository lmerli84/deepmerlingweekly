<?php
function db_connect() {

        // Define connection as a static variable, to avoid connecting more than once 
    static $connection;

        // Try and connect to the database, if a connection has not been established yet
    if(!isset($connection)) {
             // Load configuration as an array. Use the actual location of your configuration file
        $config = parse_ini_file('./secure/config.ini'); 
        $connection = mysqli_connect($config['servername'],$config['username'],$config['password'],$config['dbname']);
    }

        // If connection was not successful, handle the error
    if($connection === false) {
            // Handle error - notify administrator, log to a file, show an error screen, etc.
        return mysqli_connect_error(); 
    }
    return $connection;
}

// Connect to the database
$connection = db_connect();

// Check connection
if ($connection->connect_error) {
    die("Connection failed: " . $connection->connect_error);
} else {
    echo "connected ";
}

 
$sql = "SELECT * FROM anag_game";
$result = $connection->query($sql);
if (!$result)
    die("Database access failed: " . mysqli_error());

//echo $sql;
//echo "<p> </p>";
//echo mysqli_num_rows($result);


//SELECT `ID`, `NAME`, `OWNER`, `DESCR`, `RULES`, `RATING` FROM `anag_game` WHERE 1


?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0"/>
  <title>DeepMerlingWeekly.com</title>

  <!-- CSS  -->
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <link href="css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
  <link href="css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
</head>
<body>
  <nav class="blue lighten-1" role="navigation">
    <div class="nav-wrapper container">
      <!-- <a id="logo-container" href="#" class="brand-logo">Logo che manca</a> -->
      <ul class="right hide-on-med-and-down">
          <li><a href="http://www.deepmerlingweekly.com">Home</a></li>
          <li><a href="http://www.deepmerlingweekly.com/issues/issues.html">Issues</a></li>
          <li><a href="http://www.deepmerlingweekly.com/subscribe.html" id="download-button" class="btn waves-effect waves-light yellow darken-2">Subscribe!</a></li>
      </ul>
    </div>
  </nav>
  <div class="section no-pad-bot" id="index-banner">
    <div class="container">
      <br><br>
      <h2 class="header center yellow-text text-darken-2">Boardgames</h2>
<div class="row center" id="issue_container">

<div class="row center">
<?php
while ($row = $result->fetch_assoc()) {  

echo "<u>".$row['ID']."<b>".$row['NAME']."</b></u>";
}
?>
</div>

      </div>
    </div>
      <br><br>

    </div>
  </div>


  <footer class="page-footer yellow darken-2">
    <div class="container">
      <div class="row">
        <div class="col l6 s12">
          <h5 class="white-text">Company Bio</h5>
          <p class="grey-text text-lighten-4">Nata per scherzo, in crescita costante, si spera non muoia</p>


        </div>
        <!-- <div class="col l3 s12">
          <h5 class="white-text">Settings</h5>
          <ul>
            <li><a class="white-text" href="#!">Link 1</a></li>
            <li><a class="white-text" href="#!">Link 2</a></li>
            <li><a class="white-text" href="#!">Link 3</a></li>
            <li><a class="white-text" href="#!">Link 4</a></li>
          </ul>
        </div>
        <div class="col l3 s12">
          <h5 class="white-text">Connect</h5>
          <ul>
            <li><a class="white-text" href="#!">Link 1</a></li>
            <li><a class="white-text" href="#!">Link 2</a></li>
            <li><a class="white-text" href="#!">Link 3</a></li>
            <li><a class="white-text" href="#!">Link 4</a></li>
          </ul>
        </div>-->
      </div>
    </div>
    <div class="footer-copyright">
      <div class="container">
      Made by <a class="yellow-text text-lighten-3" href="http://materializecss.com">Materialize</a>
      </div>
    </div>
  </footer>


 <!--  Scripts-->
 <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
 <script src="js/materialize.js"></script>


  </body>
</html>
