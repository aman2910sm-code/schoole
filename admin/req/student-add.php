<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../../DB_connection.php";

        if ($_SERVER['REQUEST_METHOD'] == 'POST') {

            $fname          = trim($_POST['fname'] ?? '');
            $lname          = trim($_POST['lname'] ?? '');
            $address        = trim($_POST['address'] ?? '');
            $email          = trim($_POST['email_address'] ?? '');
            $dob            = trim($_POST['date_of_birth'] ?? '');
            $gender         = trim($_POST['gender'] ?? '');
            $username       = trim($_POST['username'] ?? '');
            $pass           = trim($_POST['pass'] ?? '');
            $parent_fname   = trim($_POST['parent_fname'] ?? '');
            $parent_lname   = trim($_POST['parent_lname'] ?? '');
            $parent_phone   = trim($_POST['parent_phone_number'] ?? '');
            $grade_id       = trim($_POST['grade_id'] ?? '');
            $section_id     = trim($_POST['section_id'] ?? '');
            $subject_ids    = $_POST['subject_id'] ?? [];

            if (empty($fname) || empty($lname) || empty($username) || empty($pass) || empty($grade_id) || empty($section_id)) {
                header("Location: ../student-add.php?error=" . urlencode("Please fill all required fields including Grade and Section"));
                exit;
            }

            // Check if username already exists
            $checkSql = "SELECT student_id FROM student WHERE username = ?";
            $checkStmt = $conn->prepare($checkSql);
            $checkStmt->execute([$username]);
            if ($checkStmt->rowCount() > 0) {
                header("Location: ../student-add.php?error=" . urlencode("This Username already exists, try another"));
                exit;
            }

            try {
                $hashedPass = password_hash($pass, PASSWORD_DEFAULT);
                $subjets    = !empty($subject_ids) ? implode(',', $subject_ids) : null;

                $sql = "INSERT INTO student
                        (fname, lname, address, email_address, date_of_birth, gender, username, password,
                         parent_fname, parent_lname, parent_phone_number, grade, section, subjets)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
                $stmt = $conn->prepare($sql);
                $stmt->execute([
                    $fname, $lname, $address, $email, $dob ?: null, $gender, $username, $hashedPass,
                    $parent_fname, $parent_lname, $parent_phone,
                    $grade_id, $section_id, $subjets
                ]);

                header("Location: ../student.php?added=1");
                exit;

            } catch (PDOException $e) {
                if ($e->getCode() == 23000) {
                    $em = "Invalid Grade or Section selected.";
                } else {
                    $em = "An error occurred while creating student record.";
                }
                header("Location: ../student-add.php?error=" . urlencode($em));
                exit;
            } catch (Exception $e) {
                header("Location: ../student-add.php?error=" . urlencode("Add failed: " . $e->getMessage()));
                exit;
            }

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