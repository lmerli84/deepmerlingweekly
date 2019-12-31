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

echo $sql;
echo "<p> </p>";
echo mysqli_num_rows($result);

echo "<b><center>Database Output</center></b><br><br>";
//SELECT `ID`, `NAME`, `OWNER`, `DESCR`, `RULES`, `RATING` FROM `anag_game` WHERE 1
while ($row = $result->fetch_assoc()) {  

   echo "<u>".$row['ID']."<b>".$row['NAME']."</b></u>";
 }

?>
