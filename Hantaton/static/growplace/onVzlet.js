var clicks = 0;
var checkbox1 = 0;
var checkbox2 = 0;
var checkbox3 = 0;
var checkbox4 = 0;

var checkbox = document.getElementById("checkbox");
var isChecked = checkbox.getAttribute("checked");

    function countClicks() {
        if(clicks!=80) {
            clicks += 25;
        document.getElementById("health").innerHTML = clicks;
        document.getElementById("health2").style.width=clicks+"%";
       let image = document.getElementById("zamok");
 image.style.transform = "rotate(5deg)";
  setTimeout(() => {
    image.style.transform = "rotate(0deg)";
  }, 50);
            
        }
        else {
             image.style.transform = "rotate(180deg)";
        }
    }



function checkCheckbox1() {
    const checkbox = document.getElementById('check1');
    if (document.getElementById('check1').checked ) {
        if(checkbox1==0)
            {
                checkbox1 = 1;
                countClicks();
            }
        
    } else {
      alert('Вы еще не прошли курс :(');
    }
  }
function checkCheckbox2() {
    const checkbox = document.getElementById('check2');
    if (document.getElementById('check2').checked ) {
        
                checkbox2 = 1;
                countClicks();
            
        
    } else {
      alert('Вы еще не прошли курс :(');
    }
  }
function checkCheckbox3() {
    const checkbox = document.getElementById('check3');
    if (document.getElementById('check3').checked ) {
        if(checkbox3==0)
            {
                checkbox3 = 1;
                countClicks();
            }
        
    } else {
      alert('Вы еще не прошли курс :(');
    }
  }
function checkCheckbox4() {
    const checkbox = document.getElementById('check4');
    if (document.getElementById('check4').checked ) {
       
        if(checkbox4==0)
            {
                checkbox4 = 1;
                countClicks();
            }
        
        
    } else {
      alert('Вы еще не прошли курс :(');
    }
  }