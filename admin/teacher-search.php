    <?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

session_start();
if (isset($_SESSION['admin_id']) && 
    isset($_SESSION['role'])) {

    if ($_SESSION['role'] == 'Admin') {
        if (isset($_POST['searchKey'])){

        $search_key = $_POST['searchKey'];
        include "../DB_connection.php";
        include "../data/teacher.php";
        include "../data/subject.php";
        include "../data/grade.php";

        if (trim($search_key) === '') {
            $teacher = getALLTeacher($conn);
        } else {
            $teacher = searchTeacher($search_key, $conn);
        }
        $allSubjects = getALLSubjects($conn);


?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Search Teachers</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
    <?php include "../inc/navbar.php"; ?>

    <?php if ($teacher != 0) { ?>
    <div class="container mt-5">
        <a href="teacher-add.php" class="btn btn-dark">Add New Teacher</a>
        <form action="teacher-search.php" class="mt-3 n-table" method="post">
                <div class="input-group mb-3">
                    <input type="text"
                    class= "form-control"
                    name="searchKey"
                    value="<?= htmlspecialchars($search_key) ?>"
                    placeholder="search...">
                    <button class="btn btn-primary">
                        <i class="fa fa-search" 
                        aria-hidden="true"></i></button>
</div>
</form>

        <?php if (isset($_GET['deleted'])) { ?>
        <div class="alert alert-info mt-3" role="alert">Successfully deleted!</div>
        <?php } ?>
        <?php if (isset($_GET['added'])) { ?>
        <div class="alert alert-info mt-3" role="alert">Successfully added!</div>
        <?php } ?>
        <?php if (isset($_GET['updated'])) { ?>
        <div class="alert alert-info mt-3" role="alert">Successfully updated!</div>
        <?php } ?>
        <div class="table-responsiv">
            <table class="table table-bordered mt-3 n-table">
                <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Id</th>
                        <th scope="col">First Name</th>
                        <th scope="col">Last Name</th>
                        <th scope="col">Username</th>
                        <th scope="col">Subject</th>
                        <th scope="col">Grade</th>
                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <?php $i = 1; foreach ($teacher as $row) { ?>
                    <tr>
                        <th scope="row"><?= $i++ ?></th>
                        <td><?= $row['teacher_id'] ?? '' ?></td>
                        <td><?= $row['fname'] ?? '' ?></td>
                        <td><?= $row['lname'] ?? '' ?></td>
                        <td><?= $row['username'] ?? '' ?></td>
                        <td>
                           <?php
                             $s = '';
                             if (!empty($row['subjets'])) {
                                 $subjects = str_split(trim($row['subjets']));
                                 foreach ($subjects as $subject) {
                                    $s_temp = getSubjectsById($subject, $conn);
                                    if ($s_temp != 0) {
                                        $s .= $s_temp['subject_code'] . ', ';
                                    }
                                 }
                             }
                             echo $s;
                           ?>
                        </td>
                        <td>
                            <?php
                             $g = '';
                             if (!empty($row['gredes'])) {
                                 $grades = str_split(trim($row['gredes']));
                                 foreach ($grades as $grade_id) {
                                    $g_temp = getGradeById($grade_id, $conn);
                                    if ($g_temp != 0) {
                                        $g .= $g_temp['grade_code'] . '-' . $g_temp['grade'] . ', ';
                                    }
                                 }
                             }
                             echo $g;
                           ?>
                        </td>
                        <td>
                            <a href="teacher-edit.php?teacher_id=<?= $row['teacher_id'] ?>" class="btn btn-warning">Edit</a>
                            <a href="teacher-delete.php?teacher_id=<?= $row['teacher_id'] ?>"
                               class="btn btn-danger"
                               onclick="return confirm('Are you sure you want to delete this teacher?');">Delete</a>
                        </td>
                    </tr>
                    <?php } ?>
                </tbody>
            </table>
        </div>
    </div>
    <?php } else { ?>
        <div class="alert alert-info" role="alert">No Result Found!
        <a href="teacher.php"
        class="btn btn-dark">Go Back</a>
</div>
    <?php } ?>

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
        header("Location: teacher.php");
        exit;
    }
    } else {
        header("Location: ../login.php");
        exit;
    }
} else {
    header("Location: ../login.php");
    exit;
}
?>