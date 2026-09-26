<?php
session_start();
if (isset($_SESSION['student_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Student') {

        include "../../DB_connection.php";

        if ($_SERVER['REQUEST_METHOD'] == 'POST') {

            // Security: always use the logged-in student's own id from the session,
            // never trust the student_id posted from the form.
            $student_id = $_SESSION['student_id'];

            $old_pass   = isset($_POST['admin_pass2']) ? $_POST['admin_pass2'] : '';
            $new_pass   = isset($_POST['new_pass'])    ? $_POST['new_pass']    : '';
            $c_new_pass = isset($_POST['c_new_pass2']) ? $_POST['c_new_pass2'] : '';

            // Field validations
            if (empty($old_pass)) {
                header("Location: ../pass.php?perror=" . urlencode("Old password is required"));
                exit;
            } elseif (empty($new_pass)) {
                header("Location: ../pass.php?perror=" . urlencode("New password is required"));
                exit;
            } elseif (empty($c_new_pass)) {
                header("Location: ../pass.php?perror=" . urlencode("Please confirm the new password"));
                exit;
            } elseif ($new_pass !== $c_new_pass) {
                header("Location: ../pass.php?perror=" . urlencode("New password and confirm password do not match"));
                exit;
            }

            // Fetch the logged-in student's own record
            $studentSql  = "SELECT * FROM student WHERE student_id = ?";
            $studentStmt = $conn->prepare($studentSql);
            $studentStmt->execute([$student_id]);
            $student = $studentStmt->fetch(PDO::FETCH_ASSOC);

            if (!$student) {
                header("Location: ../../login.php");
                exit;
            }

            // Verify the OLD password against the student's own current password
            if (!password_verify($old_pass, $student['password'])) {
                header("Location: ../pass.php?perror=" . urlencode("Incorrect old password"));
                exit;
            }

            // Password update
            $hashedPass = password_hash($new_pass, PASSWORD_DEFAULT);

            $sql  = "UPDATE student SET password = ? WHERE student_id = ?";
            $stmt = $conn->prepare($sql);
            $stmt->execute([$hashedPass, $student_id]);

            header("Location: ../pass.php?psuccess=" . urlencode("The password has been changed successfully!"));
            exit;

        } else {
            header("Location: ../pass.php");
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