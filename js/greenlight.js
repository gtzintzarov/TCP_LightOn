




$(document).ready(function () {
    
    // red light click listener
    $("#red-light").on("click", function () {
        turnOffYellow();
        turnOffGreen();
        
        if ($(this).hasClass("red-on")) {
            turnOffRed();
        } else {
            turnOnRed();
        }
    });
    
    // yellow light click listener
    $("#yellow-light").on("click", function () {  
        turnOffRed();
        turnOffGreen();
           
        if ($(this).hasClass("yellow-on")) {
            turnOffYellow();
        } else {
            turnOnYellow();
        }
    });
    
    // green light click listener
    $("#green-light").on("click", function () {       
        turnOffRed();
        turnOffYellow();
               
        if ($(this).hasClass("green-on")) {
            turnOffGreen();
        } else {
            turnOnGreen();
        }
    });
    
    

    var turnOnRed = function () {
        $("#red-light").addClass("red-on");
        $("#red-light").removeClass("red-off");
        
        $.ajax({
            url: "/RedOn_client.py",
            success: function(response) {
                console.log(response);   
            },
            error: function(response) {
                alert("Error: " + response);
            }
        });
    };
    
    var turnOffRed = function () {
        $("#red-light").removeClass("red-on red-off");
        $("#red-light").addClass("red-off");
    };
    
    var turnOnYellow = function () {
        $("#yellow-light").addClass("yellow-on");
        $("#yellow-light").removeClass("yellow-off");
    };
    
    var turnOffYellow = function () {
        $("#yellow-light").removeClass("yellow-on yellow-off");
        $("#yellow-light").addClass("yellow-off");
    };
    
    var turnOnGreen = function () {
        $("#green-light").addClass("green-on");
        $("#green-light").removeClass("green-off");
        
        $.ajax({
            url: "GreenOn_client.py",
            success: function(response) {
                console.log(response);   
            },
            error: function(response) {
                alert("Error: " + response);
            }
        });
    };
    
    var turnOffGreen = function () {
        $("#green-light").removeClass("green-on green-off");
        $("#green-light").addClass("green-off");
        
        $.ajax({
            url: "GreenOff_client.py",
            success: function(response) {
                console.log(response);   
            },
            error: function(response) {
                alert("Error: " + response);
            }
        });
    };

    
});
