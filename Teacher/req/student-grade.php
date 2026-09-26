<?php
session_start();
if (isset($_SESSION['teacher_id']) &&
    isset($_SESSION['role'])) {

    if ($_SESSION['role'] == 'Teacher') {
        include "../DB_connection.php";
        include "../Teacher/data/student.php";
        include "../data/grade.php";
        include "../data/class.php";
        include "../data/section.php";
        include "../data/course.php";

        $class_id   = $_GET['class_id']   ?? null;
        $student_id = $_GET['student_id'] ?? null;

        if ($student_id) {
            // ===== Single student grade view =====
            $one_student   = getStudentById($student_id, $conn);
            $allgrades     = getALLGrades($conn);
            $student_courses     = getALLCourses($conn);

            $student_grade_info   = null;
            $student_section_info = null;
            if ($one_student != 0) {
                if (!empty($one_student['grade'])) {
                    $g_temp = getGradeById($one_student['grade'], $conn);
                    if ($g_temp != 0) { $student_grade_info = $g_temp; }
                }
                if (!empty($one_student['section'])) {
                    $s_temp = getSectionById($one_student['section'], $conn);
                    if ($s_temp != 0) { $student_section_info = $s_temp; }
                }
            }

            // ===== Courses matching this student's grade =====
            $student_courses = [];
            $all_courses_temp = getALLCourses($conn);
            if (is_array($all_courses_temp) && $student_grade_info) {
                foreach ($all_courses_temp as $c) {
                    if ($c['grade_code'] == $student_grade_info['grade_code'] &&
                        $c['grade']      == $student_grade_info['grade']) {
                        $student_courses[] = $c;
                    }
                }
            }
        } elseif ($class_id) {
            // ===== Students of a class =====
            $current_class = getClassById($class_id, $conn);
            if ($current_class != 0) {
                $student = getStudentsByClass($current_class['grade'], $current_class['section'], $conn);
            } else {
                $student = 0;
            }
            $allgrades = getALLGrades($conn);
        } else {
            // ===== Classes list =====
            $classes = getALLClasses($conn);
        }

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teacher - Students Grade</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
    <?php include "../Teacher/inc/navbar.php"; ?>

    <?php if ($student_id) { ?>
        <!-- ===== Single Student Grade View ===== -->
        <?php if ($one_student != 0) { ?>
        <div class="container mt-5">
            <?php if (isset($_GET['updated'])) { ?>
            <div class="alert alert-info mt-3 mx-auto" style="max-width:450px;" role="alert">Successfully updated!</div>
            <?php } ?>

            <div class="shadow rounded p-4 mx-auto bg-white" style="max-width:450px;">
                <div class="mb-2 d-flex justify-content-between border-bottom pb-2">
                    <strong>ID:</strong> <span><?= $one_student['student_id'] ?? '' ?></span>
                </div>
                <div class="mb-2 d-flex justify-content-between border-bottom pb-2">
                    <strong>First Name:</strong> <span><?= $one_student['fname'] ?? '' ?></span>
                </div>
                <div class="mb-2 d-flex justify-content-between border-bottom pb-2">
                    <strong>Last Name:</strong> <span><?= $one_student['lname'] ?? '' ?></span>
                </div>
                <div class="mb-2 d-flex justify-content-between border-bottom pb-2">
                    <strong>Garde:</strong>
                    <span><?= $student_grade_info ? ($student_grade_info['grade_code'] . '-' . $student_grade_info['grade']) : '' ?></span>
                </div>
                <div class="mb-3 d-flex justify-content-between border-bottom pb-2">
                    <strong>Section:</strong>
                    <span><?= $student_section_info ? $student_section_info['section'] : '' ?></span>
                </div>

                <form method="post" action="req/student-grade-update.php">
                    <input type="hidden" name="student_id" value="<?= $one_student['student_id'] ?>">

                    <div class="mb-2 d-flex justify-content-center gap-3 border-bottom pb-2">
                        <span><strong>Year:</strong> 2023</span>
                        <span><strong>Semester</strong> II</span>
                    </div>

                    <h5 class="text-center mt-3 mb-3">Add Grade</h5>

                    <div class="mb-3">
                        <label class="form-label">Subject / Course</label>
                        <input type="text" name="subject" class="form-control" list="subjectList" autocomplete="off">
                        <datalist id="subjectList">
                            <?php foreach ($student_courses as $crs) { ?>
                            <option value="<?= htmlspecialchars($crs['course_name']) ?>">
                            <?php } ?>
                        </datalist>
                    </div>

                    <div class="input-group mb-3">
                        <input type="number" min="0" max="100" class="form-control">
                        <span class="input-group-text">/</span>
                        <input type="number" min="0" max="100" class="form-control">
                    </div>

                    <button type="submit" class="btn btn-primary">Save</button>
                    <a href="students_of_class.php" class="btn btn-dark">Go Back</a>
                </form>
            </div>


        </div>
        <?php } else { ?>
            <div class="alert alert-info" role="alert">Student not found!</div>
        <?php } ?>

    <?php } elseif (!$class_id) { ?>
        <!-- ===== Classes list ===== -->
        <?php if ($classes != 0) { ?>
        <div class="container mt-5">
            <div class="table-responsiv">
                <table class="table table-bordered mt-3 n-table">
                    <thead>
                        <tr>
                            <th scope="col">#</th>
                            <th scope="col">Class</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php $i = 1; foreach ($classes as $row) { ?>
                        <tr>
                            <th scope="row"><?= $i++ ?></th>
                            <td>
                                <a href="student-grade.php?class_id=<?= $row['class_id'] ?>" style="color:#0d6efd; text-decoration:underline;">
                                    <?= $row['grade_code'] . '-' . $row['grade_num'] . $row['section_name'] ?>
                                </a>
                            </td>
                        </tr>
                        <?php } ?>
                    </tbody>
                </table>
            </div>
        </div>
        <?php } else { ?>
            <div class="alert alert-info" role="alert">Empty!</div>
        <?php } ?>

    <?php } else { ?>
        <!-- ===== Students of the selected class, with editable Grade ===== -->
        <?php if ($student != 0) { ?>
        <div class="container mt-5">
            <a href="student-grade.php" class="btn btn-dark">Go Back</a>

            <?php if (isset($_GET['updated'])) { ?>
            <div class="alert alert-info mt-3" role="alert">Successfully updated!</div>
            <?php } ?>

            <div class="table-responsiv">
                <table class="table table-bordered mt-3 n-table">
                    <thead>
                        <tr>
                            <th scope="col">#</th>
                            <th scope="col">Id</th>
                            <th scope="col">First Name</th>
                            <th scope="col">Last Name</th>
                            <th scope="col">Username</th>
                            <th scope="col">Grade</th>
                            <th scope="col">Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php $i = 1; foreach ($student as $row) { ?>
                        <tr>
                            <th scope="row"><?= $i++ ?></th>
                            <td><?= $row['student_id'] ?? '' ?></td>
                            <td>
                                <a href="student-grade.php?class_id=<?= $class_id ?>&student_id=<?= $row['student_id'] ?>" style="color:#0d6efd; text-decoration:underline;">
                                    <?= $row['fname'] ?? '' ?>
                                </a>
                            </td>
                            <td><?= $row['lname'] ?? '' ?></td>
                            <td><?= $row['username'] ?? '' ?></td>
                            <td>
                                <form method="post" action="req/student-grade-update.php" class="d-flex align-items-center gap-2">
                                    <input type="hidden" name="student_id" value="<?= $row['student_id'] ?>">
                                    <input type="hidden" name="class_id" value="<?= $class_id ?>">
                                    <select name="grade_id" class="form-select form-select-sm" style="width:auto;">
                                        <?php foreach ($allgrades as $grd) { ?>
                                        <option value="<?= $grd['grade_id'] ?>"
                                            <?= ($grd['grade_id'] == $row['grade']) ? 'selected' : '' ?>>
                                            <?= $grd['grade_code'] . '-' . $grd['grade'] ?>
                                        </option>
                                        <?php } ?>
                                    </select>
                            </td>
                            <td>
                                    <button type="submit" class="btn btn-sm btn-primary">Save</button>
                                </form>
                            </td>
                        </tr>
                        <?php } ?>
                    </tbody>
                </table>
            </div>
        </div>
        <?php } else { ?>
            <div class="alert alert-info" role="alert">Empty!</div>
        <?php } ?>
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