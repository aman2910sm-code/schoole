<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {

    if ($_SESSION['role'] == 'Admin') {

        if (isset($_POST['school_name']) &&
            isset($_POST['slogan']) &&
            isset($_POST['about']) &&
            isset($_POST['current_year']) &&
            isset($_POST['current_semester'])) {

            include "../../DB_connection.php";

            $school_name      = trim($_POST['school_name']);
            $slogan           = trim($_POST['slogan']);
            $about            = trim($_POST['about']);
            $current_year     = trim($_POST['current_year']);
            $current_semester = trim($_POST['current_semester']);

            if (empty($school_name)) {
                $em = "School name is required";
                header("Location: ../settings.php?error=" . urlencode($em));
                exit;
            } elseif (empty($slogan)) {
                $em = "Slogan is required";
                header("Location: ../settings.php?error=" . urlencode($em));
                exit;
            } elseif (empty($about)) {
                $em = "About is required";
                header("Location: ../settings.php?error=" . urlencode($em));
                exit;
            } elseif (empty($current_year)) {
                $em = "Current year is required";
                header("Location: ../settings.php?error=" . urlencode($em));
                exit;
            } elseif (empty($current_semester)) {
                $em = "Current semester is required";
                header("Location: ../settings.php?error=" . urlencode($em));
                exit;
            } else {
                $sql  = "UPDATE setting
                         SET school_name = ?, slogan = ?, about = ?,
                             current_year = ?, current_semester = ?";
                $stmt = $conn->prepare($sql);
                $stmt->execute([$school_name, $slogan, $about, $current_year, $current_semester]);

                $sm = "Successfully updated!";
                header("Location: ../settings.php?success=" . urlencode($sm));
                exit;
            }
        } else {
            header("Location: ../settings.php");
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