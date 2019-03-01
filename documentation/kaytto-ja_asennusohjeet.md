## Sovelluksen käyttö

Sovelluksessa ei ole erillistä rekisteröitymistoimintoa. Sovelluksen ideana on, että kuka tahansa voi selata turnauksia, joukkueita ja tuloksia, mutta lisäämiseen tai muokkaamiseen tarvitaan tunnukset, joita pitää erikseen pyytää ylläpidolta. Voit tutustua sovelluksen toimintaan kirjautumalla sisään testitunnuksilla.

Turnausjärjestäjän tunnukset: turnausten luominen, muokkaaminen ja poistaminen, joukkueiden lisääminen turnaukseen sekä kyseisen turnauksen tulosten päivittäminen ja poistaminen.
* käyttäjätunnus: test
* salasana: testuser1

Ylläpitäjän tunnukset: kaikkien joukkueiden, turnausten ja tulosten luominen, päivittäminen ja poistaminen.
* käyttäjätunnus: admin
* salasana: adminuser1

## Sovelluksen asentaminen

### Tuotantoversio

1. kloonaa lähdetiedostot omalle koneellesi haluamaasi hakemistoon
```
git clone https://github.com/Niddis/Rankkauslista.git
```
2. mene kloonatun repositorion hakemistoon
```
cd Rankkauslista
```
3. pushaa esim. Herokuun
```
git push heroku master
```

### Paikallinen versio

1. kloonaa lähdetiedostot omalle koneellesi haluamaasi hakemistoon
```
git clone https://github.com/Niddis/Rankkauslista.git
```
2. mene kloonatun repositorion hakemistoon
```
cd Rankkauslista
```
3. luo hakemistoon Python-virtuaaliympäristö
```
python3 -m venv venv
```
4. käynnistä virtuaaliympäristö
```
source venv/bin/activate
```
5. asenna riippuvuudet
```
pip install -r requirements.txt
```
6. käynnistä sovellus
```
python3 run.py
```