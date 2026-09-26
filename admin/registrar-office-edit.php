<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../DB_connection.php";
        include "../data/registrar_office.php";

        // List page (registrar-Office.php) e r_user_id parameter mokle che
        $r_user_id = $_GET['r_user_id'] ?? '';
        $ruser     = getR_usersById($r_user_id, $conn);

        if ($ruser == 0) {
            header("Location: registrar-office.php");
            exit;
        }

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Edit Registrar Office User</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
        .form-w { border-radius: 16px; }
        .form-w .form-label { font-weight: 500; color: #333; margin-bottom: 8px; }
        .form-w .form-control {
            background-color: #EAF1FE;
            border: 1px solid #EAF1FE;
            border-radius: 10px;
            padding: 12px 16px;
            font-size: 15px;
        }
        .form-w .form-control:focus {
            background-color: #fff;
            border-color: #86b7fe;
            box-shadow: 0 0 0 0.2rem rgba(13,110,253,.15);
        }
        .form-w .input-group .form-control {
            border-top-right-radius: 0;
            border-bottom-right-radius: 0;
        }
        .form-w .input-group .btn {
            border-top-left-radius: 0;
            border-bottom-left-radius: 0;
        }
    </style>
</head>
<body>
    <?php include "../inc/navbar.php"; ?>

    <div class="container mt-5">
        <a href="registrar-office.php" class="btn btn-dark">Go Back</a>

        <!-- Main Details Form -->
        <form method="post"
              class="shadow p-3 mt-5 form-w"
              action="req/registrar-office-edit.php">

            <input type="hidden" name="r_user_id" value="<?= htmlspecialchars($ruser['r_user_id']) ?>">

            <h3>Edit Registrar Office User</h3><hr>
            <?php if (isset($_GET['updated'])) { ?>
            <div class="alert alert-success" role="alert">
                Successfully updated!
            </div>
            <?php } ?>
            <?php if (isset($_GET['error'])) { ?>
            <div class="alert alert-danger" role="alert">
                <?= htmlspecialchars($_GET['error']) ?>
            </div>
            <?php } ?>

            <div class="mb-3">
                <label class="form-label">First name</label>
                <input type="text" class="form-control" name="fname" required
                       value="<?= htmlspecialchars($ruser['fname'] ?? '') ?>">
            </div>
            <div class="mb-3">
                <label class="form-label">Last name</label>
                <input type="text" class="form-control" name="lname" required
                       value="<?= htmlspecialchars($ruser['lname'] ?? '') ?>">
            </div>
            <div class="mb-3">
                <label class="form-label">Username</label>
                <input type="text" class="form-control" name="Username" required
                       value="<?= htmlspecialchars($ruser['username'] ?? '') ?>">
            </div>
            <div class="mb-3">
                <label class="form-label">Address</label>
                <input type="text" class="form-control" name="address" required
                       value="<?= htmlspecialchars($ruser['address'] ?? '') ?>">
            </div>
            <div class="mb-3">
                <label class="form-label">Employee Number</label>
                <input type="text" class="form-control" name="employee_number" required
                       value="<?= htmlspecialchars($ruser['employee_number'] ?? '') ?>">
            </div>
            <div class="mb-3">
                <label class="form-label">Date Of Birth</label>
                <input type="date" class="form-control" name="date_of_birth" required
                       value="<?= htmlspecialchars($ruser['date_of_birth'] ?? '') ?>">
            </div>
            <div class="mb-3">
                <label class="form-label">Phone Number</label>
                <input type="text" class="form-control" name="phone_number" required
                       pattern="[0-9]{10}" title="Enter a valid 10-digit phone number"
                       value="<?= htmlspecialchars($ruser['phone_number'] ?? '') ?>">
            </div>
            <div class="mb-3">
                <label class="form-label">Qualification</label>
                <input type="text" class="form-control" name="qualification" required
                       value="<?= htmlspecialchars($ruser['qualification'] ?? '') ?>">
            </div>
            <div class="mb-3">
                <label class="form-label">Email Address</label>
                <input type="email" class="form-control" name="email_address" required
                       value="<?= htmlspecialchars($ruser['email_address'] ?? '') ?>">
            </div>
            <div class="mb-3">
                <label class="form-label">Gender</label><br>
                <input type="radio" value="Male" name="gender"
                       <?= (($ruser['gender'] ?? '') == 'Male') ? 'checked' : '' ?>> Male
                &nbsp; &nbsp; &nbsp; &nbsp;
                <input type="radio" value="Female" name="gender"
                       <?= (($ruser['gender'] ?? '') == 'Female') ? 'checked' : '' ?>> Female
            </div>

            <button type="submit" class="btn btn-primary">Update</button>

        </form>

        <!-- Separate Change Password Form -->
        <form method="post"
              class="shadow p-3 my-4 form-w"
              action="req/registrar-office-change.php">

            <input type="hidden" name="r_user_id" value="<?= htmlspecialchars($ruser['r_user_id']) ?>">

            <h3>Change Password</h3><hr>
            <?php if (isset($_GET['pupdated'])) { ?>
            <div class="alert alert-success" role="alert">
                Password successfully changed!
            </div>
            <?php } ?>
            <?php if (isset($_GET['perror'])) { ?>
            <div class="alert alert-danger" role="alert">
                <?= htmlspecialchars($_GET['perror']) ?>
            </div>
            <?php } ?>
            <div class="mb-3">
                <label class="form-label">Admin password</label>
                <input type="password" class="form-control" name="admin_pass2">
            </div>
            <div class="mb-3">
                <label class="form-label">New password</label>
                <div class="input-group mb-3">
                    <input type="text" class="form-control" name="new_pass" id="passInput">
                    <button class="btn btn-secondary" type="button" id="gBtn">Random</button>
                </div>
            </div>
            <div class="mb-3">
                <label class="form-label">Confirm new password</label>
                <input type="text" class="form-control" name="c_new_pass2" id="passInput2">
            </div>
            <button type="submit" class="btn btn-primary">Change</button>

        </form>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        $(document).ready(function(){
            $("#navlinks li:nth-child(7) a").addClass('active');
        });
        function makePass(length) {
            var result = '';
            var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
            for (var i = 0; i < length; i++) {
                result += characters.charAt(Math.floor(Math.random() * characters.length));
            }
            document.getElementById('passInput').value = result;
            document.getElementById('passInput2').value = result;
        }
        document.getElementById('gBtn').addEventListener('click', function(e){
            e.preventDefault();
            makePass(5);
        });
    </script>
</body>
</html>
<?php
    } else {
        header("Location: ../login.php");
        exit;
    }
} else {
    header("Location: ../login.php");
    exit;
}
?>