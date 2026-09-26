<?php
session_start();
if (isset($_SESSION['r_user_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Registrar Office') {

        include "../DB_connection.php";
        include "../data/grade.php";
        include "../data/section.php";

        $allgrades   = getALLGrades($conn);
        $allsections = getALLSections($conn);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registrar Office - Add Student</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
    <?php include "../inc/navbar.php"; ?>

    <div class="container mt-5">
        <a href="index.php" class="btn btn-dark">Go Back</a>

        <form method="post"
              class="shadow p-3 mt-5 form-w"
              action="req/student-add.php">

            <h3>Add New Student</h3><hr>
           <?php if (isset($_GET['success'])) { ?>
            <div class="alert alert-success" role="alert">
                <?= htmlspecialchars($_GET['success']) ?>
            </div>
            <?php } ?>
           <?php if (isset($_GET['error'])) { ?>
            <div class="alert alert-danger" role="alert">
                <?= htmlspecialchars($_GET['error']) ?>
            </div>
            <?php } ?>
  <div class="mb-3">
    <label class="form-label">First name</label>
    <input type="text"
    class="form-control"
    name="fname">
  </div>
  <div class="mb-3">
    <label class="form-label">Last name</label>
    <input type="text"
    class="form-control"
    name="lname">
  </div>
  <div class="mb-3">
    <label class="form-label">Address</label>
    <input type="text"
    class="form-control"
    name="address">
  </div>
   <div class="mb-3">
    <label class="form-label">Email address</label>
    <input type="text"
    class="form-control"
    name="email_address">
  </div>
 
 
 
  <div class="mb-3">
    <label class="form-label">Date of birth</label>
    <input type="date"
    class="form-control"
    name="date_of_birth">
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

  </div> <br><hr>
  <div class="mb-3">
    <label class="form-label">Username</label>
    <input type="text"
    class="form-control"
    name="username">
  </div>
  <div class="mb-3">
    <label class="form-label">Password</label>
    <div class="input-group">
        <input type="text"
    class="form-control"
    name="pass"
    id="passInput">
    <button class="btn btn-secondary"
            type="button"
            id="gBtn">
            Random</button>
    </div>
  </div><br><hr>
  <div class="mb-3">
  <label class="form-label">Parent first name</label>
    <input type="text"
    class="form-control"
    name="parent_fname">
  </div>
  <div class="mb-3">
  <label class="form-label">Parent last name</label>
    <input type="text"
    class="form-control"
    name="parent_lname">
  </div>
  <div class="mb-3">
  <label class="form-label">Parent phone number</label>
    <input type="text"
    class="form-control"
    name="parent_phone_number">
  </div><br><hr>
  <div class="mb-3">
    <label class="form-label">Grade</label>
    <div class="d-flex flex-wrap gap-3">
        <?php foreach ($allgrades as $grd) { ?>
        <div class="form-check">
            <input class="form-check-input"
                   type="radio"
                   name="grade_id"
                   value="<?= $grd['grade_id'] ?>"
                   id="grade_<?= $grd['grade_id'] ?>">
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
            <input class="form-check-input"
                   type="radio"
                   name="section_id"
                   value="<?= $sec['section_id'] ?>"
                   id="section_<?= $sec['section_id'] ?>">
            <label class="form-check-label" for="section_<?= $sec['section_id'] ?>">
                <?= htmlspecialchars($sec['section']) ?>
            </label>
        </div>
        <?php } } ?>
    </div>
  </div>

    <button type="submit" class="btn btn-primary">Register</button>

</form>

</div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        $(document).ready(function(){
            $("#navlinks li:nth-child(3) a").addClass('active');
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