# Rankkauslista

Tämä on Helsingin yliopiston Tietokantasovellus -kurssin harjoitustyö.

Harjoitustyön aiheena on rankkauslista liittyen lajiin x. Lajissa x järjestetään useamman joukkueen cup-tyyppisiä turnauksia, joiden ottelukaavio laaditaan joukkueiden rankkausarvojen mukaisesti. Kaavion pohjana käytetään turnaukseen ilmoittautuneiden joukkueiden rankkauspisteitä siten, että korkean rankkausarvon joukkue saa vastaansa korkean rankkausarvon joukkueen vasta loppupeleissä. Joukkueet saavat otteluista rankkauspisteitä, joiden määrä riippuu voitettujen otteluiden määrästä, voitettujen vastustajien rankkausarvoista sekä ylipäätään turnauksessa jaossa olevien rankkauspisteiden määrästä (mikä puolestaan riippuu turnauksen arvostuksesta).

Rankkauslista pitää kirjaa turnauksista ja niissä jaettavista pisteistä, turnauksiin osallistuvista joukkueista ja niiden rankkausarvoista sekä turnauksien tuloksista. Turnaukset, tulokset ja joukkueet ovat kaikkien nähtävillä. Turnauksen ylläpitäjä tms. päivittää turnauksen tulokset ja joukkueiden rankkausarvot.

Toimintoja:

* ylläpidon kirjautuminen  
* joukkueen rekisteröinti  
* joukkueen tietojen muokkaus ja poisto  
* turnaukseen ilmoittautuminen  
* turnaukseen ilmoittautuneiden rankkaus  
* turnaustulosten kirjaus ja korjaus  
* yleinen rankkaustilanteen katselu  
* lista turnaukseen osallistuneista joukkueista ja heidän sijoittumisensa sekä turnauksen rankkauspistesumma

[Sovellus Herokussa](https://rankkauslista.herokuapp.com/)

[CREATE TABLE -lauseet](../master/documentation/tietokantakaaviot.md)

[Käyttötapaukset](../master/documentation/kayttotapaukset.md)

[Tietokantakaavio](../master/documentation/tietokantakaavio.png)

### Huomioita

Sovelluksessa ei ole erillistä rekisteröitymistoimintoa. Sovelluksen ideana on, että kuka tahansa voi selata turnauksia, joukkueita ja tuloksia, mutta lisäämiseen tai muokkaamiseen tarvitaan tunnukset, joita pitää erikseen pyytää ylläpidolta. Voit tutustua sovelluksen toimintaan kirjautumalla sisään testitunnuksilla.

* käyttäjätunnus: test
* salasana: testuser1
