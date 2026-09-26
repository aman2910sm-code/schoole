<?php
session_start();

if (!isset($_SESSION['admin_id']) || !isset($_SESSION['role']) || $_SESSION['role'] !== 'Admin') {
    header("Location: ../login.php");
    exit;
}

include "../DB_connection.php";
include "../data/class.php";

$classes = getALLClasses($conn);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Class</title>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<body>

<?php include "../inc/navbar.php"; ?>

<div class="container mt-5">

    <a href="class-add.php" class="btn btn-dark mb-3">Add New Class</a>

    <?php if (isset($_GET['error'])): ?>
        <div class="alert alert-danger"><?= htmlspecialchars($_GET['error']) ?></div>
    <?php endif; ?>

    <?php if (isset($_GET['deleted'])): ?>
        <div class="alert alert-info">Successfully deleted!</div>
    <?php endif; ?>

    <?php if (isset($_GET['added'])): ?>
        <div class="alert alert-info">Successfully added!</div>
    <?php endif; ?>

    <?php if (isset($_GET['updated'])): ?>
        <div class="alert alert-info">Successfully updated!</div>
    <?php endif; ?>

    <?php if ($classes !== 0 && !empty($classes)): ?>

        <div class="table-responsive">
            <table class="table table-bordered mt-3 n-table">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Class</th>
                        <th>Action</th>
                    </tr>
                </thead>

                <tbody>
                <?php $i = 1; ?>

                <?php foreach ($classes as $row): ?>

                    <?php
                        $cid = $row['class_id'] ?? '';

                        $gradeCode = $row['grade_code'] ?? '';
                        $gradeNum  = $row['grade_num'] ?? '';
                        $section   = $row['section_name'] ?? '';

                        $label = trim(
                            $gradeCode . '-' . $gradeNum . ' - ' . $section,
                            " -"
                        );
                    ?>

                    <tr>
                        <th><?= $i++ ?></th>

                        <td>
                            <?= htmlspecialchars($label, ENT_QUOTES, 'UTF-8') ?>
                        </td>

                        <td>
                            <a href="class-edit.php?class_id=<?= urlencode($cid) ?>"
                               class="btn btn-warning">
                                Edit
                            </a>

                            <a href="class-delete.php?class_id=<?= urlencode($cid) ?>"
                               class="btn btn-danger"
                               onclick="return confirm('Are you sure you want to delete this class?');">
                                Delete
                            </a>
                        </td>
                    </tr>

                <?php endforeach; ?>
                </tbody>
            </table>
        </div>

    <?php else: ?>

        <div class="alert alert-info">
            No classes found.
        </div>

    <?php endif; ?>

</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>

<script>
$(document).ready(function(){
    $("#navlinks li:nth-child(6) a").addClass("active");
});
</script>

</body>
</html>