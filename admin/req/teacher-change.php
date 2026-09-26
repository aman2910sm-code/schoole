<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../../DB_connection.php";

        if ($_SERVER['REQUEST_METHOD'] == 'POST') {

            $teacher_id  = isset($_POST['teacher_id'])  ? trim($_POST['teacher_id'])  : '';
            $admin_pass  = isset($_POST['admin_pass2']) ? $_POST['admin_pass2']       : '';
            $new_pass    = isset($_POST['new_pass'])    ? $_POST['new_pass']          : '';
            $c_new_pass  = isset($_POST['c_new_pass2']) ? $_POST['c_new_pass2']       : '';

            // teacher_id vagar kai thai j na shake
            if (empty($teacher_id)) {
                header("Location: ../teacher.php");
                exit;
            }

            // Field validations
            if (empty($admin_pass)) {
                header("Location: ../teacher-edit.php?teacher_id=$teacher_id&perror=" . urlencode("Admin password is required"));
                exit;
            } elseif (empty($new_pass)) {
                header("Location: ../teacher-edit.php?teacher_id=$teacher_id&perror=" . urlencode("New password is required"));
                exit;
            } elseif (empty($c_new_pass)) {
                header("Location: ../teacher-edit.php?teacher_id=$teacher_id&perror=" . urlencode("Please confirm the new password"));
                exit;
            } elseif ($new_pass !== $c_new_pass) {
                header("Location: ../teacher-edit.php?teacher_id=$teacher_id&perror=" . urlencode("New password and confirm password do not match"));
                exit;
            }

            // Logged-in admin no password verify karo
            $adminSql  = "SELECT * FROM admin WHERE admin_id = ?";
            $adminStmt = $conn->prepare($adminSql);
            $adminStmt->execute([$_SESSION['admin_id']]);
            $admin = $adminStmt->fetch(PDO::FETCH_ASSOC);

            if (!$admin || !password_verify($admin_pass, $admin['password'])) {
                header("Location: ../teacher-edit.php?teacher_id=$teacher_id&perror=" . urlencode("Admin password is incorrect"));
                exit;
            }

            // Teacher exist kare che ke nahi check karo
            $teacherCheckSql  = "SELECT * FROM teacher WHERE teacher_id = ?";
            $teacherCheckStmt = $conn->prepare($teacherCheckSql);
            $teacherCheckStmt->execute([$teacher_id]);

            if ($teacherCheckStmt->rowCount() == 0) {
                header("Location: ../teacher.php");
                exit;
            }

            // Password update
            $hashedPass = password_hash($new_pass, PASSWORD_DEFAULT);

            $sql  = "UPDATE teacher SET password = ? WHERE teacher_id = ?";
            $stmt = $conn->prepare($sql);
            $stmt->execute([$hashedPass, $teacher_id]);

            header("Location: ../teacher-edit.php?teacher_id=$teacher_id&pupdated=1");
            exit;

        } else {
            header("Location: ../teacher.php");
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