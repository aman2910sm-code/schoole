<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        if (isset($_POST['teacher_id']) &&
            isset($_POST['fname']) &&
            isset($_POST['lname']) &&
            isset($_POST['Username'])) {

            include "../../DB_connection.php";

            $teacher_id  = $_POST['teacher_id'];
            $fname       = trim($_POST['fname']);
            $lname       = trim($_POST['lname']);
            $uname       = trim($_POST['Username']);
            $address     = trim($_POST['address'] ?? '');
            $employee_no = trim($_POST['employee_number'] ?? '');
            $dob         = trim($_POST['date_of_birth'] ?? '');
            $phone       = trim($_POST['phone_number'] ?? '');
            $qualification = trim($_POST['qualification'] ?? '');
            $email       = trim($_POST['email_address'] ?? '');
            $gender      = trim($_POST['gender'] ?? '');
            $subject_ids = isset($_POST['subject_id']) ? $_POST['subject_id'] : [];
            $grade_ids   = isset($_POST['grade_id'])   ? $_POST['grade_id']   : [];
            $section_ids = isset($_POST['section_id']) ? $_POST['section_id'] : [];

            if (empty($fname) || empty($lname) || empty($uname)) {
                $em = "Badha fields bharvu jaruri che";
                header("Location: ../teacher-edit.php?teacher_id=" . urlencode($teacher_id) . "&error=" . urlencode($em));
                exit;
            }

            // Check username already biji koi teacher pase to nathi ne (potana sivay)
            $checkSql = "SELECT * FROM teacher WHERE username = ? AND teacher_id != ?";
            $checkStmt = $conn->prepare($checkSql);
            $checkStmt->execute([$uname, $teacher_id]);

            if ($checkStmt->rowCount() > 0) {
                $em = "Aa Username pehla thi j che, biju try karo";
                header("Location: ../teacher-edit.php?teacher_id=" . urlencode($teacher_id) . "&error=" . urlencode($em));
                exit;
            }

            // IMPORTANT: comma separator vaparo, nahi to Class column ma
            // multiple grade/section IDs bhega thai ne khota ID ban se
            // (e.g. grade_id 1 ane 2 -> "12" thai jashe, jene DB ma koi
            // grade match nai male, ane list page par "-" bataye).
            $subjets = implode(',', $subject_ids);
            $gradeId  = implode(',', $grade_ids);
            $section = implode(',', $section_ids);

            $sql = "UPDATE teacher
                    SET fname = ?, lname = ?, username = ?, address = ?, employee_number = ?,
                        date_of_birth = ?, phone_number = ?, qualification = ?, email_address = ?,
                        gender = ?, subjets = ?, class = ?
                    WHERE teacher_id = ?";
            $stmt = $conn->prepare($sql);
            $stmt->execute([
                $fname, $lname, $uname, $address, $employee_no,
                $dob, $phone, $qualification, $email,
                $gender, $subjets, $gradeId,
                $teacher_id
            ]);

            header("Location: ../teacher-edit.php?teacher_id=" . urlencode($teacher_id) . "&updated=1");
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