<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../DB_connection.php";
        include "../data/class.php";
        include "../data/grade.php";
        include "../data/section.php";

        if (!isset($_GET['class_id']) || empty($_GET['class_id'])) {
            header("Location: class.php");
            exit;
        }

        $class_id = $_GET['class_id'];
        $class    = getClassById($class_id, $conn);

        if (!$class) {
            header("Location: class.php");
            exit;
        }

        $allGrades   = getALLGrades($conn);
        $allSections = getALLSections($conn);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Edit Class</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
    <?php include "../inc/navbar.php"; ?>

    <div class="container mt-5">
        <a href="class.php" class="btn btn-dark">Go Back</a>

        <form method="post"
              class="shadow p-3 mt-5 form-w"
              action="req/class-edit.php">

            <input type="hidden" name="class_id" value="<?= htmlspecialchars($class['class_id']) ?>">

            <h3>Edit Class</h3><hr>
            <?php if (isset($_GET['updated'])) { ?>
            <div class="alert alert-success" role="alert">
                Successfully updated!
            </div>
            <?php } ?>
            <?php if (isset($_GET['error'])) { ?>
            <div class="alert alert-danger" role="alert">
                <?= htmlspecialchars($_GET['error']) ?>
            </div>
            <?php } ?>

            <div class="mb-3">
                <label class="form-label">Grade</label>
                <select class="form-select" name="grade_id">
                    <option value="" disabled>Select Grade</option>
                    <?php if (!empty($allGrades)) { foreach ($allGrades as $g) { ?>
                    <option value="<?= $g['grade_id'] ?>"
                        <?= ($g['grade_id'] == $class['grade']) ? 'selected' : '' ?>>
                        <?= htmlspecialchars($g['grade_code'] . '-' . $g['grade']) ?>
                    </option>
                    <?php } } ?>
                </select>
            </div>

            <div class="mb-3">
                <label class="form-label">Section</label>
                <select class="form-select" name="section_id">
                    <option value="" disabled>Select Section</option>
                    <?php if (!empty($allSections)) { foreach ($allSections as $s) { ?>
                    <option value="<?= $s['section_id'] ?>"
                        <?= ($s['section_id'] == $class['section']) ? 'selected' : '' ?>>
                        <?= htmlspecialchars($s['section']) ?>
                    </option>
                    <?php } } ?>
                </select>
            </div>

            <button type="submit" class="btn btn-primary">Update</button>

        </form>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        $(document).ready(function(){
            $("#navlinks li:nth-child(6) a").addClass('active');
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