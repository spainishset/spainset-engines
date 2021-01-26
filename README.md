# SPanish Trainset (SPTS) - Engines

This, actually, is a small test for creating a modern replacement for the Spanish Taster Set
(spainssetw.grf)

Actually only the Norte Series 500 (2500) "0-4-0 Verraco" it's implemented as example.

## How Build

Run `build.sh` or :

1. Run `make clean`
2. Run `tools/build_nml.py steam` from the main folder
3. Run `tools/build_nml.py diesel` from the main folder
4. Run `tools/build_nml.py electric` from the main folder
5. Run `make all`

If you like to copy the NewGRF to your install of OpenTTD, run `make install`

## Objetives

Try to reimplement all the engines from the old Spanish Taster Set, with fixed
data, and some modern goodies.

## TODO

### Short-term
- [X] Investigate how use some script language like Python+templates to
    automatize all the boring repetitive coding.
- [ ] Add more trains form Spanish Taster Set
  - Iberian gauge
  - [ ] 0-3-0 "Perruca"/"Bourbonnais"
  - [x] 0-4-0 "Verraco" (Renfe 040)
  - [ ] 2-4-0 "Mastodonte"
  - [ ] 1-4-1 "Mikado"
  - [ ] 1-4-0 "Consolidación" (Renfe 140)
  - [ ] 1-4-1+1-4-1 "Garrafeta" (Renfe 282)
  - [ ] 2-4-1 "Montaña"
  - [ ] 2-3-1 "Pacific"
  - [ ] 1-5-1 "Santa Fé"
  - [ ] 2-4-2 "Confederación"
  - [ ] 590 (ex 9000) MD Ferrobús "Talguillo"
  - [ ] Talgo 1 DMU (disabled by default with a GRF parameter)
  - [ ] 350 Talgo II
  - [ ] 595 (ex 9500) MD/LD Ferrobús "TAF"
  - [ ] 316 (ex 1600) "Marilyn"
  - [ ] 314 (ex 1400)
  - [ ] 597 (ex 9700) MD/LD "TER" DMU
  - [ ] 352 (ex 2000T) Talgo III
  - [ ] 319 (ex 1900) "Retales"/"Calderos"
  - [ ] 340 (ex 4000) "Huevo"
  - [ ] 321 (ex 2100)
  - [ ] 333 (ex 3000) "Rambo"/"Prima"
  - [ ] 260 (ex 6000)
  - [ ] 261 (ex 6100)
  - [ ] 270 (ex 7000)
  - [ ] 273 (ex 7300) "Cocodrilo"
  - [ ] 281 (ex 1000)
  - [ ] 274 (ex 7400) "Bañera"
  - [ ] 278 (ex 7800) "Panchorga"
  - [ ] 276 (es 7600) "Francesa"
  - [ ] 436 (ex 600) EMU "Suiza"
  - [ ] 280 (ex 10000)
  - [ ] 439 (ex 900) EMU-MD
  - [ ] 432 EMU/LD "Obispo"
  - [ ] 269 (ex 7900) "Japonesa"
  - [ ] 441 EMU-Cerc "Automática"
  - [ ] 440 EMU-Cerc/MD "Caperucita"
  - [ ] 443 EMU-LD(pendolino) "Platanito"
  - [ ] 444/448 EMU "Españolito"/"Cangrejo"/"Lavadora"
  - [ ] 250 "Alemanas"
  - [ ] 592/593/596 DMU-Cerc/MD/LD "Camello"
  - [ ] 251 "Japonesa y media"
  - [ ] 354 Talgo Pendular "4000T"
  - [ ] 446 EMU-Cerc "Dodotis"
  - [ ] 450 EMU-Cerc "Buque"
  - [ ] 252 (Pre-EuroSprinter)
  - [ ] 594 DMU-MD (Basado en IC3) "Zodiac"
  - [ ] 101 EMU-LD (TGV Atlantique) "Euromed"
  - [ ] 120 EMU-MD/LD "Chipirón"/"Sepia"
  - [ ] 464 EMU-Cerc "Civia"
  - [ ] 598 DMU-MD "Huevo Kinder"/"Nexios"
  - [ ] 310.1 DMU Freighter
  - [ ] 334 "Euro 3000"
  - [ ] 449 EMU-MD "Besugo"
  - High Speed (Standard gauge)
  - [ ] 319 (ex 1900) Retales
  - [ ] 353 (ex 3000T) Talgo III
  - [ ] 269 (ex 7900) "Japonesa"
  - [ ] 354 Talgo Pendular "4000T"
  - [ ] 100EMU-AVE (TGV Atlantique)
  - [ ] 252 (Pre-EuroSprinter)
  - [ ] Talgo XXI DMU
  - [ ] 104 EMU-MD "Gusanito"
  - [ ] 102 EMU-AVE "Pato" (Talgo-350)
  - [ ] TRAVCAL9202 Talgo
  - [ ] 103 EMU-AVE "Velaro" (Velaro E)
- [ ] Alternative names, like The Dutch Trainset.
- [ ] Add a few more XIX century engines (Series 100 and 200 from Norte, etc)
- [ ] Add some post 2003 new Spanish engines

### Long-term
- [ ] Apply the track standard nomenclature so the engines are compatible with
    tracks from other NewGRF. This should allow to make a new Spanish High speed
    track GRF that it's compatible with other NewGRFs.
- [ ] Add "Fuel" variant of some steam engines (lower running costs)
- [ ] Parameters to show/hide some engines (hide Cercanias trains, etc)
- [ ] Incorporate narrow engines (from the FEVE GRF and a few historical used on some narrow gauge lines on Spain) 

### Dreaming
- [ ] 32bpp and x2 or x4 sprites
