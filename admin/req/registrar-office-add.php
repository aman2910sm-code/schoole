<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../../DB_connection.php";

        if ($_SERVER['REQUEST_METHOD'] == 'POST') {

            // --- 1. Form ma thi j data levu ---
            $fname           = trim($_POST['fname'] ?? '');
            $lname           = trim($_POST['lname'] ?? '');
            $username        = trim($_POST['Username'] ?? '');
            $pass            = trim($_POST['pass'] ?? '');
            $address         = trim($_POST['address'] ?? '');
            $employee_number = trim($_POST['employee_number'] ?? '');
            $phone_number    = trim($_POST['phone_number'] ?? '');
            $qualification   = trim($_POST['qualification'] ?? '');
            $email_address   = trim($_POST['email_address'] ?? '');
            $gender          = trim($_POST['gender'] ?? '');
            $date_of_birth   = trim($_POST['date_of_birth'] ?? '');

            // Error hoy to pachu form ma bharva mate session ma save karvu
            $_SESSION['old_input'] = $_POST;

            // --- 2. Khali field check (required validation) ---
            if (empty($fname)) {
                header("Location: ../registrar-office-add.php?error=" . urlencode("First name is required"));
                exit;
            }
            if (empty($lname)) {
                header("Location: ../registrar-office-add.php?error=" . urlencode("Last name is required"));
                exit;
            }
            if (empty($username)) {
                header("Location: ../registrar-office-add.php?error=" . urlencode("Username is required"));
                exit;
            }
            if (empty($pass)) {
                header("Location: ../registrar-office-add.php?error=" . urlencode("Password is required"));
                exit;
            }
            if (empty($address)) {
                header("Location: ../registrar-office-add.php?error=" . urlencode("Address is required"));
                exit;
            }
            if (empty($employee_number)) {
                header("Location: ../registrar-office-add.php?error=" . urlencode("Employee number is required"));
                exit;
            }
            if (empty($phone_number)) {
                header("Location: ../registrar-office-add.php?error=" . urlencode("Phone number is required"));
                exit;
            }
            if (empty($qualification)) {
                header("Location: ../registrar-office-add.php?error=" . urlencode("Qualification is required"));
                exit;
            }
            if (empty($email_address)) {
                header("Location: ../registrar-office-add.php?error=" . urlencode("Email address is required"));
                exit;
            }
            if (empty($gender)) {
                header("Location: ../registrar-office-add.php?error=" . urlencode("Gender is required"));
                exit;
            }
            if (empty($date_of_birth)) {
                header("Location: ../registrar-office-add.php?error=" . urlencode("Date of birth is required"));
                exit;
            }

            // --- 3. Format validation ---
            if (!filter_var($email_address, FILTER_VALIDATE_EMAIL)) {
                header("Location: ../registrar-office-add.php?error=" . urlencode("Enter a valid email address"));
                exit;
            }
            if (!preg_match('/^[0-9]{10}$/', $phone_number)) {
                header("Location: ../registrar-office-add.php?error=" . urlencode("Phone number must be 10 digits"));
                exit;
            }

            // --- 4. Username already taken che ke nahi check (PDO style) ---
            $checkStmt = $conn->prepare("SELECT r_user_id FROM registrar_office WHERE username = ?");
            $checkStmt->execute([$username]);

            if ($checkStmt->rowCount() >= 1) {
                header("Location: ../registrar-office-add.php?error=" . urlencode("Username is taken! try another"));
                exit;
            }

            // --- 5. Email already existe che ke nahi check ---
            $checkEmailStmt = $conn->prepare("SELECT r_user_id FROM registrar_office WHERE email_address = ?");
            $checkEmailStmt->execute([$email_address]);

            if ($checkEmailStmt->rowCount() >= 1) {
                header("Location: ../registrar-office-add.php?error=" . urlencode("Email address already registered"));
                exit;
            }

            // --- 6. Password ne hash kari ne save karvu (security best practice) ---
            $hashedPassword = password_hash($pass, PASSWORD_DEFAULT);

            // --- 7. Database ma insert karvu (PDO style) ---
            $insertStmt = $conn->prepare(
                "INSERT INTO registrar_office
                (fname, lname, username, password, address, employee_number, phone_number, qualification, email_address, gender, date_of_birth)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            );

            $success = $insertStmt->execute([
                $fname,
                $lname,
                $username,
                $hashedPassword,
                $address,
                $employee_number,
                $phone_number,
                $qualification,
                $email_address,
                $gender,
                $date_of_birth
            ]);

            if ($success) {
                unset($_SESSION['old_input']); // success thay etle old data hatavi do
                header("Location: ../registrar-office.php?added=1");
                exit;
            } else {
                header("Location: ../registrar-office-add.php?error=" . urlencode("Something went wrong! Please try again"));
                exit;
            }

        } else {
            // Direct GET thi aa file access thay to add page par pacha modi do
            header("Location: ../registrar-office-add.php");
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