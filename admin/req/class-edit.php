<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../../DB_connection.php";
        include "../../data/class.php";

        if ($_SERVER['REQUEST_METHOD'] == 'POST') {

            $class_id   = $_POST['class_id']   ?? '';
            $grade_id   = $_POST['grade_id']   ?? '';
            $section_id = $_POST['section_id'] ?? '';

            if (empty($class_id) || empty($grade_id) || empty($section_id)) {
                header("Location: ../class-edit.php?class_id=" . urlencode($class_id) . "&error=" . urlencode("Please select both Grade and Section"));
                exit;
            }

            if (classExistsExcluding($grade_id, $section_id, $class_id, $conn)) {
                header("Location: ../class-edit.php?class_id=" . urlencode($class_id) . "&error=" . urlencode("The class already exists"));
                exit;
            }

            try {
                updateClass($class_id, $grade_id, $section_id, $conn);

                header("Location: ../class-edit.php?class_id=" . urlencode($class_id) . "&updated=1");
                exit;

            } catch (Exception $e) {
                header("Location: ../class-edit.php?class_id=" . urlencode($class_id) . "&error=" . urlencode("Update failed: " . $e->getMessage()));
                exit;
            }

        } else {
            header("Location: ../class.php");
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