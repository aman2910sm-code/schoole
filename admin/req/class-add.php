<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../../DB_connection.php";
        include "../../data/class.php";

        if ($_SERVER['REQUEST_METHOD'] == 'POST') {

            $grade_id   = $_POST['grade_id']   ?? '';
            $section_id = $_POST['section_id'] ?? '';

            if (empty($grade_id) || empty($section_id)) {
                header("Location: ../class-add.php?error=" . urlencode("Please select both Grade and Section"));
                exit;
            }

            if (classExists($grade_id, $section_id, $conn)) {
                header("Location: ../class-add.php?error=" . urlencode("The class already exists"));
                exit;
            }

            try {
                addClass($grade_id, $section_id, $conn);

                header("Location: ../class-add.php?added=1");
                exit;

            } catch (Exception $e) {
                header("Location: ../class-add.php?error=" . urlencode("Add failed: " . $e->getMessage()));
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