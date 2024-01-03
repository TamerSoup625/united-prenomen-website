// Formatta pagina
let customTags = document.getElementsByTagName("custom");
for(let i = 0; i < customTags.length; i++) {
    let tagClass = customTags[i].getAttribute("class");
    if (tagClass == "sectionstart") {
        let tagname = customTags[i].getAttribute("name");
        let identifier = customTags[i].getAttribute("ide");
        customTags[i].innerHTML = "".concat("<h1 id=", identifier, ">", tagname, " <a title=\"Permalink a ", tagname, "\" href=#", identifier, ">#</a></h1><hr>");
    } else if (tagClass == "bannerdiv") {
        let backgroundSource = customTags[i].getAttribute("bg-source");
        customTags[i].innerHTML = "".concat("<div class=\"banner\" style=\"background-image: linear-gradient(#00000088, #00000088), url(", backgroundSource,")\"><div class=\"banner-testo\">", customTags[i].innerHTML, "</div></div>")
    }
}
fetch("pagine.txt?cachebuster=cde015bc0bce551cH").then((res) => res.text()).then((text) => {
        let splitted = text.split("\n");
        let full_text = "";

        for(let i = 0; i < splitted.length; i += 2) {
            full_text = full_text.concat("<p><a href=".concat(splitted[i + 1], ">", splitted[i], "</a></p>"));
        }

        document.getElementsByTagName("body")[0].innerHTML += "<div class=header><img src=\"icona_tendina.png?cachebuster=97312458317be6beH\"><div class=headcontent>".concat(full_text, "</div></div>");
}).catch((e) => console.error(e));

// Parte dinamica
onscroll = (_ev) => {
    let banners = document.getElementsByClassName("banner");
    for(let i = 0; i < banners.length; i++) {
        banners[i].style.backgroundPosition = "50% calc(".concat(scrollY * 0.5, "px + 50%)");
    }
}