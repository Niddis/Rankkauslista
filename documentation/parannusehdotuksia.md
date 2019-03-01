##Sovelluksen rajoitteita: 

* Sovelluksessa ei ole mahdollisuutta luoda käyttäjätunnuksia. Tämän ominaisuuden voisi mahdollisesti lisätä myöhemmin, jos haluttaisiin esim. antaa lajin seuraajille mahdollisuus määrittää omia suosikkijoukkueitaan.

##Puuttuvia ominaisuuksia:

* Sovelluksessa ei ole erillistä sivutusta, mikä voi tulla ongelmaksi, jos joukkueiden, turnausten tai tulosten määrä kasvaa kovin suureksi. Toisaalta joukkueiden järjestäminen tapahtuu tällä hetkellä teams/views.py -tiedostossa, mikä voi johtaa ongelmiin sivutuksen kanssa.

* Jokaiseen turnaukseen liittyy kokonaispistemäärä, joka jaetaan turnaukseen osallistuneiden joukkueiden välillä. Sovellus ei kuitenkaan tarkista, ettei joukkueiden saamien pisteiden yhteismäärä ylitä turnauksen kokonaispistemäärää.