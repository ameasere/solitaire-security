<?php
echo '<!DOCTYPE html>
<html>
<title>Solitaire Security</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<style>
    #submit {
    background-color: #ccc;
    -moz-border-radius: 5px;
    -webkit-border-radius: 5px;
    border-radius:6px;
    color: #fff;
    font-family: "Oswald";
    font-size: 20px;
    text-decoration: none;
    cursor: pointer;
    border:none;
}



#submit:hover {
    border: none;
    background:red;
    box-shadow: 0px 0px 1px #777;
}
#submit2 {
    background-color: #ccc;
    -moz-border-radius: 5px;
    -webkit-border-radius: 5px;
    border-radius:6px;
    color: #fff;
    font-family: "Oswald";
    font-size: 20px;
    text-decoration: none;
    cursor: pointer;
    border:none;
    transform: translate(115%, -97%);
}



#submit2:hover {
    border: none;
    background:red;
    box-shadow: 0px 0px 1px #777;
}
.g-recaptcha {
transform: translate(0%, 0%);
}
</style>
<head>
<script src="https://www.google.com/recaptcha/api.js"></script>
<script>
function validateRecaptcha() {
    var response = grecaptcha.getResponse();
    if (response.length === 0) {
        alert("reCAPTCHA incomplete.");
        return false;
    } else {
        document.getElementById("login").submit();
        return true;
    }
}
</script>
</head>
<body>
<!-- Navbar (sit on top) -->
<div class="w3-top">
  <div class="w3-bar w3-white w3-wide w3-padding w3-card">
    <a href="https://solitairesec.000webhostapp.com" class="w3-bar-item w3-button">Home</a>
  </div>
</div>

<!-- Header -->
<header class="w3-display-container w3-content w3-wide" style="max-width:1500px;" id="home">
  <img class="w3-image" src="/images/cover.png" alt="Software" width="1500" height="800">
  <div class="w3-display-middle w3-margin-top w3-center">
  </div>
</header>

<!-- Page content -->
<div class="w3-content w3-padding" style="max-width:1564px">
<h1 class="w3-xxlarge w3-text-white"><span class="w3-padding w3-black w3-opacity-min"><b>Change password</b></span></h1> 
  <!-- Contact Section -->
  <div class="w3-container w3-padding-32" id="contact">
    <h3 class="w3-border-bottom w3-border-light-grey w3-padding-16">Change password</h3>
    <p><i>Contact us if you need decryption keys for data you cannot retrieve, deleting your account or any other issues.</i></p>
    <form name="frmChange" method="post" action="chngPw.php" onSubmit="">
<div style="width:500px;">
<table border="0" cellpadding="10" cellspacing="0" width="500" align="center" class="tblSaveForm">
<tr class="tableheader">
</tr>
<tr>
<td width="40%"><label>Username</label></td>
<td width="60%"><input type="Username" name="Username" class="txtField"/><span id="currentPassword"  class="required"></span></td>
</tr>
<tr>
<td width="40%"><label>Current Password</label></td>
<td width="60%"><input type="password" name="Password" class="txtField"/><span id="currentPassword"  class="required"></span></td>
</tr>
<tr>
<td><label>New Password</label></td>
<td><input type="password" name="newPassword" class="txtField"/><span id="newPassword" class="required"></span></td>
</tr>
<td><label>Confirm Password</label></td>
<td><input type="password" name="confirmPassword" class="txtField"/><span id="confirmPassword" class="required"></span></td>
</tr>
<tr>
<td colspan="2"><input type="submit" name="submit" value="Submit" class="btnSubmit" onclick="return validateRecaptcha();"></td>
</tr>
</table>
</div>
 <div class="g-recaptcha" data-sitekey="6LeSy-MZAAAAAFxuK33bGyqPpFAz3zDp-YpjOm-x"></div>
</div>
<div class="footer">
    <p>Our use of reCAPTCHA v3 is subject to the Google Privacy Policy and Terms of Use. reCAPTCHA may only be used to fight spam and <br>abuse on your site. reCAPTCHA must not be used for any other<br> purposes such as determining credit worthiness,<br> employment eligibility, financial status, or insurability of a user.<br> More info:</p>
    <a href="https://www.termsfeed.com/blog/privacy-policy-recaptcha/">reCAPTCHA Privacy Policy</a>
</div>
</div>
</form>
</body></html>
';
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
    $arr1 = array();
    $user = $_POST['Username']; //grab "Username" from the $_POST array
    $pass = $_POST['Password']; //grab  from the $_POST array
    $newpass = $_POST['newPassword']; //grab from the $_POST array
    $newpassconfirm = $_POST['confirmPassword']; //grab from the $_POST array
    if (empty($newpass) || empty($newpassconfirm) || empty($pass) || empty($user)) {
        die();
    } elseif (!(isset($newpass)) || !(isset($pass)) || !(isset($newpass)) || !(isset($newpassconfirm))) {
        die();
    } elseif ($newpass !== $newpassconfirm) {
        echo "Passwords do not match. Try again.";
        die();
    } else {
    }
    $passHash = hash('sha384', $pass . $salt);
    $db = new PDO("sqlite:/databases/userdata.db");//use it to connect to database
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); //allow error codes
    $db->setAttribute(PDO::ATTR_EMULATE_PREPARES, false); //prevent SQL injections
    $newStmt2 = $db->prepare("SELECT * FROM users WHERE username = ? && passhash = ?"); //select all records that match
    $newStmt2->execute(array($user, $passHash)); //this variable
    $data = $newStmt2->fetchAll(); //fetch them all and save them
    foreach($data as $row) { //for each one,
        array_push($arr1, $data); //add it to an array
    }
    if (count($arr1) > 0) { //if the array is not empty,
        $newHash = hash('sha384', $newpass . $salt);
        $newStmt3 = $db->prepare("UPDATE users SET passhash = ? WHERE username = ? and passhash = ?");
        $newStmt3->execute(array($newHash, $user, $passHash)); //this variable
        $db = null; //close connection
        if (!$newStmt3) { //if this fails
            print_r($newStmt3->errorInfo()); //tell me what, why and where

	       $db = null; //close connection
        } else {
            echo "Success!"; //woohoo! user added!
        }
    } elseif (empty($arr1)) { //if array is empty
        echo "Sorry, incorrect username or password. Try again.";
    } else {
    }
    $db = null; //close connection
    $arr1 = null; //empty the array
} catch(Exception $e) { //catch my error code
    echo 'Exception -> '; //tell me i messed up
    var_dump($e->getMessage()); //tell me how I did it (var_dump) is very verbose, be warned
} catch(PDOException $exc) {
    echo 'Exception -> ';
    var_dump($exc->getMessage());
}
?>
