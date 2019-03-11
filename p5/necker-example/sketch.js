function setup() {
  // put setup code here
  createCanvas(710, 400, WEBGL);
  ortho();
}

function draw() {
  // put drawing code here
  background(250);
  strokeWeight(3);

  push();
  translate(-200, 0, 0);
  noFill();
  rotateZ(frameCount * .001)
  rotateX(frameCount * .001)
  rotateY(frameCount * .001)
  box(100, 100, frameCount * .1);
  pop();
  
  push();
  translate(0, 0, 0);
  noFill();
  rotateZ(frameCount * .001)
  rotateX(frameCount * .001)
  rotateY(frameCount * .001)
  box(100, 100, frameCount * .1);
  pop();
  

  push();
  translate(200, 0, 0);
  noFill();
  rotateZ(frameCount * .001)
  rotateX(frameCount * .001)
  rotateY(frameCount * .001)
  box(100, 100, frameCount * .1);
  pop();

}