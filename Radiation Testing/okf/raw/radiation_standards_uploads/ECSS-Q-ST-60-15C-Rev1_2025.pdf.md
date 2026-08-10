

![ECSS logo featuring a stylized Earth with a satellite orbit, the text 'EUROPEAN COOPERATION', the 'ECSS' logo, and 'FOR SPACE STANDARDIZATION'.](935eed7aa61f7777f62cfc032e11bee9_img.jpg)

The logo consists of a stylized Earth with a satellite orbiting it, represented by a blue and green globe and a purple elliptical line. Below this, the text 'EUROPEAN COOPERATION' is written in a serif font. In the center is the 'ECSS' logo, which features a large 'E' inside a square frame followed by 'CSS'. Below the logo, the text 'FOR SPACE STANDARDIZATION' is written in a serif font.

ECSS logo featuring a stylized Earth with a satellite orbit, the text 'EUROPEAN COOPERATION', the 'ECSS' logo, and 'FOR SPACE STANDARDIZATION'.

# Space product assurance ---

# Radiation hardness assurance - EEE components

ECSS Secretariat  
ESA-ESTEC  
Requirements & Standards Section  
Noordwijk, The Netherlands

# **Foreword**

ECSS is a cooperative effort of the European Space Agency, national space agencies and European industry associations for the purpose of developing and maintaining common standards. Requirements in this Standard are defined in terms of what shall be accomplished, rather than in terms of how to organize and perform the necessary work. This allows existing organizational structures and methods to be applied where they are effective, and for the structures and methods to evolve as necessary without rewriting the standards.

This Standard has been prepared by the Radiation Hardness Assurance Working Group, reviewed by the ECSS Executive Secretariat and approved by the ECSS Technical Authority.

# **Disclaimer**

ECSS does not provide any warranty whatsoever, whether expressed, implied, or statutory, including, but not limited to, any warranty of merchantability or fitness for a particular purpose or any warranty that the contents of the item are error-free. In no respect shall ECSS incur any liability for any damages, including, but not limited to, direct, indirect, special, or consequential damages arising out of, resulting from, or in any way connected to the use of this Standard, whether or not based upon warranty, business agreement, tort, or otherwise; whether or not injury was sustained by persons or property or otherwise; and whether or not loss was sustained from, or arose out of, the results of, the item, or any services that may be provided by ECSS.

Published by: ESA Requirements and Standards Section  
ESTEC, P.O. Box 299,  
2200 AG Noordwijk  
The Netherlands

Copyright: 2025© by the European Space Agency for the members of ECSS

## Change log

|                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ECSS-Q-ST-60-15A                           | Never issued                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ECSS-Q-ST-60-15B                           | Never issued                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ECSS-Q-ST-60-15C<br>1 October 2012         | First issue                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ECSS-Q-ST-60-15C<br>Rev.1<br>20 March 2025 | <p>First issue, Revision 1</p> <p>Summary of changes with respect to ECSS-Q-ST-60-15C (1 October 2012):</p> <ul style="list-style-type: none"> <li>• Implementation of change requests</li> <li>• Introduction of the notion of radiation design lifetime</li> <li>• Introduction of the phasing according to ECSS-M-ST-10 (5.1b,5.1c, 5.1w, 5.1x, 5.2b,5.2c, 5.2x, 5.2y, 5.3b, 5.3c,5.3h, 5.3i)</li> <li>• Changes in TIDL to assess TID sensitivity of Zener diodes (Table 5-1)</li> <li>• Introduction of PICs, Thyristors, IGBTsm and power GaN transistors in the list of potentially TID sensitive EEE part families (Table 5-1)</li> <li>• New requirement specifying the radiation drifts to consider after TID irradiation (5.1j)</li> <li>• Addition of new requirement for shielding analysis (5.1p, 5.1q, 5.2o, 5.2p)</li> <li>• Change of requirements for TID RVTs (5.1y)</li> <li>• Addition of new requirement about X-ray inspection of electronic boards (5.1cc)</li> <li>• Introduction of PICs, Thyristors, IGBTs in the list of potentially TNID sensitive EEE part families (Table 5-2)</li> <li>• Change of requirements for TNID RVTs (5.2z)</li> <li>• Introduction of PICs, Thyristors, IGBTsm and power GaN transistors in the list of potentially SEE sensitive EEE part families (Table 5-3)</li> <li>• Introduction of new requirements for SET templates of optocouplers (5.3i,5.3j)</li> <li>• Introduction of a new requirement to allow for SEL, HCE mitigation (5.3t)</li> <li>• Introduction of a new requirement to allow for the used of old generations of power MOSFETs (5.3w)</li> <li>• Addition of clause 5.4 "Equipment Radiation Control Board"</li> </ul> <p><i>NOTE: Due to the amount of changes it was decided to create a new DOORS module that is not linked to the previous version.</i></p> |

# --- Table of contents ---

|                                                                                |           |
|--------------------------------------------------------------------------------|-----------|
| <b>Change log .....</b>                                                        | <b>3</b>  |
| <b>1 Scope.....</b>                                                            | <b>6</b>  |
| <b>2 Normative references .....</b>                                            | <b>7</b>  |
| <b>3 Terms, definitions and abbreviated terms.....</b>                         | <b>8</b>  |
| 3.1 Terms from other standards.....                                            | 8         |
| 3.2 Terms specific to the present standard .....                               | 9         |
| 3.3 Abbreviated terms.....                                                     | 11        |
| 3.4 Nomenclature .....                                                         | 13        |
| <b>4 Principles .....</b>                                                      | <b>14</b> |
| 4.1 Overview of RHA process.....                                               | 14        |
| 4.2 Radiation effects on components .....                                      | 15        |
| 4.3 Evaluation of radiation effects.....                                       | 16        |
| 4.4 Phasing of RHA with the different phases of a space project .....          | 16        |
| 4.4.1 Phase 0: Mission analysis, Phase A: Feasibility .....                    | 16        |
| 4.4.2 Phase B: Preliminary definition .....                                    | 16        |
| 4.4.3 Phase C: Detailed definition .....                                       | 17        |
| 4.4.4 Phase D: Qualification and production .....                              | 17        |
| 4.5 Radiation reviews .....                                                    | 17        |
| <b>5 Requirements.....</b>                                                     | <b>18</b> |
| 5.1 TID hardness assurance.....                                                | 18        |
| 5.2 TNID hardness assurance .....                                              | 23        |
| 5.3 SEE hardness assurance .....                                               | 27        |
| 5.4 Equipment Radiation Control Board (ERCB).....                              | 34        |
| <b>Annex A (normative) Mission radiation environment specification – DRD35</b> |           |
| A.1.1 Requirement identification and source document.....                      | 35        |
| A.1.2 Purpose and objective.....                                               | 35        |
| A.2.1 Contents .....                                                           | 35        |
| A.2.2 Special remarks .....                                                    | 36        |
| <b>Annex B (normative) Radiation analysis report - DRD .....</b>               | <b>37</b> |
| B.1.1 Requirement identification and source document.....                      | 37        |
| B.1.2 Purpose and objective.....                                               | 37        |

---

|                                               |                       |                                     |
|-----------------------------------------------|-----------------------|-------------------------------------|
| B.2.1                                         | Contents .....        | 37                                  |
| B.2.2                                         | Special remarks ..... | 39                                  |
| <b>Bibliography.....</b>                      |                       | <b>40</b>                           |
| <b>IE PUIDs/Section Cross Reference .....</b> |                       | <b>Error! Bookmark not defined.</b> |

# **Tables**

|                                                                                             |    |
|---------------------------------------------------------------------------------------------|----|
| Table 3-1: K values for P=0,9 and C=0,9 as function of the number of tested samples n ..... | 10 |
| Table 5-1: EEE part families potentially sensitive to TID.....                              | 19 |
| Table 5-2: List of EEE part families potentially sensitive to TNID .....                    | 24 |
| Table 5-3: List of EEE part families potentially sensitive to SEE .....                     | 28 |
| Table 5-4: Analog ICs Worst-case SET templates.....                                         | 29 |
| Table 5-5: Optocouplers Worst-case SET templates .....                                      | 30 |
| Table 5-6: Environment to be assessed based on LETth (Si devices) .....                     | 31 |

# 1 Scope ---

This standard specifies the requirements for ensuring radiation hardness assurance (RHA) of space projects. These requirements form the basis for a RHA program that is required for all space projects in conformance to ECSS-Q-ST-60. RHA program is project specific. This standard addresses the three main radiation effects on electronic components: Total Ionizing Dose (TID), Displacement Damage or Total Non-Ionizing Dose (TNID), and Single event Effects (SEE).

Spacecraft charging effects are out of the scope of this standard.

In this standard the word “component” refers to Electrical, Electronic, and Electromechanical (EEE) components only. Other fundamental constituents of space hardware units and sub-systems such as solar cells, optical materials, adhesives, polymers, and any other material are not covered by this standard.

