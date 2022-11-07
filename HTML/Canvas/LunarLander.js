// Lunar Lander JavaScript source code

var canvas = document.getElementById("screen");
var ctx = canvas.getContext("2d");
var countDownSecs = 100

landerRadius = 6;

var x = canvas.clientWidth / 2;
var y = landerRadius;
var dX = 0;
var dY = 0;

const XMIN = landerRadius;
const XMAX = canvas.clientWidth - landerRadius;
const YMIN = landerRadius;
const YMAX = canvas.clientHeight - landerRadius;

draw();
//setInterval(draw, 1000);
setInterval(draw, 15);
//setInterval(draw, 16); // try 60 fps
//setInterval(draw, 30); // try 30 fps

function draw() {
    drawBackground();
    drawLander();
    drawTimer();
    countDownSecs--;

    x += dX;
    if (x > XMAX) {
        x = XMAX;
        dX = 0;
    }
    if (x < XMIN) {
        x = XMIN;
        dX = 0;
    }

    if ((y < YMAX) || (dY < 0)) {
        dY += .01 // this is the 'gravity' factor
//        y += Math.floor(dY);
        y += dY;

        if (y > YMAX) {
            y = YMAX;
            dY = 0;
        }
    }

    if (y < YMIN) {
        y = YMIN;
        dY = 0;
    }
}

function drawBackground() {
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canvas.clientWidth, canvas.clientHeight);
}

function drawLander() {
    ctx.strokeStyle = "white";

    ctx.beginPath();
    ctx.arc(x, y, landerRadius, 0, 2 * Math.PI);
    ctx.stroke();

    // draw the "fire"
//    if (dY < 0) {
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(x, y + (-50 * dY));
        ctx.stroke();
//    }
}

function drawTimer() {
    ctx.font = "12px Courier Bold";
    ctx.fillStyle = "white";
    ctx.fillText("dY: " + dY, 5, 15);
}

document.onkeydown = function (e) {
    switch (e.keyCode) {
        case 37:
//            dX = (dX == 5) ? 0 : -5;
            dX -= .5;
//            alert('left dn');
            break;
        case 38:
//            dY = (dY == 5) ? 0 : -5;
            dY -= .1; // this is the 'thrust' factor
//            alert('up dn');
            break;
        case 39:
//            dX = (dX == -5) ? 0 : 5;
            dX += .5;
//            alert('right dn');
            break;
        case 40:
//            dY = (dY == -5) ? 0 : 5;
//            alert('down dn');
            break;
        case 32:
//            alert('space up');
            break;
    }
};

//document.onkeyup = function (e) {
//    switch (e.keyCode) {
//        case 37:
//            alert('left up');
//            break;
//        case 38:
//            alert('up up');
//            break;
//        case 39:
//            alert('right up');
//            break;
//        case 40:
//            alert('down up');
//            break;
//        case 32:
//            alert('space up');
//            break;
//    }
//};
