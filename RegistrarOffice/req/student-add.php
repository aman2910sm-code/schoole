<?php
session_start();
if (isset($_SESSION['r_user_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Registrar Office') {

        include "../../DB_connection.php";

        $fname               = isset($_POST['fname'])               ? trim($_POST['fname'])               : '';
        $lname               = isset($_POST['lname'])               ? trim($_POST['lname'])               : '';
        $address             = isset($_POST['address'])              ? trim($_POST['address'])             : '';
        $email_address       = isset($_POST['email_address'])        ? trim($_POST['email_address'])       : '';
        $date_of_birth       = isset($_POST['date_of_birth'])        ? trim($_POST['date_of_birth'])       : '';
        $gender              = isset($_POST['gender'])               ? trim($_POST['gender'])              : '';
        $username            = isset($_POST['username'])             ? trim($_POST['username'])            : '';
        $pass                = isset($_POST['pass'])                 ? trim($_POST['pass'])                : '';
        $parent_fname        = isset($_POST['parent_fname'])         ? trim($_POST['parent_fname'])        : '';
        $parent_lname        = isset($_POST['parent_lname'])         ? trim($_POST['parent_lname'])        : '';
        $parent_phone_number = isset($_POST['parent_phone_number'])  ? trim($_POST['parent_phone_number']) : '';
        $grade_id            = isset($_POST['grade_id'])             ? trim($_POST['grade_id'])            : '';
        $section_id          = isset($_POST['section_id'])            ? trim($_POST['section_id'])           : (isset($_POST['section']) ? trim($_POST['section']) : '');

        // Basic validation
        if (empty($fname)) {
            header("Location: ../student-add.php?error=" . urlencode("First name is required"));
            exit;
        } elseif (empty($lname)) {
            header("Location: ../student-add.php?error=" . urlencode("Last name is required"));
            exit;
        } elseif (empty($username)) {
            header("Location: ../student-add.php?error=" . urlencode("Username is required"));
            exit;
        } elseif (empty($pass)) {
            header("Location: ../student-add.php?error=" . urlencode("Password is required"));
            exit;
        } elseif (empty($grade_id) || !is_numeric($grade_id)) {
            header("Location: ../student-add.php?error=" . urlencode("Grade is required"));
            exit;
        } elseif (empty($section_id) || !is_numeric($section_id)) {
            header("Location: ../student-add.php?error=" . urlencode("Section is required"));
            exit;
        }

        // Check if username already exists
        $checkUser = $conn->prepare("SELECT student_id FROM student WHERE username = ?");
        $checkUser->execute([$username]);
        if ($checkUser->rowCount() > 0) {
            header("Location: ../student-add.php?error=" . urlencode("Username is already taken"));
            exit;
        }

        // Hash password
        $hashed_pass = password_hash($pass, PASSWORD_DEFAULT);

        try {
            $sql = "INSERT INTO student
                    (fname, lname, address, email_address, date_of_birth, gender, username, password,
                     parent_fname, parent_lname, parent_phone_number, grade, section)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

            $stmt = $conn->prepare($sql);
            $stmt->execute([
                $fname, $lname, $address, $email_address, $date_of_birth ?: null, $gender, $username, $hashed_pass,
                $parent_fname, $parent_lname, $parent_phone_number, $grade_id, $section_id
            ]);

            header("Location: ../student-add.php?success=" . urlencode("New student registered successfully"));
            exit;

        } catch (PDOException $e) {
            if ($e->getCode() == 23000) {
                $em = "Invalid Grade or Section selected.";
            } else {
                $em = "An error occurred while creating student record.";
            }
            header("Location: ../student-add.php?error=" . urlencode($em));
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