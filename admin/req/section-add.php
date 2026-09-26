<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../../DB_connection.php";
        include "../../data/section.php";

        if ($_SERVER['REQUEST_METHOD'] == 'POST') {

            $section = $_POST['section'] ?? '';

            if (empty($section)) {
                header("Location: ../section-add.php?error=" . urlencode("Section is required"));
                exit;
            }

            try {
                if (function_exists('addSection')) {
                    addSection($section, $conn);
                } else {
                    $stmt = $conn->prepare("INSERT INTO section (section) VALUES (?)");
                    $stmt->execute([$section]);
                }

                header("Location: ../section-add.php?added=1");
                exit;

            } catch (Exception $e) {
                header("Location: ../section-add.php?error=" . urlencode("Add failed: " . $e->getMessage()));
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