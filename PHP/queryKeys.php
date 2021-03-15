<?php
$servername = "localhost";
$username = "id15413506_enigmapr0ject";
$password = "Mewgia2003!!";
$database = "id15413506_userdata";
$salt = 'fY:mjmNqwc0fprAAxs?SRgrd?B1vam+JO(GC/F*L';
try {
    if (empty($_SERVER['CONTENT_TYPE'])) {
        $_SERVER['CONTENT_TYPE'] = "application/x-www-form-urlencoded"; //this is here so we don't have to keep
        //sending the content type header as part of a POST request.
    }
    $gcmdata = null;
    $user = $_POST['Username']; //grab "Username" from the $_POST array
    $pass = $_POST['Password']; //grab "passHash" from the $_POST array
    $passHash = hash('sha384', $pass . $salt);
    $db = new PDO("sqlite:/databases/userdata.db");//use it to connect to database
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); //allow error codes
    $db->setAttribute(PDO::ATTR_EMULATE_PREPARES, false); //prevent SQL injections
    $newStmt2 = $db->prepare("SELECT gcmkey,gcmiv FROM users WHERE username = ? AND passhash = ?"); //select all records that match
    $newStmt2->execute(array($user, $passHash)); //this variable
    $data = $newStmt2->fetchAll();
    if (!$newStmt2) { //if this fails
        print_r($data->errorInfo()); //tell me what, why and where
        $db = null; //close connection
    }
    foreach($data as $row) {//for each one,
        echo $data[0][0];
        echo "\n";
        echo $data[0][1];
    }
    $db = null; //close connection
} catch(Exception $e) { //catch my error code
    echo 'Exception -> '; //tell me i messed up
    var_dump($e->getMessage()); //tell me how I did it (var_dump) is very verbose, be warned
} catch(PDOException $exc) {
    echo 'Exception -> ';
    var_dump($exc->getMessage());
}
?>
