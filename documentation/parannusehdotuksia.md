## Sovelluksen rajoitteita: 

* Sovelluksessa ei ole mahdollisuutta luoda käyttäjätunnuksia. Tämän ominaisuuden voisi mahdollisesti lisätä myöhemmin, jos haluttaisiin esim. antaa lajin seuraajille mahdollisuus määrittää omia suosikkijoukkueitaan.

* Jokaiseen turnaukseen liittyy kokonaispistemäärä, joka jaetaan turnaukseen osallistuneiden joukkueiden välillä. Sovellus ei kuitenkaan tarkista, ettei joukkueiden saamien pisteiden yhteismäärä ylitä turnauksen kokonaispistemäärää.

* Kun luodaan uutta joukkuetta tai turnausta, sovellus varmistaa, että samannimistä joukkuetta tai turnausta ei ole jo olemassa. Muokkauksen yhteydessä tätä tarkistusta ei kuitenkaan tehdä.

## Puuttuvia ominaisuuksia:

* Sovelluksessa ei ole erillistä sivutusta, mikä voi tulla ongelmaksi, jos joukkueiden, turnausten tai tulosten määrä kasvaa kovin suureksi. Toisaalta joukkueiden järjestäminen tapahtuu tällä hetkellä teams/views.py -tiedostossa, mikä voi johtaa vääränlaiseen järjestykseen sivutusta käytettäessä.