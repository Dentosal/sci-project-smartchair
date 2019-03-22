// Port setup
// Ports 2-9 are used for inputs (port 1 doesn't work for this, and skipping 0 for continuity
// Analog ports (A0-A5) are used for outputs, as well as digital ports 10 and 11

void setup() {
  // Analog ports as outputs
  for (int i = 0; i < 6; i += 1) {
    pinMode(A0 + i, OUTPUT);  
  }

  // Digital outputs
  for (int i = 10; i < 12; i += 1) {
    pinMode(i, OUTPUT);  
  }

  // Digital inputs
  for (int i = 2; i < 10; i += 1) {
    pinMode(i, INPUT_PULLUP);
  }

  // Serial baud rate high enough
  Serial.begin(9600);
}
 
void loop() {
  unsigned char data = 0; // 8 bits
 
  for (int i = 10; i >= 2; i -= 1) {
    unsigned char val = !digitalRead(i);   // Read the input pin
    data = (data << 1) | val; // Get bit
  }

  // Send through usb
  Serial.write(data);
}
