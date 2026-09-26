<?php
session_start();

if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../DB_connection.php";
        include "../data/student.php";
        include "../data/grade.php";
        include "../data/section.php";

        if (!isset($_GET['student_id']) || empty($_GET['student_id'])) {
            header("Location: student.php");
            exit;
        }

        $student_id = $_GET['student_id'];
        $student    = getStudentById($student_id, $conn);

        if ($student == 0) {
            header("Location: student.php");
            exit;
        }

        $allgrades   = getALLGrades($conn);
        $allsections = getALLSections($conn);

        $selectedGrade   = !empty($student['grade'])   ? $student['grade']   : '';
        $selectedSection = !empty($student['section']) ? $student['section'] : '';
        $selectedGender  = !empty($student['gender'])  ? $student['gender']  : '';

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Edit Student</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
    <?php include "../inc/navbar.php"; ?>

    <div class="container mt-5">
        <a href="student.php" class="btn btn-dark">Go Back</a>

        <!-- Main Details Form -->
        <form method="post"
              class="shadow p-3 mt-5 form-w"
              action="req/student-edit.php">

            <input type="hidden" name="student_id" value="<?= $student['student_id'] ?>">

            <h3>Edit Student Info</h3><hr>
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
    <input type="text" class="form-control" name="fname" value="<?= htmlspecialchars($student['fname']) ?>">
  </div>
  <div class="mb-3">
    <label class="form-label">Last name</label>
    <input type="text" class="form-control" name="lname" value="<?= htmlspecialchars($student['lname']) ?>">
  </div>
  <div class="mb-3">
    <label class="form-label">Address</label>
    <input type="text" class="form-control" name="address" value="<?= htmlspecialchars($student['address'] ?? '') ?>">
  </div>
  <div class="mb-3">
    <label class="form-label">Email address</label>
    <input type="email" class="form-control" name="email_address" value="<?= htmlspecialchars($student['email_address'] ?? '') ?>">
  </div>
  <div class="mb-3">
    <label class="form-label">Date of birth</label>
    <input type="date" class="form-control" name="date_of_birth" value="<?= htmlspecialchars($student['date_of_birth'] ?? '') ?>">
  </div>
  <div class="mb-3">
    <label class="form-label">Gender</label>
    <div class="d-flex flex-wrap gap-3">
        <div class="form-check">
            <input class="form-check-input" type="radio" name="gender" value="Male" id="gender_male"
                   <?= ($selectedGender == 'Male') ? 'checked' : '' ?>>
            <label class="form-check-label" for="gender_male">Male</label>
        </div>
        <div class="form-check">
            <input class="form-check-input" type="radio" name="gender" value="Female" id="gender_female"
                   <?= ($selectedGender == 'Female') ? 'checked' : '' ?>>
            <label class="form-check-label" for="gender_female">Female</label>
        </div>
    </div>
  </div>
  <div class="mb-3">
    <label class="form-label">Username</label>
    <input type="text" class="form-control" name="Username" value="<?= htmlspecialchars($student['username']) ?>">
  </div>
  <div class="mb-3">
    <label class="form-label">Grade</label>
    <div class="d-flex flex-wrap gap-3">
        <?php foreach ($allgrades as $grd) { ?>
        <div class="form-check">
            <input class="form-check-input" type="radio" name="grade_id"
                   value="<?= $grd['grade_id'] ?>" id="grade_<?= $grd['grade_id'] ?>"
                   <?= ($grd['grade_id'] == $selectedGrade) ? 'checked' : '' ?>>
            <label class="form-check-label" for="grade_<?= $grd['grade_id'] ?>">
                <?= $grd['grade_code'] ?>-<?= $grd['grade'] ?>
            </label>
        </div>
        <?php } ?>
    </div>
  </div>
  <div class="mb-3">
    <label class="form-label">Section</label>
    <div class="d-flex flex-wrap gap-3">
        <?php if ($allsections != 0) { foreach ($allsections as $sec) { ?>
        <div class="form-check">
            <input class="form-check-input" type="radio" name="section_id"
                   value="<?= $sec['section_id'] ?>" id="section_<?= $sec['section_id'] ?>"
                   <?= ($sec['section_id'] == $selectedSection) ? 'checked' : '' ?>>
            <label class="form-check-label" for="section_<?= $sec['section_id'] ?>"><?= $sec['section'] ?></label>
        </div>
        <?php } } ?>
    </div>
  </div>
  <div class="mb-3">
    <label class="form-label">Parent first name</label>
    <input type="text" class="form-control" name="parent_fname" value="<?= htmlspecialchars($student['parent_fname'] ?? '') ?>">
  </div>
  <div class="mb-3">
    <label class="form-label">Parent last name</label>
    <input type="text" class="form-control" name="parent_lname" value="<?= htmlspecialchars($student['parent_lname'] ?? '') ?>">
  </div>
  <div class="mb-3">
    <label class="form-label">Parent phone number</label>
    <input type="text" class="form-control" name="parent_phone_number" value="<?= htmlspecialchars($student['parent_phone_number'] ?? '') ?>">
  </div>

    <button type="submit" class="btn btn-primary">Update</button>

</form>

        <!-- Separate Change Password Form -->
        <form method="post"
              class="shadow p-3 my-4 form-w"
              action="req/student-change.php">

            <input type="hidden" name="student_id" value="<?= $student['student_id'] ?>">

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
                <div class="mb-3">
                <label class="form-label">Admin password</label>
                    <input type="password" class="form-control" name="admin_pass2">
            </div>
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
            $("#navlinks li:nth-child(3) a").addClass('active');
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