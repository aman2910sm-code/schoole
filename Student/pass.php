<?php
session_start();
if (isset($_SESSION['student_id']) && isset($_SESSION['role'])) {
        if($_SESSION['role']  == 'Student'){
        include "../DB_connection.php";
        include "data/student.php";
        include "data/grade.php";

        $student_id = $_SESSION['student_id'];
        $student    = getStudentById($student_id, $conn);

        if ($student == 0) {
            header("Location: ../login.php");
            exit;
        }

        $gradeLabel = '';
        if (!empty($student['grade'])) {
            $g_temp = getGradeById($student['grade'], $conn);
            if ($g_temp != 0) {
                $gradeLabel = $g_temp['grade_code'] . '-' . $g_temp['grade'];
            }
        }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student -  Change Password</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
        body {
            background: #F5F6FA;
        }
        .profile-card {
            border-radius: 10px;
            max-width: 420px;
            margin: 0 auto;
        }
        .student-avatar-box {
            width: 220px;
            height: 220px;
            border-radius: 50%;
            background: #BEE3F8;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 25px auto 0;
        }
        .student-avatar-box img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .detail-row {
            padding: 0.6rem 1rem;
            border-top: 1px solid #E6E9F0;
        }
        .form-w {
            width: 100%;
            max-width: 420px;
            border-radius: 10px;
        }
    </style>

</head>
<body>
    <?php
    include "inc/navbar.php";
    ?>
<div class="d-flex justify-content-center"> <form method="post"
              class="shadow p-3 my-4 form-w"
              action="req/student-change.php">

            <input type="hidden" name="student_id" value="<?= $student['student_id'] ?>">

            <h3>Change Password</h3><hr>
            <?php if (isset($_GET['psuccess'])) { ?>
            <div class="alert alert-success" role="alert">
                <?= htmlspecialchars($_GET['psuccess']) ?>
            </div>
            <?php } ?>
            <?php if (isset($_GET['perror'])) { ?>
            <div class="alert alert-danger" role="alert">
                <?= htmlspecialchars($_GET['perror']) ?>
            </div>
            <?php } ?>
            <div class="mb-3">
                <div class="mb-3">
                <label class="form-label"> Old password</label>
                    <input type="password" class="form-control" name="admin_pass2" >

            </div>
                <label class="form-label"> new pasword</label>
                <div class="input-group mb-3">
                    <input type="text" class="form-control" name="new_pass" id="passInput">
                    <button class="btn btn-secondary" type="button" id="gBtn">Random</button>
                </div>
            </div>
            <div class="mb-3">
                <label class="form-label">Confirm new pasword</label>
                    <input type="text" class="form-control" name="c_new_pass2" id="passInput2">

            </div>
<button type="submit" class="btn btn-primary">Change</button>

        </form>
</div>
   

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
     <script>
        $(document).ready(function(){
               $("#navlinks li:nth-child(3) a").addClass('active');

               $("#gBtn").on('click', function(){
                    var chars = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789";
                    var randomPass = "";
                    for (var i = 0; i < 8; i++) {
                        randomPass += chars.charAt(Math.floor(Math.random() * chars.length));
                    }
                    $("#passInput").val(randomPass);
                    $("#passInput2").val(randomPass);
               });
        });
    </script>
</body>
</html>
<?php

    }else{
        header("Location: ../login.php");
        exit;
    }
}else{
    header("Location: ../login.php");
    exit;
}

?>