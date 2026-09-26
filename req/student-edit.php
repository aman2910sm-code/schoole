<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../../DB_connection.php";

        $student_id    = isset($_POST['student_id'])    ? trim($_POST['student_id'])    : '';
        $fname         = isset($_POST['fname'])         ? trim($_POST['fname'])         : '';
        $lname         = isset($_POST['lname'])         ? trim($_POST['lname'])         : '';
        $address       = isset($_POST['address'])       ? trim($_POST['address'])       : '';
        $email         = isset($_POST['email'])         ? trim($_POST['email'])         : '';
        $dob           = isset($_POST['dob'])            ? trim($_POST['dob'])           : '';
        $gender        = isset($_POST['gender'])         ? trim($_POST['gender'])        : '';
        $uname         = isset($_POST['Username'])       ? trim($_POST['Username'])      : '';
        $parent_fname  = isset($_POST['parent_fname'])   ? trim($_POST['parent_fname'])  : '';
        $parent_lname  = isset($_POST['parent_lname'])   ? trim($_POST['parent_lname'])  : '';
        $parent_phone  = isset($_POST['parent_phone'])   ? trim($_POST['parent_phone'])  : '';
        $grade_id      = isset($_POST['grade_id'])       ? trim($_POST['grade_id'])      : '';
        $section       = isset($_POST['section'])        ? trim($_POST['section'])       : '';

        // student_id vagar update na thai shake
        if (empty($student_id)) {
            header("Location: ../student.php");
            exit;
        }

        // Field validations
        if (empty($fname)) {
            header("Location: ../student-edit.php?student_id=$student_id&error=" . urlencode("First name is required"));
            exit;
        } elseif (empty($lname)) {
            header("Location: ../student-edit.php?student_id=$student_id&error=" . urlencode("Last name is required"));
            exit;
        } elseif (empty($address)) {
            header("Location: ../student-edit.php?student_id=$student_id&error=" . urlencode("Address is required"));
            exit;
        } elseif (empty($email)) {
            header("Location: ../student-edit.php?student_id=$student_id&error=" . urlencode("Email address is required"));
            exit;
        } elseif (empty($dob)) {
            header("Location: ../student-edit.php?student_id=$student_id&error=" . urlencode("Date of birth is required"));
            exit;
        } elseif (empty($gender)) {
            header("Location: ../student-edit.php?student_id=$student_id&error=" . urlencode("Gender is required"));
            exit;
        } elseif (empty($uname)) {
            header("Location: ../student-edit.php?student_id=$student_id&error=" . urlencode("Username is required"));
            exit;
        } elseif (empty($grade_id)) {
            header("Location: ../student-edit.php?student_id=$student_id&error=" . urlencode("Please select a grade"));
            exit;
        } elseif (empty($section)) {
            header("Location: ../student-edit.php?student_id=$student_id&error=" . urlencode("Please select a section"));
            exit;
        } elseif (empty($parent_fname)) {
            header("Location: ../student-edit.php?student_id=$student_id&error=" . urlencode("Parent first name is required"));
            exit;
        } elseif (empty($parent_lname)) {
            header("Location: ../student-edit.php?student_id=$student_id&error=" . urlencode("Parent last name is required"));
            exit;
        } elseif (empty($parent_phone)) {
            header("Location: ../student-edit.php?student_id=$student_id&error=" . urlencode("Parent phone number is required"));
            exit;
        }

        // Student exist kare chhe ke nahi check karo
        $checkSql  = "SELECT * FROM student WHERE student_id = ?";
        $checkStmt = $conn->prepare($checkSql);
        $checkStmt->execute([$student_id]);

        if ($checkStmt->rowCount() == 0) {
            header("Location: ../student.php");
            exit;
        }

        // Username koi bija student e nathi vaparyu e check karo
        $dupSql  = "SELECT * FROM student WHERE username = ? AND student_id != ?";
        $dupStmt = $conn->prepare($dupSql);
        $dupStmt->execute([$uname, $student_id]);

        if ($dupStmt->rowCount() > 0) {
            header("Location: ../student-edit.php?student_id=$student_id&error=" . urlencode("This username already exists, try another"));
            exit;
        }

        // Update query
        $sql = "UPDATE student SET
                    fname = ?,
                    lname = ?,
                    address = ?,
                    email_address = ?,
                    date_of_birth = ?,
                    gender = ?,
                    username = ?,
                    parent_fname = ?,
                    parent_lname = ?,
                    parent_phone_number = ?,
                    grade = ?,
                    section = ?
                WHERE student_id = ?";

        $stmt = $conn->prepare($sql);
        $stmt->execute([
            $fname,
            $lname,
            $address,
            $email,
            $dob,
            $gender,
            $uname,
            $parent_fname,
            $parent_lname,
            $parent_phone,
            $grade_id,
            $section,
            $student_id
        ]);

        header("Location: ../student-edit.php?student_id=$student_id&updated=1");
        exit;

    } else {
        header("Location: ../../login.php");
        exit;
    }
} else {
    header("Location: ../../login.php");
    exit;
}
?>