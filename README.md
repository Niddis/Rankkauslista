# Rankkauslista

Tämä on Helsingin yliopiston Tietokantasovellus -kurssin harjoitustyö.

Harjoitustyön aiheena on rankkauslista liittyen lajiin x. Lajissa x järjestetään useamman joukkueen cup-tyyppisiä turnauksia, joiden ottelukaavio laaditaan joukkueiden rankkauspisteiden mukaisesti. Kaavion pohjana käytetään turnaukseen ilmoittautuneiden joukkueiden sijoitusta sarjataulukossa siten, että sarjataulukon yläpäässä oleva joukkue saa vastaansa toisen korkealle sijoittuneen joukkueen vasta loppupeleissä. Joukkueiden rankkauspisteiden määrä riippuu voitettujen otteluiden määrästä, voitettujen vastustajien sijoituksesta sarjataulukossa sekä ylipäätään turnauksessa jaossa olevien rankkauspisteiden määrästä (mikä puolestaan riippuu turnauksen arvostuksesta).

Rankkauslista pitää kirjaa turnauksista ja niissä jaettavista pisteistä, turnauksiin osallistuvista joukkueista ja niiden sijoituksista sekä turnauksien tuloksista. Turnaukset, tulokset ja joukkueet ovat kaikkien nähtävillä. Turnausjärjestäjä päivittää turnauksen tulokset ja joukkueiden sijoitus sarjataulukossa lasketaan saatujen rankkauspisteiden perusteella.

Toimintoja:

* ylläpidon kirjautuminen
* turnausjärjestäjän kirjautuminen
* joukkueen luominen, tietojen muokkaus ja poisto  
* turnauksen luominen, tietojen muokkaus ja poisto
* joukkueiden lisääminen turnaukseen
* turnaustulosten kirjaus ja korjaus  
* yleinen tulosten tarkastelu ja tulosten järjestäminen joukkueiden, turnausten, rankkauspisteiden ja sijoitusten mukaan
* tulosten tarkastelu turnaus- ja joukkuekohtaisesti
* joukkueiden sijoittuminen sarjataulukossa

[Sovellus Herokussa](https://rankkauslista.herokuapp.com/)

[CREATE TABLE -lauseet](../master/documentation/CreateTable_lauseet.md)

[Käyttötapaukset](../master/documentation/kayttotapaukset.md)

[Tietokantakaavio](../master/documentation/tietokantakaavio.png)

[Sovellukseen liittyvät rajoitteet yms.](../master/documentation/parannusehdotuksia.md)

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
```git
git clone https://github.com/Niddis/Rankkauslista.git
```
2. mene kloonatun repositorion hakemistoon
```git
cd Rankkauslista
```
3. liitä kansio omaan github-repositorioosi
```
git remote add origin omanrepositoriosiurl
```
4. pushaa esim. Herokuun

### Paikallinen versio

1. kloonaa lähdetiedostot omalle koneellesi haluamaasi hakemistoon
```git
git clone https://github.com/Niddis/Rankkauslista.git
```
2. mene kloonatun repositorion hakemistoon
```git
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