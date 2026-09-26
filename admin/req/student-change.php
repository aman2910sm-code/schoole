<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../../DB_connection.php";

        if ($_SERVER['REQUEST_METHOD'] == 'POST') {

            $student_id = isset($_POST['student_id'])  ? trim($_POST['student_id'])  : '';
            $admin_pass = isset($_POST['admin_pass2']) ? $_POST['admin_pass2']       : '';
            $new_pass   = isset($_POST['new_pass'])    ? $_POST['new_pass']          : '';
            $c_new_pass = isset($_POST['c_new_pass2']) ? $_POST['c_new_pass2']       : '';

            // student_id vagar kai thai j na shake
            if (empty($student_id)) {
                header("Location: ../student.php");
                exit;
            }

            // Field validations
            if (empty($admin_pass)) {
                header("Location: ../student-edit.php?student_id=$student_id&perror=" . urlencode("Admin password is required"));
                exit;
            } elseif (empty($new_pass)) {
                header("Location: ../student-edit.php?student_id=$student_id&perror=" . urlencode("New password is required"));
                exit;
            } elseif (empty($c_new_pass)) {
                header("Location: ../student-edit.php?student_id=$student_id&perror=" . urlencode("Please confirm the new password"));
                exit;
            } elseif ($new_pass !== $c_new_pass) {
                header("Location: ../student-edit.php?student_id=$student_id&perror=" . urlencode("New password and confirm password do not match"));
                exit;
            }

            // Logged-in admin no password verify karo
            $adminSql  = "SELECT * FROM admin WHERE admin_id = ?";
            $adminStmt = $conn->prepare($adminSql);
            $adminStmt->execute([$_SESSION['admin_id']]);
            $admin = $adminStmt->fetch(PDO::FETCH_ASSOC);

            if (!$admin || !password_verify($admin_pass, $admin['password'])) {
                header("Location: ../student-edit.php?student_id=$student_id&perror=" . urlencode("Admin password is incorrect"));
                exit;
            }

            // Student exist kare che ke nahi check karo
            $studentCheckSql  = "SELECT * FROM student WHERE student_id = ?";
            $studentCheckStmt = $conn->prepare($studentCheckSql);
            $studentCheckStmt->execute([$student_id]);

            if ($studentCheckStmt->rowCount() == 0) {
                header("Location: ../student.php");
                exit;
            }

            // Password update
            $hashedPass = password_hash($new_pass, PASSWORD_DEFAULT);

            $sql  = "UPDATE student SET password = ? WHERE student_id = ?";
            $stmt = $conn->prepare($sql);
            $stmt->execute([$hashedPass, $student_id]);

            header("Location: ../student-edit.php?student_id=$student_id&pupdated=1");
            exit;

        } else {
            header("Location: ../student.php");
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