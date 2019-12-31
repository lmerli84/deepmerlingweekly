<?php
function db_connect() {
    static $connection;
    if(!isset($connection)) {
        $config = parse_ini_file('./secure/config.ini'); 
        $connection = mysqli_connect($config['servername'],$config['username'],$config['password'],$config['dbname']);
    }
    if($connection === false) {
        return mysqli_connect_error(); 
    }
    return $connection;
}
$connection = db_connect();
if ($connection->connect_error) {
    die("Connection failed: " . $connection->connect_error);
}

$sql = "SELECT * FROM anag_game";
$result = $connection->query($sql);
if (!$result)
    die("Database access failed: " . mysqli_error());
//echo $sql;
//echo "<p> </p>";
//echo mysqli_num_rows($result)

//SELECT `ID`, `NAME`, `OWNER`, `DESCR`, `RULES`, `RATING` FROM `anag_game` WHERE 1
include "header.php"
?>

<div class="container">
    <h2 class="header center yellow-text text-darken-2">Boardgames</h2>
        <div class="row center" id="issue_container">
            <div class="row center">
                <table>
                    <thead>
                        <tr>
                            <th>Titolo</th>
                            <th>Descrizione</th>
                            <th>Regolamento</th>
                            <th>Proprietario</th>
                        </tr>
                    </thead>
                    <tbody>   
<?php
while ($row = $result->fetch_assoc()) {  
///SELECT `ID`, `NAME`, `OWNER`, `DESCR`, `RULES`, `RATING` FROM `anag_game` WHERE 1
echo "<tr>";
echo "<td>".$row['NAME']."</td><td>".$row['DESCR']."</td><td>".$row['RULES']."</td><td>".$row['OWNER']."</td>";
echo "</tr>";
}
?>
                    </tbody>
                </table>
</div>
