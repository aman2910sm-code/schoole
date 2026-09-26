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

        try {
            $success = deleteCourse($conn, $course_id);

            if ($success) {
                header("Location: course.php?deleted=1");
                exit;
            } else {
                header("Location: course.php?error=" . urlencode("Something went wrong! Please try again"));
                exit;
            }
        } catch (PDOException $e) {
            header("Location: course.php?error=" . urlencode("Cannot delete course: database error occurred."));
            exit;
        }

    } else {
        header("Location: ../login.php");
        exit;
    }
} else {
    header("Location: ../login.php");
    exit;
}
?>