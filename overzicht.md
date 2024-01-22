# Artikel docker overzicht


## Hoofdstukken
1. virtualizatie
2. shell (bourne) (nodig voor debuggen & eigen docker images maken)
3. docker
4. docker-compose
5. what is een kernel
6. containers & lxc
7. docker op windows with wsl pros & cons

---

## Opdracht
- Zorg dat je je zo breed mogelijk oriënteert tijdens deze onderzoeksfase.
- Alleen de documentatie van de programmeertaal of product is dus niet voldoende! 
- kijk naar andere artikelen
- kijk naar andere docker gebruikers
- hoeft niet alleen geschreven
- min 1 opdracht
- presentatie
- In ieder geval afscheiding (---) voorafgaand aan elk (sub-)kopje!
- Het heeft onze voorkeur dat je je informatie stapsgewijs aanbiedt in de vorm een lijst, dat leest gemakkelijker.
title: titel
order: volgorder van hoofdstuk/opdracht, komt overeen filename
active: of aan staat, normaal 1
goto: 'assignment 1' etc. bepaald volgende bladzijde
flags: voor opdrachten 'key' moet gemaakt worden, chain 'word later op gebouwd in andere les', bonus optionele opdracht
- Gebruik vooral afbeeldingen voor concepten


## Kernel
Een kernel is een stuk software dat dient als de kern van een operating systeem.
Het doel is om een abstractie te geven over verschillende hardware componenten,
zodat het operating systeem op verschillende hardware kan draaien & daar niet mee bezig hoeft te zijn.
Een populaire kernel is de linux kernel, veel servers gebruiken een operating systeem die linux als kernel gebruikt, zoals debian (een linux distrobutie / distro).

## Lxc
Linux containers
Een functie die de linux kernel heeft is namespacing. Dat betekend bijvoorbeeld dat als je een programma in een andere pid (process id) namespace draait, dat het niet kan zien wat voor andere programmas draaien.
Deze technologie is waar containers en dus docker op gebouwd is.
Een andere technologie die lxc gebruikt voor sandboxing is bubblewrap [link](https://localhost)

## Containers
de oci container image specificatie heeft een platform nodig met cpu architectuur & os, dus containers zijn niet cross platform
[image spec](https://github.com/opencontainers/image-spec/blob/main/spec.md)
[spec image index](https://github.com/opencontainers/image-spec/blob/main/image-index.md)

## Docker
wie hoe wat waar wanneer waarom docker
containers maken efficienter gebruikt van de host os resources dan virtuele machines, maar gebruiken dezelfde kernel als het host operating systeem
voor containers hoef je niet rekening te houden met de state vm configuraties, dat hoeft anders ook niet met een vm orchestrator
Docker is een runtime voor containers die de oci standaard gebruiken.
Containers zijn een lighte virtualisatie technologie gebouwd op de linux kernel.
Docker word gebruikt
- om programmas onafhankelijk van operating systeem en systeem configuratie op te zetten
    Dit betekend bijvoorbeeld dat je programmas die verschillende versies hebben op dezelfde computer kan draaien
- om te prototypen
    Als er iets verkeerd gaat met het opzetten van bijvoorbeeld een database,
    dan is dat heel gemakkelijk terug te zetten.
- om te experiementeren
    Als je met een container werkt is dat onafhankelijk van het operating systeem, dus je kan niet je firewall verknallen!
- voor security
    security werkt met lagen en de docker runtime isoleert het van het host systeem met de juiste configuraties

# Todo
- spelcheck
- uitnodigen github sven
- move to template structure

