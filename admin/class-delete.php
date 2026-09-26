<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../DB_connection.php";
        include "../data/class.php";

        if (!isset($_GET['class_id']) || empty($_GET['class_id'])) {
            header("Location: class.php");
            exit;
        }

        $class_id = $_GET['class_id'];

        try {
            if (function_exists('deleteClass')) {
                deleteClass($class_id, $conn);
            } else {
                $stmt = $conn->prepare("DELETE FROM class WHERE class_id = ?");
                $stmt->execute([$class_id]);
            }

            header("Location: class.php?deleted=1");
            exit;

        } catch (PDOException $e) {
            if ($e->getCode() == 23000) {
                $em = "Cannot delete this Class because it is referenced by other records.";
            } else {
                $em = "An error occurred while deleting the class.";
            }
            header("Location: class.php?error=" . urlencode($em));
            exit;
        } catch (Exception $e) {
            header("Location: class.php?error=" . urlencode("Delete failed: " . $e->getMessage()));
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