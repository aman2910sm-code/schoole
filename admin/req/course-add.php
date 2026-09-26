<?php
session_start();
if (isset($_SESSION['admin_id']) &&
    isset($_SESSION['role'])) {

    if ($_SESSION['role'] == 'Admin') {
        include "../../DB_connection.php";
        include "../../data/course.php";

        if ($_SERVER['REQUEST_METHOD'] == 'POST') {

            $course_name = trim($_POST['course_name'] ?? '');
            $course_code = trim($_POST['course_code'] ?? '');
            $grade_raw   = trim($_POST['grade'] ?? '');

            if ($course_name === '' || $course_code === '' || $grade_raw === '') {
                header("Location: ../course-add.php?error=" . urlencode("All fields are required")
                    . "&course_name=" . urlencode($course_name)
                    . "&course_code=" . urlencode($course_code));
                exit;
            }

            // Split "KG-1" or "G-1" into grade_code = "KG"/"G" and grade = "1"
            $parts      = explode('-', $grade_raw, 2);
            $grade_code = $parts[0] ?? '';
            $grade      = $parts[1] ?? '';

            if ($grade_code === '' || $grade === '') {
                header("Location: ../course-add.php?error=" . urlencode("Invalid grade selected")
                    . "&course_name=" . urlencode($course_name)
                    . "&course_code=" . urlencode($course_code));
                exit;
            }

            // Check for duplicate course (same name + same grade)
            if (courseExists($conn, $course_name, $grade_code, $grade)) {
                header("Location: ../course-add.php?error=" . urlencode("The course is already exists")
                    . "&course_name=" . urlencode($course_name)
                    . "&course_code=" . urlencode($course_code));
                exit;
            }

            $success = addCourse($conn, $course_name, $course_code, $grade_code, $grade);

            if ($success) {
                header("Location: ../course.php?added=1");
                exit;
            } else {
                header("Location: ../course-add.php?error=" . urlencode("Something went wrong! Please try again")
                    . "&course_name=" . urlencode($course_name)
                    . "&course_code=" . urlencode($course_code));
                exit;
            }

        } else {
            header("Location: ../course.php");
            exit;
        }

    } else {
        header("Location: ../../login.php");
        exit;
    }
} else {
    header("Location: ../../login.php");
    exit;
}
?>