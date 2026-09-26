<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {

    if ($_SESSION['role'] == 'Admin') {
        include "../DB_connection.php";
        include "../data/grade.php";

        $grades = getALLGrades($conn);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Grade</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
    <?php include "../inc/navbar.php"; ?>

    <?php if (!empty($grades)) { ?>
    <div class="container mt-5">
        <a href="grade-add.php" class="btn btn-dark">Add New Grade</a>

        <?php if (isset($_GET['error'])) { ?>
        <div class="alert alert-danger mt-3" role="alert">
            <?= htmlspecialchars($_GET['error']) ?>
        </div>
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

        <div class="table-responsiv">
            <table class="table table-bordered mt-3 n-table">
                <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Grade</th>
                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <?php $i = 1; foreach ($grades as $row) {
                        $gid = $row['grade_id'] ?? '';
                        $label = $row['grade'] ?? '';
                    ?>
                    <tr>
                        <th scope="row"><?= $i++ ?></th>
                        <td><?= htmlspecialchars($label) ?></td>
                        <td>
                            <a href="grade-edit.php?grade_id=<?= $gid ?>" class="btn btn-warning">Edit</a>
                            <a href="grade-delete.php?grade_id=<?= $gid ?>"
                               class="btn btn-danger"
                               onclick="return confirm('Are you sure you want to delete this grade?');">Delete</a>
                        </td>
                    </tr>
                    <?php } ?>
                </tbody>
            </table>
        </div>
    </div>
    <?php } else { ?>
        <div class="container mt-5">
            <a href="grade-add.php" class="btn btn-dark mb-3">Add New Grade</a>
            <?php if (isset($_GET['error'])) { ?>
            <div class="alert alert-danger" role="alert">
                <?= htmlspecialchars($_GET['error']) ?>
            </div>
            <?php } ?>
            <div class="alert alert-info" role="alert">Empty!</div>
        </div>
    <?php } ?>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        $(document).ready(function(){
            $("#navlinks li:nth-child(4) a").addClass('active');
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