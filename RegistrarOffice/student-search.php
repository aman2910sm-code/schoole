<?php
session_start();
if (isset($_SESSION['r_user_id']) && 
    isset($_SESSION['role'])) {

    if ($_SESSION['role'] == 'Registrar Office') {
        include "../DB_connection.php";
        include "../data/student.php";
        include "../data/subject.php";
        include "../data/grade.php";

        $search_key = $_POST['searchKey'] ?? '';

        $student = getALLStudents($conn);

        if ($search_key !== '' && $student != 0) {
            $search_key_lower = strtolower($search_key);
            $student = array_filter($student, function ($row) use ($search_key_lower) {
                return strpos(strtolower($row['fname'] ?? ''), $search_key_lower) !== false
                    || strpos(strtolower($row['lname'] ?? ''), $search_key_lower) !== false
                    || strpos(strtolower($row['username'] ?? ''), $search_key_lower) !== false;
            });
        }

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registrar Office - Search Students</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
    <?php include "../inc/navbar.php"; ?>

    <?php if ($student != 0 && count($student) > 0) { ?>
    <div class="container mt-5">
        <a href="student-add.php" class="btn btn-dark">Add New Student</a>
        <a href="student.php" class="btn btn-dark">Go Back</a>
         <form action="student-search.php" class="mt-3 n-table" method="post">
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
                        <th scope="col">Grade</th>
                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <?php $i = 1; foreach ($student as $row) { ?>
                    <tr>
                        <th scope="row"><?= $i++ ?></th>
                        <td><?= $row['student_id'] ?? '' ?></td>
                        <td><?= $row['fname'] ?? '' ?></td>
                        <td><?= $row['lname'] ?? '' ?></td>
                        <td><?= $row['username'] ?? '' ?></td>
                        <td>
                            <?php
                             $g = '';
                             if (!empty($row['grade'])) {
                                $g_temp = getGradeById($row['grade'], $conn);
                                if ($g_temp != 0) {
                                    $g = $g_temp['grade_code'] . '-' . $g_temp['grade'];
                                }
                             }
                             echo $g;
                           ?>
                        </td>
                        <td>
                            <a href="student-edit.php?student_id=<?= $row['student_id'] ?>" class="btn btn-warning">Edit</a>
                            <a href="student-delete.php?student_id=<?= $row['student_id'] ?>"
                               class="btn btn-danger"
                               onclick="return confirm('Are you sure you want to delete this student?');">Delete</a>
                        </td>
                    </tr>
                    <?php } ?>
                </tbody>
            </table>
        </div>
    </div>
    <?php } else { ?>
<div class="alert alert-info" role="alert">Empty!    
    <a href="student.php"
        class="btn btn-dark">Go Back</a>
        </div>
    <?php } ?>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
   
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