<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../../DB_connection.php";
        include_once "../../data/class.php";

        if ($_SERVER['REQUEST_METHOD'] == 'POST') {

            $fname            = isset($_POST['fname']) ? trim($_POST['fname']) : '';
            $lname            = isset($_POST['lname']) ? trim($_POST['lname']) : '';
            $uname            = isset($_POST['Username']) ? trim($_POST['Username']) : '';
            $pass             = isset($_POST['pass']) ? $_POST['pass'] : '';
            $address          = isset($_POST['address']) ? trim($_POST['address']) : '';
            $employee_number  = isset($_POST['employee_number']) ? trim($_POST['employee_number']) : '';
            $phone_number     = isset($_POST['phone_number']) ? trim($_POST['phone_number']) : '';
            $qualification    = isset($_POST['qualification']) ? trim($_POST['qualification']) : '';
            $email_address    = isset($_POST['email_address']) ? trim($_POST['email_address']) : '';
            $gender           = isset($_POST['gender']) ? trim($_POST['gender']) : '';
            $date_of_birth    = isset($_POST['date_of_birth']) ? trim($_POST['date_of_birth']) : '';

            $subject_ids = isset($_POST['subject_id']) ? $_POST['subject_id'] : [];
            $class_ids   = isset($_POST['class_id'])   ? $_POST['class_id']   : [];

            // Process class IDs and extract corresponding grades
            $cleaned_class_ids = [];
            $grade_ids         = [];

            foreach ($class_ids as $c) {
                $c = trim($c);
                if (empty($c)) continue;

                if (strpos($c, '_') !== false) {
                    // "grade_section" format (e.g. "3_2")
                    $parts = explode('_', $c);
                    if (count($parts) == 2) {
                        $grade_ids[] = $parts[0];
                        $stmtClass = $conn->prepare("SELECT class_id FROM class WHERE grade = ? AND section = ? LIMIT 1");
                        $stmtClass->execute([$parts[0], $parts[1]]);
                        $matchedClass = $stmtClass->fetch(PDO::FETCH_ASSOC);
                        if ($matchedClass) {
                            $cleaned_class_ids[] = $matchedClass['class_id'];
                        } else {
                            $cleaned_class_ids[] = $parts[0];
                        }
                    }
                } else {
                    // Direct class_id from class table
                    $cleaned_class_ids[] = $c;
                    $class_info = getClassById($c, $conn);
                    if ($class_info && isset($class_info['grade'])) {
                        $grade_ids[] = $class_info['grade'];
                    }
                }
            }

            // Direct grade_id fallback if provided
            if (empty($grade_ids) && !empty($_POST['grade_id']) && is_array($_POST['grade_id'])) {
                $grade_ids = $_POST['grade_id'];
            }
            if (empty($cleaned_class_ids) && !empty($grade_ids)) {
                $cleaned_class_ids = $grade_ids;
            }

            // Save old input into session for repopulating form on validation error
            $_SESSION['old_input'] = $_POST;

            if (empty($fname)) {
                header("Location: ../teacher-add.php?error=" . urlencode("First name is required"));
                exit;
            } elseif (empty($lname)) {
                header("Location: ../teacher-add.php?error=" . urlencode("Last name is required"));
                exit;
            } elseif (empty($uname)) {
                header("Location: ../teacher-add.php?error=" . urlencode("Username is required"));
                exit;
            } elseif (empty($pass)) {
                header("Location: ../teacher-add.php?error=" . urlencode("Password is required"));
                exit;
            } elseif (empty($address)) {
                header("Location: ../teacher-add.php?error=" . urlencode("Address is required"));
                exit;
            } elseif (empty($employee_number)) {
                header("Location: ../teacher-add.php?error=" . urlencode("Employee number is required"));
                exit;
            } elseif (empty($phone_number)) {
                header("Location: ../teacher-add.php?error=" . urlencode("Phone number is required"));
                exit;
            } elseif (empty($qualification)) {
                header("Location: ../teacher-add.php?error=" . urlencode("Qualification is required"));
                exit;
            } elseif (empty($email_address)) {
                header("Location: ../teacher-add.php?error=" . urlencode("Email address is required"));
                exit;
            } elseif (empty($gender)) {
                header("Location: ../teacher-add.php?error=" . urlencode("Gender is required"));
                exit;
            } elseif (empty($date_of_birth)) {
                header("Location: ../teacher-add.php?error=" . urlencode("Date of birth is required"));
                exit;
            } elseif (empty($subject_ids)) {
                header("Location: ../teacher-add.php?error=" . urlencode("Please select at least one Subject"));
                exit;
            } elseif (empty($cleaned_class_ids)) {
                header("Location: ../teacher-add.php?error=" . urlencode("Please select at least one Class"));
                exit;
            } else {

                $checkSql  = "SELECT * FROM teacher WHERE username = ?";
                $checkStmt = $conn->prepare($checkSql);
                $checkStmt->execute([$uname]);

                if ($checkStmt->rowCount() > 0) {
                    header("Location: ../teacher-add.php?error=" . urlencode("This Username already exists, try another"));
                    exit;
                }

                unset($_SESSION['old_input']);

                $subjets = implode(',', $subject_ids);
                $class   = implode(',', $cleaned_class_ids);
                $gradeId = !empty($grade_ids) ? $grade_ids[0] : 0;
                $hashedPass = password_hash($pass, PASSWORD_DEFAULT);

                $sql  = "INSERT INTO teacher (fname, lname, username, password, 
                                              subjets, gradeId, class, address, 
                                              employee_number, date_of_birth, phone_number, 
                                              qualification, gender, email_address, date_of_joined)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NOW())";
                $stmt = $conn->prepare($sql);
                $stmt->execute([$fname, $lname, $uname, $hashedPass, $subjets, $gradeId, $class,
                                $address, $employee_number, $date_of_birth, $phone_number,
                                $qualification, $gender, $email_address]);

                header("Location: ../teacher.php?added=1");
                exit;
            }

        } else {
            header("Location: ../teacher-add.php");
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