#include <LiquidCrystalRus.h>
#include <AmperkaKB.h>
#include <Servo.h>

AmperkaKB KB(A0, A1, A2, A3, 5, 4, 3, 2);
LiquidCrystalRus lcd(6, 7, 8, 9, 10, 11);
int tone_pin = 13;
int servo_pin = 12;

Servo servo;

String enteredPassword = "";
char newKey;
bool started;
int attemps = 3;

long error_delay = millis();
long click_delay = millis();
long closed_delay;
bool sing_song = true;

bool opened = false;
bool closed = false;
String password = "69AC";


void setup()
{
    Serial.begin(9600);
    KB.begin(KB4x4);
    servo.attach(servo_pin);
    servo.write(0);
    lcd.begin(16, 2);
    lcd.setCursor(2, 0);
    lcd.print("Для открытия");
    lcd.setCursor(0, 1);
    lcd.print("Введите пароль");
}

void loop()
{
    KB.read();

    if (KB.justPressed()
        and !closed and millis() - error_delay > 1500
        and millis() - click_delay > 200
        and !opened) {
        newKey = KB.getChar;
        enteredPassword += newKey;
        lcd.clear();
        lcd.setCursor(3, 0);
        lcd.print(enteredPassword);
        click_delay = millis();
    }
    else if (KB.justPressed() and opened) {
        lcd.clear();
        lcd.setCursor(2, 0);
        lcd.print("Для открытия");
        lcd.setCursor(0, 1);
        lcd.print("Введите пароль");
        servo.write(0);
        opened = false;
        attemps = 3;
    }

    if (enteredPassword.length() >= 4 and enteredPassword != password) {
        attemps--;
        lcd.clear();
        lcd.setCursor(3, 0);
        lcd.print("Неверно!");
        lcd.setCursor(0, 1);
        String str;

        if (attemps != 1) {
            str = String(attemps) + " раза осталось";
        }
        else {
            str = "Последняя попытка!";
        }

        lcd.print(str);
        enteredPassword = "";
            
        error_delay = millis();

        if (attemps <= 0) {
            Serial.println(0);
            tone(tone_pin, 500, 5000);
            closed = true;
            attemps = 3;
            closed_delay = millis();
        }
    }

    if (millis() - closed_delay > 30000 and closed) {
        closed = false;
        lcd.clear();
        lcd.setCursor(1, 0);
        lcd.print("Введите пароль");
    }

    else if (enteredPassword == password) {
        Serial.println(1); 
        lcd.clear();
        lcd.setCursor(3, 0);
        lcd.print("Пароль верен!");
        lcd.setCursor(3, 1);
        lcd.print("Нажмите клавишу");
        enteredPassword = "";
        opened = true;
        servo.write(90);
    }
}
