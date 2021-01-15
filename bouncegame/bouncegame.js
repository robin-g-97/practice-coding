var obstacles = [];
var diam = 15;
var bouncemult = 1.1;
var maxspeed = 25;
var obstacleamount = 3; //document.getElementById("Enemynumber").value;
var prevmouseX;
var trailstep = 1.5;
var points = 0;
var winpoints = 500;
var bRed, bGreen, bBlue, backgroundColorinit;
var canvasWidth = window.innerWidth;
var canvasHeight = window.innerHeight/1.5;
var prevcanvasWidth, prevcanvasHeight;
var level = 1;

// main code
function setup() {
    createCanvas(canvasWidth, canvasWidth / 3);
    frameRate(30);
    enemyGenerate(obstacleamount);
    bRed = bGreen = bBlue = backgroundColorinit = 200;
}

function draw() {
	printPoints(points);
	canvasCreation();
//	diam = 15 * document.getElementById("Ballscale").value;
	backgroundDarken(bRed, bGreen, bBlue);

	// Canvas code
	if (prevcanvasWidth != canvasWidth || prevcanvasHeight != canvasHeight) {
		createCanvas(canvasWidth, canvasHeight);
		for (var j = 0; j < obstacles.length; j++) {
			obstacles[j].relative();
		}
		return;
	};


/*
	// Enemy amount code when the amount of enemies is changed
	if(obstacleamount != document.getElementById("Enemynumber").value){
		obstacleamount = document.getElementById("Enemynumber").value;
		enemyGenerate(obstacleamount);
		return;
	}
*/
	//Playing
	if(points < winpoints){
		if((0 < mouseX) && (mouseX < width) && (0 < mouseY) && (mouseY < height)){
			for (var j = 0; j < obstacles.length; j++) {
				if(mouseX !=prevmouseX){
					obstacles[j].move();
					points += 1;
				}
				obstacles[j].display();
				intersect(mouseX, mouseY, obstacles[j].x, obstacles[j].y, diam);
			}
			prevmouseX = mouseX;
		}
	}
	// Wincondition
	levelIncrement();
}


//-------------------------------------------------------------------------
// obstacle object
function obstacle() {
	this.x = random(0, width);
	this.y = random(0, height);
	this.xspeed = random(5, 10 ) * (round(random()) * 2 - 1) * (1+level/(level + 2));
	this.initxspeed = this.xspeed;
	this.yspeed = random(5, 10) * (round(random()) * 2 - 1) * (1+ level/(level+2));
	this.inityspeed = this.yspeed;
	this.redTint = random(100, 200)
	this.centercolor = random(0, 75);
	this.diameter = diam;
	this.trailamount = 4;


	this.display = function(){
		fill(this.redTint, 0, 0);
		noStroke();
		ellipse(this.x, this.y, diam, diam);
		fill(this.centercolor);
		ellipse(this.x, this.y, diam/1.5, diam/1.5);
		for (this.steps = 1; this.steps < this.trailamount; this.steps++){
			ellipse(this.x - trailstep * this.xspeed * this.steps, this.y - trailstep * this.yspeed * this.steps, diam/2, diam/2);
		}
		

	}

	this.move = function(){
		if (this.x <= 0 || this.x >= width) {
			this.xspeed = -this.xspeed;
			if(abs(this.xspeed) <= maxspeed){
				this.xspeed = this.xspeed * bouncemult;
			}
		};
		if (this.y <= 0 || this.y >= height) {
			this.yspeed = -this.yspeed;
			if(abs(this.yspeed) <= maxspeed){
				this.yspeed = this.yspeed * bouncemult;
			}
		}
		this.x += this.xspeed;
		this.y += this.yspeed;
	}
	this.relative = function(){
		this.x = canvasWidth/prevcanvasWidth * this.x;
		this.y = canvasHeight/prevcanvasHeight * this.y;
	}
//FIX DIT FF!!
	this.reset = function(){
		this.xspeed = abs(this.initxspeed) * (this.xspeed/abs(this.xspeed));
		this.yspeed = abs(this.inityspeed) * (this.yspeed/abs(this.yspeed));
	}
}

function intersect(x1, y1, x2, y2, touch){
	var d = dist(x1, y1, x2, y2);
	if (d < touch) {
		background(200, 0, 0);
		points = 0;
		for (var i = obstacles.length - 1; i >= 0; i--) {
			obstacles[i].reset();
		};
	};
	if(d >= touch) {
		fill(0, 200, 100);
		noStroke();
		ellipse(mouseX, mouseY, diam, diam);
	}
}

function printPoints(_points){
	document.getElementById("ppoints").innerHTML = _points;
	document.getElementById("maxpoints").innerHTML = winpoints;
	document.getElementById("plevel").innerHTML = level;
	document.getElementById("enemycount").innerHTML = obstacleamount;

}

function levelIncrement(){
	winpoints = 500 * level;
	if (points >= winpoints) {
		points = 0;
		bouncemult += 0.1;
		level++;
		obstacleamount++;
		diam +=  (level)/(level+1);
		if(backgroundColorinit>50){
			backgroundColorinit = 255 - (50 * random(0.0,1)/level);
		}
		bRed = backgroundColorinit * random(0.5,1);
		bGreen = backgroundColorinit * random(0.5,1);
		bBlue = backgroundColorinit * random(0.5,1);
		enemyGenerate(obstacleamount);

	};
}

function enemyGenerate(_obstacleamount){
	obstacles = [];
	for (var i = 0; i < _obstacleamount; i++) {
    	obstacles.push(new obstacle());
	}
}
function backgroundDarken(_r, _g, _b){
	background(_r - _r * points/winpoints, _g - _g * points/winpoints, _b - _b * points/winpoints,);
}

function canvasCreation() {
	prevcanvasWidth = canvasWidth;
	prevcanvasHeight = canvasHeight;
	canvasWidth = window.innerWidth;
	canvasHeight = window.innerHeight/1.5;
}
