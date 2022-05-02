# SPanish Trainset (SPTS) - Engines

This is a modern replacement for the Spanish Taster Set (spainssetw.grf)

TT-forums thread: https://www.tt-forums.net/viewtopic.php?f=26&t=88456

## How Build

First, go to *tools* folder and run `pip3 install .` to grab the python dependencies.
Then you can run `build.sh` or follow this manual steps :

1. Run `make clean`
2. Run `tools/build_nml.py steam` from the main folder
3. Run `tools/build_nml.py single` from the main folder
4. Run `tools/build_nml.py mu` from the main folder
5. Run `make all`

If you like to copy the NewGRF to your install of OpenTTD, run `make install`

## Objetives

Try to reimplement all the engines and wagons from the old Spanish Taster Set, with fixed data, and some modern goodies.

Project evolution and documentation: https://docs.google.com/spreadsheets/d/1-FiiYils_twxTgcudiL_BsNrjCdRhsIz4bYIDnOckaI/edit#gid=0
Discord : https://discord.gg/kArHNjkD

## TODO

More updated/detailed on the previous Google Docs document.

### Short-term
- [X] Investigate how use some script language like Python+templates to automatize all the boring repetitive coding.
- [ ] Add more trains form Spanish Taster Set
  - Steam engines
  - [X] XX Steam engines
  - Single unit engines
  - [X] Diesel engine
  - [X] Electric engine
  - Multiple units
  - [X] Diesel units
  - [X] Electric units
  - Wagons
  - [ ] Passenger wagons
  - [ ] Cargo wagons
- Add a few more XIX century engines (Mataró, Caldas, Series 100 and 200 from Norte, etc)
  - [ ] Sprites
  - [ ] Models/Data
- Add some post 2003 new Spanish engines
  - [ ] Sprites
  - [ ] Models/Data

### Long-term
- [X] Apply the track standard nomenclature so the engines are compatible with
    tracks from other NewGRF. This should allow to make a new Spanish High speed
    track GRF that it's compatible with other NewGRFs.
- [ ] Track sprites
- Incorporate narrow engines (from the FEVE GRF and a few historical used on some narrow gauge lines on Spain)
  - [X] Track type
  - [ ] Steam engines
  - [ ] Single Unit Diesel
  - [ ] Single Unit Electric
  - [ ] Multiple Unit Diesel
  - [ ] Multiple Unit Electric
- [ ] Alternative names, like The Dutch Trainset.
- [ ] Add "Fuel" variant of some steam engines (lower running costs)
- [ ] Parameters to show/hide some engines (hide "Cercanias" trains, etc)

### Dreaming
- [ ] 32bpp and x2 or x4 sprites
