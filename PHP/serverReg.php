<?php
try {
    $servername = "localhost";
    $username = "id15413506_enigmapr0ject";
    $password = "Mewgia2003!!";
    $database = "id15413506_userdata";
    $salt = 'fY:mjmNqwc0fprAAxs?SRgrd?B1vam+JO(GC/F*L';
    if (empty($_SERVER['CONTENT_TYPE'])) {
        $_SERVER['CONTENT_TYPE'] = "application/x-www-form-urlencoded"; //this is here so we don't have to keep
        //sending the content type header as part of a POST request.
    }
    $digits = 32;
    $returnString = mt_rand(1, 9);
    while (strlen($returnString) < $digits) {
        $returnString .= mt_rand(0, 9);
    }
    $returnIV = mt_rand(1,9);
    while (strlen($returnIV) < 16) {
        $returnIV .= mt_rand(0, 9);
    }
    $arr1 = array();
    $user = $_POST['Username']; //grab "Username" from the $_POST array
    $pass = $_POST['Password']; //grab "passHash" from the $_POST array
    $passHash = hash('sha384', $pass . $salt);
    $db = new PDO("sqlite:/databases/userdata.db");//use it to connect to database
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); //allow error codes
    $db->setAttribute(PDO::ATTR_EMULATE_PREPARES, false); //prevent SQL injections
    $db->exec("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT, passhash TEXT, gcmkey TEXT, gcmiv TEXT)");
    //above statement makes table if it doesn't exist. This saves commenting it out after every test and
    //prevents error codes every single time. Very convenient.
    if (strlen($user) === 0 || strlen($passHash) === 0) { //if the POST vars are empty
        echo "Failed to enter data. Please try again"; //tell you that you messed up somewhere
        $db = null;
    } else { //otherwise...
        $newStmt2 = $db->prepare("SELECT username FROM users WHERE username = ?"); //select all records that match
        $newStmt2->execute(array($user)); //this variable
        $data = $newStmt2->fetchAll(); //fetch them all and save them
        foreach($data as $row) { //for each one,
            array_push($arr1, $data); //add it to an array
        }
        if (count($arr1) > 0) { //if the array is not empty,
            echo "Error 100: Username taken"; //tell the user the user is taken
            $arr1 = null; //empty the array
            $db = null; //close connection
        } else { //if array is empty
            $newStmt = $db->prepare("INSERT INTO users(username, passhash, gcmkey, gcmiv) VALUES(?, ?, ?, ?)"); //prepare for insertion
            $pol = $newStmt->execute([$user, $passHash, $returnString, $returnIV]); //insert POST vars to the table in their respective columns
            if (!$pol) { //if this fails
                print_r($pol->errorInfo()); //tell me what, why and where

	            $db = null; //close connection
        } else {
                echo "Success!"; //woohoo! user added!
            }
            $db = null; //close connection
        }
    }
} catch(Exception $e) { //catch my error code
    echo 'Exception -> '; //tell me i messed up
    var_dump($e->getMessage()); //tell me how I did it (var_dump) is very verbose, be warned
} catch(PDOException $exc) {
    echo 'Exception -> ';
    var_dump($exc->getMessage());
}
?>
