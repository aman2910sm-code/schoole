<?php
session_start();
if (isset($_SESSION['admin_id']) &&
    isset($_SESSION['role'])) {

    if ($_SESSION['role'] == 'Admin') {

        include "../DB_connection.php";

        if (!isset($_GET['grade_id']) || empty($_GET['grade_id'])) {
            header("Location: grade.php");
            exit;
        }

        $grade_id = $_GET['grade_id'];

        // Grade exist kare chhe ke nahi check karo
        $checkSql  = "SELECT * FROM grades WHERE grade_id = ?";
        $checkStmt = $conn->prepare($checkSql);
        $checkStmt->execute([$grade_id]);

        if ($checkStmt->rowCount() == 0) {
            header("Location: grade.php");
            exit;
        }

        // Grade delete karo
        try {
            $sql  = "DELETE FROM grades WHERE grade_id = ?";
            $stmt = $conn->prepare($sql);
            $stmt->execute([$grade_id]);

            header("Location: grade.php?deleted=1");
            exit;
        } catch (PDOException $e) {
            if ($e->getCode() == 23000) {
                $em = "Cannot delete this Grade because it is assigned to active classes, students, or subjects.";
            } else {
                $em = "An error occurred while deleting the grade.";
            }
            header("Location: grade.php?error=" . urlencode($em));
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