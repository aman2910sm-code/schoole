<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../DB_connection.php";
        include "../data/section.php";

        if (!isset($_GET['section_id']) || empty($_GET['section_id'])) {
            header("Location: section.php");
            exit;
        }

        $section_id = $_GET['section_id'];

        try {
            if (function_exists('deleteSection')) {
                deleteSection($section_id, $conn);
            } else {
                $stmt = $conn->prepare("DELETE FROM section WHERE section_id = ?");
                $stmt->execute([$section_id]);
            }

            header("Location: section.php?deleted=1");
            exit;

        } catch (PDOException $e) {
            if ($e->getCode() == 23000) {
                $em = "Cannot delete this Section because it is assigned to active classes or students.";
            } else {
                $em = "An error occurred while deleting the section.";
            }
            header("Location: section.php?error=" . urlencode($em));
            exit;
        } catch (Exception $e) {
            header("Location: section.php?error=" . urlencode("Delete failed: " . $e->getMessage()));
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