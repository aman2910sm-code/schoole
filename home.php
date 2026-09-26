<?php
session_start();
if (isset($_SESSION['id']) && isset($_SESSION['role'])) {
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home -  Raino School</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="style.css">
    <link rel="icon" href="logo1.png">
</head>
<body class="main-container">
    <div class="d-flex justify-content-center
    align-items-center vh-100">
    <div class="profile-card p-3 text-center">
        <small>Role:
            <b> 
                <?php
                if ($_SESSION['role'] == 'Admin') {
                   echo "Admin"; 
                }else if ($_SESSION['role'] == 'Teacher'){
                  echo "Teacher";
                }else{
                  echo "Student";
                }
                ?>
            </b><br>
            <h3 class="display-4"> <?=$_SESSION['fname']?> </h3>
            <a href="logout.php" class="btn btn-warning">
            Logout
            </a>
        </small>
</div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
<?php }else{
    header("Location: login.php");
    exit;
} ?>