This standard may be tailored for the specific characteristic and constraints of a space project in conformance with ECSS-S-ST-00.

# 2 Normative references ---

The following normative documents contain provisions which, through reference in this text, constitute provisions of this ECSS Standard. For dated references, subsequent amendments to, or revision of any of these publications do not apply. However, parties to agreements based on this ECSS Standard are encouraged to investigate the possibility of applying the more recent editions of the normative documents indicated below. For undated references, the latest edition of the publication referred to applies.

|                              |                                                                                                                        |
|------------------------------|------------------------------------------------------------------------------------------------------------------------|
| ECSS-S-ST-00-01              | ECSS system - Glossary of terms                                                                                        |
| ECSS-Q-ST-10-09              | Space product assurance - Nonconformance control system                                                                |
| ECSS-Q-ST-30                 | Space product assurance - Dependability                                                                                |
| ECSS-Q-ST-60                 | Space product assurance - Electrical, electronic, and electromechanical (EEE) components                               |
| ECSS-E-ST-10-04              | Space engineering - Space environment                                                                                  |
| ECSS-E-ST-10-12              | Space engineering - Methods for the calculation of radiation received and its effects, and a policy for design margins |
| ESCC 22900                   | ESCC Basic Specification: Total dose steady state irradiation test method                                              |
| ESCC 25100                   | ESCC Basic Specification: Single Event Effect Test Method and Guidelines                                               |
| ESCC 22500                   | ESCC Basic Specification: Guidelines for Displacement Damage Irradiation Testing                                       |
| MIL-STD-750<br>method 1080   | Test methods for semiconductor devices - Single event burnout and single event gate rupture test                       |
| MIL-STD-750<br>method 1019   | Test methods for semiconductor devices - Steady-state total dose irradiation procedure                                 |
| MIL-STD-750<br>method 1017   | Test methods for semiconductor devices -Neutron irradiation                                                            |
| MIL-STD-883<br>method 1019   | Microcircuits - Ionizing radiation (total dose) test procedure                                                         |
| MIL-STD-883<br>method 1017   | Microcircuits – Neutron irradiation                                                                                    |
| MIL-HDBK-814<br>(8 Feb 1994) | Military Handbook: Ionizing dose and neutron hardness Assurance guidelines for microcircuits and semiconductor devices |

# **Terms, definitions and abbreviated terms** ---

## **3.1 Terms from other standards**

- a. For this Standard, the terms and definitions from ECSS-S-ST-00-01 apply, in particular for the following terms:
  - 1. applicable document
  - 2. approval
  - 3. assurance
  - 4. derating
  - 5. EEE component
  - 6. environment
  - 7. equipment
  - 8. failure
  - 9. information
  - 10. lifetime
  - 11. outage
  - 12. recommendation
  - 13. required function
  - 14. requirement
  - 15. review
  - 16. risk
  - 17. specification
  - 18. standard
  - 19. subsystem
  - 20. system
  - 21. test
  - 22. traceability
  - 23. validation
  - 24. verification
  
- b. For the purpose of this Standard, the terms and definitions from ECSS-Q-ST-60 apply, in particular for the following terms:
  - 1. characterization
  - 2. commercial component
  - 3. screening
  - 4. space qualified parts

- c. For the purpose of this Standard, the terms and definitions from ECSS-E-ST-10-04 apply, in particular for the following terms:
  - 1. dose
  - 2. equivalent fluence
  - 3. fluence
  - 4. flux
  - 5. linear energy transfer (LET)
  
- d. For the purpose of this Standard, the terms and definitions from ECSS-E-ST-10-12 apply, in particular for the following terms:
  - 1. cross-section
  - 2. displacement damage
  - 3. LET threshold
  - 4. minimum radiation design margin (MRDM)
  - 5. multiple cell upset (MCU)
  - 6. (total) non-ionizing dose, (T)NID, or non-ionizing energy loss (NIEL) dose
  - 7. non-ionizing energy loss (NIEL)
  - 8. projected range
  - 9. radiation design margin (RDM)
  - 10. sensitive volume (SV)
  - 11. single event burnout (SEB)
  - 12. single event dielectric rupture (SEDR)
  - 13. single event effect (SEE)
  - 14. single event functional interrupt (SEFI)
  - 15. single event gate rupture (SEGR)
  - 16. single event latch-up (SEL)
  - 17. single event transient (SET)
  - 18. single event upset (SEU)
  - 19. solar energetic particle event (SEPE)
  - 20. total ionizing dose (TID)

## 3.2 Terms specific to the present standard

### 3.2.1 component type TIDS

TID level at which the part exceeds its parametric/functional requirements

### 3.2.2 component type TNIDS

TNID level at which the part exceeds its parametric/functional requirements

### 3.2.3 enhanced low dose rate sensitivity (ELDRS)

increased electrical parameter degradation of a part when it is irradiated with a lower dose rate

### 3.2.4 equivalent LET

averaged ionizing energy loss rate (dE/dx) along a charged particle track equivalent to the total amount of energy deposited in the traversed (sensitive) volume.

### 3.2.5 one sided tolerance limit

limit that will not be exceeded with a probability P and a confidence level C, assuming that TID degradation of electrical parameters follow a normal distribution law

NOTE If  $\langle \Delta x \rangle$  is the mean shift among tested population of n samples,  $\sigma$  is the standard deviation of the shift, and K is the one sided tolerance limit factor, then:

- $\Delta XL = \langle \Delta x \rangle + K \sigma$ , for increasing total dose shift
- $\Delta XL = \langle \Delta x \rangle - K \sigma$ , for decreasing total dose shift
- K depends on the number of tested samples n, the probability of success P and the confidence limit C. K values are available in MIL-HDBK-814. A 3 sigma ( $K=3$ ) approach is often used. With 10 samples tested it gives a probability of success P of 90% with a confidence level C of 99%. Table 3-1 gives the values of K as a function of the number of tested samples n for  $P=0,9$  and  $C=0,9$

**Table 3-1: K values for  $P=0,9$  and  $C=0,9$  as function of the number of tested samples n**

| n  | K     |
|----|-------|
| 3  | 4,259 |
| 4  | 3,188 |
| 5  | 2,742 |
| 6  | 2,493 |
| 7  | 2,332 |
| 8  | 2,218 |
| 9  | 2,133 |
| 10 | 2,065 |

### **3.2.6 radiation design lifetime**

lifetime under a specific radiation environment for which an electronic system has been designed. It can be different from nominal or extended mission lifetime

### **3.2.7 radiation design margin (RDM)**

ratio of TIDS over TIDL for TID and ratio of TNIDS over TNIDL for TNID

### **3.2.8 radiation lot acceptance test (RADLAT)**

see “radiation verification test”

### **3.2.9 radiation verification test (RVT)**

radiation test performed on sample coming from the same diffusion lot as the flight parts

NOTE This test is also known as “radiation lot acceptance test (RADLAT)”.

### **3.2.10 rebound**

devices exhibiting more degradation after annealing (room or elevated temperature) than after irradiation

### **3.2.11 total ionizing dose level (TIDL)**

calculated TID level received by the part at the end of its radiation design lifetime

### **3.2.12 total non-ionizing dose level (TNIDL)**

calculated TNID level received by the part at the end of its radiation design lifetime

## **3.3 Abbreviated terms**

For the purpose of this Standard, the abbreviated terms from ECSS-S-ST-00-01 and the following apply:

| <b>Abbreviation</b> | <b>Meaning</b>                                  |
|---------------------|-------------------------------------------------|
| APS                 | active pixel sensor                             |
| ASIC                | application specific integrated circuit         |
| BiCMOS              | bipolar complementary metal oxide semiconductor |
| BJT                 | bipolar junction transistor                     |
| CCD                 | charge coupled device                           |
| CDR                 | critical design review                          |
| DCL                 | declared part list                              |
| CIS                 | CMOS image sensor                               |
| CMOS                | complementary metal oxide semiconductor         |
| DRD                 | document requirements definition                |
| ELDRS               | enhanced low dose rate sensitivity              |
| EOL                 | end of lifetime                                 |
| ERCB                | Equipment Radiation Control Board               |
| EQSR                | Equipment Qualification Status Review           |

