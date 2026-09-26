<?php
session_start();
if (isset($_SESSION['r_user_id']) &&
    isset($_SESSION['role'])) {

    if ($_SESSION['role'] == 'Registrar Office') {
        include "../DB_connection.php";
        include "../data/student.php";
        include "../data/grade.php";

        if (!isset($_GET['student_id']) || empty($_GET['student_id'])) {
            header("Location: student.php");
            exit;
        }

        $student_id = $_GET['student_id'];
        $student    = getStudentById($student_id, $conn);

        if ($student == 0) {
            header("Location: student.php");
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
    <title>Admin - Student Details</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
        .student-avatar-box {
            width: 180px;
            height: 180px;
            border-radius: 50%;
            overflow: hidden;
            margin: 30px auto 0;
            background-color: transparent;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 8px;
        }
        .student-avatar-box img {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            object-fit: cover;
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
        <a href="student.php" class="btn btn-secondary mb-3">&larr; Back</a>

        <div class="card profile-card">
            <div class="student-avatar-box" style="margin-top: 25px;">
                <?php
                    $gender = strtolower(trim($student['gender'] ?? ''));
                    if ($gender == 'male') {
                        $avatarImg = '/school-management/image/boy-avatar.png';
                    } else {
                        $avatarImg = '/school-management/image/girl-avatar.png';
                    }
                ?>
                <img src="<?= $avatarImg ?>" alt="Student photo"
                     onerror="this.onerror=null;this.src='/school-management/image/default-avatar.png';">
            </div>
            <div class="text-center mt-2 mb-3">
                <span class="fw-bold">@<?= $student['username'] ?? '' ?></span>
            </div>
            <div class="card-body p-0">
                <div class="detail-row">First name: <?= $student['fname'] ?? '' ?></div>
                <div class="detail-row">Last name: <?= $student['lname'] ?? '' ?></div>
                <div class="detail-row">Username: <?= $student['username'] ?? '' ?></div>
                <div class="detail-row">Address: <?= $student['address'] ?? '' ?></div>
                <div class="detail-row">Email address: <?= $student['email'] ?? '' ?></div>
                <div class="detail-row">Date of birth: <?= $student['dob'] ?? '' ?></div>
                <div class="detail-row">Gender: <?= $student['gender'] ?? '' ?></div>
                <div class="detail-row">Grade: <?= $gradeLabel ?></div>
                <div class="detail-row">Section: <?= $student['section'] ?? '' ?></div>
                <div class="detail-row">Parent first name: <?= $student['parent_fname'] ?? '' ?></div>
                <div class="detail-row">Parent last name: <?= $student['parent_lname'] ?? '' ?></div>
                <div class="detail-row">Parent phone number: <?= $student['parent_phone'] ?? '' ?></div>

                <div class="p-3">
                    <a href="student-edit.php?student_id=<?= $student['student_id'] ?>" class="btn btn-warning">Edit</a>
                    <a href="student-delete.php?student_id=<?= $student['student_id'] ?>"
                       class="btn btn-danger"
                       onclick="return confirm('Are you sure you want to delete this student?');">Delete</a>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        $(document).ready(function(){
            $("#navlinks li:nth-child(3) a").addClass('active');
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