<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../../DB_connection.php";
        include "../../data/section.php";

        if ($_SERVER['REQUEST_METHOD'] == 'POST') {

            $section_id = $_POST['section_id'] ?? '';
            $section    = $_POST['section']    ?? '';

            if (empty($section_id) || empty($section)) {
                header("Location: ../section-edit.php?section_id=" . urlencode($section_id) . "&error=" . urlencode("Please fill all fields"));
                exit;
            }

            try {
                if (function_exists('updateSection')) {
                    updateSection($section_id, $section, $conn);
                } else {
                    $stmt = $conn->prepare("UPDATE section SET section = ? WHERE section_id = ?");
                    $stmt->execute([$section, $section_id]);
                }

                header("Location: ../section-edit.php?section_id=" . urlencode($section_id) . "&updated=1");
                exit;

            } catch (Exception $e) {
                header("Location: ../section-edit.php?section_id=" . urlencode($section_id) . "&error=" . urlencode("Update failed: " . $e->getMessage()));
                exit;
            }

        } else {
            header("Location: ../section.php");
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