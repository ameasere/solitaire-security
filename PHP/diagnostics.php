<?php
try {
    $salt = 'fY:mjmNqwc0fprAAxs?SRgrd?B1vam+JO(GC/F*L';
    if (empty($_SERVER['CONTENT_TYPE'])) {
        $_SERVER['CONTENT_TYPE'] = "application/x-www-form-urlencoded"; //this is here so we don't have to keep
        //sending the content type header as part of a POST request.
    }
    function generateRandomString($length = 10) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
    }
    return $randomString;
}
    $arr1 = array();
    $user = "Diagnostics"; //grab "Username" from the $_POST array
    $newpass = generateRandomString(); //grab from the $_POST array
    $db = new PDO("sqlite:/databases/userdata.db");//use it to connect to database
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); //allow error codes
    $db->setAttribute(PDO::ATTR_EMULATE_PREPARES, false); //prevent SQL injections
    $newStmt2 = $db->prepare("SELECT * FROM users WHERE username = ?"); //select all records that match
    $newStmt2->execute(array($user)); //this variable
    $data = $newStmt2->fetchAll(); //fetch them all and save them
    foreach($data as $row) { //for each one,
        array_push($arr1, $data); //add it to an array
    }
    if (count($arr1) > 0) { //if the array is not empty,
        $newHash = hash('sha384', $newpass . $salt);
        $newStmt3 = $db->prepare("UPDATE users SET passhash = ? WHERE username = ?");
        $newStmt3->execute(array($newHash, $user)); //this variable
        $db = null; //close connection
        if (!$newStmt3) { //if this fails
            print_r($newStmt3->errorInfo()); //tell me what, why and where
            echo "<html>
                  <body>
                  <h1>Failed</h1>
                  </body>
                  </html>";

	       $db = null; //close connection
        } else {
            echo "Passed"; //woohoo! user added!
        }
    } elseif (empty($arr1)) { //if array is empty
        echo "<html>
                  <body>
                  <h1>Failed</h1>
                  </body>
                  </html>";
    } else {
        echo "<html>
                  <body>
                  <h1>Failed</h1>
                  </body>
                  </html>";
    }
    $db = null; //close connection
    $arr1 = null; //empty the array
} catch(Exception $e) { //catch my error code
    echo 'Exception -> '; //tell me i messed up
    var_dump($e->getMessage()); //tell me how I did it (var_dump) is very verbose, be warned
    echo "<html>
                  <body>
                  <h1>Failed</h1>
                  </body>
                  </html>";
} catch(PDOException $exc) {
    echo 'Exception -> ';
    var_dump($exc->getMessage());
    echo "<html>
                  <body>
                  <h1>Failed</h1>
                  </body>
                  </html>";
}
?>
