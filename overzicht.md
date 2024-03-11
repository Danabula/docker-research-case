# Docker research case overzicht


De folder layout is als volgt
- de src folder wordt geupload naar codecrashers.nl en verwerkt.
- de local folder bevat bronbestanden voor de src folder en een aantal ongebruikte bestanden.


## Opdracht

- Zorg dat je je zo breed mogelijk oriënteert tijdens deze onderzoeksfase.
- Alleen de documentatie van de programmeertaal of product is dus niet voldoende! 
- kijk naar andere artikelen
- kijk naar andere docker gebruikers
- hoeft niet alleen geschreven
- presentatie
- Het heeft onze voorkeur dat je je informatie stapsgewijs aanbiedt in de vorm een lijst, dat leest gemakkelijker.
- informatie koppelen met bekende informatie
- Gebruik vooral afbeeldingen voor concepten
- meta
    title: titel
    order: volgorder van hoofdstuk/opdracht, komt overeen filename
    active: of aan staat, normaal 1
    goto: 'assignment 1' etc. bepaald volgende bladzijde
    flags: voor opdrachten 'key' moet gemaakt worden, chain 'word later op gebouwd in andere les', bonus optionele opdracht


## Todos text

- docker & container history paragraph
    geschiedenis containers & docker
    tijdlijn
        - docker creatie
        - stop gebruikt lxc naar libcontainer
        - libcontainer wordt runc
        - docker splitsing
        - oci oprichting voor standards
    podman?
- opdrachten
    - setup old project in vm
    - dockerize old project
    - setup dockerised old in vm
    - refactor de neofetch dockerfile om alpine linux te gebruiken in plaats van debian
- docker ecosystem image
    - kubernetes
    - ddev
    - cri spec
    - grpc
    - crio
    - skopeo, buildah
    - docker swarm
    - wsl
    - podman (machine)
- debug container ideas
    bad logging (eg. no exec in shell script entrypoint)
    multi program container
    pipe daemon into tail
    non persistent database, oplossing is een rw mount
    ?, oplossing is log rotatie
    image gigantisch door het niet verwijderen van build dependencies
    standalone image
    host resolution using container name
    not stopping on sigterm (eg. docker stop), solution only pid1 gets signals
    interactief nodig: run -it --rm *container naam* & docker exec sh
    explain that removing packages in new layer shrink image, because the files are on a previous still used in an earlier layer


## Todos

- split subject 03
- read codecrashers mysql exercise
- create exercises
- spelcheck


