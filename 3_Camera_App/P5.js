// ----- P5.js -----
let cnv;
let primaryColor;
let capture;
let cameraStarted = false;
let startstopBtn;
let bg_img;

function setup() {
    cnv = createCanvas(windowWidth * 0.8, windowHeight * 0.8);

    // bg-img
    bg_img=loadImage('Images/camera.png');

    // button
    buttonFn();
}

// ----- center canvas -----
function centerCanvas() {
    let x = (windowWidth - width) / 2;
    let y = (windowHeight - height) / 2;
    cnv.position(x, y);
}

// ----- style canvas -----
function styleCanvas() {
    cnv.style('border', '3px solid #FF4655');
    cnv.style('border-radius', '5px');
}

// ----- start camera -----
function buttonFn() {
    startstopBtn = createButton('Start Camera');
    
    // CSS styles
    startstopBtn.style('all', 'unset')
    startstopBtn.style('background', '#FF4655')
    startstopBtn.style('color', 'white');
    startstopBtn.style('width', '140px');
    startstopBtn.style('height', '40px');
    startstopBtn.style('text-align', 'center');
    startstopBtn.style('text-decoration', 'none');
    startstopBtn.style('display', 'inline-block');
    startstopBtn.style('font-size', '17px');
    startstopBtn.style('cursor', 'pointer');
    startstopBtn.style('border-radius', '5px');


    // Center the button 
    let buttonX = (windowWidth - startstopBtn.width) / 2;
    let buttonY = (windowHeight - startstopBtn.height) / 2 + windowHeight * 0.35;
    startstopBtn.position(buttonX, buttonY);

    startstopBtn.mousePressed(startStopCamera);
}

function startStopCamera() {
    if (!cameraStarted) {
        startCamera();
        startstopBtn.html('Stop Camera');
    } else {
        if (capture) {
            capture.stop();
            capture.remove(); 
            capture = null;   
        }
        cameraStarted = false;
        startstopBtn.html('Start Camera');
    }
}

function startCamera() {
    if (!cameraStarted) {
        capture = createCapture(VIDEO);
        capture.size(windowWidth * 0.8, windowHeight * 0.8);
        capture.hide();
        cameraStarted = true;
    } else {
        capture.stop();
        cameraStarted = false;
    }
}

// ----- draw -----
function draw() {
    background(255);
    centerCanvas();
    styleCanvas();

    // fix img
    let imgWidth, imgHeight;
    let sizeFactor = 0.6;
    if (!cameraStarted) {
        if (bg_img.width > bg_img.height) {
            imgWidth = width * sizeFactor;
            imgHeight = bg_img.height * (imgWidth / bg_img.width);
        } else {
            imgHeight = height * sizeFactor;
            imgWidth = bg_img.width * (imgHeight / bg_img.height);
        }

        let imgX = (width - imgWidth) / 2;
        let imgY = (height - imgHeight) / 2;

        image(bg_img, imgX, imgY, imgWidth, imgHeight);

        let transparency = 0.7;
        tint(255, 255 * (1 - transparency));
    }

    // camera
    if (capture) {
        tint(255, 255);
        image(capture, 0, 0, width, height);
    }
}
