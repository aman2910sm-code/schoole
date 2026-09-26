<?php
session_start();
if (isset($_SESSION['admin_id']) &&
    isset($_SESSION['role'])) {

    if ($_SESSION['role'] == 'Admin') {
        include "../DB_connection.php";
        include "../data/registrar_office.php";

        if (!isset($_GET['r_user_id'])) {
            header("Location: registrar-Office.php");
            exit;
        }

        $r_user_id = $_GET['r_user_id'];
        $teacher   = getR_usersById($r_user_id, $conn);

        if ($teacher == 0) {
            header("Location: registrar-Office.php");
            exit;
        }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Registrar Office Details</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
        .teacher-avatar-box {
            width: 180px;
            height: 160px;
            margin: 30px auto 0;
            background-color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .teacher-avatar-box i {
            font-size: 150px;
            color: #000000;
        }
        .detail-row {
            padding: 10px 15px;
            border-bottom: 1px solid #e5e5e5;
        }
        .detail-row:last-child {
            border-bottom: none;
        }
        .profile-card {
            max-width: 380px;
            margin: 30px auto 0;
        }
    </style>
</head>
<body>
    <?php include "../inc/navbar.php"; ?>

    <div class="container mt-5">
        <a href="registrar-Office.php" class="btn btn-secondary mb-3">&larr; Back</a>

        <div class="card profile-card">
            <div class="teacher-avatar-box">
                <i class="fa fa-address-card-o" aria-hidden="true"></i>
            </div>
            <div class="text-center mt-2 mb-3">
                <span class="fw-bold">@<?= htmlspecialchars($teacher['username'] ?? '') ?></span>
            </div>
            <div class="card-body p-0">
                <div class="detail-row">First name: <?= htmlspecialchars($teacher['fname'] ?? '') ?></div>
                <div class="detail-row">Last name: <?= htmlspecialchars($teacher['lname'] ?? '') ?></div>
                <div class="detail-row">Username: <?= htmlspecialchars($teacher['username'] ?? '') ?></div>
                <div class="detail-row">Address: <?= htmlspecialchars($teacher['address'] ?? '') ?></div>
                <div class="detail-row">Employee number: <?= htmlspecialchars($teacher['employee_number'] ?? '') ?></div>
                <div class="detail-row">Date of birth: <?= htmlspecialchars($teacher['date_of_birth'] ?? '') ?></div>
                <div class="detail-row">Phone number: <?= htmlspecialchars($teacher['phone_number'] ?? '') ?></div>
                <div class="detail-row">Qualification: <?= htmlspecialchars($teacher['qualification'] ?? '') ?></div>
                <div class="detail-row">Email address: <?= htmlspecialchars($teacher['email_address'] ?? '') ?></div>
                <div class="detail-row">Gender: <?= htmlspecialchars($teacher['gender'] ?? '') ?></div>
                <div class="detail-row">Date of joined: <?= htmlspecialchars($teacher['date_of_joined'] ?? '') ?></div>
                <div class="p-3">
                    <a href="registrar-office-edit.php?r_user_id=<?= urlencode($teacher['r_user_id']) ?>" class="btn btn-warning">Edit</a>
                    <a href="registrar-office-delete.php?r_user_id=<?= urlencode($teacher['r_user_id']) ?>"
                       class="btn btn-danger"
                       onclick="return confirm('Are you sure you want to delete this user?');">Delete</a>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        $(document).ready(function(){
            $("#navlinks li:nth-child(7) a").addClass('active');
        });
    </script>
</body>
</html>
<?php
    } else {
        header("Location: ../login.php");
        exit;
    }
} else {
    header("Location: ../login.php");
    exit;
}
?>