| <b>Abbreviation</b> | <b>Meaning</b>                                |
|---------------------|-----------------------------------------------|
| <b>FMECA</b>        | failure mode effects and criticality analysis |
| <b>GEO</b>          | geostationary Earth orbit                     |
| <b>HBT</b>          | heterojunction bipolar transistor             |
| <b>HCE</b>          | high current event                            |
| <b>HEMT</b>         | high electron mobility transistor             |
| <b>IGBT</b>         | Insulated-gate bipolar transistor             |
| <b>LED</b>          | light emitting diode                          |
| <b>LET</b>          | linear energy transfer                        |
| <b>MCU</b>          | multiple cell upset                           |
| <b>MMIC</b>         | microwave monolithic integrated circuit       |
| <b>MOS</b>          | metal oxide semiconductor                     |
| <b>MRDM</b>         | minimum radiation design margin               |
| <b>MRR</b>          | manufacturing readiness review                |
| <b>NCR</b>          | nonconformance report                         |
| <b>NIEL</b>         | non-ionizing energy loss                      |
| <b>PAD</b>          | part approval document                        |
| <b>PDR</b>          | preliminary design review                     |
| <b>PIC</b>          | photonic integrated circuit                   |
| <b>QR</b>           | qualification review                          |
| <b>RADLAT</b>       | radiation lot acceptance test                 |
| <b>RDM</b>          | radiation design margin                       |
| <b>RHA</b>          | radiation hardness assurance                  |
| <b>RVT</b>          | radiation verification test                   |
| <b>SEB</b>          | single event burnout                          |
| <b>SEDR</b>         | single event dielectric rupture               |
| <b>SEE</b>          | single event effect                           |
| <b>SEFI</b>         | single event functional interrupt             |
| <b>SEGR</b>         | single event gate rupture                     |
| <b>SEL</b>          | single event latch-up                         |
| <b>SET</b>          | single event transient                        |
| <b>SEU</b>          | single event upset                            |
| <b>SRR</b>          | system requirement review                     |
| <b>TID</b>          | total ionizing dose                           |
| <b>TIDL</b>         | total ionizing dose level                     |
| <b>TIDS</b>         | total ionizing dose sensitivity               |
| <b>TNID</b>         | total non-ionizing dose                       |
| <b>TNIDL</b>        | total non-ionizing dose level                 |
| <b>TNIDS</b>        | total non-ionizing dose sensitivity           |
| <b>TRR</b>          | Test Readiness Review                         |
| <b>VLSI</b>         | Very Large Scale Integration                  |
| <b>WCA</b>          | worst case analysis                           |

## 3.4 Nomenclature

The following nomenclature applies throughout this document:

- a. The word “shall” is used in this Standard to express requirements. All the requirements are expressed with the word “shall”.
- b. The word “should” is used in this Standard to express recommendations. All the recommendations are expressed with the word “should”.

NOTE It is expected that, during tailoring, recommendations in this document are either converted into requirements or tailored out.

- c. The words “may” and “need not” are used in this Standard to express positive and negative permissions, respectively. All the positive permissions are expressed with the word “may”. All the negative permissions are expressed with the words “need not”.
- d. The word “can” is used in this Standard to express capabilities or possibilities, and therefore, if not accompanied by one of the previous words, it implies descriptive text.

NOTE In ECSS “may” and “can” have completely different meanings: “may” is normative (permission), and “can” is descriptive.

- e. The present and past tenses are used in this Standard to express statements of fact, and therefore they imply descriptive text.

# 4 Principles

## 4.1 Overview of RHA process

Survival and successful operation of space systems in the space radiation environment cannot be ensured without careful consideration of the effects of radiation. RHA consists of all those activities undertaken to ensure that the electronics of a space system perform to their specification after exposure to the space radiation environment. A key element of RHA is the selection of components having a sufficient tolerance to radiation effects for their application. However, RHA process is not confined to the part level. It has implications with system requirements and operations, system and subsystems circuit design, and spacecraft layout. Figure 4-1 shows an overview of the process. The RHA process follows an iterative and top-down approach where mission radiation environment is calculated from mission requirements and the radiation environments models and rules defined in ECSS-E-ST-10-04. Top level requirements derived from mission radiation environment specification are employed as the starting point. Then, when necessary, radiation environment is transferred to component level via sector analysis or Monte Carlo analysis according to the methods described in ECSS-E-ST-10-12. Then, radiation analysis is performed at equipment level. Radiation sensitivity of each component is defined and its impact on equipment performance is analyzed. An equipment electronic design is validated when the equipment can fulfil its requirement under exposure to the mission space environment with a sufficient RDM.

![Flowchart of the RHA process overview showing the iterative and top-down approach from mission requirements to system response analysis.](bd671b21db63e6fdb2196e9b18502aac_img.jpg)

```
graph TD; MR[MISSION/SYSTEM REQUIREMENTS] --> SC[SYSTEM AND CIRCUIT DESIGN]; MR --> PMS[PARTS AND MATERIALS RADIATION SENSITIVITY]; MR --> RED[RADIATION ENVIRONMENT DEFINITION]; MR --> RL[RADIATION LEVELS WITHIN THE SPACECRAFT]; MR --> ACS[ANALYSIS OF THE CIRCUITS, COMPONENTS, SUBSYSTEMS AND SYSTEM RESPONSE TO THE RADIATION ENVIRONMENT]; SC --> PMS; SC --> RL; SC --> ACS; PMS --> ACS; RED --> RL; RL --> ACS; ACS --> MR; ACS --> SC; ACS --> PMS; ACS --> RED; ACS --> RL;
```

The diagram illustrates the RHA process overview as an iterative and top-down approach. It begins with 'MISSION/SYSTEM REQUIREMENTS' at the top left. From this box, arrows point to 'SYSTEM AND CIRCUIT DESIGN' (a white box), 'PARTS AND MATERIALS RADIATION SENSITIVITY' (a yellow box), 'RADIATION ENVIRONMENT DEFINITION' (a yellow box), 'RADIATION LEVELS WITHIN THE SPACECRAFT' (a yellow box), and directly to 'ANALYSIS OF THE CIRCUITS, COMPONENTS, SUBSYSTEMS AND SYSTEM RESPONSE TO THE RADIATION ENVIRONMENT' (a large yellow box at the bottom). 'SYSTEM AND CIRCUIT DESIGN' also has arrows pointing to 'PARTS AND MATERIALS RADIATION SENSITIVITY' and 'RADIATION LEVELS WITHIN THE SPACECRAFT'. 'PARTS AND MATERIALS RADIATION SENSITIVITY' and 'RADIATION LEVELS WITHIN THE SPACECRAFT' both have arrows pointing to the final analysis box. A large green curved arrow on the left side of the diagram indicates an iterative feedback loop from the final analysis box back to the 'MISSION/SYSTEM REQUIREMENTS' box. Another green curved arrow at the top points from the analysis box back to 'SYSTEM AND CIRCUIT DESIGN'.

Flowchart of the RHA process overview showing the iterative and top-down approach from mission requirements to system response analysis.

Figure 4-1: RHA process overview

## 4.2 Radiation effects on components

A comprehensive compendium of radiation effects is provided in ECSS-E-HB-10-12A section 3. Radiation effects that are important to be considered for instrument and spacecraft design fall roughly into three categories: degradation from TID, degradation from TNID, or NIEL or DDD, and SEE.

Degradation from TID in electronics is a cumulative, long term degradation mechanism due to ionizing radiation—mainly primary protons and electrons and secondary particles arising from interactions between these primary particles and spacecraft materials. It causes threshold shifts, leakage current and timing skews. The effect first appears as parametric degradation of the device and ultimately results in functional failure. It is possible to reduce TID with shielding material that absorbs most electrons and lower energy protons. As shielding is increased, shielding effectiveness decreases because of the difficulty in slowing down the higher energy protons. When a manufacturer advertises a part as “rad-hard”, he is almost always referring to its total ionizing dose characteristics. Rad-hard does not usually imply that the part is hard to non-ionizing dose or single event effects. In some cases, a “rad-hard” part can perform significantly worse in the space radiation environment if unrepresentative ground irradiation tests were performed by the manufacturer in the qualification process (e.g. Enhanced Low Dose Rate Sensitivity in linear bipolar devices).

Degradation from TNID or displacement damage is cumulative, long-term non-ionizing damage due to protons, electrons, and neutrons. These particles produce defects mainly in optoelectronics components such as APS, CCDs, and optocouplers. Displacement damage also affects the performance of linear bipolar devices but to a lesser extent. The effectiveness of shielding depends on the location of the device. Increasing shielding beyond a critical threshold, however, is not usually effective for optoelectronic components because the high-energy protons are capable of penetrating most spacecraft electronic enclosures. For detectors in instruments it is necessary to understand the instrument technology and geometry to determine the vulnerability to the environment.

SEEs result from ionization by a single charged particle as it passes through a sensitive junction of an electronic device. SEEs are caused by heavier ions, but for some devices, protons can also contribute. In some cases, SEEs are induced through direct ionization by the proton, but in most instances, proton induced effects result from secondary particles produced when the proton scatters of a nucleus in the device material. Some SEEs are non-destructive, as in the case of SEU, SET, MCU, and SEFI. Single event effects can also be destructive as in the case of single event SEL, SEGR, and SEB. The severity of the effect can range from noisy data to loss of the mission, depending on the type of effect and the criticality of the system in which it occurs. Shielding is not an effective mitigator for SEEs because they are induced by very penetrating high energy particles. The preferred method for dealing with destructive failures is to use SEE-hard parts. When SEE-hard parts are not available, latch-up protection circuitry is sometimes used in conjunction with failure mode analysis. (Note: Care is necessary when using SEL protection circuitry, because SEL can damage a microcircuit and reduce its reliability even when it does not cause outright failure.) For non-destructive effects, mitigation takes the form of, for example, error-detection and correction codes (EDAC), and filtering circuitry.

