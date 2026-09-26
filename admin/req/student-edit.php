<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../../DB_connection.php";

        if ($_SERVER['REQUEST_METHOD'] == 'POST') {

            $student_id     = $_POST['student_id'] ?? '';
            $fname          = trim($_POST['fname'] ?? '');
            $lname          = trim($_POST['lname'] ?? '');
            $address        = trim($_POST['address'] ?? '');
            $email_address          = trim($_POST['email_address'] ?? '');
            $date_of_birth            = trim($_POST['date_of_birth'] ?? '');
            $gender         = trim($_POST['gender'] ?? '');
            $username       = trim($_POST['Username'] ?? '');
            $grade_id       = trim($_POST['grade_id'] ?? '');
            $section_id     = trim($_POST['section_id'] ?? '');
            $parent_fname   = trim($_POST['parent_fname'] ?? '');
            $parent_lname   = trim($_POST['parent_lname'] ?? '');
            $parent_phone_number   = trim($_POST['parent_phone_number'] ?? '');

            /*if (empty($student_id) || empty($fname) || empty($lname) || empty($username)) {
                //header("Location: ../student-edit.php?student_id=" . urlencode($student_id) . "&error=" . urlencode("Please fill all required fields"));
                exit;
            }*/

            $errors = [];

            if (empty($student_id)) $errors[] = 'Student ID';
            if (empty($fname))      $errors[] = 'First Name';
            if (empty($lname))      $errors[] = 'Last Name';
            if (empty($username))   $errors[] = 'Username';
            if (empty($email_address)) $errors[] = 'Email';
            if (empty($grade_id))   $errors[] = 'Grade';
            if (empty($section_id)) $errors[] = 'Section';

            if (!empty($errors)) {
                $msg = 'Required fields missing: ' . implode(', ', $errors);
                header("Location: ../student-edit.php?student_id=" . urlencode($student_id) . "&error=" . urlencode($msg));
                exit;
            }

            try {
                $sql = "UPDATE student SET
                            fname = ?, lname = ?, address = ?, email_address = ?, date_of_birth = ?,
                            gender = ?, username = ?, grade = ?, section = ?,
                            parent_fname = ?, parent_lname = ?, parent_phone_number = ?
                        WHERE student_id = ?";
                $stmt = $conn->prepare($sql);
                $stmt->execute([
                    $fname, $lname, $address, $email_address, $date_of_birth ?: null,
                    $gender, $username, $grade_id, $section_id,
                    $parent_fname, $parent_lname, $parent_phone_number,
                    $student_id
                ]);

                header("Location: ../student-edit.php?student_id=" . urlencode($student_id) . "&updated=1");
                exit;

            } catch (PDOException $e) {
                if ($e->getCode() == 23000) {
                    $em = "Invalid Grade or Section selected.";
                } else {
                    $em = "An error occurred while updating student record.";
                }
                header("Location: ../student-edit.php?student_id=" . urlencode($student_id) . "&error=" . urlencode($em));
                exit;
            } catch (Exception $e) {
                header("Location: ../student-edit.php?student_id=" . urlencode($student_id) . "&error=" . urlencode("Update failed: " . $e->getMessage()));
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