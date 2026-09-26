<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../../DB_connection.php";

        if ($_SERVER['REQUEST_METHOD'] == 'POST') {

            $grade_code = isset($_POST['grade_code']) ? trim($_POST['grade_code']) : '';
            $grade      = isset($_POST['grade'])      ? trim($_POST['grade'])      : '';

            if (empty($grade_code)) {
                header("Location: ../grade-add.php?error=" . urlencode("Grade Code is required"));
                exit;
            } elseif (empty($grade)) {
                header("Location: ../grade-add.php?error=" . urlencode("Grade is required"));
                exit;
            }

            $sql = "INSERT INTO grades (grade_code, grade) VALUES (?, ?)";
            $stmt = $conn->prepare($sql);
            $stmt->execute([$grade_code, $grade]);

            header("Location: ../grade-add.php?added=1");
            exit;

        } else {
            header("Location: ../grade-add.php");
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