Knowledge of parts radiation sensitivity is an essential part of the overall RHA program. For the total dose environment, the damage is caused by the ionization energy absorbed by the sensitive materials, measured in rad or in gray (1 gray = 100 rad). This implies that a number of ionization sources can be used for simulation of space environment at ground level. However, the total dose response is also a strong function of the dose rate. Displacement damage can be simulated for any particle by using the value of NIEL. This implies that the effects of the displacement are to a first approximation, only proportional to the total energy loss through displacements and not dependant on the nature of the displacements. The single particle environment is usually simulated by the particle LET. For heavy ions this seems to be a reasonable measure of the environment as long as the particle type and energy are adjusted to produce the appropriate range of the ionization track. For protons, however, the LET is not the primary parameter since the upsets result primarily from secondary particles resulting from the interaction of proton with device's atoms. Thus, for the proton environment, the simulations should be conducted with protons of the appropriate energy.

## **4.3 Evaluation of radiation effects**

For assessing TID and TNID damages, electrical parameter drift values of each single individual component are derived from TID levels and TNID levels with an appropriate RDM. These drifts are used as input for WCA as defined in ECSS-Q-ST-30 clause 6.4.2.7. Rationale for establishing RDM for TID and TNID is provided in ECSS-E-ST-10-12.

SEE are generally analyzed during Failure Mode Effects and Criticality Analysis (FMECA) as defined in ECSS-Q-ST-30 clause 6.4.2.2. Operational impact of each single individual component SEE is analyzed and its criticality is assessed based on the SEE rate of occurrence with an appropriate RDM. Rationale for establishing RDM for SEE is provided in ECSS-E-ST-10-12.

## **4.4 Phasing of RHA with the different phases of a space project**

### **4.4.1 Phase 0: Mission analysis, Phase A: Feasibility**

Mission environment is defined and top-level radiation requirements can be derived. RHA requirements (e.g. RDM) are tailored to the specific project needs. Preliminary radiation characterization studies can be started to help technology selection and design trade-off activities.

### **4.4.2 Phase B: Preliminary definition**

For SRR, Mission environment and RHA requirements are finalized. Electronic design and spacecraft layout are defined. Preliminary shielding analyses can be started as well as radiation characterization activities.

### 4.4.3 Phase C: Detailed definition

Radiation characterization tests are performed. Equipment shielding analyses, equipment circuit design analyses (e.g. WCA, SEE analysis) are performed. Radiation analysis and WCA reports are provided in equipment CDR data package. When necessary, impact of radiation effect at equipment level is analysed at upper (subsystem and system) levels and documented in upper levels CDR data packages. At the end of phase C, most of the RHA work is completed.

### 4.4.4 Phase D: Qualification and production

Remaining RHA activities are radiation tests on flight lots (e.g. RVT). At this stage of program development, radiation effects issues resulting in redesign activities are very costly.

## 4.5 Radiation reviews

