<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../DB_connection.php";
        include "../data/registrar_office.php";

        // List page (registrar-Office.php) e r_user_id parameter mokle che
        $r_user_id = $_GET['r_user_id'] ?? '';

        if (empty($r_user_id)) {
            header("Location: registrar-office.php");
            exit;
        }

        // User khare j existe che ke nahi check karvu
        $ruser = getR_usersById($r_user_id, $conn);

        if ($ruser == 0) {
            header("Location: registrar-office.php");
            exit;
        }

        try {
            // Database mathi delete karvu (PDO style)
            $deleteStmt = $conn->prepare("DELETE FROM registrar_office WHERE r_user_id = ?");
            $success = $deleteStmt->execute([$r_user_id]);

            if ($success) {
                header("Location: registrar-office.php?deleted=1");
                exit;
            } else {
                header("Location: registrar-office.php?error=" . urlencode("Something went wrong! Please try again"));
                exit;
            }
        } catch (PDOException $e) {
            header("Location: registrar-office.php?error=" . urlencode("Cannot delete registrar office user: database error occurred."));
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