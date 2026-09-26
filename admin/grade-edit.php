<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../DB_connection.php";
        include "../data/grade.php";

        if (!isset($_GET['grade_id']) || empty($_GET['grade_id'])) {
            header("Location: grade.php");
            exit;
        }

        $grade_id = $_GET['grade_id'];

        // Prefer a dedicated function if it exists in data/grade.php,
        // otherwise fall back to a direct query.
        if (function_exists('getGradeById')) {
            $grade = getGradeById($grade_id, $conn);
        } else {
            $stmt = $conn->prepare("SELECT * FROM grade WHERE grade_id = ?");
            $stmt->execute([$grade_id]);
            $grade = $stmt->fetch(PDO::FETCH_ASSOC);
        }

        if (!$grade) {
            header("Location: grade.php");
            exit;
        }

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Edit Grade</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
    <?php include "../inc/navbar.php"; ?>

    <div class="container mt-5">
        <a href="grade.php" class="btn btn-dark">Go Back</a>

        <form method="post"
              class="shadow p-3 mt-5 form-w"
              action="req/grade-edit.php">

            <input type="hidden" name="grade_id" value="<?= htmlspecialchars($grade['grade_id']) ?>">

            <h3>Edit Grade</h3><hr>
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
                <label class="form-label">Grade Code</label>
                <input type="text" class="form-control" name="grade_code"
                       value="<?= htmlspecialchars($grade['grade_code'] ?? '') ?>">
            </div>
            <div class="mb-3">
                <label class="form-label">Grade</label>
                <input type="text" class="form-control" name="grade"
                       value="<?= htmlspecialchars($grade['grade'] ?? '') ?>">
            </div>

            <button type="submit" class="btn btn-primary">Update</button>

        </form>

    </div>

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