Equipment, subsystem, and system radiation analysis reports are part of project reviews data packages (from PDRs (all levels) to CDRs (all levels), QRs (all levels), and, finally, SAR. Radiation data on parts and part radiation testing are also reviewed during PAD review process. However, PAD approval for a part is only a provisional approval. As far as radiation effects are concerned, use of a part in a specific application is only validated when corresponding equipment radiation analysis and WCA reports are approved.

As-designed Equipment radiation reviews (ERCBs) held in after equipment PDR, are also performed on customer request. These reviews are useful to review available radiation test data, define the radiation tests to perform, define or review the test plans, review shielding strategy and preliminary shielding analysis. Then, another as-built ERCB, is held between MRR and TRR. The main goal of this review is to check if radiation data on flight parts is in conformity with radiation analysis. The timeline of the ERCBs is presented in Figure 4-2.

![Timeline of ERCBs flowchart](43837b056625d3d6ce615e4c02f163bb_img.jpg)

```
graph LR; PDR[PDR] --> ERCB1{As designed ERCB}; ERCB1 --> CDR[CDR]; CDR --> MRR[MRR]; MRR --> ERCB2{As built ERCB}; ERCB2 --> TRR[TRR]
```

The diagram illustrates the timeline of Equipment Radiation Characterization Reviews (ERCBs). It consists of a sequence of six elements connected by arrows: a blue rectangular box labeled 'PDR', followed by a yellow diamond-shaped box labeled 'As designed ERCB', then a blue rectangular box labeled 'CDR', a blue rectangular box labeled 'MRR', another yellow diamond-shaped box labeled 'As built ERCB', and finally a blue rectangular box labeled 'TRR'.

Timeline of ERCBs flowchart

Figure 4-2: Timeline of ERCBs

# 5 Requirements ---

## 5.1 TID hardness assurance

ECSS-Q-ST-60-15\_1620001

- a. Mission TID radiation environment shall be defined according to ECSS-E-ST-10-04 and documented in a Mission Radiation Environment Specification in conformance with the DRD in Annex A.

ECSS-Q-ST-60-15\_1620002

- b. For a program applying a phasing as defined in ECSS-M-ST-10 (phases 0, A, B, C, D, E, F), a draft version of the mission environment specification shall be available at the beginning of phase A and the final version is delivered at the latest at SRR.

ECSS-Q-ST-60-15\_1620003

- c. When the phasing as per ECSS-M-ST-10 is not applicable, final version of mission radiation environment shall be available at proposal time frame.

ECSS-Q-ST-60-15\_1620004

- d. The equipment unit shall be designed to account for TID during its radiation design lifetime according to the mission radiation environment specification.

ECSS-Q-ST-60-15\_1620005

- e. No effect due to TID shall cause permanent damage to a system or subsystem, or equipment, or degrade its performances outside its specification limits during its radiation design lifetime.

ECSS-Q-ST-60-15\_1620006

- f. Each EEE part belonging to families and sub-families listed in Table 5-1 shall be assessed for sensitivity to TID effects to the level specified in this table.

NOTE      Hybrids can also be treated as an electronic box.  
In this case, RHA requirements, as listed in this document, are applicable to every die used in the hybrid.

**Table 5-1: EEE part families potentially sensitive to TID**

| EEE part family                 | Sub family                                                                 | TIDL                      |
|---------------------------------|----------------------------------------------------------------------------|---------------------------|
| Diodes                          | High accuracy (<1 %) Zener used as voltage reference                       | If TIDL>100 krad-Si eq.   |
|                                 | Temperature compensated Zener used as Voltage reference with accuracy < 2% | If TIDL>100 krad-Si eq.   |
|                                 | Other Zener                                                                | If TIDL> 300 krad-Si eq.  |
|                                 | Switching, rectifier, Schottky                                             | If TIDL> 300 krad-Si eq.  |
|                                 | Microwave                                                                  | If TIDL> 300 krad-Si eq.  |
| Thyristors                      | -                                                                          | all                       |
| Integrated Circuits             | all                                                                        | all                       |
| MMICS                           | GaAs, GaN                                                                  | If TIDL > 300 krad-Si eq. |
|                                 | SiGe                                                                       | If TIDL > 100 krad-Si eq. |
| Oscillators (hybrids)           | -                                                                          | all                       |
| Image sensors                   | CCD, CIS, and others                                                       | all                       |
| Other optoelectronics           | Photodiodes<br>Phototransistors<br>LED<br>Optocouplers<br>Laser diodes     | all                       |
| PICs                            | all                                                                        | all                       |
| Transistors                     | BJT<br>MOS (Si, SiC)<br>Power GaN<br>IGBTs                                 | all                       |
|                                 | GaAs, GaN HEMTs                                                            | If TIDL> 300 krad-Si eq.  |
|                                 | SiGe HBTs                                                                  | If TIDL > 100 krad-Si eq. |
| Hybrids containing active parts | -                                                                          | all                       |

- g. TID test data used to assess TIDS shall comply with the following rules to be acceptable:
1. tests are performed in conformance to ESCC 22900, MIL-STD-883 method 1019, or MIL-STD-750 method 1019, and
  2. devices that contain bipolar transistors are tested at a dose rate of less than 360 rad/h, and
  3. tested parts are manufactured with technology identical to the technology of flight parts: same process, same diffusion mask, and same wafer fabrication facility, and
  4. test bias conditions are worse or equivalent to the application.

ECSS-Q-ST-60-15\_1620009

- h. If acceptable component TID test data does not exist, ground testing shall be performed in conformance to ESCC 22900 and requirements 5.1g.2 to 5.1g.4.

ECSS-Q-ST-60-15\_1620010

- i. Acceptable component TID test data shall be available latest at CDR for category C and D equipment and at EQSR for category A and B equipment.

NOTE Equipment categories according to heritage are defined in ECSS-E-ST-10-02.

ECSS-Q-ST-60-15\_1620011

- j. Radiation drifts to consider shall be the drifts after irradiation except for CMOS devices when a room temperature annealing was performed as per MIL-STD-883 method 1019 condition 3.11.2.

ECSS-Q-ST-60-15\_1620012

- k. Devices exhibiting “rebound” effects shall not be used, unless test data justifying device acceptance is provided to customer for review and validation prior use.

NOTE In MOS structures, rebound is a subset of Time Dependent Effects involving a net degradation of performance due to changes in trapped oxide charge and interface state density over periods of time of the order of several weeks.

ECSS-Q-ST-60-15\_1620013

- l. Component type TIDS shall be based on the parametric and functional limits given in component detail specification or manufacturer data sheet, or on the maximum parameter degradation acceptable to ensure equipment operation in compliance with equipment performance specification at the end of its radiation design lifetime.

NOTE TIDS is defined by comparing part parametric/functional requirements with TID test data.

ECSS-Q-ST-60-15\_1620014

- m. Component type TIDS shall be calculated as the Total Dose level at which the one-sided tolerance limit, as defined in MIL-HDBK-814, to guarantee a probability of survival  $P_s$  of at least 90 % with a confidence level of at least 90 % exceeds its limits as defined in requirement 5.11 (statistical approach).

NOTE See also Table 3-1 of definition 3.2.5 “one sided tolerance limit”.

ECSS-Q-ST-60-15\_1620015

- n. Any other approach to define TIDS shall be justified on a case-by-case basis and submitted to the customer for approval.

- o. Component received TID level (TIDL) shall be calculated using 3D Monte Carlo analysis or ray-tracing analysis in conformance with ECSS-E-ST-10-12.

NOTE 1 The solid sphere dose-depth curve is used in conjunction with the slant technique to evaluate the TIDL and the NORM technique to evaluate the equivalent shielding thickness (6-face analysis).

NOTE 2 The shell sphere dose-depth curve can be used in conjunction with the NORM technique both for evaluating TIDL and equivalent shielding thickness.

- p. Ray trace or sector-based analysis shall be implemented as follows:
1. Calculating the dose at the centre (called detector) of a sphere. The  $4\pi$  spherical surface surrounding the detector is sectored into N elemental solid angles equally distributed over the full space solid angle ( $4\pi$ ). The minimum number of sectors is 2000; or
  2. Calculating the dose at the centre of a parallelepiped with each face meshed in quadrilaterals and rays are launched from the detector within each cell. The number of cells per face is greater than 400 and at least 20 rays are launched per cell.

- q. If Reverse Monte-Carlo codes are used, acceptance criteria shall be as follows:
1. number of histories shall be greater than 2000 (NOVICE), or
  2. convergence results are higher than 98 %.

- r. TID MRDM shall be 1,2

NOTE TID\_MRDM is the minimum margin used to cover for uncertainties solely related to EEE parts (e.g. sample to sample variation, test uncertainties, etc.). Uncertainties relevant to the radiation environment are included in the inputs from the environmental specifications.

- s. For any component that is estimated to have on-orbit performance degradation due to TID, a WCA of the function shall be performed in accordance with requirements of ECSS-Q-ST-30 to demonstrate that the function performs within specification despite radiation induced drifts in its constituent part parameters at the end of its radiation design lifetime.

ECSS-Q-ST-60-15\_1620021

- t. If requirements 5.1r and 5.1s are not met, mitigation shall be implemented to eliminate the possibility of damage to equipment, subsystem and system, or degradation of its performance outside its specification limits during its radiation design lifetime.

ECSS-Q-ST-60-15\_1620022

- u. Mitigation shall be verified by analysis or test.

ECSS-Q-ST-60-15\_1620023

- v. The supplier shall document the TID analysis in the equipment radiation analysis report in conformance to Annex B – DRD for customer approval.

ECSS-Q-ST-60-15\_1620024

- w. A draft radiation analysis report shall be part of equipment PDR data package for category C or D equipment.

ECSS-Q-ST-60-15\_1620025

- x. A final version of radiation analysis report shall be issued for equipment CDR in case of equipment of category C or D and at equipment EQSR for category A or B equipment.

NOTE At that stage all RHA activities except RVTs are completed.

ECSS-Q-ST-60-15\_1620026

- y. If flight model part diffusion lot number is different from tested part diffusion lot number radiation verification test (RVT) on flight lot shall be performed according to the following condition:

- 1. for all optoelectronic parts, all lots;
- 2. for all other parts if TID RDM < 2.

ECSS-Q-ST-60-15\_1620027

- z. Conformity of RVT results with as designed radiation analysis shall be checked.

NOTE 1 As designed radiation analysis includes TIDL based on shielding, TIDS based on existing data and radiation drifts considered in WCA.

NOTE 2 RVT results are in conformance with radiation analysis when measured degradations are less than the ones considered in radiation and WCA analysis.

ECSS-Q-ST-60-15\_1620028

- aa. Nonconformities of RVT results with as designed radiation analysis shall be reported in a NCR in conformance with ECSS-Q-ST-10-09.

ECSS-Q-ST-60-15\_1620029

- bb. All radiation test reports, including RVT reports, shall be available for customer review at the latest between MRR and TRR.

- cc. The deposited dose during X-ray inspection of boards shall be recorded and accounted for the TID RDM calculation

NOTE Requirement 12.4d. of ECSS-Q-ST-70-61 requires that the maximum dose during X-ray inspection shall be less than 5 % of the eligible dose of the most sensitive component according to its specification.

## 5.2 TNID hardness assurance

ECSS-Q-ST-60-15\_1620031

- a. Mission TNID radiation environment shall be defined according to ECSS-E-ST-10-04 and ECSS-E-ST-10-12 and documented in Mission Radiation Environment Specification in conformance to Annex A.

ECSS-Q-ST-60-15\_1620032

- b. For a program applying a phasing as defined in ECSS-M-ST-10 (phases 0, A, B, C, D, E, F), a draft version of the mission environment specification shall be available at the beginning of phase A and the final version is delivered at the latest at SRR.

ECSS-Q-ST-60-15\_1620033

- c. When the phasing as per ECSS-M-ST-10 is not applicable, final version of mission radiation environment shall be available at proposal time frame.

ECSS-Q-ST-60-15\_1620034

- d. The equipment unit shall be designed to account for TNID/DD during its radiation design lifetime according to the mission environment specification.

ECSS-Q-ST-60-15\_1620035

- e. No effect due to TNID shall cause permanent damage to a system or subsystem, or equipment, or degrade its performances outside its specification limits during its radiation design lifetime.

ECSS-Q-ST-60-15\_1620036

- f. Each EEE part belonging to families and sub-families listed in Table 5-2 shall be assessed for sensitivity to TNID, to the levels specified in this table.

NOTE Guidelines and NIEL rates for calculating environment definition and monoenergetic equivalent proton fluences are provided in ECSS-E-HB-10-12 section 7.5.

**Table 5-2: List of EEE part families potentially sensitive to TNID**

| Family                | Sub-Family                                                             | TNIDL                                                                            |
|-----------------------|------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Image sensors         | CCD, CIS, others                                                       | all                                                                              |
| Other Optoelectronics | Photodiodes<br>Phototransistors<br>LED<br>Optocouplers<br>Laser diodes | all                                                                              |
| PICs                  | -                                                                      | all                                                                              |
| Integrated circuits   | Silicon monolithic bipolar or BiCMOS                                   | If $TNIDL > 2 \times 10^{11}$ p/cm <sup>2</sup> 50 MeV equivalent proton fluence |
| Diodes                | Zener used as voltage reference                                        | If $TNIDL > 2 \times 10^{11}$ p/cm <sup>2</sup> 50 MeV equivalent proton fluence |
| Thyristor             | -                                                                      | If $TNIDL > 2 \times 10^{11}$ p/cm <sup>2</sup> 50 MeV equivalent proton fluence |
| Transistor            | BJT<br>IGBT                                                            | If $TNIDL > 2 \times 10^{11}$ p/cm <sup>2</sup> 50 MeV equivalent proton fluence |

ECSS-Q-ST-60-15\_1620038

- g. Displacement Damage Equivalent Fluence at a given proton energy shall be derived from TNID versus depth curve in mission radiation environment specification using the same NIEL tables than the ones used to define the TNID environment specification.

ECSS-Q-ST-60-15\_1620039

- h. TNID data used to assess TNIDS shall satisfy the following criteria to be acceptable:
1. Tests are performed:
    - (a) for **all devices**: in accordance with ESCC 22500; or
    - (b) for **Si discrete devices only**: in accordance with or MIL-STD-883 method 1017 or MIL-STD-750 method 1017; or
    - (c) for **Si microcircuits only**: in accordance with MIL-STD-883 method 1017.
  2. Tested parts are manufactured with technology identical to the technology of flight parts: same process, same diffusion mask, and same wafer fabrication facility.
- NOTE to item 1: Historical test data obtained prior issue of ESCC22500 that have been validated by the customer is acceptable.

ECSS-Q-ST-60-15\_1620040

- i. If acceptable component TNID test data does not exist, ground testing shall be performed in conformance to requirement 5.2h.1.

ECSS-Q-ST-60-15\_1620041

- j. Acceptable TNID test data shall be available latest at CDR for category C and D equipment, and at EQSR for category A and B equipment.

ECSS-Q-ST-60-15\_1620042

- k. Component type TNIDS shall be based on the parametric and functional limits given in detail specification or manufacturer data sheet, or on the maximum parameter degradation acceptable to ensure equipment operation in compliance with equipment performance specification at the end of its radiation design lifetime.

NOTE TNIDS is defined by comparing part parametric/functional requirements with TNID test data

ECSS-Q-ST-60-15\_1620043

- l. Component type TNIDS shall be calculated as the TNID level at which the one-sided tolerance limit as defined in MIL-HDBK-814 exceeds its limits as defined in requirement 5.2k (statistical approach) to guarantee a probability of survival Ps of at least 90 % with a confidence level of at least 90 %.

NOTE See also Table 3-1 of definition 3.2.5 "one sided tolerance limit".

ECSS-Q-ST-60-15\_1620044

- m. Any other approach to define TNIDS shall be justified on a case-by-case basis and submitted to the customer for approval.

ECSS-Q-ST-60-15\_1620045

- n. Component TNID level (TNIDL) shall be calculated using 3D Monte Carlo or ray tracing analysis in conformance to ECSS-E-ST-10-12.

NOTE 3D Monte-Carlo analysis is the preferred method especially for electron rich environment (e.g. GEO or high MEO orbits).

ECSS-Q-ST-60-15\_1620046

- o. Reverse Monte-Carlo codes may be used, if the number of histories is greater than 2000 (NOVICE) or if TNIDL results have a convergence higher than 98 %.

ECSS-Q-ST-60-15\_1620047

- p. Calculation of TNIDL through ray-tracing analysis shall be submitted to the customer for approval and implemented as follows:

- 1. SLANT technique is used with the solid sphere non-ionizing dose-depth curve;

2. the non-ionizing dose is calculated at the centre (called the detector in the following) of a sphere: The  $4\pi$  spherical surface surrounding the detector is then be sectorised into N elementary solid angles equally distributed over the full space solid angle ( $4\pi$ ). The minimum number of sectors is 2000; or
3. the non-ionizing dose is calculated at the centre (called the detector in the following) of a parallelepiped with each face meshed with quadrilaterals and rays are launched from the detector within each cell. The number of cells per face is greater than 400 and at least 20 rays are launched per cell.

ECSS-Q-ST-60-15\_1620048

- q. TNID MRDM shall be 1,2.

NOTE TNID MRDM is the minimum margin used to cover for uncertainties solely related to EEE parts (e.g. sample to sample, test uncertainties and test limitations, etc.). Uncertainties relevant to the radiation environment are included in the inputs from the environmental specifications.

ECSS-Q-ST-60-15\_1620049

- r. For any component that is estimated to have on-orbit performance degradation due to TNID, a WCA of the function shall be performed in accordance with requirements of ECSS-Q-ST-30 to demonstrate that the function performs within specification despite radiation induced drifts in its constituent part parameters at the end of its radiation design lifetime.

ECSS-Q-ST-60-15\_1620050

- s. Both TNID and TID degradations shall be combined to define the component parameter drifts for WCA.

ECSS-Q-ST-60-15\_1620051

- t. If combined TNID and TID tests are used to get the combined TID/TNID sensitivity, such test plans shall be submitted to customer for approval.

NOTE Generally, TNID sensitive parts are also sensitive to TID.

ECSS-Q-ST-60-15\_1620052

- u. If requirements 5.2q and 5.2r cannot be met, mitigation shall be implemented to eliminate the possibility of damage to equipment, subsystem, and system or degradation of its performance outside its specification limits during its radiation design lifetime.

ECSS-Q-ST-60-15\_1620053

- v. TNID mitigation shall be verified by analysis or test.

ECSS-Q-ST-60-15\_1620054

- w. TNID analysis shall be documented in the equipment radiation analysis report in conformance with the DRD in Annex B.

ECSS-Q-ST-60-15\_1620055

- x. A draft radiation analysis report shall be part of equipment PDR data package for category C or D equipment.

ECSS-Q-ST-60-15\_1620056

- y. A final version of radiation analysis report shall be issued for equipment CDR for category C or D equipment and at equipment EQSR for category A or B equipment.

NOTE At that stage all RHA activities except RVTs are completed.

ECSS-Q-ST-60-15\_1620057

- z. If the flight model part diffusion lot number is different from tested part diffusion lot number radiation verification testing (RVT) on flight lot shall be performed according to the following conditions:

1. for non-Silicon discrete optoelectronic parts: all lots;
2. for image sensors and PICs: all lots;
3. for all other parts, if  $TNID\_RDM < 2$ .

ECSS-Q-ST-60-15\_1620058

- aa. Conformity of RVT results with as designed radiation analysis shall be checked.

NOTE 1 As designed radiation analysis includes TNIDL based on shielding, TNIDS based on existing data and radiation drift considered in WCA.

NOTE 2 RVT results are in conformance with radiation analysis when measured degradations are less than the ones considered in radiation and WCA analysis.

ECSS-Q-ST-60-15\_1620059

- bb. Nonconformities of RVT results with as designed radiation analysis shall be reported in a NCR in conformance with ECSS-Q-ST-10-09.

ECSS-Q-ST-60-15\_1620060

- cc. All radiation test reports, including RVT reports, shall be available for customer review between MRR and TRR.

## 5.3 SEE hardness assurance

ECSS-Q-ST-60-15\_1620061

- a. Mission SEE radiation environment shall be defined according to ECSS-E-ST-10-04 and documented in a Mission Radiation Environment Specification in conformance with the DRD in Annex A.

ECSS-Q-ST-60-15\_1620062

- b. For a program applying a phasing as defined in ECSS-M-ST-10 (phases 0, A, B, C, D, E, F), a draft version of the mission environment specification shall be available at the beginning of phase A and the final version is delivered at the latest at SRR.

- c. When the phasing as per ECSS-M-ST-10 is not applicable, final version of mission radiation environment shall be available at proposal time frame.

- d. No SEE shall cause damage to a system or a subsystem or an equipment, or induce performance anomalies or outages not compliant with mission specifications during its radiation design lifetime.

- e. Each EEE part belonging to families and sub-families listed in Table 5-3 shall be assessed for sensitivity to SEE.

NOTE A description of different types of SEE can be found in ECSS-E-ST-10-12.

**Table 5-3: List of EEE part families potentially sensitive to SEE**

| Family                                                                                                                                                 | Sub-family                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Diodes power                                                                                                                                           | Si Schottky*<br>Si > 400V**<br>SiC<br>GaN                              |
| Thyristors                                                                                                                                             | -                                                                      |
| Integrated Circuits                                                                                                                                    | all                                                                    |
| MMICs                                                                                                                                                  | all                                                                    |
| Transistors power                                                                                                                                      | Si, SiC MOSFET<br>GaN FET<br>IGBT                                      |
| Transistors microwave                                                                                                                                  | GaAs, GaN HEMT<br>SiGe HBT                                             |
| Image sensors                                                                                                                                          | CCD, CIS, others                                                       |
| PICs                                                                                                                                                   | all                                                                    |
| Discrete other optoelectronic                                                                                                                          | Photodiodes<br>Phototransistors<br>LED<br>Optocouplers<br>Laser diodes |
| NOTE 1: (*) the perimeter of potential SEB sensitivity Schottky Si diodes is limited to devices whose reverse voltage Vr is > 50% of specified Vr max. |                                                                        |
| NOTE 2: (**) Si non-Schottky diodes rated > 400V can also be sensitive to SEB when reverse voltage Vr is > 50% of specified Vr max.                    |                                                                        |

- f. SEE test data shall meet the following criteria to be acceptable:
1. Test are performed in conformance to
    - (a) MIL-STD-750 method 1080 for power MOSFET,
    - (b) ESCC 25100 for all other parts.
  2. Tested parts are manufactured with technology identical to the technology of flight parts: same process and same diffusion mask.
  3. Test conditions are worse or equivalent to the application.
 

NOTE 1 Useful information about SEE testing is also provided in EIA/JESD 57.

NOTE 2 Test conditions include, but are not limited to, bias conditions, clock frequency, test pattern, and temperature.

ECSS-Q-ST-60-15\_1620068

- g. If acceptable component test data does not exist, heavy-ion ground testing shall be performed.

ECSS-Q-ST-60-15\_1620069

- h. For the criticality analysis of SET in analog ICs, worst case SET templates in Table 5-4 may be used, for the listed device types only, in the absence of acceptable test data.

ECSS-Q-ST-60-15\_1620070

**Table 5-4: Analog ICs Worst-case SET templates**

| Device type                                                                | SET nature at device output                       |
|----------------------------------------------------------------------------|---------------------------------------------------|
| OP-amps                                                                    | $V_{\max} = \pm V_{cc} \ \& \ t_{\max} = 15\mu s$ |
| Comparators                                                                | $V_{\max} = \pm V_{cc} \ \& \ t_{\max} = 10\mu s$ |
| Voltage Regul.                                                             | $V_{\max} = \pm V_{cc} \ \& \ t_{\max} = 10\mu s$ |
| Voltage Ref.                                                               | $V_{\max} = \pm V_{cc} \ \& \ t_{\max} = 10\mu s$ |
| NOTE: SET recovery time can be longer than the response time of the device |                                                   |

ECSS-Q-ST-60-15\_1620071

- i. For the criticality analysis of SET in optocouplers, worst case SET templates in Table 5-5 may be used in the absence of acceptable test data.
- NOTE 1 The definitions of optocoupler families as described in the notes of Table 5-5 only apply for this requirement and cannot be generic and used in another context.
- NOTE 2 The duration of the worst-case SET template should be selected for a collector pull-up resistor  $R_c$  of value higher than the one considered for the application.

- NOTE 3 The response time of the device should be consistent with the SET worst case templates in Table 5-5.
- NOTE 4 Digital optocouplers can exhibit positive and negative going SETs, while all other types of optocouplers are only exhibiting negative going SETs.

ECSS-Q-ST-60-15\_1620072

- j. Optocoupler types that do not belong to any of the families listed in Table 5-5 shall be tested.

ECSS-Q-ST-60-15\_1620073

**Table 5-5: Optocouplers Worst-case SET templates**

| Optocoupler Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | SET nature at device output (optocoupler and Rc) |                                  |                                 |                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|----------------------------------|---------------------------------|-----------------------|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Amplitude                                        | Duration as function of Rc value |                                 |                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                  | $\leq 1k\Omega$                  | $1k\Omega < R_c \leq 10k\Omega$ | $R_c \leq 100k\Omega$ |
| Analog                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | $V_{max} = 60\% V_{cc}$                          | 0,5 $\mu s$                      | 2 $\mu s$                       | 5 $\mu s$             |
| Standard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | $V_{max} = 30\% V_{cc}$                          | 75 $\mu s$                       | 200 $\mu s$                     | 1,5 ms(*)             |
| LED input and digital output stage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | $V_{max} = V_{cc}$                               | 3 $\mu s$                        |                                 |                       |
| Fast linear                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | $V_{max} = V_{cc}$                               | 500 ns                           | 20 $\mu s$                      | 1 ms                  |
| NOTE 1: (*) in this case, SET waveform may embed a glitch of less than 100 ns whose amplitude can reach up to 60% of Vcc.<br>NOTE 2: An analog optocoupler is defined as a LED coupled to a Photodiode.<br>NOTE 3: A standard optocoupler is defined as a LED coupled to a Phototransistor with an open collector output, and a switching time above 1 $\mu s$ .<br>NOTE 4: Fast linear optocouplers have a bandwidth of at least several MHz.<br>NOTE 5: Pullup resistor Rc is not always present on digital output optocouplers and when it is, it has little impact on SET duration. |                                                  |                                  |                                 |                       |

ECSS-Q-ST-60-15\_1620074

- k. All SEE testing shall be performed in conformance to requirements of clause 5.3f.

ECSS-Q-ST-60-15\_1620075

- l. SEE analysis and need for proton test data shall take place based on LET threshold (LET<sub>th</sub>) in Silicon of the candidate devices as specified in Table 5-6.

NOTE In accordance with this table, no further analysis is necessary above a LET<sub>th</sub> of 60 MeVcm<sup>2</sup>/mg, because parts are commonly considered immune to SEE in the space environment.

**Table 5-6: Environment to be assessed based on LETth (Si devices)**

| Device LETth (MeVcm <sup>2</sup> /mg) | Environment to be assessed                                                   |
|---------------------------------------|------------------------------------------------------------------------------|
| LETth < 15                            | Heavy ions (GCR, solar event ions)<br>Protons (trapped, solar event protons) |
| LETth= 15-60                          | Heavy ions (GCR, solar event ions)                                           |
| LETth>60                              | No analysis required                                                         |

ECSS-Q-ST-60-15\_1620077

- m. Below a LETth level of 60 MeVcm<sup>2</sup>/mg, SEE analysis shall be performed.

ECSS-Q-ST-60-15\_1620078

- n. Below a LETth of 15 MeVcm<sup>2</sup>/mg, proton induced sensitivity analysis shall be analyzed.

NOTE CMOS VLSI devices whose technology feature size is lower or equal to 65 nm and an ion SEE LET threshold lower than 1 MeVcm<sup>2</sup>/mg can be sensitive to SEE induced by protons via direct ionization mechanism.

ECSS-Q-ST-60-15\_1620079

- o. The LETth levels as described in the requirements 5.3m and 5.3n shall be recalculated for parts made of other material than Silicon.

NOTE For example: GaAs, SiC, GaN, SiGe.

ECSS-Q-ST-60-15\_1620080

- p. Proton SEE test data shall satisfy requirement 5.3f to be acceptable.

ECSS-Q-ST-60-15\_1620081

- q. If acceptable proton SEE data is not available, proton ground testing shall be performed according to 5.3f.

ECSS-Q-ST-60-15\_1620082

- r. Acceptance of simulation tools to obtain proton SEU cross-section curves on digital devices shall be approved by customer.

NOTE For SEUs, proton cross-section curve can be obtained from heavy ion cross-section curve with simulation tools such as SIMPA or PROFIT.

ECSS-Q-ST-60-15\_1620083

- s. For any component that is not immune to destructive SEE analysis, it shall be demonstrated that the probability of occurrence in the mission environment and during its radiation design lifetime is more than 10 times lower than component intrinsic failure rate or the event rate is taken into account in the equipment reliability calculation.

NOTE Examples of destructive SEE are: SEL, SEB, SEGR and SEDR.

ECSS-Q-ST-60-15\_1620084

- t. The use of SEL or HCE protection circuitry shall be based on accurate SEL or HCE current characterization of the device to protect with a flight representative protection circuitry and submitted to customer for approval

NOTE Even if a SEL or an HCE is not always destructive, part reliability can be affected by high current condition during SELs.

ECSS-Q-ST-60-15\_1620085

- u. One of the following two power MOSFET SEB/SEGR assessment methods shall be applied:

1. SEB/SEGR failure rates based on SEB/SEGR cross-section versus equivalent LET curves;
2.  $V_{DSmax}$ ,  $V_{Csoff}$  max derating based on  $V_{DS}$  versus  $V_{GS}$  SOA.

NOTE Power MOSFET have a deep sensitive volume. Therefore, LET can vary significantly along ion path in sensitive volume.

ECSS-Q-ST-60-15\_1620086

- v. Practical implementation of the method used to assess power MOSFET SEB/SEGR sensitivity, as specified in the requirement 5.3u, if not specified by the customer shall be defined by the supplier and submitted to customer for approval.

ECSS-Q-ST-60-15\_1620087

- w. For old parts from International Rectifier generation 3 and 4 device types, with  $BVDSS < 200$  V, following derating rules on bias conditions ( $V_{DS}$ ,  $V_{GS}$ ) may be used to prevent SEB and SEGR permanent damage:

1.  $V_{DS} < 0,5 \times BVDSS$
2. N Channel :  $V_{GS} > 0$  V
3. P Channel :  $V_{GS} < 0$  V

NOTE P-Channel MOSFETs are intrinsically insensitive to SEB.

ECSS-Q-ST-60-15\_1620088

- x. For non-destructive SEEs the criticality of a component in its specific application shall be defined including impacts at higher level, i.e. subsystem and system.

NOTE 1 Examples of non-destructive SEE are: SEU, SET, MCU, and SEFI.

NOTE 2 A SEE is considered critical when it has an impact on the specified performances, the unit availability, data integrity or functional state.

ECSS-Q-ST-60-15\_1620089

- y. Criticality analysis of SETs in analog ICs and optocouplers shall be performed via electrical simulations with SPICE or equivalent tool applying min/max voltage directly at the IC output according to the worst case SET for this device (from test data or template).

ECSS-Q-ST-60-15\_1620090

- z. In case a SET is considered critical based on an analysis with the templates in Table 5-4 or Table 5-5, a SET test in application conditions shall be performed.

ECSS-Q-ST-60-15\_1620091

- aa. The mission event rate shall be calculated when a SEE on a given component for a given application is considered critical or potentially critical.

ECSS-Q-ST-60-15\_1620092

- bb. The mission event rate (ions and protons) shall be calculated for the mission background environment and a solar event environment as defined in mission radiation environment specification in conformance to ECSS-E-ST-10-12.

ECSS-Q-ST-60-15\_1620093

- cc. The following RDM shall be applied on calculated proton error rate:
  - 1. 10, when proton error rate is based on simulation from heavy ion data;
  - 2. No RDM, when proton error rate is based on actual proton test data.

NOTE No RDM is applied on heavy-ion rates.

ECSS-Q-ST-60-15\_1620094

- dd. The calculated event rates shall be such that the application meets the projected availability, functional, performance and reliability requirements.

ECSS-Q-ST-60-15\_1620095

- ee. If requirements 5.3s and 5.3dd are not met, mitigation shall be implemented to eliminate the possibility of damage to equipment or degradation of its functionality and performance outside its specification limits during its radiation design lifetime.

ECSS-Q-ST-60-15\_1620096

- ff. Mitigation shall be verified by analysis or test.

ECSS-Q-ST-60-15\_1620097

- gg. All data and analysis shall be documented in Radiation Analysis report in conformance with the DRD in Annex B.

ECSS-Q-ST-60-15\_1620098

- hh. A draft radiation analysis report shall be part of equipment PDR data package for category C or D equipment.

- ii. A final version of radiation analysis report shall be issued for equipment CDR for category C or D equipment and at equipment EQSR for category A or B equipment.

- jj. All radiation test reports shall be available for customer review before MRR.

## 5.4 Equipment Radiation Control Board (ERCB)

- a. An “as designed” ERCB shall be held between PDR and CDR when a baseline design is mature enough and inputs documents are updated accordingly to cover the following points:
  - 1. TID, TNID, and SEE test reports;
  - 2. traceability of EEE parts versus radiation test data including PAD review;
  - 3. identification of part types that need to be submitted to an evaluation or a RVT (TID, TNID), and review of radiation test plans for these parts;
  - 4. preliminary shielding analysis;
  - 5. preliminary assessment on TID and TNID;
  - 6. preliminary SEE criticality analysis including mitigation strategies;
  - 7. consideration of radiation impact at equipment level propagating to higher level (subsystem, system);
  - 8. part selection;
  - 9. tools and calculation methods used;
  - 10. RHA RFD/RFW;
  - 11. Assessment on open radiation alerts.

NOTE Input documents for an ERCB are for example: radiation analysis, DCL, FMEA, WCA, and PSSA.

- b. An “as-built” radiation review shall be held before TRR to validate the as designed status provided in the final radiation analysis and as built verification activities, covering the following points:
  - 1. final shielding analysis;
  - 2. final assessment on TID and TNID;
  - 3. final SEE criticality analysis;
  - 4. traceability of flight lots;
  - 5. Validation of radiation data including RVT results;
  - 6. RHA RFD/RFW;
  - 7. assessment on open radiation alerts.

# **Annex A (normative)****Mission radiation environment specification – DRD** ---

## **A.1 DRD identification**

### **A.1.1 Requirement identification and source document**

This DRD is called from ECSS-Q-ST-60-15, requirements 5.1a, 5.2a, and 5.3a.

### **A.1.2 Purpose and objective**

The purpose of mission environment specification is to document in a single place the particle fluxes (shielded and unshielded), the TID and TNID versus shielding dose curves, and the LET spectra.

## **A.2 Expected Response**

### **A.2.1 Contents**

#### **<1> Mission definition**

ECSS-Q-ST-60-15\_1620103

- a. Mission orbit, duration, and, possibly, launch date shall be documented.

#### **<2> TID and TNID environment**

ECSS-Q-ST-60-15\_1620104

- a. High energy electrons and protons spacecraft incident fluence versus energy spectra shall be presented with figures and tables.

NOTE High energy electrons and protons can be trapped and solar.

ECSS-Q-ST-60-15\_1620105

- b. Total dose curve in Silicon versus Aluminium shield thickness for a solid sphere geometry shall be presented with figure and table.

NOTE Aluminium shield thickness can vary between 10 µm and 100 mm).

