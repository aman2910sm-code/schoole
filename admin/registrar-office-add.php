<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../DB_connection.php";

        // Jo pachla submit ma validation error aavyu hoy, to user e bharel
        // data session ma pade hase - e ahi le lo ane session mathi hatavi do.
        $old = isset($_SESSION['old_input']) ? $_SESSION['old_input'] : [];
        unset($_SESSION['old_input']);

        // Text field ni value pacha bharva mate helper
        function old_val($old, $key) {
            return isset($old[$key]) ? htmlspecialchars($old[$key]) : '';
        }

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registrar Office - Add User</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
        .form-w {
            border-radius: 16px;
        }
        .form-w .form-label {
            font-weight: 500;
            color: #333;
            margin-bottom: 8px;
        }
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

        <form method="post"
              class="shadow p-3 mt-5 form-w"
              action="req/registrar-office-add.php">

            <h3>Add New Registrar Office User</h3><hr>
           <?php if (isset($_GET['error'])) { ?>
            <div class="alert alert-danger" role="alert">
                <?=$_GET['error']?>
</div>
<?php } ?>
  <div class="mb-3">
    <label class="form-label">First name</label>
    <input type="text"
    class="form-control"
    value="<?= old_val($old, 'fname') ?>"
    name="fname" required>
  </div>
  <div class="mb-3">
    <label class="form-label">Last name</label>
    <input type="text"
    class="form-control"
    value="<?= old_val($old, 'lname') ?>"
    name="lname" required>
  </div>
  <div class="mb-3">
    <label class="form-label">Username</label>
    <input type="text"
    class="form-control"
    value="<?= old_val($old, 'Username') ?>"
    name="Username" required>
  </div>
  <div class="mb-3">
    <label class="form-label">Password</label>
    <div class="input-group mb-3">
        <input type="text"
    class="form-control"
    value="<?= old_val($old, 'pass') ?>"
    name="pass"
    id="passInput" required>
    <button class="btn btn-secondary"
            type="button"
            id="gBtn">
            Random</button>
  </div>
</div>
<div class="mb-3">
    <label class="form-label">Address</label>
    <input type="text"
    class="form-control"
    value="<?= old_val($old, 'address') ?>"
    name="address" required>
  </div>
  <div class="mb-3">
    <label class="form-label">Employee Number</label>
    <input type="text"
    class="form-control"
    value="<?= old_val($old, 'employee_number') ?>"
    name="employee_number" required>
  </div>
   <div class="mb-3">
    <label class="form-label">Phone Number</label>
    <input type="text"
    class="form-control"
    value="<?= old_val($old, 'phone_number') ?>"
    name="phone_number" required pattern="[0-9]{10}" title="Enter a valid 10-digit phone number">
  </div>
  <div class="mb-3">
    <label class="form-label">Qualification</label>
    <input type="text"
    class="form-control"
    value="<?= old_val($old, 'qualification') ?>"
    name="qualification" required>
  </div>
   <div class="mb-3">
    <label class="form-label">Email Address</label>
    <input type="email"
    class="form-control"
    value="<?= old_val($old, 'email_address') ?>"
    name="email_address" required>
  </div>
   <div class="mb-3">
    <label class="form-label">Gender</label><br>
    <input type="radio"
    value="Male"
    <?= (!isset($old['gender']) || $old['gender'] == 'Male') ? 'Checked' : '' ?>
    name="gender"> Male
     &nbsp; &nbsp; &nbsp;    &nbsp;
    <input type="radio"
    value="Female"
    <?= (isset($old['gender']) && $old['gender'] == 'Female') ? 'Checked' : '' ?>
    name="gender"> Female
  </div>
   <div class="mb-3">
    <label class="form-label">Date Of Birth</label>
    <input type="date"
    class="form-control"
    value="<?= old_val($old, 'date_of_birth') ?>"
    name="date_of_birth" required>
  </div>

    <button type="submit" class="btn btn-primary">Add</button>

</form>

</div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        $(document).ready(function(){
            $("#navlinks li:nth-child(7) a").addClass('active');
        });
    function makePass(length) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    var passInput = document.getElementById('passInput');
    passInput.value = result;
    return result;
}

    var gBtn = document.getElementById('gBtn');
    gBtn.addEventListener('click', function(e){
      e.preventDefault();
      makePass(5);
    });

    // Har field mate custom "required" message set karvu
    var customMessages = {
        fname: "First name is required",
        lname: "Last name is required",
        Username: "Username is required",
        pass: "Password is required",
        address: "Address is required",
        employee_number: "Employee number is required",
        phone_number: "Phone number is required",
        qualification: "Qualification is required",
        email_address: "Email address is required",
        date_of_birth: "Date of birth is required"
    };

    Object.keys(customMessages).forEach(function(name){
        var field = document.getElementsByName(name)[0];
        if (!field) return;
        field.addEventListener('invalid', function(){
            if (field.validity.valueMissing) {
                field.setCustomValidity(customMessages[name]);
            } else if (field.validity.patternMismatch) {
                // pattern na potanu title attribute vaparse
                field.setCustomValidity('');
            } else {
                field.setCustomValidity('');
            }
        });
        field.addEventListener('input', function(){
            field.setCustomValidity('');
        });
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