
const screenCanvas = document.getElementById('screenCanvas');
screenCanvas.width = innerWidth / 3;
screenCanvas.height = innerHeight / 5;
screenCanvas.addEventListener("click", onClick);
const ctx = screenCanvas.getContext("2d");

let haveFullScreen = false;
let clickCounter = 0;

drawIntro();

function drawIntro() {
    drawBackground();
    drawInstructions();
    drawDebugText();
}

function drawBackground() {
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, screenCanvas.clientWidth, screenCanvas.clientHeight);
}

function drawInstructions() {
    ctx.fillStyle = "white";
    ctx.textAlign = "center";
    const againText = clickCounter > 0 ? "again " : "";

    if (screenCanvas.clientHeight < screen.height) {
        ctx.fillText("Click " + againText + "to try to get full screen", screenCanvas.clientWidth / 2, screenCanvas.clientHeight / 2);
    }
    else {
        haveFullScreen = true;
        ctx.fillText("100% full screen achieved.  Click to play", screenCanvas.clientWidth / 2, screenCanvas.clientHeight / 2);
    }
}

function drawDebugText() {
    ctx.fillText(
        clickCounter + " clicks. Resolution: " + screenCanvas.clientWidth + "/" + screen.width + " x " + screenCanvas.clientHeight + "/" + screen.height,
        screenCanvas.clientWidth / 2,
        (screenCanvas.clientHeight / 2) + 12
    );
}

function startGame() {
    draw();
}

function draw() {
    drawBackground();
    drawTerrain();
    drawLander();
}

function drawTerrain() {
}

function drawLander() {
}

////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////

function onClick() {
    ++clickCounter;
    if (!haveFullScreen) {
        screenCanvas.webkitRequestFullScreen();
        screenCanvas.width = innerWidth;
        screenCanvas.height = innerHeight;
        drawIntro();
    } else {
        screenCanvas.removeEventListener("click", onClick)
        startGame();
    }
}