ECSS-Q-ST-60-15\_1620106

- c. Total non-ionizing dose curves for Silicon and GaAs materials versus Aluminium shield thickness for a solid sphere geometry shall be presented with figure and table.

NOTE      Aluminium shield thickness can vary between  
10  $\mu\text{m}$  and 100 mm).

#### <3>      **SEE environment**

ECSS-Q-ST-60-15\_1620107

- a. GCR fluxes versus LET spectrum calculated for a given Aluminium shield thickness (e.g. 1  $\text{g}/\text{cm}^2$ ) shall be presented with figure and table.

ECSS-Q-ST-60-15\_1620108

- b. Solar particle event ion fluxes versus LET spectrum for a given Aluminium shield thickness (e.g. 1  $\text{g}/\text{cm}^2$ ) shall be presented with figure and table.

ECSS-Q-ST-60-15\_1620109

- c. Trapped and solar protons fluxes versus energy spectra shall be presented with figures and tables.

### **A.2.2      Special remarks**

None.

# Annex B (normative)Radiation analysis report - DRD ---

## B.1 DRD identification

### B.1.1 Requirement identification and source document

This DRD is called from ECSS-Q-ST-60-15, requirements 5.1v, 5.2w and 5.3gg.

### B.1.2 Purpose and objective

The purpose of the equipment Radiation Analysis report is to document in a single place all baseline information (data, assumptions, methods and techniques) used for the radiation analyses, and the results obtained.

