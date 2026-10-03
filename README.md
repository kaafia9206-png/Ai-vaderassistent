# Väderassistent

## Syfte

Väderassistenten är ett Python-projekt som hämtar aktuell väderdata från ett API.

Användaren skriver in en stad och programmet hämtar stadens koordinater, temperatur och väderförhållande. Informationen sparas även i en CSV-fil.

## Mål

Målet med projektet är att skapa en enkel väderassistent och samtidigt visa grundläggande kunskaper inom Python.

Projektet använder funktioner, loopar, villkor, klasser, arv, felhantering, CSV-filer, API-anrop och externa bibliotek.

## Metod

Programmet använder Open-Meteo API för att hämta väderdata.

Först skriver användaren in en stad. Programmet använder sedan ett geocoding-API för att hitta stadens latitud och longitud.

Koordinaterna används därefter för att hämta aktuell temperatur och väderkod från väder-API:et.

Väderkoden omvandlas till en enkel beskrivning, till exempel klart väder, molnigt, regn eller snö.

Väderinformationen sparas sedan i en CSV-fil tillsammans med datum och tid.

Projektet innehåller även klasser och arv. Klassen WeatherData innehåller information om stad och temperatur. WeatherAssistant ärver från WeatherData och kan visa en temperaturvarning.

## Funktioner i programmet

Programmet kan:

- Ta emot en stad från användaren
- Hämta koordinater för staden
- Hämta aktuell väderdata från ett API
- Tolka väderkoder
- Analysera temperatur
- Visa temperatur och väderförhållande
- Spara väderdata i en CSV-fil
- Läsa data från CSV-filen
- Hantera fel med try/except

## Teknik och bibliotek

Projektet är utvecklat i Python.

Standardbibliotek som används:

- csv
- datetime

Ett externt bibliotek som används:

- requests

Requests används för att skicka HTTP-anrop till API:et.

## API och extern data

Projektet använder Open-Meteo API för att hämta aktuell väderdata.

Programmet använder först geocoding-API:et för att omvandla stadens namn till koordinater.

Därefter används koordinaterna för att hämta väderdata.

## Datahantering

Väderinformationen sparas i filen `weather_data.csv`.

CSV-filen innehåller bland annat:

- Stad
- Temperatur
- Väderförhållande
- Datum och tid

Programmet kan både skriva till och läsa från CSV-filen.

## Klasser och arv

Projektet innehåller en basklass:

`WeatherData`

Klassen innehåller attribut för stad och temperatur samt en metod för att visa temperaturen.

Projektet innehåller även en underklass:

`WeatherAssistant`

WeatherAssistant ärver från WeatherData och har en egen metod för att visa temperaturvarningar.

## Koppling till AI-branschen

Python används mycket inom AI och datarelaterade områden eftersom det finns många bibliotek och verktyg för att hämta, bearbeta och analysera data.

Att kunna hämta data från API:er och strukturera data är relevant inom AI-utveckling eftersom data ofta behöver samlas in och bearbetas innan den kan användas i AI- och analyslösningar.

Projektet är därför kopplat till AI-utveckling genom datainsamling, datahantering och automatisering.

Exempel på roller där liknande kunskaper kan vara relevanta är AI Developer, Data Engineer och Python Developer.

## Relevant certifikat

Ett relevant certifikat för Python är PCEP – Certified Entry-Level Python Programmer.

Certifikatet fokuserar på grundläggande Python-kunskaper och är relevant för personer som vill visa sina kunskaper inom Python.

Jag har inte tagit certifikatet inom detta projekt, men det är ett exempel på ett relevant certifikat att undersöka vidare.

## Resultat

Resultatet är en fungerande väderassistent som kan hämta väderdata för en vald stad.

Programmet kan visa aktuell temperatur och en beskrivning av väderförhållandet. Informationen kan även sparas i en CSV-fil för senare användning.

Projektet uppfyller de grundläggande kraven genom användning av Python, funktioner, villkor, loopar, klasser, arv, felhantering, CSV, standardbibliotek, externt bibliotek, API och GitHub.

## Reflektion

Under projektet har jag fått träna på att använda Python i ett eget projekt från början till slut.

Jag har bland annat arbetat med funktioner, API-anrop, CSV-filer, felhantering, klasser och arv.

En viktig del av projektet har varit att förstå hur olika delar av programmet hänger ihop. Jag har också fått erfarenhet av Git och GitHub för versionshantering.

Projektet har gjort det tydligare hur Python kan användas för att hämta och bearbeta data från externa källor.

## Installation

Projektet kräver Python 3.

Installera det externa biblioteket requests med:

```bash
pip install requests

Projektet kan köras i Jupyter Notebook eller Visual Studio Code.

## Filer

Projektet innehåller:

- `vaderassistent.ipynb` – Jupyter Notebook med projektets kod och förklaringar
- `weather_data.csv` – sparad väderdata
- `README.md` – projektbeskrivning och dokumentation

## GitHub

GitHub-repository:

https://github.com/kaafia9206-png/Ai-vaderassistent