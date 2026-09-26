<?php
session_start();
if (isset($_SESSION['admin_id']) && 
    isset($_SESSION['role'])) {

    if ($_SESSION['role'] == 'Admin') {
        include "../DB_connection.php";
        include "../data/teacher.php";
        include "../data/subject.php";
        include "../data/grade.php";
        include "../data/class.php";

        $teacher     = getALLTeacher($conn);
        $allSubjects = getALLSubjects($conn);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Teachers</title>
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
        <a href="index.php" class="btn btn-dark">Go Back</a>
        <form action ="teacher-search.php" class="mt-3 n-table" method="post">
            <div class="input-group mb-3">
                <input type="text" class="form-control" name="searchKey" placeholder="search...">
                <button class="btn btn-primary">
                    <i class="fa fa-search" aria-hidden="true"></i>
                </button>
            </div>
        </form>

        <?php if (isset($_GET['error'])) { ?>
        <div class="alert alert-danger mt-3" role="alert"><?= htmlspecialchars($_GET['error']) ?></div>
        <?php } ?>
        <?php if (isset($_GET['deleted'])) { ?>
        <div class="alert alert-info mt-3" role="alert">Successfully deleted!</div>
        <?php } ?>
        <?php if (isset($_GET['added'])) { ?>
        <div class="alert alert-info mt-3" role="alert">Successfully added!</div>
        <?php } ?>
        <?php if (isset($_GET['updated'])) { ?>
        <div class="alert alert-info mt-3" role="alert">Successfully updated!</div>
        <?php } ?>
        
        <div class="table-responsive">
            <table class="table table-bordered mt-3 n-table">
                <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Id</th>
                        <th scope="col">First Name</th>
                        <th scope="col">Last Name</th>
                        <th scope="col">Username</th>
                        <th scope="col">Subject</th>
                        <th scope="col">Class</th>
                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <?php $i = 1; foreach ($teacher as $row) { ?>
                    <tr>
                        <th scope="row"><?= $i++ ?></th>
                        <td><?= $row['teacher_id'] ?? '' ?></td>
                        <td><a href="teacher-view.php?teacher_id=<?= $row['teacher_id'] ?>"><?= $row['fname'] ?? '' ?></a></td>
                        <td><?= $row['lname'] ?? '' ?></td>
                        <td><?= $row['username'] ?? '' ?></td>
                        <td>
                           <?php
                             $s = '';
                             if (!empty($row['subjets'])) {
                                 $subjects = array_filter(
                                     array_map('trim', explode(',', trim($row['subjets'], ',')))
                                 );
                                 foreach ($subjects as $subject) {
                                    $s_temp = getSubjectsById($subject, $conn);
                                    if ($s_temp != 0) {
                                        $s .= $s_temp['subject_code'] . ', ';
                                    }
                                 }
                             }
                             echo rtrim($s, ', ');
                           ?>
                        </td>
                        <td>
                            <?php
                            //echo "G". implode(", ", str_split($row['class']));
                             /*$c = '';
                             if (!empty($row['class'])) {
                                 $classes = array_filter(
                                     array_map('trim', explode(',', trim($row['class'], ',')))
                                 );
                                 foreach ($classes as $class_id) {
                                     // 1. First get row from class table
                                     $class_info = getClassById($class_id, $conn);
                                     
                                     if ($class_info != 0 && isset($class_info['grade'])) {
                                         // 2. Get grade details from grades table using grade_id
                                         $grade_info = getGradeById($class_info['grade'], $conn);
                                         
                                         if ($grade_info != 0) {
                                             $code = $grade_info['grade_code'] ?? '';
                                             $num  = $grade_info['grade'] ?? '';
                                             $c .= $code . '-' . $num . ', ';
                                         } else {
                                             $c .= 'G-' . $class_info['grade'] . ', ';
                                         }
                                     } else {
                                         // Fallback if class row not found
                                         $g_fallback = getGradeById($class_id, $conn);
                                         if ($g_fallback != 0) {
                                             $c .= ($g_fallback['grade_code'] ?? '') . '-' . ($g_fallback['grade'] ?? '') . ', ';
                                         } else {
                                             $c .= 'G-' . $class_id . ', ';
                                         }
                                     }
                                 }
                             }
                             echo rtrim($c, ', ');*/
                             $c = '';
if (!empty($row['class'])) {
    // Split only by commas (no digit splitting)
    $classes = array_filter(
        array_map('trim', explode(',', trim($row['class'], ',')))
    );

    foreach ($classes as $class_id) {
        $class_info = getClassById($class_id, $conn);

        if ($class_info != 0 && isset($class_info['gradeId'])) {
            // Found class row → get grade by gradeId
            $grade_info = getGradeById($class_info['gradeId'], $conn);

            if ($grade_info != 0) {
                $code = $grade_info['grade_code'] ?? 'G';
                $num  = $grade_info['grade'] ?? $class_info['gradeId'];
                $c .= $code . $num . ', ';
            } else {
                $c .= 'G' . $class_info['gradeId'] . ', ';
            }
        } else {
            // Fallback: treat class_id itself as gradeId
            $g_fallback = getGradeById($class_id, $conn);
            if ($g_fallback != 0) {
                $c .= ($g_fallback['grade_code'] ?? 'G') . ($g_fallback['grade'] ?? $class_id) . ', ';
            } else {
                $c .= 'G' . $class_id . ', ';
            }
        }
    }
}
echo rtrim($c, ', ');


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
        <div class="container mt-5">
            <a href="teacher-add.php" class="btn btn-dark">Add New Teacher</a>
            <a href="index.php" class="btn btn-dark">Go Back</a>
            <?php if (isset($_GET['error'])) { ?>
            <div class="alert alert-danger mt-3" role="alert"><?= htmlspecialchars($_GET['error']) ?></div>
            <?php } ?>
            <div class="alert alert-info mt-3" role="alert">No teachers found!</div>
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
        header("Location: ../login.php");
        exit;
    }
} else {
    header("Location: ../login.php");
    exit;
}
?>