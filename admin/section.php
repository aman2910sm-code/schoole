<?php
session_start();
if (isset($_SESSION['admin_id']) &&
    isset($_SESSION['role'])) {

    if ($_SESSION['role'] == 'Admin') {
        include "../DB_connection.php";
        include "../data/section.php";

        $sections = getALLSections($conn);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Section</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
    <?php include "../inc/navbar.php"; ?>

    <?php if (!empty($sections)) { ?>
    <div class="container mt-5">
        <a href="section-add.php" class="btn btn-dark">Add New Section</a>

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
                        <th scope="col">Section</th>
                        <th scope="col"></th>
                    </tr>
                </thead>
                <tbody>
                    <?php $i = 1; foreach ($sections as $row) {
                        $sid = $row['section_id'] ?? '';
                        $label = $row['section'] ?? '';
                    ?>
                    <tr>
                        <th scope="row"><?= $i++ ?></th>
                        <td><?= htmlspecialchars($label) ?></td>
                        <td>
                            <a href="section-edit.php?section_id=<?= $sid ?>" class="btn btn-warning">Edit</a>
                            <a href="section-delete.php?section_id=<?= $sid ?>"
                               class="btn btn-danger"
                               onclick="return confirm('Are you sure you want to delete this section?');">Delete</a>
                        </td>
                    </tr>
                    <?php } ?>
                </tbody>
            </table>
        </div>
    </div>
    <?php } else { ?>
        <div class="container mt-5">
            <a href="section-add.php" class="btn btn-dark mb-3">Add New Section</a>
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
            $("#navlinks li:nth-child(5) a").addClass('active');
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