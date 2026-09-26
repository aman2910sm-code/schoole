<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {

    if ($_SESSION['role'] == 'Admin') {
        include "../DB_connection.php";
        include "../data/setting.php";

        $setting = getsetting($conn);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Setting</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
    <?php include "../inc/navbar.php"; ?>

    <div class="container mt-5">
        <?php if ($setting != 0) { ?>
        <form method="post" action="req/setting-edit.php"
              class="shadow p-4 rounded bg-white" style="max-width: 560px;">
            <h3>Edit</h3>
            <hr>

            <?php if (isset($_GET['error'])) { ?>
            <div class="alert alert-danger" role="alert">
                <?= htmlspecialchars($_GET['error']) ?>
            </div>
            <?php } ?>
            <?php if (isset($_GET['success'])) { ?>
            <div class="alert alert-success" role="alert">
                <?= htmlspecialchars($_GET['success']) ?>
            </div>
            <?php } ?>

            <div class="mb-3">
                <label class="form-label">School Name</label>
                <input type="text" class="form-control" name="school_name"
                       value="<?= htmlspecialchars($setting['school_name'] ?? '') ?>">
            </div>
            <div class="mb-3">
                <label class="form-label">Slogan</label>
                <input type="text" class="form-control" name="slogan"
                       value="<?= htmlspecialchars($setting['slogan'] ?? '') ?>">
            </div>
            <div class="mb-3">
                <label class="form-label">About</label>
                <textarea class="form-control" name="about" rows="4"><?= htmlspecialchars($setting['about'] ?? '') ?></textarea>
            </div>

            <div class="mb-3">
                <label class="form-label">Current Year</label>
                <input type="text" class="form-control" name="current_year"
                       value="<?= htmlspecialchars($setting['current_year'] ?? '') ?>">
            </div>
            <div class="mb-3">
                <label class="form-label">Current Semester</label>
                <input type="text" class="form-control" name="current_semester"
                       value="<?= htmlspecialchars($setting['current_semester'] ?? '') ?>">
            </div>

            <button type="submit" class="btn btn-primary">Update</button>
        </form>
        <?php } else { ?>
            <div class="alert alert-info" role="alert">Empty!</div>
        <?php } ?>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        $(document).ready(function(){
            $("#navlinks li:nth-child(10) a").addClass('active');
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