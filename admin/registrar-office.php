<?php
session_start();
if (isset($_SESSION['admin_id']) && 
    isset($_SESSION['role'])) {

    if ($_SESSION['role'] == 'Admin') {
        include "../DB_connection.php";
        include "../data/registrar_office.php";
        

        $teacher     = getALLR_users($conn);
        $allSubjects = getALLSubjects($conn);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Registrar Office</title>
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
        <a href="registrar-office-add.php" target="_blank" rel="noopener noreferrer" class="btn btn-dark">Add New User</a>

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
                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <?php $i = 1; foreach ($teacher as $row) {
                        // Safely pull every field with a fallback, so a missing
                        // column NEVER prints a PHP warning inside the HTML.
                        $r_user_id  = $row['r_user_id'] ?? '';
                        $r_fname    = $row['fname'] ?? '';
                        $r_lname    = $row['lname'] ?? '';
                        $r_username = $row['username'] ?? '';
                    ?>
                    <tr>
                        <th scope="row"><?= $i ?></th>
                        <td><?= htmlspecialchars($r_user_id !== '' ? $r_user_id : $i) ?></td>
                        <td><a href="registrar_office_view.php?r_user_id=<?= urlencode($r_user_id) ?>"><?= htmlspecialchars($r_fname) ?></a></td>
                        <td><?= htmlspecialchars($r_lname) ?></td>
                        <td><?= htmlspecialchars($r_username) ?></td>
                        <td>
                            <a href="registrar-office-edit.php?r_user_id=<?= urlencode($r_user_id) ?>" class="btn btn-warning">Edit</a>
                            <a href="registrar-office-delete.php?r_user_id=<?= urlencode($r_user_id) ?>"
                               class="btn btn-danger"
                               onclick="return confirm('Are you sure you want to delete this teacher?');">Delete</a>
                        </td>
                    </tr>
                    <?php $i++; } ?>
                </tbody>
            </table>
        </div>
    </div>
    <?php } else { ?>
    <div class="container mt-5">
        <a href="registrar-office-add.php" target="_blank" rel="noopener noreferrer" class="btn btn-dark mb-3">Add New User</a>
        <?php if (isset($_GET['error'])) { ?>
        <div class="alert alert-danger" role="alert"><?= htmlspecialchars($_GET['error']) ?></div>
        <?php } ?>
        <div class="alert alert-info" role="alert">Empty!</div>
    </div>
    <?php } ?>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        $(document).ready(function(){
            $("#navlinks li:nth-child(7) a").addClass('active');
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