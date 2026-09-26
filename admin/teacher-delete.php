<?php
session_start();
if (isset($_SESSION['admin_id']) && 
    isset($_SESSION['role'])) {

    if ($_SESSION['role'] == 'Admin') {

        include "../DB_connection.php";
        include "../data/teacher.php";

        if (!isset($_GET['teacher_id']) || empty($_GET['teacher_id'])) {
            header("Location: teacher.php");
            exit;
        }

        $teacher_id = $_GET['teacher_id'];

        // Teacher exist kare che ke nahi check karo
        $teacher = getTeacherById($teacher_id, $conn);

        if ($teacher == 0) {
            header("Location: teacher.php");
            exit;
        }

        // Teacher delete karo
        try {
            $sql  = "DELETE FROM teacher WHERE teacher_id = ?";
            $stmt = $conn->prepare($sql);
            $stmt->execute([$teacher_id]);

            header("Location: teacher.php?deleted=1");
            exit;
        } catch (PDOException $e) {
            if ($e->getCode() == 23000) {
                $em = "Cannot delete this Teacher because they have assigned student scores.";
            } else {
                $em = "An error occurred while deleting the teacher.";
            }
            header("Location: teacher.php?error=" . urlencode($em));
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