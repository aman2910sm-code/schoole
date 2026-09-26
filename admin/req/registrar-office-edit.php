<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../../DB_connection.php";

        if ($_SERVER['REQUEST_METHOD'] == 'POST') {

            // --- 1. Form ma thi data levu ---
            $r_user_id       = trim($_POST['r_user_id'] ?? '');
            $fname           = trim($_POST['fname'] ?? '');
            $lname           = trim($_POST['lname'] ?? '');
            $username        = trim($_POST['Username'] ?? '');
            $address         = trim($_POST['address'] ?? '');
            $employee_number = trim($_POST['employee_number'] ?? '');
            $phone_number    = trim($_POST['phone_number'] ?? '');
            $qualification   = trim($_POST['qualification'] ?? '');
            $email_address   = trim($_POST['email_address'] ?? '');
            $gender          = trim($_POST['gender'] ?? '');
            $date_of_birth   = trim($_POST['date_of_birth'] ?? '');

            if (empty($r_user_id)) {
                header("Location: ../registrar-office.php");
                exit;
            }

            // --- 2. Khali field check ---
            if (empty($fname)) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&error=" . urlencode("First name is required"));
                exit;
            }
            if (empty($lname)) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&error=" . urlencode("Last name is required"));
                exit;
            }
            if (empty($username)) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&error=" . urlencode("Username is required"));
                exit;
            }
            if (empty($address)) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&error=" . urlencode("Address is required"));
                exit;
            }
            if (empty($employee_number)) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&error=" . urlencode("Employee number is required"));
                exit;
            }
            if (empty($phone_number)) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&error=" . urlencode("Phone number is required"));
                exit;
            }
            if (empty($qualification)) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&error=" . urlencode("Qualification is required"));
                exit;
            }
            if (empty($email_address)) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&error=" . urlencode("Email address is required"));
                exit;
            }
            if (empty($gender)) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&error=" . urlencode("Gender is required"));
                exit;
            }
            if (empty($date_of_birth)) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&error=" . urlencode("Date of birth is required"));
                exit;
            }

            // --- 3. Format validation ---
            if (!filter_var($email_address, FILTER_VALIDATE_EMAIL)) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&error=" . urlencode("Enter a valid email address"));
                exit;
            }
            if (!preg_match('/^[0-9]{10}$/', $phone_number)) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&error=" . urlencode("Phone number must be 10 digits"));
                exit;
            }

            // --- 4. Username koi bija user e (potana sivay) le lidhu che ke nahi check ---
            $checkStmt = $conn->prepare("SELECT r_user_id FROM registrar_office WHERE username = ? AND r_user_id != ?");
            $checkStmt->execute([$username, $r_user_id]);

            if ($checkStmt->rowCount() >= 1) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&error=" . urlencode("Username is taken! try another"));
                exit;
            }

            // --- 5. Email koi bija user e (potana sivay) le lidhu che ke nahi check ---
            $checkEmailStmt = $conn->prepare("SELECT r_user_id FROM registrar_office WHERE email_address = ? AND r_user_id != ?");
            $checkEmailStmt->execute([$email_address, $r_user_id]);

            if ($checkEmailStmt->rowCount() >= 1) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&error=" . urlencode("Email address already registered"));
                exit;
            }

            // --- 6. Database ma update karvu (PDO style) ---
            $updateStmt = $conn->prepare(
                "UPDATE registrar_office SET
                    fname = ?, lname = ?, username = ?, address = ?,
                    employee_number = ?, phone_number = ?, qualification = ?,
                    email_address = ?, gender = ?, date_of_birth = ?
                 WHERE r_user_id = ?"
            );

            $success = $updateStmt->execute([
                $fname,
                $lname,
                $username,
                $address,
                $employee_number,
                $phone_number,
                $qualification,
                $email_address,
                $gender,
                $date_of_birth,
                $r_user_id
            ]);

            if ($success) {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&updated=1");
                exit;
            } else {
                header("Location: ../registrar-office-edit.php?r_user_id=$r_user_id&error=" . urlencode("Something went wrong! Please try again"));
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