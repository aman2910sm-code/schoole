<?php
session_start();
if (isset($_SESSION['admin_id']) &&
    isset($_SESSION['role'])) {

    if ($_SESSION['role'] == 'Admin') {
        include "../DB_connection.php";
        include "../data/course.php";

        $course_id = $_GET['course_id'] ?? '';

        if ($course_id === '' || !is_numeric($course_id)) {
            header("Location: course.php?error=" . urlencode("Invalid course"));
            exit;
        }

        $course = getCoursesById($course_id, $conn);

        if (!$course) {
            header("Location: course.php?error=" . urlencode("Course not found"));
            exit;
        }

        $grades = getAllGradesForDropdown($conn);

        // Current grade value in "GRADE_CODE-GRADE" format, e.g. "G-2"
        $current_grade_value = $course['grade_code'] . '-' . $course['grade'];
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Edit Course</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
        .form-w { border-radius: 16px; }
        .form-w .form-label { font-weight: 500; color: #333; margin-bottom: 8px; }
        .form-w .form-control, .form-w .form-select {
            background-color: #EAF1FE;
            border: 1px solid #EAF1FE;
            border-radius: 10px;
            padding: 12px 16px;
            font-size: 15px;
        }
        .form-w .form-control:focus, .form-w .form-select:focus {
            background-color: #fff;
            border-color: #86b7fe;
            box-shadow: 0 0 0 0.2rem rgba(13,110,253,.15);
        }
    </style>
</head>
<body>
    <?php include "../inc/navbar.php"; ?>

    <div class="container mt-5">
        <a href="course.php" class="btn btn-dark">Go Back</a>

        <form method="post"
              class="shadow p-3 mt-5 form-w"
              action="req/course-edit.php">

            <input type="hidden" name="course_id" value="<?= htmlspecialchars($course['course_id']) ?>">

            <h3>Edit Course</h3><hr>
            <?php if (isset($_GET['error'])) { ?>
            <div class="alert alert-danger" role="alert">
                <?= htmlspecialchars($_GET['error']) ?>
            </div>
            <?php } ?>

            <div class="mb-3">
                <label class="form-label">Course Name</label>
                <input type="text" class="form-control" name="course_name" required
                       value="<?= isset($_GET['course_name']) ? htmlspecialchars($_GET['course_name']) : htmlspecialchars($course['course_name']) ?>">
            </div>

            <div class="mb-3">
                <label class="form-label">Course Code</label>
                <input type="text" class="form-control" name="course_code" required
                       value="<?= isset($_GET['course_code']) ? htmlspecialchars($_GET['course_code']) : htmlspecialchars($course['course_code']) ?>">
            </div>

            <div class="mb-3">
                <label class="form-label">Grade</label>
                <select class="form-select" name="grade" required>
                    <option value="" disabled>Select grade</option>
                    <?php foreach ($grades as $g) {
                        $value = $g['grade_code'] . '-' . $g['grade'];
                        $selected = ($value === $current_grade_value) ? 'selected' : '';
                    ?>
                    <option value="<?= htmlspecialchars($value) ?>" <?= $selected ?>>
                        <?= htmlspecialchars($g['grade_label']) ?>
                    </option>
                    <?php } ?>
                </select>
            </div>

            <button type="submit" class="btn btn-primary">Update</button>

        </form>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        $(document).ready(function(){
            $("#navlinks li:nth-child(8) a").addClass('active');
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