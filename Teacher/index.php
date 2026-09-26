<?php
session_start();
if (isset($_SESSION['teacher_id']) && isset($_SESSION['role'])) {
        if($_SESSION['role']  == 'Teacher'){
        include "../DB_connection.php";
        include "data/teacher.php";
        include "data/subject.php";
        include "data/grade.php";
        include "data/section.php";

        $teacher_id = $_SESSION['teacher_id'];
        $teacher    = getTeacherById($teacher_id, $conn);

        if ($teacher == 0) {
            header("Location: ../login.php");
            exit;
        }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teacher -  Home</title>
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
            padding: 0.6rem 1rem;
            border-top: 1px solid #E6E9F0;
        }
    </style>

</head>
<body>
    <?php
    include "inc/navbar.php";
    ?>

    <div class="container mt-5">
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
                <div class="detail-row">Employee number: <?= $teacher['employee_number'] ?? '' ?></div>
                <div class="detail-row">Address: <?= $teacher['address'] ?? '' ?></div>
                <div class="detail-row">Email address: <?= $teacher['email_address'] ?? '' ?></div>
                <div class="detail-row">Date of birth: <?= $teacher['date_of_birth'] ?? '' ?></div>
                <div class="detail-row">Phone number: <?= $teacher['phone_number'] ?? '' ?></div>
                <div class="detail-row">Qualification: <?= $teacher['qualification'] ?? '' ?></div>
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
                        echo rtrim($s, ', ');
                    ?>
                </div>
                <div class="detail-row">
                    Class:
                    <?php
                        $grade_ids   = !empty($teacher['class'])   ? array_values(array_filter(array_map('trim', explode(',', trim($teacher['class'], ','))))) : [];
                        $section_ids = !empty($teacher['section']) ? array_values(array_filter(array_map('trim', explode(',', trim($teacher['section'], ','))))) : [];

                        $labels = [];
                        $count = max(count($grade_ids), count($section_ids));

                        for ($i = 0; $i < $count; $i++) {
                            $gradeLabel   = '';
                            $sectionLabel = '';

                            if (isset($grade_ids[$i])) {
                                $g_temp = getGradeById($grade_ids[$i], $conn);
                                if ($g_temp != 0) {
                                    $gradeLabel = $g_temp['grade_code'] . '-' . $g_temp['grade'];
                                }
                            }

                            if (isset($section_ids[$i])) {
                                $sec_temp = getSectionById($section_ids[$i], $conn);
                                if ($sec_temp != 0) {
                                    $sectionLabel = $sec_temp['section'];
                                }
                            }

                            $combined = trim($gradeLabel . ' - ' . $sectionLabel, " -");
                            if ($combined !== '') {
                                $labels[] = $combined;
                            }
                        }

                        echo htmlspecialchars(implode(', ', $labels), ENT_QUOTES, 'UTF-8');
                    ?>
                </div>

                
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
     <script>
        $(document).ready(function(){
               $("#navlinks li:nth-child(1) a").addClass('active');
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