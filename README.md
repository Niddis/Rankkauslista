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

[Käyttö- ja asennusohjeet](../master/documentation/kaytto-ja_asennusohjeet.md)

[CREATE TABLE -lauseet](../master/documentation/CreateTable_lauseet.md)

[Käyttötapaukset](../master/documentation/kayttotapaukset.md)

[Tietokantakaavio](../master/documentation/tietokantakaavio.png)

[Sovellukseen liittyvät rajoitteet yms.](../master/documentation/parannusehdotuksia.md)