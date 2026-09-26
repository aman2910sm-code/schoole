<?php
session_start();
if (isset($_SESSION['student_id']) && isset($_SESSION['role'])) {
        if($_SESSION['role']  == 'Student'){
        include "../DB_connection.php";
        include "data/student.php";

        $student_id = $_SESSION['student_id'];
        $student    = getStudentById($student_id, $conn);

        if ($student == 0) {
            header("Location: ../login.php");
            exit;
        }

        // ---------------------------------------------------------------
        // PLACEHOLDER DATA - replace this with a real query once you
        // have a table that stores each student's course results
        // (course code, title, marks per component, total, grade,
        // semester, year). Group the rows by "Year X - Semester Y".
        // ---------------------------------------------------------------
        $gradeSummary = [
            'Year 2025 - Semester I' => [
                ['code' => 'Ph01', 'title' => 'Physics', 'grade' => 'B+', 'marks' => ['10/10', '20/20', '15/30', '40/40'], 'total' => 85],
                ['code' => 'Ph01', 'title' => 'Physics', 'grade' => 'B+', 'marks' => ['10/10', '20/20', '15/30', '40/40'], 'total' => 85],
                ['code' => 'Ph01', 'title' => 'Physics', 'grade' => 'B+', 'marks' => ['10/10', '20/20', '15/30', '40/40'], 'total' => 85],
            ],
            'Year 2025 - Semester II' => [
                ['code' => 'Ph01', 'title' => 'Physics', 'grade' => 'B+', 'marks' => ['10/10', '20/20', '15/30', '40/40'], 'total' => 85],
                ['code' => 'Ph01', 'title' => 'Physics', 'grade' => 'B+', 'marks' => ['10/10', '20/20', '15/30', '40/40'], 'total' => 85],
                ['code' => 'Ph01', 'title' => 'Physics', 'grade' => 'B+', 'marks' => ['10/10', '20/20', '15/30', '40/40'], 'total' => 85],
            ],
        ];
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student -  Grade Summary</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
        body {
            background: #F5F6FA;
        }
        .grade-table {
            background: #fff;
            border-radius: 8px;
            overflow: hidden;
        }
        .grade-table thead th {
            background: #fff;
            border-bottom: 2px solid #dee2e6;
        }
        .semester-heading {
            font-weight: 600;
            margin-top: 2.5rem;
            margin-bottom: 1rem;
            text-align: center;
        }
        .marks-cell span {
            display: inline-block;
            margin-right: 6px;
        }
    </style>

</head>
<body>
    <?php
    include "inc/navbar.php";
    ?>

    <div class="container mt-4">
        <?php foreach ($gradeSummary as $heading => $rows) { ?>
            <h5 class="semester-heading"><?= htmlspecialchars($heading) ?></h5>
            <table class="table grade-table align-middle">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Course Code</th>
                        <th>Course Title</th>
                        <th>Grade</th>
                        <th>Results</th>
                        <th>Total</th>
                    </tr>
                </thead>
                <tbody>
                    <?php $i = 1; foreach ($rows as $row) { ?>
                        <tr>
                            <td><?= $i++ ?></td>
                            <td><?= htmlspecialchars($row['code']) ?></td>
                            <td><?= htmlspecialchars($row['title']) ?></td>
                            <td><?= htmlspecialchars($row['grade']) ?></td>
                            <td class="marks-cell">
                                <?php foreach ($row['marks'] as $m) { ?>
                                    <span><?= htmlspecialchars($m) ?></span>
                                <?php } ?>
                            </td>
                            <td><?= htmlspecialchars($row['total']) ?></td>
                        </tr>
                    <?php } ?>
                </tbody>
            </table>
        <?php } ?>
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

    }else{
        header("Location: ../login.php");
        exit;
    }
}else{
    header("Location: ../login.php");
    exit;
}

?>