## B.2 Expected response

### B.2.1 Contents

#### <1> Identification of parts sensitive to radiation effects

ECSS-Q-ST-60-15\_1620110

- a. The radiation analysis report shall list all radiation sensitive parts, as defined in ECSS-Q-ST-60-15 Table 5-1, Table 5-2, and Table 5-3, extracted from the DCL.

ECSS-Q-ST-60-15\_1620111

- b. The list shall include the full part number and manufacturer information.

#### <2> TID analysis

ECSS-Q-ST-60-15\_1620112

- a. The radiation analysis report shall provide TID tolerance of each sensitive component with reference of test report.

ECSS-Q-ST-60-15\_1620113

- b. The radiation analysis report shall identify the parts submitted to RVT.

ECSS-Q-ST-60-15\_1620114

- c. The radiation analysis report shall include the description of mechanical model, assumption, method and tools used for ray trace or Monte Carlo analysis, and results obtained.

ECSS-Q-ST-60-15\_1620115

- d. The radiation analysis report shall present TIDL and TIDS for each part as well as RDM and associated status for lot acceptance.

ECSS-Q-ST-60-15\_1620116

- e. The radiation analysis report shall reference the TID drifts to be considered in WCA as well as description of TID mitigations implemented (if any).

#### **<3> TNID analysis**

