<?php
session_start();
if (isset($_SESSION['admin_id']) && 
    isset($_SESSION['role'])) {

    if ($_SESSION['role'] == 'Admin') {

        include "../DB_connection.php";
        include "../data/student.php";

        if (!isset($_GET['student_id']) || empty($_GET['student_id'])) {
            header("Location: student.php");
            exit;
        }

        $student_id = $_GET['student_id'];

        // Student exist kare che ke nahi check karo
        $student = getStudentById($student_id, $conn);

        if ($student == 0) {
            header("Location: student.php");
            exit;
        }

        // Student delete karo
        try {
            $sql  = "DELETE FROM student WHERE student_id = ?";
            $stmt = $conn->prepare($sql);
            $stmt->execute([$student_id]);

            header("Location: student.php?deleted=1");
            exit;
        } catch (PDOException $e) {
            if ($e->getCode() == 23000) {
                $em = "Cannot delete this Student because related records depend on it.";
            } else {
                $em = "An error occurred while deleting the student.";
            }
            header("Location: student.php?error=" . urlencode($em));
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