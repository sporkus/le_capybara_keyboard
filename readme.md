Le Capybara Keyboard
----

Capacitive sensing (aka Topre) keyboard in Le Chiffre layout

## Status
Fully tested 

## Manufacturing
Plates have m2 threaded holes for securing the plate and switches to the PCB.  DIY tapping is not difficult if your plate manufacturer does not offer tapping services.

Recommended plate material is 1.2mm steel. Plate files are in the expected physical dimensions. No kerf adjustments have been applied. The dxf files have been used successfully with SendCutSend and LaserBoost. JLCPCB is not recommnded for the plates without further testing to adapt to their milling process.

- [PCB production files](./production/)
- [Plate files](./plate/)


## Assembly

EC housing from DESKEYS and KLC playground have been tested.

#### Parts needed
- 32 - 34: 1u EC housing + slider
- 0 - 2: 2u EC housing + slider
- 34 - 36: Rubber domes
- 34 - 36: Conical springs
- 16: m2 x 8mm screws

**Optional**
- Silencing rings
- EC 11 rotary encoder or 1 MX switch for the center button


## Misc
#### 3D assembly preview
* [online viewer](https://3dviewer.net/#model=https://github.com/sporkus/le_capybara_keyboard/blob/dev/documentation/le_capybara-3D.step)
* [step assembly](./documentation/le_capybara-3D.step)

#### PCB Renders
![](./documentation/le_capybara-top.jpg)
![](./documentation/le_capybara-bottom.jpg)

#### Interactive BoM
Download and open this [html](./documentation/le_capybara-ibom.html) locally

#### Schematic
[pdf](./documentation/le_capybara-schematic.pdf)


## Change log
- 2024-02-21: V1.0 release for group buy. Change mounting method to tapped plate for ease of assembly.
