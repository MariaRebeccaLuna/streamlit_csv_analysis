# Enkel Streamlit-app för dataanalys

## Om projektet:
Det här projektet är en enkel Stremlit-applikation som används för att analysera data från en cvs-fil.

Användaren kan ladda upp en csv-fil och appen visar följande:
- Antal rader
- Antal kolumner
- Total försäljning
- Försäljning per produkt
- Stapeldiagram
- Filtrerad datatabell

## Teknik:
Projektet är byggt med:
- Python
- Streamlit
- Pandas

## Projektstruktur:
streamlit_csv_analysis
- app.py
- README.md
- requirements.txt
- data
    - sales.csv

## Installation:
Installera paketet med: " pip install -r requirements.txt "

## Starta applikationen:
Kör följande kommando i terminalen: " python -m streamlit run app.py "

## Användning:
1. Starta applikationen.
2. Ladda upp en csv-fil.
3. Välj en produkt i filtret.
4. Se sammanfattningen och diagrammet.
5. Undersök den filtrerade datan.

## Exempeldata:
Projektet innehåller en liten CSV-fil med försäljningsdata.
Datan innehåller:
- Månad
- Produkt
- Region
- Försäljning

## Begränsningar:
Applikationen är en väldigt enkel prototyp. Den är främst anpassad till CSV filer som innehåller en kolumn med namnet "Sales" och en kolumn med namnet "Product".
Mer avancerade funktioner, databadkoppling, användarlogging och avancerad dataanalys ingår inte i projektet.