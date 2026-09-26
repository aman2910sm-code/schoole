<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../DB_connection.php";
        include "../data/subject.php";
        include "../data/class.php";

        $allSubjects = getALLSubjects($conn);
        $classes     = getALLClasses($conn);

        // Retrieve repopulation data if previous submission failed
        $old = isset($_SESSION['old_input']) ? $_SESSION['old_input'] : [];
        unset($_SESSION['old_input']);

        function old_val($old, $key) {
            return isset($old[$key]) ? htmlspecialchars($old[$key]) : '';
        }

        $old_subjects = isset($old['subject_id']) && is_array($old['subject_id']) ? $old['subject_id'] : [];
        $old_classes  = isset($old['class_id']) && is_array($old['class_id']) ? $old['class_id'] : [];

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Add Teacher</title>
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
        <a href="teacher.php" class="btn btn-dark">Go Back</a>

        <form method="post"
              class="shadow p-3 mt-5 form-w"
              action="req/teacher-add.php">

            <h3>Add New Teacher</h3><hr>
            <?php if (isset($_GET['error'])) { ?>
            <div class="alert alert-danger" role="alert">
                <?= htmlspecialchars($_GET['error']) ?>
            </div>
            <?php } ?>
            <?php if (isset($_GET['success'])) { ?>
            <div class="alert alert-success" role="alert">
                <?= htmlspecialchars($_GET['success']) ?>
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
                            id="gBtn">Random</button>
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
                       name="phone_number" required>
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
                       <?= (!isset($old['gender']) || $old['gender'] == 'Male') ? 'checked' : '' ?>
                       name="gender"> Male
                &nbsp; &nbsp; &nbsp; &nbsp;
                <input type="radio"
                       value="Female"
                       <?= (isset($old['gender']) && $old['gender'] == 'Female') ? 'checked' : '' ?>
                       name="gender"> Female
            </div>
            <div class="mb-3">
                <label class="form-label">Date Of Birth</label>
                <input type="date"
                       class="form-control"
                       value="<?= old_val($old, 'date_of_birth') ?>"
                       name="date_of_birth" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Subject</label>
                <div class="d-flex flex-wrap gap-3">
                    <?php if (!empty($allSubjects) && $allSubjects != 0) { foreach ($allSubjects as $sub) { ?>
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" name="subject_id[]"
                               value="<?= $sub['subject_id'] ?>" id="subject_<?= $sub['subject_id'] ?>"
                               <?= in_array($sub['subject_id'], $old_subjects) ? 'checked' : '' ?>>
                        <label class="form-check-label" for="subject_<?= $sub['subject_id'] ?>">
                            <?= htmlspecialchars($sub['subject']) ?>
                        </label>
                    </div>
                    <?php } } else { ?>
                        <span class="text-muted">No subjects found</span>
                    <?php } ?>
                </div>
            </div>
            <div class="mb-3">
                <label class="form-label">Class</label>
                <div class="d-flex flex-wrap gap-3">
                    <?php if (!empty($classes) && $classes != 0) { foreach ($classes as $c) { ?>
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" name="class_id[]"
                               value="<?= $c['class_id'] ?>" id="class_<?= $c['class_id'] ?>"
                               <?= in_array($c['class_id'], $old_classes) ? 'checked' : '' ?>>
                        <label class="form-check-label" for="class_<?= $c['class_id'] ?>">
                            <?= htmlspecialchars($c['grade_code'] . '-' . $c['grade_num'] . ' (' . $c['section_name'] . ')') ?>
                        </label>
                    </div>
                    <?php } } else { ?>
                        <span class="text-muted">No classes found. <a href="class-add.php">Add class</a></span>
                    <?php } ?>
                </div>
            </div>

            <button type="submit" class="btn btn-primary">Add</button>
        </form>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        $(document).ready(function(){
            $("#navlinks li:nth-child(2) a").addClass('active');
        });

        function makePass(length) {
            var result = '';
            var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
            for (var i = 0; i < length; i++) {
                result += characters.charAt(Math.floor(Math.random() * characters.length));
            }
            document.getElementById('passInput').value = result;
        }

        var gBtn = document.getElementById('gBtn');
        if (gBtn) {
            gBtn.addEventListener('click', function(e){
                e.preventDefault();
                makePass(5);
            });
        }
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