ECSS-Q-ST-60-15\_1620117

- a. The radiation analysis report shall provide TNID tolerance of each sensitive component with reference of test report.

ECSS-Q-ST-60-15\_1620118

- b. The radiation analysis report shall identify the parts submitted to RVT.

ECSS-Q-ST-60-15\_1620119

- c. The radiation analysis report shall include the description of mechanical model, assumption, method and tools used for ray-trace or Monte-Carlo analysis, and results obtained.

ECSS-Q-ST-60-15\_1620120

- d. The radiation analysis report shall present TNIDL and TNIDS for each part as well as RDM and associated status for lot acceptance.

ECSS-Q-ST-60-15\_1620121

- e. The radiation analysis report shall reference the TNID drifts to be considered in WCA as well as description of TNID mitigations implemented (if any).

#### **<4> SEE analysis**

ECSS-Q-ST-60-15\_1620122

- a. The radiation analysis report shall provide SEE tolerance of each sensitive component and each SEE type with reference of test report.

ECSS-Q-ST-60-15\_1620123

- b. The radiation analysis report shall describe the assumptions methods and tools used for SEE rate predictions as well as SEE rates.

ECSS-Q-ST-60-15\_1620124

- c. The radiation analysis report shall present SEE criticality analysis results:
  - 1. Comparison of application voltage and SEE SOA for devices sensitive to SEB/SEGR;
  - 2. Detailed SET analysis with input considered (template or test data) and description of impact at equipment level, and mitigation (if any);

3. SEU/SEFI analysis with description of impact at equipment level, mitigation (if any), and methods of recovery;
4. Identification of SEE that propagate at higher level (subsystem/system).

NOTE The analyses of items 2, 3 and 4 can be included in WCA or FMEA documents.

### **B.2.2 Special remarks**

None.

# Bibliography ---

|                 |                                                                                                                          |
|-----------------|--------------------------------------------------------------------------------------------------------------------------|
| ECSS-S-ST-00    | ECSS system – Description, implementation and general requirements                                                       |
| ECSS-E-HB-10-12 | Space engineering - Methods for the calculation of radiation received and its effects and a policy for the design margin |
| EIA/JESD 57     | Test Procedure For The Management Of Single-event Effects In Semiconductor Devices From Heavy Ion Irradiation            |