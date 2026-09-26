<?php
session_start();
if (isset($_SESSION['admin_id']) &&
    isset($_SESSION['role'])) {

    if ($_SESSION['role'] == 'Admin') {
        include "../DB_connection.php";
        include "../data/teacher.php";
        include "../data/subject.php";
        include "../data/grade.php";
        include "../data/section.php";

        if (!isset($_GET['teacher_id'])) {
            header("Location: teacher.php");
            exit;
        }

        $teacher_id = $_GET['teacher_id'];
        $teacher    = getTeacherById($teacher_id, $conn);

        if ($teacher == 0) {
            header("Location: teacher.php");
            exit;
        }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Teacher Details</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
        .teacher-avatar-box {
            width: 180px;
            height: 180px;
            border-radius: 50%;
            overflow: hidden;
            margin: 30px auto 0;
            background-color: #17a2a2;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 8px;
        }
        .teacher-avatar-box img {
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
        <a href="teacher.php" class="btn btn-secondary mb-3">&larr; Back</a>

        <div class="card profile-card">
            <div class="teacher-avatar-box" style="margin-top: 25px;">
                <?php
                    $gender = strtolower(trim($teacher['gender'] ?? ''));
                    if ($gender == 'male') {
                        $avatarImg = '/school-management/image/png-clipart-computer-icons-male-woman-organization-flat-people-miscellaneous-face.png';
                    } else {
                        $avatarImg = '/school-management/image/Woman-with-Circle-Background-Graphics-26722128-1.png';
                    }
                ?>
                <img src="<?= $avatarImg ?>" alt="Teacher photo">
            </div>
            <div class="text-center mt-2 mb-3">
                <span class="fw-bold">@<?= $teacher['username'] ?? '' ?></span>
            </div>
            <div class="card-body p-0">
                <div class="detail-row">First name: <?= $teacher['fname'] ?? '' ?></div>
                <div class="detail-row">Last name: <?= $teacher['lname'] ?? '' ?></div>
                <div class="detail-row">Username: <?= $teacher['username'] ?? '' ?></div>
                <div class="detail-row">Address: <?= $teacher['address'] ?? '' ?></div>
                <div class="detail-row">Employee number: <?= $teacher['employee_number'] ?? '' ?></div>
                <div class="detail-row">Date of birth: <?= $teacher['date_of_birth'] ?? '' ?></div>
                <div class="detail-row">Phone number: <?= $teacher['phone_number'] ?? '' ?></div>
                <div class="detail-row">Qualification: <?= $teacher['qualification'] ?? '' ?></div>
                <div class="detail-row">Email address: <?= $teacher['email_address'] ?? '' ?></div>
                <div class="detail-row">Gender: <?= $teacher['gender'] ?? '' ?></div>
                <div class="detail-row">Date of joined: <?= $teacher['date_of_joined'] ?? '' ?></div>
                <div class="detail-row">
                    Subject:
                    <?php
                        $s = '';
                        if (!empty($teacher['subjets'])) {
                            $subjects = array_filter(array_map('trim', explode(',', trim($teacher['subjets'], ','))));
                            foreach ($subjects as $subject) {
                                $s_temp = getSubjectsById($subject, $conn);
                                if ($s_temp != 0) {
                                    $s .= $s_temp['subject_code'] . ', ';
                                }
                            }
                        }
                        echo $s;
                    ?>
                </div>
                <div class="detail-row">
                    Grade:
                    <?php
                        $g = '';
                        if (!empty($teacher['class'])) {
                            $grades = array_filter(array_map('trim', explode(',', trim($teacher['class'], ','))));
                            foreach ($grades as $grade_id) {
                                $g_temp = getGradeById($grade_id, $conn);
                                if ($g_temp != 0) {
                                    $g .= $g_temp['grade_code'] . '-' . $g_temp['grade'] . ', ';
                                }
                            }
                        }
                        echo $g;
                    ?>
                </div>
                <div class="detail-row">
                    Section:
                    <?php
                        $sec = '';
                        if (!empty($teacher['section'])) {
                            $sections = array_filter(array_map('trim', explode(',', trim($teacher['section'], ','))));
                            foreach ($sections as $section_id) {
                                $sec_temp = getSectionById($section_id, $conn);
                                if ($sec_temp != 0) {
                                    $sec .= $sec_temp['section'] . ', ';
                                }
                            }
                        }
                        echo $sec;
                    ?>
                </div>
                <div class="p-3">
                    <a href="teacher-edit.php?teacher_id=<?= $teacher['teacher_id'] ?>" class="btn btn-warning">Edit</a>
                    <a href="teacher-delete.php?teacher_id=<?= $teacher['teacher_id'] ?>"
                       class="btn btn-danger"
                       onclick="return confirm('Are you sure you want to delete this teacher?');">Delete</a>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        $(document).ready(function(){
            $("#navlinks li:nth-child(2) a").addClass('active');
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