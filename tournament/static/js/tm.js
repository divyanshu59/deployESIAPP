
function myDesc() {
    document.getElementById("aboutC").style.display = "none";
    document.getElementById("rulesC").style.display = "none";
    document.getElementById("prizesC").style.display = "none";
    document.getElementById("scheduleC").style.display = "none";
    document.getElementById("contactC").style.display = "none";
  }
function myFunction() {
    document.getElementById("descC").style.display = "none";
    document.getElementById("aboutC").style.display = "block";
    document.getElementById("rulesC").style.display = "none";
    document.getElementById("prizesC").style.display = "none";
    document.getElementById("scheduleC").style.display = "none";
    document.getElementById("contactC").style.display = "none";
  }
  function myFunction5() {
    document.getElementById("descC").style.display = "block";
    document.getElementById("aboutC").style.display = "none";
    document.getElementById("rulesC").style.display = "none";
    document.getElementById("prizesC").style.display = "none";
    document.getElementById("scheduleC").style.display = "none";
    document.getElementById("contactC").style.display = "none";
  }

function myFunction1() {
    document.getElementById("descC").style.display = "none";
    document.getElementById("aboutC").style.display = "none";
    document.getElementById("rulesC").style.display = "block";
    document.getElementById("prizesC").style.display = "none";
    document.getElementById("scheduleC").style.display = "none";
    document.getElementById("contactC").style.display = "none";
}
  function myFunction2() {
    document.getElementById("descC").style.display = "none";
    document.getElementById("aboutC").style.display = "none";
    document.getElementById("rulesC").style.display = "none";
    document.getElementById("prizesC").style.display = "block";
    document.getElementById("scheduleC").style.display = "none";
    document.getElementById("contactC").style.display = "none";
  }
  function myFunction3() {
    document.getElementById("descC").style.display = "none";
    document.getElementById("aboutC").style.display = "none";
    document.getElementById("rulesC").style.display = "none";
    document.getElementById("prizesC").style.display = "none";
    document.getElementById("scheduleC").style.display = "block";
    document.getElementById("contactC").style.display = "none";
  }
  function myFunction4() {
    document.getElementById("descC").style.display = "none";
    document.getElementById("aboutC").style.display = "none";
    document.getElementById("rulesC").style.display = "none";
    document.getElementById("prizesC").style.display = "none";
    document.getElementById("scheduleC").style.display = "none";
    document.getElementById("contactC").style.display = "block";
  }



  //formShow
  var toggle=0;
    function showForm(){
        if(toggle == 0)
        {
            console.log(toggle);
            document.getElementById("formData").style.display = "block";
            console.log(toggle);
            toggle++;
        }
        else
        {
            console.log(toggle);
            toggle--;
            document.getElementById("formData").style.display = "none";
        }
    }

    