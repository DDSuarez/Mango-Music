#include <Adafruit_NeoPixel.h>
int ledpin = 2;
#define PIN 6
// small led 73
// large led 116
int ledLenght = 73;
int timeLen = 100;

// Parameter 1 = number of pixels in strip
// Parameter 2 = pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(ledLenght, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(9600);
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
  //pinMode(ledpin,OUTPUT);
}

void loop() {
  String state = Serial.readString();
  float input[5];
  input[0]=state.substring(0,4).toFloat();
  input[1]=state.substring(5,9).toFloat();
  input[2]=state.substring(10,14).toFloat();
  input[3]=state.substring(15,19).toFloat();
  input[4]=state.substring(20,24).toFloat();
 
float greatest = 0.0;
int larg=10;
for (int i = 0; i < 5; i++) {
 if (input[i] > greatest) {
  greatest = input[i];
  larg=i;
  }
}

  double angW = 255 * input[0];
  double disW = 255 * input[1];
  double fearW = 255 * input[2];
  double joyW = 255 * input[3];
  double sadW = 255 * input[4];

  double firstBlendedR = 255 - sqrt(((255-angW)^2 + (255-0)^2)/2);
  double firstBlendedG = 255 - sqrt(((255-0)^2 + (255-disW)^2)/2);
  double firstBlendedB = 255 - sqrt(((255-0)^2 + (255-0)^2)/2);

  double secondBlendedR = 255 - sqrt(((255-firstBlendedR)^2 + (255-fearW)^2)/2);
  double secondBlendedG = 255 - sqrt(((255-firstBlendedG)^2 + (255-0)^2)/2);
  double secondBlendedB = 255 - sqrt(((255-firstBlendedB)^2 + (255-fearW)^2)/2);

  double thirdBlendedR = 255 - sqrt(((255-secondBlendedR)^2 + (255-joyW)^2)/2);
  double thirdBlendedG = 255 - sqrt(((255-secondBlendedG)^2 + (255-joyW)^2)/2);
  double thirdBlendedB = 255 - sqrt(((255-secondBlendedB)^2 + (255-0)^2)/2);

  int finalBlendedR = 255 - sqrt(((255-thirdBlendedR)^2 + (255-0)^2)/2);
  int finalBlendedG = 255 - sqrt(((255-thirdBlendedG)^2 + (255-0)^2)/2);
  int finalBlendedB = 255 - sqrt(((255-thirdBlendedB)^2 + (255-sadW)^2)/2);

  theaterChase(strip.Color(finalBlendedR, finalBlendedG, finalBlendedB));
/*
  if (larg==0){                       // wait for a second
  theaterChase(strip.Color(255, 0, 0), timeLen); //red
  delay(500);
  }else if(larg==1){
  theaterChase(strip.Color(0, 255, 0), timeLen); //green
  delay(500); 
  }else if(larg==2){
  theaterChase(strip.Color(255, 0, 255), timeLen);//purple
  delay(500); 
  }else if(larg==3){
  theaterChase(strip.Color(255, 255, 0), timeLen); //yellow
  delay(500); 
  }else if(larg==4){
  theaterChase(strip.Color(0, 0, 255), timeLen); //blue
  delay(500); 
  }else{
    theaterChase(strip.Color(0,  0, 0), 1);//Off
  }
  
    
} */


//Theatre-style crawling lights.
void theaterChase(uint32_t c, uint8_t wait) {
  for (int j=0; j<10; j++) {  //do 10 cycles of chasing
    for (int q=0; q < 3; q++) {
      for (int i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, c);    //turn every third pixel on
      }
      strip.show();
     
      delay(wait);
     
      for (int i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, 0);        //turn every third pixel off
      }
    }
  }
}



