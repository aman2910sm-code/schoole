<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../DB_connection.php";
        include "../data/section.php";

        if (!isset($_GET['section_id']) || empty($_GET['section_id'])) {
            header("Location: section.php");
            exit;
        }

        $section_id = $_GET['section_id'];

        if (function_exists('getSectionById')) {
            $section = getSectionById($section_id, $conn);
        } else {
            $stmt = $conn->prepare("SELECT * FROM sections WHERE section_id = ?");
            $stmt->execute([$section_id]);
            $section = $stmt->fetch(PDO::FETCH_ASSOC);
        }

        if (!$section) {
            header("Location: section.php");
            exit;
        }

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Edit Section</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
    <?php include "../inc/navbar.php"; ?>

    <div class="container mt-5">
        <a href="section.php" class="btn btn-dark">Go Back</a>

        <form method="post"
              class="shadow p-3 mt-5 form-w"
              action="req/section-edit.php">

            <input type="hidden" name="section_id" value="<?= htmlspecialchars($section['section_id']) ?>">

            <h3>Edit Section</h3><hr>
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
                <label class="form-label">Section</label>
                <input type="text" class="form-control" name="section"
                       value="<?= htmlspecialchars($section['section'] ?? '') ?>">
            </div>

            <button type="submit" class="btn btn-primary">Update</button>

        </form>

    </div>

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