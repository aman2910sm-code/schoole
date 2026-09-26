<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../../DB_connection.php";

        if ($_SERVER['REQUEST_METHOD'] == 'POST') {

            // --- 1. Form ma thi data levu ---
            $r_user_id   = trim($_POST['r_user_id'] ?? '');
            $admin_pass2 = trim($_POST['admin_pass2'] ?? '');
            $new_pass    = trim($_POST['new_pass'] ?? '');
            $c_new_pass2 = trim($_POST['c_new_pass2'] ?? '');

            if (empty($r_user_id)) {
                header("Location: ../registrar-office.php");
                exit;
            }

            // --- 2. Khali field check ---
            if (empty($admin_pass2)) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&perror=" . urlencode("Admin password is required"));
                exit;
            }
            if (empty($new_pass)) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&perror=" . urlencode("New password is required"));
                exit;
            }
            if (empty($c_new_pass2)) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&perror=" . urlencode("Please confirm the new password"));
                exit;
            }

            // --- 3. New password ane confirm password match thay che ke nahi ---
            if ($new_pass !== $c_new_pass2) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&perror=" . urlencode("New password and confirm password do not match"));
                exit;
            }

            // --- 4. Logged in admin no password sachho che ke nahi verify karvu ---
            $adminStmt = $conn->prepare("SELECT password FROM admin WHERE admin_id = ?");
            $adminStmt->execute([$_SESSION['admin_id']]);
            $admin = $adminStmt->fetch();

            if (!$admin || !password_verify($admin_pass2, $admin['password'])) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&perror=" . urlencode("Admin password is incorrect"));
                exit;
            }

            // --- 5. r_user_id sachu che ke nahi check ---
            $userStmt = $conn->prepare("SELECT r_user_id FROM registrar_office WHERE r_user_id = ?");
            $userStmt->execute([$r_user_id]);
            if ($userStmt->rowCount() != 1) {
                header("Location: ../registrar-office.php");
                exit;
            }

            // --- 6. New password ne hash kari ne update karvu ---
            $hashedPassword = password_hash($new_pass, PASSWORD_DEFAULT);

            $updateStmt = $conn->prepare("UPDATE registrar_office SET password = ? WHERE r_user_id = ?");
            $success = $updateStmt->execute([$hashedPassword, $r_user_id]);

            if ($success) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&pupdated=1");
                exit;
            } else {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&perror=" . urlencode("Something went wrong! Please try again"));
                exit;
            }

        } else {
            header("Location: ../registrar-office.php");
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