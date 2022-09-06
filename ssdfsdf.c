
#include <NMEAGPS.h>

#include <GPSport.h>

#include <Streamers.h>
static NMEAGPS  gps;

static gps_fix  fix;

static void doSomeWork()
{
  if(fix.latitude()>0){
  Serial.print(fix.latitude(), 6 );
  Serial.print(",");
  Serial.println(fix.longitude(), 6);
  }
}static void GPSloop()
{
  if (gps.available( gpsPort )) {
    fix = gps.read();
    if (fix.valid.location) {
      doSomeWork();
    }}
  }

}
void setup()
{
  Serial.begin(9600);
  //DEBUG_PORT.flush();

  gpsPort.begin( 9600 );
}

void loop()
{
  GPSloop();
}
