1- Cose IMPORTANTI prima di cominciare
- Per poter visitare il sito correttamente, devi eseguire il file "test_pagina.bat", poi devi aprire il tuo browser e digitare il link "localhost:8000" (senza virgolette).
- Se si prova ad aprire il file html dall'Esplora File non funzionerà correttamente.
- C'è una cosa particolare con l'eseguire il sito in questo modo: viene usata la cache del browser.
	Praticamente, invece di riscaricare il file, esso viene memorizzato nel computer.
	Però ciò significa che se un file viene modificato, le modifiche non appariranno subito sul browser anche se si ricarica la pagina.
	Per risolvere questo, se cerchi sui file .html e .js noterai che i link finiscono tutti con "?n=<un numero qualsiasi>".
	Cambia quel numero per i vari riferimenti a quel file e se tutto va correttamente la modifica dovrebbe apparire.
	Ad esempio, se hai modificato il file pagine.txt, vai sul file builder.js, trova la stringa "pagine.txt?n=<un numero>", e cambia quel numero scrivendo il suo successivo.
	Però se ancora non vedi il cambiamento, dovrai anche modificare il riferimeno a builder.js nei file ".html". Si trova dentro il tag script nell'attributo src per ogni pagina. Il tag script di solito si trova alla fine.
- Tra i riferimenti che potresti modificare per risolevere il rpoblema della cache ci sono:
	- Quello del file .css nei file .html
	- Quello del file .js nei file .html
	- Quello di pagine.txt nel file builder.js
	- Riferimenti a immagini se le modifichi nei file .html, .css, e .js

2- La pagina base.html
Ho fatto una pagina base.html come base per altre pagine html.
Quando devi fare una nuova pagina fai una copia di quel file.

3- Il file pagine.txt
Se devi fare una nuova pagina, dovrà essere mostrata nel menù a tendina.
Nel file pagine.txt sono elencate il nome e l'indirizzo a tutte le pagine. Aggiungi la pagina da lì.
Da notare, come detto prima, che dovrai modificare il riferimento del file su builder.js

4- Classi di CSS
Nel sito vengono utilizzate varie classi personalizzate che provengono dal file .css
Per usare una classe, inserisci l'attributo "class" nel tag: "<img class="bandierabordo">"
Non me la sento di elencarle tutte, guarda le pagine che ho già fatto e vedi come usarle da lì.

5- Il tag <custom>
Ho creato con JavaScript un tag personalizzato: <custom>. Assegnali una classe per usarla.
Non so che succede se non chiudi il tag comunque chiudilo.
Anche questa volta sono pigro, vai a guardare come vengono utilizzati.

Spero che sia tutto. Chiedimi se hai delle domande.