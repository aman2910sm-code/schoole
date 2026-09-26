<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../../DB_connection.php";
        include "../../data/grade.php";

        if ($_SERVER['REQUEST_METHOD'] == 'POST') {

            $grade_id   = $_POST['grade_id']   ?? '';
            $grade_code = $_POST['grade_code'] ?? '';
            $grade      = $_POST['grade']      ?? '';

            if (empty($grade_id) || empty($grade_code) || empty($grade)) {
                header("Location: ../grade-edit.php?grade_id=" . urlencode($grade_id) . "&error=" . urlencode("Please fill all fields"));
                exit;
            }

            try {
                if (function_exists('updateGrade')) {
                    updateGrade($grade_id, $grade_code, $grade, $conn);
                } else {
                    $stmt = $conn->prepare("UPDATE grades SET grade_code = ?, grade = ? WHERE grade_id = ?");
                    $stmt->execute([$grade_code, $grade, $grade_id]);
                }

                header("Location: ../grade-edit.php?grade_id=" . urlencode($grade_id) . "&updated=1");
                exit;

            } catch (Exception $e) {
                header("Location: ../grade-edit.php?grade_id=" . urlencode($grade_id) . "&error=" . urlencode("Update failed: " . $e->getMessage()));
                exit;
            }

        } else {
            header("Location: ../grade.php");
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