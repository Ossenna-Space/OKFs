

![JSC Engineering NASA logo](2dfa6ac3edfe874f68aa0cbccaa42322_img.jpg)

The logo is a triangular shield with a blue background. Inside, there is a white stylized 'A' with a yellow star and a white swoosh. The text 'JSC' is at the top, 'ENGINEERING' is in the middle, and 'NASA' is at the bottom.

JSC Engineering NASA logo

**JSC-67551**

**BASIC**

**16 APRIL 2021**

# JSC Avionics Ionizing Radiation Effects Standard (AIRES)

**Engineering Directorate**

**Office of Primary Responsibility: EV5 / Avionic  
Systems Division**

Compliance is Mandatory

## Public Release Statement

This document has been reviewed for Proprietary, SBU, and Export Control (ITAR/EAR) information and has been determined to be non-sensitive.

It has been released to the public via the NASA Scientific and Technical Information (STI) Document Availability Authorization (DAA) process  
NF-1676 20230013399

![NASA logo](d3294dc879b451b369c0b06f42e9b39f_img.jpg)

The NASA logo is a circular emblem with a blue background. It features the word 'NASA' in white, with a red swoosh and a white star.

NASA logo

**National Aeronautics and  
Space Administration**

### Cover page for the JSC-67551 Public Release Version

The original scope of JSC-67551 Avionics Ionizing Radiation Effects Standard (AIRES) was limited to Government Furnished Equipment (GFE) provided / furnished by the NASA Johnson Space Center (JSC). JSC-67551 identifies JSC GFE Radiation Hardness Assurance (RHA) process stakeholders and assigns them specific roles and responsibilities. For successful adoption of JSC-67551 by programs and projects outside the NASA JSC GFE realm, it is critical that these roles and responsibilities – including the RHA process technical authority - be re-assigned early on to appropriate project, program and/or customer stakeholders, and participation be defined in the appropriate panels and/or boards. Fundamentally, this re-assignment constitutes additional required tailoring of the standard, is in scope of JSC-67551 requirement RAD003 (memorandum of agreement, MoA), and requires customer approval. Stakeholders, roles and responsibilities defined in JSC-67551 that must be re-assigned / re-defined include at the minimum those below:

1. The JSC Ionizing Radiation Panel (IRP) including chair, contractor and customer participation, and decision authority
2. The technical authority for JSC-67551 requirements tailoring, interpretation verification, and other JSC-67551 in-scope tasks
3. The ASD Ionizing Radiation Effects Technical Discipline Lead (TDL)
4. ASD ionizing radiation engineering
5. The JSC EA Parts Control Board (EA PCB) or other cognizant program board with authority to accept risk

In addition, the choice of requirement tier(s) represents a risk decision. Depending upon the project and/or program requirements including design & construction (D&C) standards, project- and/or program-acceptable risk tolerance posture, and other factors, specific instances of JSC-67551 requirement tier selection or tailoring require waiver, deviation, or equivalent mechanisms for program risk acceptance.

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 203" src="521a8c9f9a0b2d9d56a4e87b68c24964_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 2 of 53           |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

## Change Record

| Revision / DCN | Date          | Originator                  | Approvals                      | Description     |
|----------------|---------------|-----------------------------|--------------------------------|-----------------|
| Basic          | 16 April 2021 | <a href="#">Razvan Gaza</a> | Per <a href="#">EA-CCB-444</a> | Initial Release |
|                |               |                             |                                |                 |
|                |               |                             |                                |                 |

See Cover for full disclosure. Verify correct revision before use at  
<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>.

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="e7d8b5b0b16d40adb8b16585e46611c1_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 3 of 53           |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

**Prepared by: Razvan Gaza**

Digitally signed by Razvan Gaza  
Date: 2021.05.04 17:24:19 -05'00'

Razvan Gaza, Ph.D.

Date

Ionizing Radiation Effects Technical Discipline Lead

Avionic Systems Division

**Reviewed by: SUSAN MORGAN**

Digitally signed by SUSAN MORGAN  
Date: 2021.05.10 16:24:45 -05'00'

Susan Morgan

Date

Branch Chief, EV5 Electronic Design and Manufacturing Branch

Avionic Systems Division

**Concurred by: BRUCE MANNERS**

Digitally signed by BRUCE MANNERS  
Date: 2021.05.13 13:20:14 -05'00'

Bruce Manners

Date

Division Chief, Avionic Systems Division

Engineering Directorate

**Approved by: Carolyn Fritz**

Digitally signed by Carolyn Fritz  
Date: 2021.05.18 13:38:53 -05'00'

Julie Kramer White, Director

Date

Engineering Directorate

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>.

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 203" src="3005db07d7ee45cc8e0733b0c57ea82c_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 4 of 53           |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

## Table of Contents

|                                                                                                |           |
|------------------------------------------------------------------------------------------------|-----------|
| <b>1. Introduction</b>                                                                         | <b>7</b>  |
| 1.1 PURPOSE.....                                                                               | 7         |
| 1.2 SCOPE.....                                                                                 | 7         |
| 1.3 DESIGN REQUIREMENTS.....                                                                   | 8         |
| 1.4 APPLICABLE DOCUMENTS.....                                                                  | 8         |
| 1.5 REFERENCE DOCUMENTS.....                                                                   | 9         |
| 1.6 ACRONYMS AND DEFINITIONS.....                                                              | 9         |
| <b>2. Requirements list</b>                                                                    | <b>13</b> |
| <b>3. Radiation Hardening Assurance Executive Summary</b>                                      | <b>18</b> |
| <b>4. Radiation Hardening Assurance (RHA) Process- and Administrative Requirements</b>         | <b>21</b> |
| 4.1 AIRES TAILORING AND REQUIREMENT VERIFICATION PROCESS.....                                  | 21        |
| 4.1.1 REQUIREMENT TIERS.....                                                                   | 22        |
| 4.1.2 MEMORANDUM OF AGREEMENT (MOA).....                                                       | 25        |
| 4.2 RHA ANALYSES.....                                                                          | 26        |
| 4.3 RHA SCHEDULE.....                                                                          | 27        |
| <b>5. EEE Parts Selection and Characterization Requirements for Total Dose</b>                 | <b>29</b> |
| <b>6. EEE Parts Selection and Characterization Requirements for Single-Event Effects (SEE)</b> | <b>32</b> |
| 6.1 ACCEPTABLE SOURCES OF SEE RADIATION DATA.....                                              | 33        |
| 6.2 SIMILARITY.....                                                                            | 34        |
| 6.3 SEE RADIATION LOT ACCEPTANCE TESTS (SLAT).....                                             | 35        |
| 6.4 SEE TEST DATA COMMON REQUIREMENTS.....                                                     | 35        |
| 6.5 SEL TEST DATA REQUIREMENTS.....                                                            | 36        |
| 6.6 SEU/SET/SEFI TEST DATA REQUIREMENTS.....                                                   | 37        |
| 6.7 SEB/SEGR/SEDR TEST DATA REQUIREMENTS.....                                                  | 37        |
| 6.8 SEE PROTON TESTING.....                                                                    | 39        |
| <b>7. SEE circuit level testing</b>                                                            | <b>40</b> |
| <b>8. SEE Analysis</b>                                                                         | <b>40</b> |
| 8.1 RADIATION ASSESSMENT MATRIX (RAM).....                                                     | 42        |

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>.

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="887e5be4ad414103b9ed733d140ad3d0_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 5 of 53           |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

|                                   |                                                                                                                                 |           |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------|-----------|
| <b>9.</b>                         | <b>SEE Test Planning and Reporting</b>                                                                                          | <b>43</b> |
| 9.1                               | RADIATION TEST PLAN .....                                                                                                       | 43        |
| 9.2                               | RADIATION TEST REPORT .....                                                                                                     | 43        |
| <b>10.</b>                        | <b>The JSC Ionizing Radiation Panel (IRP)</b>                                                                                   | <b>44</b> |
| 10.1                              | RADIATION NSPAR PROCESS .....                                                                                                   | 44        |
| <b>11.</b>                        | <b>Documentation</b>                                                                                                            | <b>45</b> |
| 11.1                              | RADIATION TEST PLAN .....                                                                                                       | 45        |
| 11.2                              | RADIATION TEST REPORT .....                                                                                                     | 46        |
| 11.3                              | DATA RETENTION REQUIREMENTS .....                                                                                               | 46        |
| <b>12.</b>                        | <b>Additional Guidance</b>                                                                                                      | <b>47</b> |
| 12.1                              | PART SELECTION BEST PRACTICES.....                                                                                              | 47        |
| 12.2                              | SEE RATE CALCULATIONS .....                                                                                                     | 48        |
| 12.2.1                            | HEAVY ION RATES.....                                                                                                            | 48        |
| 12.2.2                            | PROTON RATES .....                                                                                                              | 48        |
| 12.2.3                            | PROTON RATES DERIVED FROM HEAVY ION DATA.....                                                                                   | 48        |
| 12.2.4                            | HEAVY ION RATES DERIVED FROM PROTON DATA.....                                                                                   | 48        |
| 12.3                              | RADIATION SUSCEPTIBILITY OF DIFFERENT EEE PART TYPES AND TECHNOLOGIES .....                                                     | 49        |
| 12.4                              | SET SIGNATURES .....                                                                                                            | 49        |
| 12.5                              | RADIATION DESIGN RECOMMENDATIONS FOR NON-CRITICAL HARDWARE .....                                                                | 50        |
| 12.6                              | SEE HEAVY ION TESTING: HIGH ENERGY (NSRL) VS. LOW ENERGY (TAMU, LBNL); PART-LEVEL CHARACTERIZATION VS. CARD-LEVEL TESTING ..... | 51        |
| <b>Appendix A: NSPAR template</b> |                                                                                                                                 | <b>53</b> |

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="bedec0dd135ece8858586bd92a100ab7_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 6 of 53           |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

## **List of Tables**

Table 1. Requirement Tiers ..... 22  
 Table 2. Requirement Tiers Applicability Matrix ..... 25  
 Table 3. Requirement Tiers Verification Matrix ..... 25  
 Table 4. SRR Radiation Deliverables ..... 27  
 Table 5. PDR Radiation Deliverables ..... 28  
 Table 6. CDR Radiation Deliverables ..... 28  
 Table 7. MRR Radiation Deliverables ..... 28  
 Table 8. RHA data to be presented at design reviews ..... 28  
 Table 9. Acceptability criteria for TID and TNID characterization test data (adapted from SMC-S-010) ..... 31  
 Table 10. Acceptability criteria for TID RWLAT test data (adapted from SMC-S-010) .. 32  
 Table 11. Similarity criteria (adapted from JSC-08080-2B) ..... 34  
 Table 12. Heavy ion test fluence requirements ..... 36  
 Table 13. Typical bounding minimum penetration depth for MOSFET testing ..... 38  
 Table 14. SEE Category definitions..... 41  
 Table 15. RAM contents ..... 42  
 Table 16. Minimum contents of an SEE test plan..... 45  
 Table 17. Minimum contents of an SEE test report..... 46  
 Table 18. Typical radiation effects for various part technologies ..... 49  
 Table 19. SET signature guidelines ..... 50  
 Table 20. Advantages and disadvantages of low-energy- vs. high-energy heavy ion testing..... 51  
 Table 21. Advantages and disadvantages of part- vs. card- (or box) level heavy ion testing..... 52

# **List of Figures**

Figure 1. RHA process flow and timing ..... 20

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="228b525aeddd826691dfd0327516afa7_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 7 of 53           |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

# 1. INTRODUCTION

## 1.1 Purpose

This document, the JSC Engineering Directorate Avionics Ionizing Radiation Effects Standard (AIRES), provides design, test, and analysis requirements to ensure electronic hardware meets functional, performance and reliability requirements in the mission ionizing radiation environment. This suite of activities is referred to as Radiation Hardening Assurance (RHA) and is an integral part of the hardware design process.

## 1.2 Scope

The scope of AIRES includes any Government Furnished Equipment (GFE) human spacecraft hardware item containing electronic piece-parts and being developed / furnished by NASA JSC.

The requirements in this document are to be tailored for individual projects based on criticality, mission environments, risk tolerance posture, and other relevant considerations. AIRES tailoring and waivers are subject to approval by the sponsoring Program.

The terminologies “Electrical, Electronic, and Electro-mechanical Parts (EEE Parts)” and “Electrical, Electronic, Electro-mechanical, and Electro-optical Parts (EEEE Parts)” are equivalent for the purpose of this document, and include electro-optical components. All active electronic EEE Parts used in flight are in scope of AIRES and the RHA process unless specifically exempted. Passive devices such as resistors, capacitors, transformers, etc. are exempt by their inherent design. Low-voltage and small current diodes are considered low risk and generally do not require testing. Schottky diodes are in scope. The JSC Ionizing Radiation Panel (IRP) has the authority to make final determination on specific part types being in scope of the RHA effort. All ionizing radiation effects specific to electronic devices are in scope including total ionizing dose (TID), total non-ionizing dose (TNID) / displacement damage dose (DDD), and destructive and non-destructive single-event effects (SEE).

The full RHA process representing the current state-of-the-practice intended for critical application is generally incompatible with commercial-off-the-shelf (COTS) hardware. For example, understanding of COTS circuitry is typically insufficient for circuit analyses based on piece-part radiation characterization data. Circuit card assembly (CCA) level testing presents limitations as described in another sections of this document. Traceability of COTS EEE parts manufacturing processes is typically insufficient to guarantee flight parts have the same radiation susceptibility as tested (i.e., “radiation similarity”). While limited RHA, including limited characterization testing and development of system-level mitigation may be possible, use of COTS for critical

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="e519e1f1ab7309e7fd6e0431266a81f4_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 8 of 53           |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

application presents inherent and sometimes unquantifiable risks that have to be accepted by Programs.

The following are out of scope of this document:

- a. Ionizing radiation effects on bulk materials.
- b. Effects from other radiation types such as EMI/EMC, thermal, ultraviolet / visible / infrared
- c. AIRES requirements do not apply to ground and engineering units.
- d. Worst Case Analyses (WCA) beyond provision of radiation contribution
- e. Systems engineering radiation activities such as integration of critical JSC GFE with other critical systems

## 1.3 Design Requirements

Reliability and performance goals for JSC GFE projects are defined by the cognizant program office. IRP does not levy or approve reliability or availability requirements. IRP does evaluate performance of piece parts or cards/boxes. This includes radiation test data including SEE characteristics, radiation environments, rates, as well as piece part mitigations.

SEE are Markov (stochastic memoryless) processes. Depending on the SEE mechanism, mitigation is by risk avoidance or by risk quantification and acceptance. In the former case, assurance of acceptable risk is provided by adherence to a set of best practices. In the latter case, SEE radiation performance is described by predicted occurrence rate(s) in specific environment(s). SEE rate prediction is subject to large intrinsic uncertainties, spanning one order of magnitude (factor of 10x) or more. SEE follow a Poisson distribution in the fluence space (i.e., probability is defined per incident particle) and therefore vary with environment intensity. This has implications for redundancy analyses. Radiation environment (particle flux) increases such as during a solar particle event (SPE) cause the SEE probability to increase simultaneously in all legs of redundancy. As such, robustness analyses must reflect the worst case environments (e.g., peak SPE fluxes). The timing of specific SEE occurrences cannot be predicted. In a given environment, SEE are equally likely to occur during the first-, the last-, or any minute of the mission. It is the project's responsibility to determine if the rates predicted in the analysis meet the reliability and availability requirements and their intent as stated in requirements documents.

## 1.4 Applicable Documents

The following documents are applicable to the extent referenced by this standard. Use the latest revision of each document unless otherwise indicated in this standard.

- a. MIL-STD-883, Method 1019 Ionizing Radiation (Total Dose) Test Procedure
- b. MIL-STD-750, Method 1019 Steady-State Total Dose Irradiation Procedure

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 203" src="72a075ef383d9b5618bc3507c013827f_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 9 of 53           |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

- c. MIL-HDBK-814 Ionizing Dose and Neutron Hardness Assurance Guidelines for Microcircuits and Semiconductor Devices
- d. MIL-STD-750, Method 1080 Single-Event Burnout and Single-Event Gate Rupture
- e. Single-Event Effect Criticality Analysis (SEECA), Sponsored by NASA Headquarters/ Code QW, February 15, 1996, available at <https://radhome.gsfc.nasa.gov/radhome/papers/seeca2.htm> (retrieved Feb 01, 2021)

## 1.5 Reference Documents

- a. SMC-S-010 Parts, Materials, and Processes Technical Requirements for Space and Launch Vehicles, Air Force Space Command, Space and Missile Systems Center Standard, Appendix A Radiation Hardness Assurance Requirements
- b. JESD57A Test Procedures for the Measurement of Single-Event Effects in Semiconductor Devices from Heavy ion Irradiation
- c. ASTM F1192 Standard Guide for the Measurement of Single-Event Phenomena (SEP) Induced by Heavy Ion Irradiation of Semiconductor Devices
- d. SLS-SPEC-159 Cross Program Design Specification for Natural Environments (DSNE)
- e. SSP30512 Space Station Ionizing Radiation Design Environment
- f. JESD234 Test Standard for the Measurement of Proton Radiation Single-Event Effects in Electronic Devices
- g. JSC-08080-2 JSC Design and Procedural Standards
- h. MPCV 70043 "Orion Multi-Purpose Crew Vehicle (MPCV) Program Hardware Failure Modes and Effects Analysis / Critical Items List (FMEA/CIL) Requirements Document", Rev B, June 10, 2015

## 1.6 Acronyms and Definitions

|       |                                                                        |
|-------|------------------------------------------------------------------------|
| ABPL  | As-Built parts list                                                    |
| ADPL  | As-designed parts list                                                 |
| AIRES | JSC Avionics Ionizing Radiation Effects Standard                       |
| CCA   | Circuit-Card Assembly                                                  |
| CDR   | Critical Design Review                                                 |
| CEV   | Crew Exploration Vehicle                                               |
| COTS  | Commercial-Off-the-Shelf                                               |
| DAC   | Design Analysis Cycle                                                  |
| DCR   | Design Certification Review                                            |
| DDD   | Displacement Damage Dose. Equivalent to Total Non-ionizing Dose (TNID) |
| DRM   | Design Reference Mission                                               |
| DSEE  | Destructive Single-Event Effect                                        |

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="1a3ad853512f8c7160d1e582c6d1059c_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 10 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

|            |                                                                                                                                                                                  |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DSNE       | Design Specification for Natural Environments                                                                                                                                    |
| DUT        | Device Under Test                                                                                                                                                                |
| EA PCB     | JSC Engineering Directorate Parts Control Board                                                                                                                                  |
| EDD        | Environments Definition Document                                                                                                                                                 |
| EEE Parts  | Electrical, Electronic, and Electro-mechanical Parts. For the purposes of this document, “EEE” and “EEEE” are interchangeable and include Electro-optical parts.                 |
| EEEE Parts | Electrical, Electronic, Electro-mechanical and Electro-optical Parts. For the purposes of this document, “EEE” and “EEEE” are interchangeable and include Electro-optical parts. |
| ELDRS      | Enhanced Low Dose Rate Sensitivity                                                                                                                                               |
| EOL        | End of Life                                                                                                                                                                      |
| EU         | Engineering Unit                                                                                                                                                                 |
| FDIR       | Fault Detection, Isolation, and Recovery                                                                                                                                         |
| FRR        | Flight Readiness Review                                                                                                                                                          |
| GCR        | Galactic Cosmic Radiation                                                                                                                                                        |
| GEMCB      | Government Equipment and Materials Control Board                                                                                                                                 |
| GFE        | Government Furnished Equipment                                                                                                                                                   |
| GSE        | Ground Support Equipment                                                                                                                                                         |
| HSF        | Human Space Flight                                                                                                                                                               |
| ISO        | International Standardization Organization                                                                                                                                       |
| IRP        | Ionizing Radiation Panel                                                                                                                                                         |
| ISS        | International Space Station                                                                                                                                                      |
| LEO        | Low Earth Orbit                                                                                                                                                                  |
| LET        | Linear Energy Transfer                                                                                                                                                           |
| MBU        | Multiple Bit Upset – A non-destructive SEE type that causes upsets in multiple bits of a single piece part. Most common in memory ICs.                                           |
| MoA        | Project or component specific, IRP-approved Memorandum of Agreement                                                                                                              |
| MOSFET     | Metal Oxide Semiconductor Field-Effect Transistor                                                                                                                                |
| MRR        | Manufacturing Readiness Review                                                                                                                                                   |
| NASA       | National Aeronautics and Space Administration                                                                                                                                    |
| NDSEE      | Non-Destructive Single-Event Effect                                                                                                                                              |
| NSPAR      | Non-Standard Parts Approval Request                                                                                                                                              |
| PCN        | Parts Change Notice                                                                                                                                                              |
| PDR        | Preliminary Design Review                                                                                                                                                        |
| QML        | Qualified Manufacturer List, maintained by the US Defense Logistics Agency                                                                                                       |
| QPL        | Qualified Parts List                                                                                                                                                             |

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 203" src="3b1a0a7d4cf0e92e6559401c7ecdf089_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 11 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

|       |                                                                                                                                                                                                                                                                                                                          |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RAM   | Radiation Assessment Matrix - SEE analysis and documentation tool capturing application SEE circuit effects and their impacts to functional performance.                                                                                                                                                                 |
| RHA   | Radiation Hardness Assurance                                                                                                                                                                                                                                                                                             |
| RWLAT | Radiation Wafer Lot Acceptance Test                                                                                                                                                                                                                                                                                      |
| RDM   | Radiation Design Margin                                                                                                                                                                                                                                                                                                  |
| SEB   | Single-Event Burn-out – A type of destructive SEE due to a high current state in a power transistor resulting from a single ionized particle.                                                                                                                                                                            |
| SEDR  | Single-Event Dielectric Rupture - A type of destructive SEE that results in the destruction of the gate oxide of a MOS or similar capacitor structure.                                                                                                                                                                   |
| SEE   | Single-Event Effect – A destructive or non-destructive effect caused by a single ionizing particle. This term refers to a broad category of errors that can be non-destructive (e.g., SET, SEU, SEFI) as well as destructive (e.g., SEL, SEB, SEGR).                                                                     |
| SEFI  | Single-Event Functional Interrupt – A type of non-destructive SEE where a generally complex device stops normal functions, and usually requires a reset or power cycle to resume normal operations. It is a special case of SEU changing an internal control signal.                                                     |
| SEGR  | Single-Event Gate Rupture – A type of destructive SEE in power MOSFETs, which results in the formation of a conducting path in the gate oxide.                                                                                                                                                                           |
| SEL   | Single-Event Latchup – A type of SEE which consists of a parasitic thyristor structure being turned on by an ionizing particle. SELs are high current events. SELs are to be considered destructive events until proven otherwise by test data. Non-destructive SEL require power cycle to restore device functionality. |
| SET   | Single-Event Transient – A type of non-destructive SEE that causes a temporary (transient) perturbation of an analog signal internal to, or at the inputs/outputs of a part. SETs self-clear but may have persistent down-stream effects.                                                                                |
| SEU   | Single-Event Upset - A type of non-destructive SEE that causes a change of digital state in or at the output of a part.                                                                                                                                                                                                  |
| SLAT  | SEE Radiation Lot Acceptance Test                                                                                                                                                                                                                                                                                        |
| SMD   | Standard Microcircuit Drawing                                                                                                                                                                                                                                                                                            |
| SOC   | System-On-a-Chip                                                                                                                                                                                                                                                                                                         |
| SPE   | Solar Particle Event                                                                                                                                                                                                                                                                                                     |
| SRR   | System Requirements Review                                                                                                                                                                                                                                                                                               |

See Cover for full disclosure. Verify correct revision before use at

<https://gmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 203" src="aae931686f171424d9dd35b358f91ce6_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 12 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TID                      | Total Ionizing Dose                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| TNID                     | Total Non-ionizing Dose – Equivalent to Displacement Damage Dose (DDD)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| TR                       | Test Report                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| VAC                      | Verification Analysis Cycle                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| VDBP                     | Variable Depth Bragg Peak – Test method developed at the Johnson Space Center. A high-energy heavy ion beam Bragg peak is moved throughout the part under test using degraders. The response of the DUT is used to calibrate the LET at the active region. This testing is only possible at the NASA Space Radiation Laboratory (NSRL) at the Brookhaven National Laboratory (BNL), and only for specific part types. (see N. J-H. Roche et al., “Validation of the Variable Depth Bragg Peak Method for Single-Event Latchup Testing Using Ion Beam Characterization”, IEEE Transaction on Nuclear Science, Vol. 61, No. 6, December 2014 and references). |
| Availability             | The probability that a system will work as required and when required during a mission. Time durations in SEFI and SEFI recovery modes reduce availability.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Characterization         | The process for determining, either by test or analysis, a piece-part response to ionizing radiation. Piece parts may have multiple characterizations corresponding to multiple functional modes, multiple responses, and multiple radiation environments.                                                                                                                                                                                                                                                                                                                                                                                                  |
| Component                | Electronic box or CCA containing multiple EEE Parts                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Die fabrication facility | The facility where the semiconductors are built from the bulk silicon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Foundry                  | The facility where the bulk silicon wafer was grown.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| LET Threshold            | The LET level below which a part exhibits no response. Thresholds are established by a) the maximum test LET at which the part exhibits no response, or b) as the onset parameter of the Weibull fit of the measured SEE cross-sections <a href="https://creme.isde.vanderbilt.edu/CREME-MC/help/weibull">https://creme.isde.vanderbilt.edu/CREME-MC/help/weibull</a> .                                                                                                                                                                                                                                                                                     |
| Mask design              | The masks used to form the active structures and metallization in/on the silicon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| QML/RHA device           | EEE Part procured with RHA guarantees from a QML manufacturer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| RHA device               | EEE Part procured with RHA guarantees from a QML or non-QML manufacturer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| SEE Rate                 | The expected number of SEE occurrences per unit time in a specific environment. SEE Probability – Defined for a specified                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="1298f18cf995a7a0e2f4555ff628ef38_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 13 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

|           |                                                                                                 |
|-----------|-------------------------------------------------------------------------------------------------|
|           | environment and time duration $t$ . Related to the SEE rate $r$ by $p = 1 - \exp(-r \cdot t)$ . |
| Stuck Bit | A type of SEE that causes a bit or logic unit to be permanently fixed in a "1" or "0" state.    |

# 2. REQUIREMENTS LIST

**RAD001** Prior to SRR, JSC GFE Projects shall perform radiation requirements tailoring in coordination with the JSC Ionizing Radiation Panel (IRP) compliant to the process below, and with any deviation approved by IRP.

**RAD002** In preparation for SRR, the Project shall coordinate with the IRP to obtain concurrence on the applicable radiation requirements tier selected from Table 1. and include it in the Project Requirements Document.

**RAD003** In preparation for SRR, the Project and IRP shall establish a Memorandum of Agreement (MoA) to document any AIRES tailoring.

**RAD004** The Project shall perform radiation environment analyses prior to SRR, document the results in an Environments Definition Document (EDD), and update analyses / maintain EDD as needed throughout the duration of the project.

**RAD005** The Project shall perform radiation analyses to verify that the hardware meets its functional, performance, and reliability requirements during and after exposure to the mission radiation environment

**RAD006** The Project shall provide the products listed in Table 4 as SRR (or equivalent) deliverables

**RAD007** The project shall provide the products listed in Table 5 as PDR (or equivalent) deliverables

**RAD008** The project shall provide the products listed in Table 6 as CDR (or equivalent) deliverables

**RAD009** The project shall provide the products listed in Table 7 as MMR (or equivalent) deliverables

**RAD010** RHA status shall be presented at engineering and design reviews including SRR, PDR, CDR and MRR or equivalent consistent with Table 8.

**RAD011** All EEE parts shall be characterized for TID, ELDRS, TNID and synergistic effects as applicable

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="cbfcf451a51842bb2601dc60b3e05663_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 14 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

**RAD012** No effect due to TID (including ELDRS) or TNID shall cause system/subsystem failure or performance degradation outside specification.

**RAD013** EEE parts that are inherently (by technology) TID- (including ELDRS) radiation hard to levels >5x design environment are exempted from further TID testing

**RAD014** EEE parts that are inherently (by technology) TNID radiation hard to levels >5x design environment are exempted from further TNID testing

**RAD015** EEE parts procured with TID RHA guarantees by QML listed manufacturer (i.e., QML/RHA devices) to levels >2x design environment are exempted from further TID testing pending confirmation of no ELDRS concerns and validation of the RWLAT protocol.

**RAD016** EEE parts procured with TNID RHA guarantees by QML listed manufacturer (i.e., QML/RHA devices) to levels >2x design environment are exempted from further TNID testing pending validation of the RWLAT protocol.

**RAD017** EEE parts procured with RHA guarantees by non-QML listed manufacturer (i.e., non-QML/RHA devices) can be treated in a similar manner to QML/RHA devices as long as the procuring agency assumes responsibility for third party validation of the part's RHA process.

**RAD018** Non-RHA devices shall exhibit acceptable parametric degradation due to synergistic TID, ELDRS and TNID effects of radiation exposure, demonstrated by circuit parametric analysis based on compliant test data.

**RAD019** EEE parts performance degradation due to radiation effects shall be included / documented in worst-case circuit analysis (WCCA)

**RAD020** Radiation degradation limits of non-RHA devices shall be set at the minimum 99% probability at 90% confidence (P99/C90) per MIL-HDBK-814 and to dose level >2x the design environment unless otherwise approved by the IRP.

**RAD021** TID and TNID characterization test data for non-RHA devices shall comply with Table 9

**RAD022** For EEE parts potentially susceptible to ELDRS, TID characterization and RWLAT data shall be obtained compliant to MIL-STD-883/MIL-STD-750 Method 1019 Condition D

**RAD023** RWLAT shall be compliant with Table 10.

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="9ba49be3e8a62ee7164efebdcb3a7ede_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 15 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

**RAD024** Devices exhibiting a minimum RDM of 10x are exempted from RWLAT unless required by IRP for specific devices.

**RAD025** Devices exhibiting an RDM of 3x-10x may be exempted from RWLAT pending IRP approval of supplier provided protocol.

**RAD026** EEE parts shall be immune to destructive and non-recoverable SEE up to and including  $LET_{th} = 60 \text{ MeV-cm}^2/\text{mg}$

**RAD027** EEE parts shall be fully characterized for susceptibility to recoverable SEE up to an including  $LET = 60 \text{ MeV-cm}^2/\text{mg}$

**RAD028** No SEE shall cause loss of safety-critical functions

**RAD029** SEE data shall originate from AIRES or IRP approved sources

**RAD030** Unless the applicability of SEE characterization data is guaranteed by design, manufacturer or SMD, or test samples were from the flight lot, projects shall perform a similarity analysis to verify that all similarity criteria in Table 11 are met.

**RAD031** If similarity is not positively verified, projects shall present status to IRP for disposition. Options include SEE Radiation Lot Acceptance Tests (SLAT), NSPAR, or elevation for risk decision.

**RAD032** SEE data shall envelop the flight circuit application.

**RAD033** The sample size for SEE characterization shall be no less than three (3) samples unless otherwise approved by IRP.

**RAD034** The minimum heavy ion test fluence shall comply with Table 12. Heavy ion test fluence requirements, or until a destructive (DSEE) failure has occurred.

**RAD035** For SEE types subject to rate calculations, the cross-section vs. LET curve shall reflect LET range and number of data points sufficient to determine the threshold, knee region shape, and saturation cross-section.

**RAD036** For devices potentially susceptible to SEL, the DUT shall be monitored during test to characterize high current error modes.

**RAD037** SEL test data shall envelop the device maximum flight application temperature

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="fa17ecf8c66b02ac92d9e609ae5599e4_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 16 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

**RAD038 SEL shall be considered destructive unless IRP-approved evidence is provided to the contrary, including consideration of latent effects due to device stress.**

**RAD039 Ions used for SEL testing shall have a minimum range of 100  $\mu\text{m}$  unless otherwise approved by IRP.**

**RAD040 SEU/SET/SEFI test data shall envelop the device minimum flight application temperature**

**RAD041 Recoverable SEFIs that cause current increases shall be assessed for susceptibility to cause latent degradation due to device stress.**

**RAD042 For devices potentially susceptible to SEDR or SEGR, destructive SEE test data shall reflect irradiation with beam at normal incidence and room ambient temperature.**

**RAD043 Power MOSFETs shall be derated to 75% of their maximum survival drain-source voltage ( $V_{DS}$ ) as determined by SEGR testing at 133% of the worst-case circuit-application gate-source ( $V_{GS}$ ) turnoff voltage**

**RAD044 The maximum survival drain-source voltage ( $V_{DS}$ ) shall be established from exposure at normal beam incidence to a minimum fluence of  $5e+5$  ions/ $\text{cm}^2$  of an ion with the minimum LET of DSEE  $\text{LET}_{th}$  stipulated in RAD026 throughout the sensitive charge-collection region (epilayer(s)) of the device**

**RAD045 Part types that are susceptible to single-event burnout (SEB) shall not be used in applications with maximum voltage levels exceeding 75% of the maximum survivable voltage as determined in SEB testing**

**RAD046 The survival voltage ( $V_{CE}$ ,  $V_R$ , or  $V_{DS}$ ) shall be established from exposure at normal beam incidence to a minimum fluence of  $5e+5$  ions/ $\text{cm}^2$  of an ion with the minimum LET of DSEE  $\text{LET}_{th}$  stipulated in RAD026 throughout the depletion depth of the device when at its maximum voltage**

**RAD047 Acceptable SEE test data for Power MOSFETs shall be compliant with MIL-STD-750, Method 1080 for test circuit and post gate-stress tests.**

**RAD048 Devices with LET thresholds less than  $14 \text{ MeV-cm}^2/\text{mg}$  and for which accurate rate calculation is critical shall be proton SEE tested**

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="ec788ac3d43f427d6dca7fa19dce3874_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 17 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

**RAD049 Proton SEE testing shall be performed with high energy protons ( $E = 200 \pm 30$  MeV) to a fluence of  $1E+11$  protons/cm<sup>2</sup> unless otherwise approved by IRP due to device TID tolerance or practical test limitations**

**RAD050 Projects shall identify situations when circuit level testing is recommended, and present to IRP for concurrence.**

**RAD051 SEE Analysis shall be performed at card / box level including SEE propagation analysis, SEE function criticality categorization, and SEE rate calculations**

**RAD052 SEE propagation analysis shall be performed by project electrical design engineer(s) with support from ASD ionizing radiation engineering**

**RAD053 SEE function criticality categorization shall be performed by project electrical design engineer(s) with support from ASD ionizing radiation engineering according to the definitions in Table 14.**

**RAD054 SEE rate calculations shall be performed using IRP-approved tools and methods**

**RAD055 For devices susceptible to proton induced SEE, SEE rates for the proton and heavy ion environments shall be calculated and documented independently.**

**RAD056 Rate calculations shall be performed individually for all driving environments**

**RAD057 EEE Parts radiation data, TID, TNID and SEE compliance status, results of SEE circuit analyses, rates and similarity analysis shall be documented in Radiation Assessment Matrices (RAMs)**

**RAD058 The RAM contents shall comply with Table 15**

**RAD059 Radiation test readiness reviews (TRR) shall be scheduled to occur no less than 10 business days prior to the scheduled test date, unless otherwise approved by IRP**

**RAD060 Radiation test plans shall be submitted to the IRP for review and concurrence no less than 3 working days prior to the TRR, unless otherwise approved by IRP**

**RAD061 Initial test results “flash report” shall be provided to IRP no more than 10 business days after test completion, unless otherwise approved by IRP**

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="75a5ffee7be6378fc8f2c27ee056408e_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 18 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

**RAD062 Radiation test reports shall be made available to the project no more than 60 business days after test completion, unless otherwise approved by IRP**

**RAD063 Radiation NSPARs shall be written by the project and provided to the IRP for dispositioning or elevation for risk acceptance.**

**RAD064 At a minimum, SEE test plans shall include the information in Table 16**

**RAD065 At a minimum, TID test plans shall include the information in IRP Tech Memo TBR**

**RAD066 At a minimum, SEE test reports shall include the information in Table 17**

**RAD067 At a minimum, TID test reports shall include the information in IRP Tech Memo TBR**

**RAD068 The project shall maintain the radiation data (Test Procedures, Test Reports, RAM, Design Review Status Chart) in the project repository.**

# **3. RADIATION HARDENING ASSURANCE EXECUTIVE SUMMARY**

Radiation hardening assurance (RHA) refers to the suite of activities required for hardware containing electronic piece parts to meet their reliability and availability requirements in the space ionizing radiation environment.

There is no “one size fits all” solution to RHA. Rather, the RHA approach, including requirement tailoring, is driven by MEAL and risk posture for space systems. MEAL refers to Mission, (mission) Environment, Application, and Lifetime (of the application).<sup>1</sup>

For example, low-criticality applications for more benign radiation environments such as LEO may effectively implement low-cost RHA approaches based on COTS components screening (a.k.a. “radiation hardness by serendipity”).

In contrast, RHA of critical systems designed for long missions and/or harsh radiation environments such as lunar or Mars missions requires considerable scope and resources. For it to be successful, RHA must be pursued as an integral part of the design and engineering process. RHA elements include input to architecture trades, requirements development, environment and shielding analyses, EEE parts selection, functional analyses, radiation testing, circuit single-event effect (SEE) criticality analysis (SEECA), design and operational mitigation to eliminate / control radiation impacts,

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="22869a12e33113937504835078800f31_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 19 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

development of FPGA VHDL codes, firmware and software, and system level integration.

In the context of RHA, criticality refers to mission success and crew safety. In some cases, different criticalities are assigned to functional performance vs. safety hazards. A holistic criticality assessment is a required component of the MEAL approach to RHA. Starting RHA early in the design and adhering to state-of-the-practice recommended timing is critical to the design meeting its functional, performance, availability and reliability requirements in the mission environment. The typical RHA process flow is shown in Figure 1.

The RHA process described in this document is intended to envelop the entire range of applications for the foreseeable NASA human space missions. For less critical applications and environments, MEAL tailoring based on input from cognizant stakeholders is crucial to balance RHA rigor and scope against Project and Program risk tolerance posture.

The Avionic Systems Division (ASD) of the Engineering Directorate at NASA Johnson Space Center (JSC) is assigned responsibility for-, and control over AIRES and its documentation. The Avionics Ionizing Radiation Effects TDL, their designees, individually and through the Ionizing Radiation Panel (IRP) as described in this document, are the technical authority for AIRES requirements tailoring, interpretation, verification, and other AIRES in-scope tasks.

<sup>1</sup><https://ntrs.nasa.gov/api/citations/20180007358/downloads/20180007358.pdf>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="16f64b266536c4f0747e0cdd07dc57c0_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 20 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

![RHA Process Flow and Timing diagram showing the progression from requirements to final integration, with milestones SRR, PDR, CDR, and MRR/CoFR.](812e188283162af0b54fb3e30ffee51b_img.jpg)

```

graph TD
    PR[Program Requirements] --> MR[Mission Duration]
    PR --> HA[Hardware Criticality]
    SA[System & Architecture] --> HA
    S[Shielding] --> IREA[Initial Radiation Environment Analysis]
    D[Destination e.g., LEO, exo-LEO] --> IREA
    D --> RR[Radiation Requirements]
    MD[Mission Duration] --> RR
    HA --> RR
    IREA --> RR
    IREA --> IREAU[Radiation Environment Analysis Updates]
    RR --> IPS[Initial Parts Selection Initial Design]
    IPS --> PSIMP[Parts Selection Iteration Mitigation Design Performance Analysis]
    IREAU --> RT[Radiation Testing SEE Rate Analysis RAM NSPARs]
    RT --> PSIMP
    PSIMP --> SV[Similarity Verification Analysis Closure RAM Updates Documentation Radiation System Integration]
    SV --> MRR[MRR/CoFR]
    
    subgraph Milestones
        SRR[SRR]
        PDR[PDR]
        CDR[CDR]
        MRR[MRR/CoFR]
    end
  
```

The diagram illustrates the RHA (Radiation Hardware Analysis) process flow and timing. It begins with inputs from Program Requirements, System & Architecture, Shielding, Destination (e.g., LEO, exo-LEO), Mission Duration, and Hardware Criticality. These inputs feed into Initial Radiation Environment Analysis and Radiation Requirements. The process then moves through Initial Parts Selection Initial Design, Radiation Environment Analysis Updates, Radiation Testing (SEE Rate Analysis, RAM, NSPARs), and Parts Selection Iteration Mitigation Design Performance Analysis. The final stage is Similarity Verification Analysis Closure, RAM Updates, Documentation, and Radiation System Integration. The process is divided into four phases by dashed lines: SRR (System Requirements Review), PDR (Preliminary Design Review), CDR (Critical Design Review), and MRR/CoFR (Mission Review/Configuration Review).

RHA Process Flow and Timing diagram showing the progression from requirements to final integration, with milestones SRR, PDR, CDR, and MRR/CoFR.

**FIGURE 1. RHA PROCESS FLOW AND TIMING**

RHA is performed by projects with ASD ionizing radiation engineering support. System engineering support is critical for successful radiation integration.

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="ea0e870e2f3087f34e4061d806b0356e_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 21 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

# 4. RADIATION HARDENING ASSURANCE (RHA) PROCESS- AND ADMINISTRATIVE REQUIREMENTS

For the purpose of this document, Government Furnished Equipment (GFE) is defined as flight hardware, including flight vehicle core systems, crew equipment, payloads, advanced flight systems, and flight experiments or Development Test Objective (DTO)/Development Science/Supplementary Objective (DSO) which require design and implementation work. Design solutions may include Commercial Off the Shelf (COTS) hardware exclusively or in part.

RAD001 Prior to SRR, JSC GFE Projects shall perform radiation requirements tailoring in coordination with the JSC Ionizing Radiation Panel (IRP) compliant to the process below, and with any deviation approved by IRP.

Rationale for this requirement is provided in Section 3 of this document. Projects own this requirement, with IRP supporting throughout the process.

## 4.1 AIRES Tailoring and Requirement Verification Process

AIRES tailoring consists of two parts:

- Selection of a requirement tier is the primary means to tailor AIRES and is driven primarily by component criticality. As the tier is representative of the scope of the RHA effort, it is critical for the requirement wording to be prominently captured in the Project Requirement Document and vetted by the Program and other stakeholders.
- The Memorandum of Agreement (MoA) represents the secondary means to tailor or provides exemptions to specific AIRES requirements, in order to account for factors such as the mission environment (e.g., LEO vs. exo-LEO), mission duration, and other relevant criteria. The MoA is project- or component specific, and subject to IRP approval.

Individual AIRES requirements do not have to undergo the formal requirements verification process such as for design reviews and for flight certification. Their verification is implicit in the IRP approval of Radiation Assessment Matrix (RAM), Radiation Test Reports, NSPARs and other radiation deliverables, and formally documented as verification of the higher level radiation requirements captured in the Project Requirement Document.

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 203" src="fbefd66b71c3b00084b84867ac6f9ce4_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 22 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

### 4.1.1 Requirement Tiers

RAD002 In preparation for SRR, the Project shall coordinate with the IRP to obtain concurrence on the applicable radiation requirements tier selected from Table 1. and include it in the Project Requirements Document.

**TABLE 1. REQUIREMENT TIERS**

| Tier | Requirements wording and rationale                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A    | <p>A.1. <b>The component</b> shall meet its functional, performance, availability and reliability requirements in the mission radiation environment.</p> <p><i>Rationale: Radiation testing is characterization testing. Mitigation of radiation effects is by threat avoidance and/or threat quantification. Verification of radiation availability and reliability requirements is by analysis (known as Single-Event Effect Criticality Analysis SEECA), which in turn require full test characterization data at piece-part level.</i></p> <p>A.2. EEE Parts used in <b>the component</b> shall meet Program SEE radiation requirements compliant to JSC-67551 AIRES or as tailored in the Project MoA.</p> <p><i>Rationale: Detailed SEE requirements are derived consistent with Program requirements and NASA guidelines and documented in the Ionizing Radiation Effects Standard. AIRES requirements include SEE immunity or characterization thresholds (typically LET = 60 MeV-cm<sup>2</sup>/mg), test and analysis requirements, etc.</i></p> <p>A.3. EEE Parts used in <b>the component</b> design shall meet Program TID, TNID, and ELDRS radiation requirements compliant to JSC-67551 AIRES and Environments Definition Document (EDD) or equivalent, or as tailored in the Project MoA.</p> <p><i>Rationale: TID, TNID, and ELDRS requirements are derived by analyses of DSNE environments, shielding, and mission duration, and consistent with Project/Program requirements and NASA guidelines.</i></p> |

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="3c2a9038ec163892f18216d25a9db22b_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 23 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

| Tier | Requirements wording and rationale                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| B    | <p><b>B.1. The component</b> shall exhibit no non-recoverable single-event effects (SEE) during or after irradiation to <math>1\text{e}+7</math> p/cm<sup>2</sup> heavy ions of LET no less than 60 MeV-cm<sup>2</sup>/mg or as tailored in the Project MoA.</p> <p><i>Rationale: Per the current state-of-the-practice, immunity to non-recoverable SEE up to LET = 60-75 MeV-cm<sup>2</sup>/mg derived as per NASA guidelines provides acceptable reliability threat avoidance for most HSF applications beyond LEO. Short lifetime and/or reduced environments may constitute rationale for reducing the non-recoverable SEE threshold LET down to 37 MeV-cm<sup>2</sup>/mg as documented in a Project MoA. SEE testing can be performed at piece-part- or CCA level. Per NASA guidelines, CCA level testing presents intrinsic limitations that should be assessed for impacts.</i></p> <p><b>B.2. The component</b> shall be characterized for susceptibility to recoverable single-event effects (SEE) during or after irradiation to <math>1\text{e}+7</math> p/cm<sup>2</sup> heavy ions of LET no less than 60 MeV-cm<sup>2</sup>/mg or as tailored in the Project MoA.</p> <p><i>Rationale: SEE testing is characterization testing and can be performed at piece-part- or CCA level. CCA level testing must be sufficiently instrumented to capture all relevant error modes.</i></p> <p><b>B.3.</b> Acceptable impact of recoverable SEE to error-critical and error-vulnerable <b>component</b> functions shall be demonstrated by analysis.</p> <p><i>Rationale: Mitigation of radiation effects is by threat quantification and/or threat avoidance. CCA level testing is generally insufficient to provide confidence in threat quantification.</i></p> <p><b>B.4. The component</b> shall meet Program TID, TNID, and ELDRS radiation requirements compliant to JSC-67551 AIRES and Project Environments Definition Document (EDD) or equivalent and/or as tailored in the Project MoA.</p> <p><i>Rationale: TID, TNID, and ELDRS requirements are derived by analyses of DSNE environments, shielding, and mission duration, and consistent with Program/Project requirements and NASA guidelines. Heavy ion test data is generally not considered acceptable for TID characterization.</i></p> |

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 203" src="f0367f317ffaf58c722285085a21855b_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 24 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

| Tier | Requirements wording and rationale                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C    | <p><b>C.1. The component</b> shall exhibit no non-recoverable single-event effects (SEE) during or after irradiation to <math>1\text{e}+11</math> p/cm<sup>2</sup> protons of energy <math>E = 200\text{+/-}10</math> MeV or as tailored in the Project MoA.</p> <p><i>Rationale: Proton testing is useful for initial screening and non-critical LEO applications. Protons typically generate SEE by indirect ionizations. For practical purposes, the secondary ions have LET up to 6-8 MeV-cm<sup>2</sup>/mg (14 MeV-cm<sup>2</sup>/mg theoretical maximum), and small range insufficient to cause DSEE in some cases. Proton test fluence and statistics are limited by total dose effects. SEE testing can be performed at piece-part- or CCA level. CCA level testing presents intrinsic limitations that should be assessed for impacts.</i></p> <p><b>C.2. The component</b> shall be characterized for susceptibility to recoverable single-event effects (SEE) during or after irradiation to <math>1\text{e}+10</math> p/cm<sup>2</sup> protons of energy <math>E = 200\text{+/-}10</math> MeV or as tailored in the Project MoA.</p> <p><i>Rationale: SEE testing is characterization testing and can be performed at piece-part- or CCA level. CCA level testing must be sufficiently instrumented to capture all relevant error modes.</i></p> <p><b>C.3. Acceptable impact of recoverable SEE to error-critical and error-vulnerable component functions</b> shall be demonstrated by analysis.</p> <p><i>Rationale: Mitigation of radiation effects is by threat quantification and/or threat avoidance. CCA level testing is generally insufficient to provide confidence in threat quantification.</i></p> <p><b>C.4. The component</b> shall meet Program TID and TNID radiation requirements compliant to the Project MoA and/or Environments Definition Document (EDD) or equivalent.</p> <p><i>Rationale: For non-critical applications, TID and TNID requirements can be verified by proton testing.</i></p> |

The terminology “error-critical”, “error-vulnerable”, and “error-functional” is defined in the NASA document “Single-Event Effect Criticality Analysis” (referenced in the Applicable Document list).

Tier A represents requirements for critical hardware. Absent MoA tailoring, Tier A is considered equivalent “meet or exceed the intent” to Exploration standards including SMC-S-010 Appendix A and NASA-STD-8739.10. Limited tailoring may be approved by IRP while still meeting the intent of these standards. Tier B and C requirements are not

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="883711b52496b36c72249e6e0be28a23_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 25 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

intended to meet the intent of SMC-S-010. In order to perform RHA consistent with Tier B or C requirements, projects subject to Exploration standards will need a waiver or deviation from the Program. Early requirements definition is critical to estimating the scope of the RHA and requirement verification effort.

Notional correlation of the applicable radiation requirement tier vs. assigned criticality is provided in Table 2. Criticality definitions are consistent with MPCV 70043 "Orion Multi-Purpose Crew Vehicle (MPCV) Program Hardware Failure Modes and Effects Analysis / Critical Items List (FMEA/CIL) Requirements Document".

**TABLE 2. REQUIREMENT TIERS APPLICABILITY MATRIX**

| Criticality                                            | Tier | Notes                                                                                    |
|--------------------------------------------------------|------|------------------------------------------------------------------------------------------|
| 1 (all), 2 (all)                                       | A    | Full RHA; significant scope for critical applications                                    |
| 1R#*†, 1S*, 1SR*†, 2R*†                                | B    | Reduced RHA (e.g., CCA level heavy ion testing); reduced scope for medium risk tolerance |
| 3                                                      | C    | Proton testing; minimal scope for non-critical applications                              |
| *with Program risk acceptance                          |      |                                                                                          |
| †with consideration to similar / dissimilar redundancy |      |                                                                                          |

The requirement tiers verification matrix is shown in Table 3. "A" is Analysis, "T" Test, "I" Inspection e.g., of SMDs or manufacturer specification sheets. Combinations of test and inspection are typically required to support analyses. Projects own the requirement verification. Radiation testing in itself is typically insufficient to verify that the reliability and availability requirements are met.

**TABLE 3. REQUIREMENT TIERS VERIFICATION MATRIX**

| Requirement | Verification | Requirement | Verification | Requirement | Verification |
|-------------|--------------|-------------|--------------|-------------|--------------|
| A.1         | A            | B.1         | A,T,I        | C.1         | A,T,I        |
| A.2         | A,T,I        | B.2         | A,T,I        | C.2         | A,T,I        |
| A.3         | A,T,I        | B.3         | A            | C.3         | A            |
|             |              | B.4         | A,T,I        | C.4         | A,T,I        |

### 4.1.2 Memorandum of Agreement (MoA)

RAD003 In preparation for SRR, the Project and IRP shall establish a Memorandum of Agreement (MoA) to document any AIRES tailoring.

The memorandum of agreement represents an additional means for MEAL requirements tailoring. Examples of tailoring captured in the MoA consist of test LET reduction, TID, TNID or ELDRS requirement applicability exceptions, etc. The MoA is considered a critical element of AIRES tailoring, in addition to and separate from the

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="9743f8f92823fcfc2fbd387f854d183a_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 26 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

choice of requirement tier. Including the detailed tailoring in the Project Requirements Document is considered counterproductive and un-necessarily increasing the complexity of the aforementioned document

## 4.2 RHA Analyses

Starting RHA early in the design process is critical to successful, cost effective accomplishment of the design meeting its functional, performance, safety and reliability requirements in the space ionizing radiation environment.

RAD004 The Project shall perform radiation environment analyses prior to SRR, document the results in an Environments Definition Document EDD), and update analyses / maintain EDD as needed throughout the duration of the project.

Environment analyses must be performed sufficiently early to define the total dose environments to establish the corresponding TID and TNID/DD EEE part selection requirements. Input to these analyses include mission duration and shielding assumptions as provided by the projects. Shielding strongly affects the total dose incurred by parts in most relevant environments. Over-conservative shielding assumptions un-necessarily limit EEE parts selection aperture and drive costs. Insufficiently conservative assumptions introduce risk of the design not meeting its reliability and availability requirements for the entire mission duration. SEE environments are for rate analysis purposes only and can be refined until the PDR/CDR timeframe to improve rate calculations accuracy without necessarily driving design changes.

Ionizing radiation environments for LEO and Exploration missions are provided in SLS-SPEC-159 Design Specification for Natural Environments (DSNE). Although DSNE functionally supersedes SSP 30512 Space Station Ionizing Radiation Design Environment, SSP 30512 may still be found as an artifact applicable document. DSNE defines extra-vehicular environments for different mission durations and destinations. DSNE also provides selected sets of intra-vehicular environments corresponding to generic shielding thickness values. If no shielding information is initially available to the project, 100 mils Aluminum-equivalent shall be assumed unless otherwise directed by the IRP.

RAD005 The Project shall perform radiation analyses to verify that the hardware meets its functional, performance, and reliability requirements during and after exposure to the mission radiation environment

Piece-part radiation evaluation, test, and analysis are fundamental to Radiation RHA. Radiation testing is characterization testing, and provides input data to risk assessment

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="106404c26bd0d9c15c7b8546bc776a91_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 27 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

and development of mitigation. EEE Parts are characterized for susceptibility to radiation effects. e.g., SEE signatures and cross-sections. In some cases, SEE rates can be predicted in the mission environments. In other cases, part selection criteria reflect risk avoidance state-of-the-practice. Verification of the hardware meeting its functional, performance and reliability requirements during and after exposure to the mission radiation environment is by analysis anchored in radiation characterization test data. Equivalent terminology for functional and performance requirements includes utilization, availability, etc.

The project owns the radiation deliverables. Typical tasks performed by project radiation personnel typically include the following: Perform radiation shielding, environment and rate analyses based on project-provided design and mission data; Advise the project on potential failure modes for specific part types; Interpret available radiation data for specific applications; Coordinate with circuit and application designers and provide recommendations for radiation test strategy, operating modes, instrumentation, data collection, and radiation characteristics; lead test planning, execution, and reporting; provide programmatic support such as presenting NSPARs, radiation status at design reviews etc.

## 4.3 RHA Schedule

A summary of RHA elements and their timing with respect to the Project schedule is provided in the tables below.

RAD006 The Project shall provide the products listed in Table 4 as SRR (or equivalent) deliverables

**TABLE 4. SRR RADIATION DELIVERABLES**

| Element                                                                       | Prerequisites                                         |
|-------------------------------------------------------------------------------|-------------------------------------------------------|
| AIRES requirement tier                                                        | Assigned criticality                                  |
| Environment Definition Document (EDD) including total dose part requirements* | Mission destination & duration, shielding assumptions |
| AIRES MoA tailoring                                                           | Elements # 1 & 2                                      |
| * The EDD is updated as needed throughout the component lifecycle             |                                                       |

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="c5fe8f57e7a8541b205b3906c0f60920_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 28 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

RAD007 The project shall provide the products listed in Table 5 as PDR (or equivalent) deliverables

**TABLE 5. PDR RADIATION DELIVERABLES**

| Element                                                                                                               | Prerequisites                 |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------|
| ADPL screening for radiation data                                                                                     | As-Designed Parts List (ADPL) |
| Characterization testing data for complex critical parts such as FPGAs, SoCs, microprocessors, microcontrollers, etc. |                               |

RAD008 The project shall provide the products listed in Table 6 as CDR (or equivalent) deliverables

**TABLE 6. CDR RADIATION DELIVERABLES**

| Element                                                                             | Prerequisites                                             |
|-------------------------------------------------------------------------------------|-----------------------------------------------------------|
| Characterization testing completed w/ preliminary similarity                        | Test samples, circuit design info, test boards, beam time |
| Radiation Assessment Matrix (RAM) analysis complete w/ documented impacts and rates | SEE characterization data                                 |
| Circuit design for SEE mitigation complete                                          | SEE characterization data                                 |
| IRP processing of radiation NSPARs                                                  | As-Designed Parts List, Test data                         |

RAD009 The project shall provide the products listed in Table 7 as MMR (or equivalent) deliverables

**TABLE 7. MRR RADIATION DELIVERABLES**

| Element                                                              | Prerequisites             |
|----------------------------------------------------------------------|---------------------------|
| Similarity complete                                                  | As-Built Parts List       |
| Open liens closed out, updated RAM analysis & documentation complete | Delta testing as needed   |
| Radiation system integration complete                                | Updated analysis complete |

RAD010 RHA status shall be presented at engineering and design reviews including SRR, PDR, CDR and MRR or equivalent consistent with Table 8.

**TABLE 8. RHA DATA TO BE PRESENTED AT DESIGN REVIEWS**

|   |                                                                                                                                              |
|---|----------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | Provide a list of hardware to be addressed in the radiation review. This information establishes the scope for the radiation effects review. |
| 2 | Describe / reference the radiation environments (SEE, and TID if applicable) used in the radiation assessment.                               |

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 203" src="e4d0a23b957417e9017a24b4dfe81023_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 29 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

|   |                                                                                                                                                                                                                                                                               |
|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3 | Provide the EEE parts BOM showing total dose and SEE data identified for each device, similarity, and test candidate status                                                                                                                                                   |
| 4 | Provide RAM summary in the form of a Category 1, Category 2, and Category 3 rates roll-up (at card level) and compare against applicable system availability and reliability requirements.                                                                                    |
| 5 | Present details on SEE modes identified as high concern based on impact severity (i.e., high category) and/or rates. Include information on system response, existing and required mitigation at both circuit and system level, and any forward work required to reduce risk. |
| 6 | Identify any spacecraft system level hardware, software or operational design accommodations used or required to be implemented to mitigate adverse radiation effects.                                                                                                        |
| 7 | Provide a summary of radiation compliance, margins, open items / liens, radiation testing, system integration, and path to closure.                                                                                                                                           |

# 5. EEE PARTS SELECTION AND CHARACTERIZATION REQUIREMENTS FOR TOTAL DOSE

Cumulative radiation exposure causes EEE part parametric degradation and failure. In general, EEE parts should be considered susceptible to TID (including ELDRS) and TNID effects while both biased and unbiased. Bipolar and Bi-CMOS devices are potentially susceptible to Enhanced Low Dose Rate Susceptibility (ELDRS) effects. Certain part types and technologies such as optocouplers, optical imaging-, bipolar devices and other are potentially susceptible to TNID effects in addition to TID. These can manifest as deterioration of performance characteristics or optical properties.

**RAD011** All EEE parts shall be characterized for TID, ELDRS, TNID and synergistic effects as applicable

Acceptable total dose performance characterization include hard by technology, manufacturer guarantee based on test data, or test data. Per SMC-S-010 A.7.4.1, cumulative degradation effects shall be assessed either in test or analytically.

**RAD012** No effect due to TID (including ELDRS) or TNID shall cause system/subsystem failure or performance degradation outside specification.

Parts must be selected to ensure the design operates within specification for the entire lifetime.

**RAD013** EEE parts that are inherently (by technology) TID- (including ELDRS) radiation hard to levels >5x design environment are exempted from further TID testing

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 203" src="3a7740c0d98796c37d1c4c9d60071314_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 30 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

RAD014 **EEE parts that are inherently (by technology) TNID radiation hard to levels >5x design environment are exempted from further TNID testing**

Certain EEE parts technologies are considered inherently hard up to various total ionizing- and non-ionizing dose environment levels. The levels of concern vary among sources. For example, rectifier diodes are considered inherently TID rad-hard to  $1\text{e}+6$  –  $1\text{e}+7$  rad(Si) by some manufacturers, and to  $3\text{e}+5$  rad(Si) per ESA standard ECSS-Q-ST-60-15C regardless of manufacturer. Conservative approach is required by IRP when assessing EEE part technologies as inherently total dose radiation hard. TNID radiation hardness levels are typically expressed as 50 MeV equivalent proton-, or 1 MeV neutron fluence. The levels of concern for both TID and TNID are typically significantly above those encountered in human space flight, and conservatism in most cases does not constrain parts selection.

RAD015 **EEE parts procured with TID RHA guarantees by QML listed manufacturer (i.e., QML/RHA devices) to levels >2x design environment are exempted from further TID testing pending confirmation of no ELDRS concerns and validation of the RWLAT protocol.**

RAD016 **EEE parts procured with TNID RHA guarantees by QML listed manufacturer (i.e., QML/RHA devices) to levels >2x design environment are exempted from further TNID testing pending validation of the RWLAT protocol.**

EEE parts procured with radiation hardness assurance (RHA) from qualified manufacturers list (QML) listed manufacturers on are accepted as sufficiently characterized, and guaranteed to meet post-exposure EOL specifications. The 2x radiation design margin (RDM) is imposed to account for uncertainties in total dose testing and flight environments. If part is susceptible to ELDRS, manufacturer-performed RWLAT must meet RAD022. The RWLAT protocol must be validated against the flight design to verify that the irradiation bias circuit envelops the flight application. For additional details on radiation wafer lot acceptance testing (RWLAT), refer to SMC-S-010 A.5.1

RAD017 **EEE parts procured with RHA guarantees by non-QML listed manufacturer (i.e., non-QML/RHA devices) can be treated in a similar manner to QML/RHA devices as long as the procuring agency assumes responsibility for third party validation of the part's RHA process.**

Per SMC-S-010 A.4.2.2.4, validation shall include verification that the procedures for generation of post-radiation limits and for radiation acceptance of wafer lots is equivalent to and as effective as those of QML/RHA pedigree.

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="c59cf0104cb29e0812e732e14fed5115_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 31 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

RAD018 Non-RHA devices shall exhibit acceptable parametric degradation due to synergistic TID, ELDRS and TNID effects of radiation exposure, demonstrated by circuit parametric analysis based on compliant test data.

Non-RHA parts are defined as parts not procured with RHA guarantees. Use of non-RHA parts requires significant effort for part characterization testing and analysis.

RAD019 EEE parts performance degradation due to radiation effects shall be included / documented in worst-case circuit analysis (WCCA)

Worst-case circuit analysis (WCCA) is necessary to demonstrate that the design will satisfy its performance requirements at end of life.

RAD020 Radiation degradation limits of non-RHA devices shall be set at the minimum 99% probability at 90% confidence (P99/C90) per MIL-HDBK-814 and to dose level >2x the design environment unless otherwise approved by the IRP.

Full statistical approach for single sided tolerance limit calculations is described in the literature, e.g., in SMC-S-010 and MIL-HDBK-814. As an example, Twenty-three (23) test samples are required to achieve P99/C90 with three (3) standard deviations from the average. The IRP can approve less stringent requirement based on mission duration, shielding, environment, and other considerations.

RAD021 TID and TNID characterization test data for non-RHA devices shall comply with Table 9

**TABLE 9. ACCEPTABILITY CRITERIA FOR TID AND TNID CHARACTERIZATION TEST DATA (ADAPTED FROM SMC-S-010)**

|                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum sample size is five (5) per wafer (or wafer lot), plus one (1) control sample                                                                                                                                                                      |
| Test samples span multiple wafer lots to the greatest extent and uniformity possible                                                                                                                                                                       |
| Test samples represent the current design and manufacturing process at the same foundry                                                                                                                                                                    |
| Test results quantify parameters degradation to an extent sufficient to determine application impacts                                                                                                                                                      |
| Assessment of successful post radiation performance shall include verification of functional capability at intermediate dose levels below rated dose and beyond (minimum of 50% above rated TID and/or TNID of the device or failure, whichever is lower). |
| Radiation test and bias conditions envelop the flight application                                                                                                                                                                                          |
| TID radiation test is performed in compliance to MIL-STD-883 Method 1019 or MIL-STD-750 Method 1019. Use only Condition D for ELDRS-susceptible devices.                                                                                                   |

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="df49c445aef8fead90407bf8504d888f_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 32 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

RAD022 For EEE parts potentially susceptible to ELDRS, TID characterization and RWLAT data shall be obtained compliant to MIL-STD-883/MIL-STD-750 Method 1019 Condition D

Bipolar and Bi-CMOS devices are potentially susceptible to Enhanced Low Dose Rate Susceptibility (ELDRS) effects.

RAD023 RWLAT shall be compliant with Table 10.

**TABLE 10. ACCEPTABILITY CRITERIA FOR TID RWLAT TEST DATA (ADAPTED FROM SMC-S-010)**

|                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Recommended sample size is five (5) per wafer (or wafer lot), plus one (1) control sample                                                                |
| TID radiation test is performed in compliance to MIL-STD-883 Method 1019 or MIL-STD-750 Method 1019. Use only Condition D for ELDRS-susceptible devices. |

RAD024 Devices exhibiting a minimum RDM of 10x are exempted from RWLAT unless required by IRP for specific devices.

Radiation design margin (RDM) is defined as the part qualification TID / TID environment. Lot-to-lot variations in the TID susceptibility of commercial parts are typically no more than 3x. RDM of 10x provides sufficient confidence per SMC-S-010 A.5.2. IRP may require RWLAT independent of RDM for known problematic parts, technologies, ELDRS concerns, etc.

RAD025 Devices exhibiting an RDM of 3x-10x may be exempted from RWLAT pending IRP approval of supplier provided protocol.

Lot-to-lot variations in the TID susceptibility of commercial parts are typically no more than 3x. To control costs, RWLAT exceptions may be granted by IRP.

# **6. EEE PARTS SELECTION AND CHARACTERIZATION REQUIREMENTS FOR SINGLE-EVENT EFFECTS (SEE)**

For the vast majority of HSF applications, single-event effects constitute the primary driver for EEE parts selection, radiation design, and analysis. SEE RHA is in many regards more expensive, complex, and lengthy than TID/TNID RHA. It is critical that the SEE RHA implications are understood of the architecture, part selection, and other relevant trades and properly captured in the RHA scope.

RAD026 EEE parts shall be immune to destructive and non-recoverable SEE up to and including  $LET_{th} = 60 \text{ MeV-cm}^2/\text{mg}$

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="e303a21017b9ea3b0b9ce92b22bc477c_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 33 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

Destructive and non-recoverable SEE such as SEL, SEB, SEGR, SEDR, are mitigated by risk avoidance. Use of QML/RHA parts is strongly recommended. Dependent upon the application and with IRP concurrence, the LET threshold may be tailored at SRR. On a part-by-part basis, the IRP may approve other LET threshold based on circuit function / criticality, technology, environment, etc. Unless otherwise determined by IRP, low voltage and current bipolar junction transistors (BJTs) are considered DSEE immune.  $LET_{th} = 60 \text{ MeV-cm}^2/\text{mg}$  is in family with existing standards and the accepted state-of-the-practice for critical exo-LEO applications.

RAD027 **EEE parts shall be fully characterized for susceptibility to recoverable SEE up to an including  $LET = 60 \text{ MeV-cm}^2/\text{mg}$**

Recoverable SEE such as SEU, SET, SEFI cause impacts to hardware reliability and availability. Full characterization includes SEE signatures, cross-sections as a function of LET, and recovery characteristics for all applicable SEE modes. Unless otherwise determined by IRP, SET are considered low risk for low current and low voltage bipolar junction transistors (BJTs) and do not require testing.

RAD028 **No SEE shall cause loss of safety-critical functions**

Both non-recoverable and recoverable SEE can impact system performance including . SEE Criticality Analysis (SEECA) takes into account architecture, redundancy, circuit design and other data to determine SEE impacts to safety-critical functions.

## **6.1 Acceptable sources of SEE radiation data**

RAD029 **SEE data shall originate from AIRES or IRP approved sources**

AIRES approved sources are shown below. IRP may impose exceptions, or approve other sources upon request.

- Hard by design: Families of parts, mask sets, and manufacturing processes accepted by the IRP as immune to specific SEE types (e.g., SEL).
- Standard Microcircuit Drawing (SMD): SMD radiation guarantees constitute acceptable data.
- Part manufacturer guarantees as per Specification Sheets.
- Part manufacturer provided test data: Test reports posted on manufacturer's web sites or provided by request, with similarity analysis
- Flight application SEE testing using flight lot samples (SLAT) or with similarity analysis.
- Existing test data sources such as JSC publications, GSFC, JPL databases, IEEE publications, supplemented by full test reports and similarity analysis as determined by IRP.

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="af78c52baf93c86dd7bb2f8d494dbcbe_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 34 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

Use of hard by design parts or parts with existing SEE characterization data is preferable from a risk and cost standpoint. SEE radiation testing is complex, expensive, and schedule impacting due to limited beam time availability from limited accelerator facilities. Use of generic data e.g., SET signature guidelines is subject to IRP approval.

## 6.2 Similarity

RAD030 Unless the applicability of SEE characterization data is guaranteed by design, manufacturer or SMD, or test samples were from the flight lot, projects shall perform a similarity analysis to verify that all similarity criteria in Table 11 are met.

**TABLE 11. SIMILARITY CRITERIA (ADAPTED FROM JSC-08080-2B)**

|   |                                                                                                                                                                                                                         |
|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | The flight and tested parts must be the product of the same QPL, QML, and/or ISO 9000 manufacturer                                                                                                                      |
| 2 | The flight and tested wafers must be manufactured in the same foundry (only applicable if bulk Silicon properties are relevant, e.g., if no epi-layer or for TID effects)                                               |
| 3 | The flight and tested parts must be manufactured using the same epitaxial layer characteristics including deposition temperature, thickness and resistivity                                                             |
| 4 | The flight and tested parts must be manufactured at the same die fabrication facility                                                                                                                                   |
| 5 | The flight and tested parts must be manufactured using the same mask set, deposition, and doping                                                                                                                        |
| 6 | The flight and tested parts must be manufactured using the same SEE critical processes, especially the critical parameters of rate of oxide growth, temperature of the oxide growing process and final oxide thickness. |

Process changes that may degrade radiation performance include die shrink, die fabrication facility move, mask layout, passivation, gate oxide, field oxide, field implant, doping profiles and “well depth” changes (see MIL-PRF-38535, G.3.4.2, Change Control Procedures, Fabrication Process Change).

The similarity assessment ensures SEE data apply to the flight part. As a matter of design process, a review shall be performed of PCNs and GIDEP alerts for all parts proposing use of existing data to identify any process changes potentially impacting applicability of existing data. Recommended data sources include GIDEP, GSFC EPIMS, DLA (for QML parts) and the part manufacturer (for non-QML parts). When the flight parts lot date codes become available, project radiation engineers shall request confirmation from the part manufacturer POC that all the criteria are met.

The result of the similarity assessment shall be documented in the RAM, including lot numbers / date codes for the tested and flight parts, contact information for the part manufacturer POC, and confirmation on each of the similarity criteria.

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="533c7476d4bf3b9564d1ad12dc650709_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 35 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

## 6.3 SEE Radiation Lot Acceptance Tests (SLAT)

RAD031 If similarity is not positively verified, projects shall present status to IRP for disposition. Options include SEE Radiation Lot Acceptance Tests (SLAT), NSPAR, or elevation for risk decision.

## 6.4 SEE test data common requirements

Published SEE test standards and guidelines include JEDEC Standard 57A "Test Procedures for the Measurement of Single-Event Effects in Semiconductor Devices from Heavy Ion Irradiation" (JESD57A), JEDEC Standard 234 "Test Standard For The Measurement of Proton Radatiation Single-Event Effects in Electronic Devices" (JESD234), ASTM F1192 "Standard Guide for the Measurement of Single-Event Phenomena (SEP) Induced by Heavy Ion Irradiation of Semiconductor Devices" and others. These references provide information about the state-of-the-practice SEE testing critical to successful planning, execution, and interpretation of SEE test results.

RAD032 SEE data shall envelop the flight circuit application.

Verification of this requirement is two-fold:

- The previous test report must sufficiently reflect the test conditions such as test protocol / method, test circuit including voltage, bias conditions, power, loads, test temperature, and data results. Not all conditions are relevant for all part types. ASD ionizing radiation engineering can assist to determine relevant conditions for specific part types.
- An analysis of the current flight application performed by the circuit design engineer confirms that the flight device is in an equal or less stressful application than used for previous test.

High temperature and voltage are considered worst-case test conditions for SEL. Conversely, low temperature and voltage are considered worst-case test conditions for SET/SEU.

RAD033 The sample size for SEE characterization shall be no less than three (3) samples unless otherwise approved by IRP.

IRP can provide support to projects for test samples availability planning. Significantly more than three samples may be required depending upon test specifics, such as:

- Testing for destructive SEE
- Testing a device for multiple applications if an enveloping case cannot be identified
- Inconsistent SEE test results indicative of test anomalies
- Inconsistent SEE test results indicative of sample to sample SEE variations and uncertainties introduced by special sample prep such as backside thinning tolerances

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="a956db41b39bff6f66335a17db14bb06_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 36 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

- e. TID constraints
- f. Delidding yield/losses

Less than three samples may be approved by the IRP for complex or expensive devices such as SOC's, FPGA's, DC/DC converters, image sensors, etc.

RAD034 The minimum heavy ion test fluence shall comply with Table 12. Heavy ion test fluence requirements, or until a destructive (DSEE) failure has occurred.

**TABLE 12. HEAVY ION TEST FLUENCE REQUIREMENTS**

| Test type                 | Minimum fluence (p/cm <sup>2</sup> )                                                                                  |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------|
| DSEE other than SEB, SEGR | 1e+7                                                                                                                  |
| SEB, SEGR                 | 5e+5                                                                                                                  |
| NDSEE                     | 1e+7 or a statistically significant number of events has been captured (typically 50-100) for each configuration/mode |
| VDBP (NSRL)               | 1e+5 – 1e+6 / degrader step as determined by IRP                                                                      |

SEE testing is characterization testing. It is performed at particle fluences orders of magnitude higher than encountered in the flight. Its purpose is to identify all possible failure modes with reasonable confidence and (in some cases) enable rate predictions for specific environments. SEE test fluences must balance statistic confidence against part technology feature size, test duration, fluence rate (flux) effects, total dose degradation, test sample availability, and others. More detailed rationale is available in technical literature including JEDEC Standard JESD57A.

RAD035 For SEE types subject to rate calculations, the cross-section vs. LET curve shall reflect LET range and number of data points sufficient to determine the threshold, knee region shape, and saturation cross-section.

SEE tests shall be designed and conducted to detect and record each type SEE with sufficient LET resolution to characterize the device susceptibility and in turn accurately determine rates. Further guidance is provided in JEDEC Standard JESD57A 7.6.2.

## 6.5 SEL test data requirements

RAD036 For devices potentially susceptible to SEL, the DUT shall be monitored during test to characterize high current error modes.

CMOS devices are considered potentially susceptible to single-event latch-up (SEL). SEL manifests as current increases. Mitigation circuitry may be used for cross-section measurements but not when determination is made of SEL being destructive or not.

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="8a595fb12673444b0647911603264350_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 37 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

Efficient SEL mitigation circuitry should be designed to provide response time in the millisecond (ms) timeframe (JESD234).

RAD037 SEL test data shall envelop the device maximum flight application temperature  
SEL susceptibility generally increases with temperature.

RAD038 SEL shall be considered destructive unless IRP-approved evidence is provided to the contrary, including consideration of latent effects due to device stress.

In addition to catastrophic failure, high current conditions may induce latent damage reducing the device lifetime. SELs are considered destructive until sufficient evidence is presented proving otherwise, including that no latent damage results from the overcurrent condition. Evidence shall be detailed in the final test report.

RAD039 Ions used for SEL testing shall have a minimum range of 100  $\mu\text{m}$  unless otherwise approved by IRP.

As the substrate contributes to the parasitic thyristor structure, the sensitive volume for SEL may extend several tens of microns in the device. IRP may accept values lower than 100  $\mu\text{m}$ , e.g., with manufacturer confirmation that the range is sufficient.

## 6.6 SEU/SET/SEFI test data requirements

RAD040 SEU/SET/SEFI test data shall envelop the device minimum flight application temperature

SEU/SET/SEFI susceptibility generally decreases with temperature. Room temperature (RT) test data is usually acceptable for human space flight application. Projects should seek IRP guidance for special concerns.

RAD041 Recoverable SEFIs that cause current increases shall be assessed for susceptibility to cause latent degradation due to device stress.

High current conditions may induce latent damage reducing the device lifetime. Some methods to determine damage are functional testing, life testing, failure investigation of the device, thermography, plus others.

## 6.7 SEB/SEGR/SEDR test data requirements

RAD042 For devices potentially susceptible to SEDR or SEGR, destructive SEE test data shall reflect irradiation with beam at normal incidence and room ambient temperature.

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="8e96238d63f620a9dd3429e36158b307_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 38 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

Devices containing MOS capacitors are potentially susceptible to single effect dielectric rupture (SEDR). MOSFETs are potentially susceptible to single-event gate rupture (SEGR).

RAD043 Power MOSFETs shall be derated to 75% of their maximum survival drain-source voltage ( $V_{DS}$ ) as determined by SEGR testing at 133% of the worst-case circuit-application gate-source ( $V_{GS}$ ) turnoff voltage

The IRP may approve exceptions based on device rating and technology.

RAD044 The maximum survival drain-source voltage ( $V_{DS}$ ) shall be established from exposure at normal beam incidence to a minimum fluence of  $5e+5$  ions/cm<sup>2</sup> of an ion with the minimum LET of DSEE LET<sub>th</sub> stipulated in RAD026 throughout the sensitive charge-collection region (epilayer(s)) of the device

The Bragg Peak must occur past the epilayer. Typical bounding minimum required ion ranges are presented in Table 13. These can be used for orientation purposes unless otherwise indicated by IRP.

**TABLE 13. TYPICAL BOUNDING MINIMUM PENETRATION DEPTH FOR MOSFET TESTING**

| $V_{DS}$ Rating (V) | Minimum Ion Range ( $\mu$ m) |
|---------------------|------------------------------|
| $\leq 100$          | 30                           |
| 101-250             | 40                           |
| 251 to 400          | 80                           |
| 401-1000            | 200                          |

For extremely high energy heavy ion testing in absence of part de-lidding (such as at Brookhaven National Lab NASA Space Radiation Laboratory NSRL), the part packaging must be characterized sufficiently to determine the minimum LET throughout the sensitive volume.

RAD045 Part types that are susceptible to single-event burnout (SEB) shall not be used in applications with maximum voltage levels exceeding 75% of the maximum survivable voltage as determined in SEB testing

Part types susceptible to SEB include but may not be limited to BJTs, MOSFETs, and Schottky diodes.

RAD046 The survival voltage ( $V_{CE}$ ,  $V_R$ , or  $V_{DS}$ ) shall be established from exposure at normal beam incidence to a minimum fluence of  $5e+5$  ions/cm<sup>2</sup> of an ion with the

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="e8fffbff4a142f1b3a1f57370438e624_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 39 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

minimum LET of DSEE  $LET_{th}$  stipulated in RAD026 throughout the depletion depth of the device when at its maximum voltage

RAD047 Acceptable SEE test data for Power MOSFETs shall be compliant with MIL-STD-750, Method 1080 for test circuit and post gate-stress tests.

The standard differentiates between Characterization and Verification tests and imposes additional requirements such including post gate-stress test performed after irradiation. Verification tests are acceptable to control Project costs provided they envelop the flight application.

## **6.8 SEE Proton Testing**

RAD048 Devices with LET thresholds less than 14 MeV-cm<sup>2</sup>/mg and for which accurate rate calculation is critical shall be proton SEE tested

SEE “soft” devices (i.e., exhibiting low LET threshold in heavy ion testing) are potentially susceptible to proton-induced SEE. Proton rates can drive the risk posture in proton-rich environments. Proton SEE rates estimations from heavy ion characterization data are known to be inaccurate up to one order of magnitude (factor of 10x). Criticality assessments should include this factor. Devices denoted as error-critical and error-vulnerable shall be proton tested for accurate risk quantification. Proton testing is in addition to, and does not substitute for accurate heavy ion cross-section vs. LET curve characterization required by RAD035.

RAD049 Proton SEE testing shall be performed with high energy protons ( $E = 200 \pm 30$  MeV) to a fluence of  $1E+11$  protons/cm<sup>2</sup> unless otherwise approved by IRP due to device TID tolerance or practical test limitations

Proton energy around 200 MeV is commonly available from medical facilities. Protons generate SEE by indirect ionizations. Increased fluence vs. heavy ion testing is required to achieve statistically relevant results in terms of secondary particle production and areal coverage of device features. Proton SEE testing has numerous shortcomings vs. heavy ion testing including limited range of secondary particles. This in turn limits the ability of protons to produce SEE in thick sensitive regions typically associated with destructive effects such as SEL. Proton SEE testing is a valuable complementary effort to heavy ion testing but not a substitute.

Soft complex devices may exhibit SEFIs, and require power cycle/resets to recover nominal operation mode. Too frequent a need for operator intervention may limit the amount of SEFI cross-section data. In most cases, the test can continue in accelerated to capture other (e.g., destructive) SEE modes.

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="e0a2a5a039e90af91716139b5250fcdf_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 40 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

# 7. SEE CIRCUIT LEVEL TESTING

RAD050 Projects shall identify situations when circuit level testing is recommended, and present to IRP for concurrence.

Circuit card assembly (CCA) level testing may be necessary to support circuit analysis through resolution of response uncertainties. The principal focus of circuit testing is on complex mitigation such as hardware-firmware-software interactions difficult to analyze, or with the objective to validate analytically derived post-mitigation rates.

Circuit testing may also be necessary when piece-part testing is not feasible, e.g., in the case of hybrid devices. As circuit testing generally cannot meet de-rating and full characterization requirements, circuit testing in lieu of piece-part characterization typically requires IRP concurrence for NSPAR or request for waiver / deviation (RFW/RFD).

# 8. SEE ANALYSIS

RAD051 SEE Analysis shall be performed at card / box level including SEE propagation analysis, SEE function criticality categorization, and SEE rate calculations

SEE analysis is necessary to verify reliability and availability requirements. This analysis can be performed from many vantage points. The approach is described here as a bottom-up approach. Such approach involves analysis of all SEE modes observed in testing and for all piece-parts in the design Alternatively, projects may perform top-down analyses or hybrid approaches with IRP and Program concurrence. SEE Analyses shall be documented in the Radiation Assessment Matrix (RAM).

RAD052 SEE propagation analysis shall be performed by project electrical design engineer(s) with support from ASD ionizing radiation engineering

SEE propagation analysis is functionally equivalent to mathematical circuit simulations and straightforward to electrical engineering. Its purpose is to determine how SEE types to which the various parts are susceptible to affect the downstream circuit. SEE propagation analysis is based on SEE part characterization data including SEE signature. Detailed understanding of the circuit including that of implemented mitigation is critical to accurate determination of SEE circuit impacts at card or box level. Additional information required for accurate SEE propagation analysis includes understanding of complex electronics design implementation including but not limited to VHDL coding of FPGAs and any EDAC implemented in firmware / software.

RAD053 SEE function criticality categorization shall be performed by project electrical design engineer(s) with support from ASD ionizing radiation engineering according to the definitions in Table 14.

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="7a9db9f671f26bd817164ba4ecd08c2b_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 41 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

SEE functional analysis / criticality categorization is performed to prioritize radiation test and mitigation development efforts and to allow critical radiation effects to be efficiently elevated for system level review and disposition.

**TABLE 14. SEE CATEGORY DEFINITIONS**

| Category (Cat) | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0              | SEE that do not result in a system impact. Errors that escape the circuit-level fault management system become a Cat 1, Cat 2, or a Cat 3 effect. As an example, occasional bit errors in non-critical vehicle-to-ground telemetry are considered Cat 0 effects. Rates for Cat 0 effects have to be known only to the extent of confirming they do not constitute a nuisance or overwhelm mitigation such as filtering or averaging.                                                                                                                                   |
| 1              | Self-recovering SEE that temporarily interrupt or degrade performance, or reduce redundancy, and correct/recover autonomously due to circuit mitigation such as watchdog timers. Recovery process and time must be specified in the circuit analysis. In case recovery is effected by FPGA or other complex electronics, it needs to be verified by the VHDL designer or equivalent. Effects that result in self-recovery of the part but require non-autonomous card / box re-initialization (e.g., by software FDIR, crew or ground intervention) are Cat 2 effects. |
| 2              | Recoverable SEE other than Cat 0 or Cat 1. Cat 2 effects may temporarily interrupt or degrade performance, or reduce redundancy, and require intervention external to the card to correct/recover or reinitialize the system to the prior commanded state. This includes recovery by software FDIR, crew or ground intervention. Recovery process and time must be verified by knowledgeable stakeholders such as FDIR, SW and Ops.                                                                                                                                    |
| 3              | SEE causing unrecoverable effects. These include destructive SEE (e.g., SEB, SEDR, SEGR, SEL) and non-destructive SEE that cause "out-of-spec" or non-recoverable adverse condition on any electronic piece parts in the circuit.                                                                                                                                                                                                                                                                                                                                      |

Cat 1 and 2 effects represent radiation impact to system availability. Cat 3 effects represent radiation impact to system reliability. Alternative SEE categorization available in the literature refers to "error-functional" (equivalent to Cat 0), error-vulnerable (loosely equivalent to Cat 1 and Cat 2) and error-critical (loosely equivalent to Cat 3).

RAD054 SEE rate calculations shall be performed using IRP-approved tools and methods

Rate (probability) calculations can be performed for SEE types such as SET, SEU, SEL, etc. In conjunction with functional analyses, the rates constitute input to risk decisions.

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="009036d641f157d2cd556072d8fb6e9b_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 42 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

SEE rate calculations are performed using accepted tools-of-the-trade, and by experienced radiation engineers.

No widely accepted rate calculation approaches currently exist for other SEE types such as SEGR/SEB, rendering them subject to a risk avoidance approach. Probability predictions for these effects is subject to IRP concurrence.

RAD055 For devices susceptible to proton induced SEE, SEE rates for the proton and heavy ion environments shall be calculated and documented independently.

Proton SEE rates estimations from heavy ion characterization data are acceptable for error-functional devices. Criticality determinations should take into account large uncertainties of proton rates derived from heavy ion data (see rationale of RAD048).

RAD056 Rate calculations shall be performed individually for all driving environments

Different environments drive different end-points, e.g., design decisions vs. mission risk assessment.

## **8.1 Radiation Assessment Matrix (RAM)**

RAD057 EEE Parts radiation data, TID, TNID and SEE compliance status, results of SEE circuit analyses, rates and similarity analysis shall be documented in Radiation Assessment Matrices (RAMs)

The RAM is a tool used to analyze, describe and document the circuit response of each active EEE piece part. The RAM is presented informally to IRP throughout the product life cycle and is formally required for spacecraft, subsystem, and box/card design reviews CDRs, DCRs, and as part of the DAC/VAC analyses. An example RAM is provided in section L.8 Radiation Assessment Matrix (RAM). The RAM provides data for all active piece parts included in the most current parts list culminating with the ABPL.

RAD058 The RAM contents shall comply with Table 15

**TABLE 15. RAM CONTENTS**

|   |                                                                                                                                                                                                                                                                                                                                                                                    |
|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | Parts List tab. Organized at card or box level. For each individual part (P/N), the RAM shall list: <ol style="list-style-type: none"> <li>1. All applicable part numbers (P/Ns) (e.g., Flight and Generic)</li> <li>2. Part radiation characteristics (e.g., DSEE and NDSEE LET thresholds, Weibull parameters)</li> <li>3. TID rating</li> <li>4. Similarity analysis</li> </ol> |
|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="f475ccc05d231e5349e9e439a2788078_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 43 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2 | <p>Circuit Effects tab. Organized at card level. For each individual instance (or group of instances performing same function in circuit), the RAM shall list:</p> <ol style="list-style-type: none"> <li>5. Part number(s)</li> <li>6. Reference designator(s)</li> <li>7. Number of instances if applicable</li> <li>8. Part function in circuit</li> <li>9. SEE response in circuit</li> <li>10. SEE piece part event rate and calculation details. <ol style="list-style-type: none"> <li>a. Separate rates shall be presented for each environment of interest (e.g., GCR and SPE) in sufficient detail to recalculate rates for different DRM duration.</li> <li>b. Details shall include applicable environment definitions (or reference as applicable).</li> </ol> </li> <li>11. Description of SEE circuit mitigation as implemented at card level</li> <li>12. Post-circuit-mitigation response description and time to recovery if applicable</li> <li>13. Post-circuit-mitigation SEE response category</li> <li>14. Post-circuit-mitigation rate</li> <li>15. Box mitigation approach, post box mitigation rate, and post box mitigation time to recovery and response description</li> </ol> |
| 3 | <p>Card-level total rates for Category 1, Category 2, and Category 3 SEE responses. Organized at card level.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

The format for the above data list is in the most recent Radiation Assessment Matrix (RAM) spreadsheet format available from IRP. The Radiation Assessment Matrix will be reviewed in the IRP meetings as necessary. The RAM constitutes the primary radiation input to design reviews.

# 9. SEE TEST PLANNING AND REPORTING

## 9.1 Radiation Test Plan

RAD059 Radiation test readiness reviews (TRR) shall be scheduled to occur no less than 10 business days prior to the scheduled test date, unless otherwise approved by IRP

RAD060 Radiation test plans shall be submitted to the IRP for review and concurrence no less than 3 working days prior to the TRR, unless otherwise approved by IRP

## 9.2 Radiation Test Report

RAD061 Initial test results "flash report" shall be provided to IRP no more than 10 business days after test completion, unless otherwise approved by IRP

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="3d14d18d008a5046d3b287e41f3176b8_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 44 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

The purpose of the flash report is to promptly provide information needed by the project to make immediate decisions. The contents of the flash report will be specified by the IRP.

RAD062 Radiation test reports shall be made available to the project no more than 60 business days after test completion, unless otherwise approved by IRP

# 10. THE JSC IONIZING RADIATION PANEL (IRP)

The Ionizing Radiation Panel (IRP) is the technical authority for AIRES requirements tailoring, interpretation, verification, and other AIRES in-scope tasks. IRP is chaired by the ASD Ionizing Radiation Effects Technical Discipline Lead (TDL) or designee. Participants include Project representatives (NASA and Contractor as applicable), Safety and Mission Assurance, EEE Parts, Reliability engineers and others on an “as needed” basis.

Items coordinated through the IRP include:

- a. Radiation requirements tailoring, interpretation, and verification
- b. IR test schedules (near term/long term) and plans
- c. Common parts testing
- d. Radiation NSPAR review
- e. Review of Similarity checklists
- f. Review of test status and results

IRP will review and resolve radiation related issues applicable to EEE parts testing, circuit performance, reliability rates, validity of radiation data and similarity, and radiation NSPARs. IRP minutes and documentation will be stored on the IRP file server.

## 10.1 Radiation NSPAR Process

RAD063 Radiation NSPARs shall be written by the project and provided to the IRP for dispositioning or elevation for risk acceptance.

The Radiation Non-Standard Parts Approval Request (NSPAR) process provides an avenue for data equivalency assessments. NSPARs provide data in support of equivalent risk decisions in case specific requirements are not met. Examples include flight heritage data in enveloping applications, test data on parts in the same family with similarity rationale, etc. Other mitigating circumstances that can be addressed in a Radiation NSPAR to allow part usage may consist of limited duty cycles, practical aspects preventing testing to full compliance, etc.

Information presented to IRP will include system impact of potential radiation effects applicable to all part instances covered by the NSPAR. Upon request by the project, Radiation NSPARs will be scheduled for presentation at IRP. NSPARs will be made

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 203" src="c9ad263212ccc3e43da72ed4cfe82f44_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 45 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

available for review by the IRP chair no less than one week before scheduled for presentation at the IRP. The NSPAR format is provided in Appendix B.

IRP is the technical authority for AIRES requirements interpretation matters. Equivalent risk decisions remain at IRP level, and are documented as Radiation NSPAR approvals. Risk acceptance decisions and reclama will be elevated to the EA PCB or other cognizant program board.

# 11. DOCUMENTATION

## 11.1 Radiation Test Plan

RAD064 At a minimum, SEE test plans shall include the information in Table 16

**TABLE 16. MINIMUM CONTENTS OF AN SEE TEST PLAN**

|    |                                                                                                                                                                                                                                                                                     |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | Device type, generic part number, part description, part manufacturer, #samples, and #controls.                                                                                                                                                                                     |
| 2  | All traceability information on the device under test, including part type, manufacturer's part number, description, lot-date code (serial numbers if applicable), etc.                                                                                                             |
| 3  | Photographs of the DUT prior to de-lidding showing package markings                                                                                                                                                                                                                 |
| 4  | Number of devices to be tested and the minimum number of test data points to be taken.                                                                                                                                                                                              |
| 5  | Flight application(s) in which the device will be used                                                                                                                                                                                                                              |
| 6  | Constraints data (activity that immediately constrains or is constrained by this test), qualification test, evaluation purpose, etc.                                                                                                                                                |
| 7  | Governing test protocol (e.g., MIL-STD-883 Method 1019)                                                                                                                                                                                                                             |
| 8  | Test facility, test parameters, test conditions and specification limits (pass-fail criteria) and rationale, test dates, if lidded or de-lidded, test particle species or test cocktail; range determination; LET at sensitive volume; energy determination; accumulated dose; etc. |
| 9  | Test Team; define who has the authority to red-line test procedure                                                                                                                                                                                                                  |
| 10 | Test Circuit schematic including all instrumentation interfaces                                                                                                                                                                                                                     |
| 11 | Test instrumentation list, serial #, calibration date interface diagram, and settings                                                                                                                                                                                               |
| 12 | Definition of functional measurements required pre- and post-SEE testing                                                                                                                                                                                                            |
| 13 | Test procedures                                                                                                                                                                                                                                                                     |
| 14 | Conditions that must be maintained during test or inspection, i.e., stresses (ambient, environmental conditions, electrical) duration and sequence, as well as precautions to be observed to prevent damage.                                                                        |

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 203" src="bcd27d2a67af43868a5ca81ac6cbb349_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 46 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

RAD065 At a minimum, TID test plans shall include the information in IRP Tech Memo TBR

Reserved

## 11.2 Radiation Test Report

RAD066 At a minimum, SEE test reports shall include the information in Table 17

**TABLE 17. MINIMUM CONTENTS OF AN SEE TEST REPORT**

|    |                                                                                                                                                                  |
|----|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | Self-contained test summary                                                                                                                                      |
| 2  | All information previously required for / included in the test plan, with redlines                                                                               |
| 3  | Test personnel                                                                                                                                                   |
| 4  | Pictures of experimental setup and die structure (when appropriate)                                                                                              |
| 5  | 'As Run' Test Procedure (in sufficient detail such that the test can be repeated)                                                                                |
| 6  | Description of SEE modes including recovery steps                                                                                                                |
| 7  | Scope screen captures and raw output files as acquired                                                                                                           |
| 8  | Description of any test anomalies                                                                                                                                |
| 9  | Test results including raw and processed data for all parts and each event type, e.g., cross-section vs. LET, Weibull fit, error bars, pass/fail conditions etc. |
| 10 | Post-test functional evaluation or characterization of test device                                                                                               |
| 11 | Copy of beam log as inline and as Excel attachment                                                                                                               |

RAD067 At a minimum, TID test reports shall include the information in IRP Tech Memo TBR

Reserved

## 11.3 Data Retention Requirements

RAD068 The project shall maintain the radiation data (Test Procedures, Test Reports, RAM, Design Review Status Chart) in the project repository.

The project owns the requirement verification and documentation. The IRP will maintain a selective repository of radiation data such as test reports for the benefit of other projects. Radiation data are in many cases application specific. Applicability of radiation data for other applications must be assessed in coordination with IRP and in the full context of MEAL.

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="e7fdc38cfe08fed59228fb881bbae0d9_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 47 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

# 12. ADDITIONAL GUIDANCE

## 12.1 Part selection best practices

Use of parts with known radiation performance is strongly recommended for critical hardware designs. This is generally the most cost-effective approach to ensure that the performance requirements are met in the mission radiation environment. Many military (DSCC / 5962) and high reliability / space grade parts from reputable manufacturers are guaranteed for both SEE and total dose (TID and/or TNID/DD) characteristics. This type of parts also typically provide consistent manufacturing processes and lot traceability, which ensure applicability of radiation test data to flight parts.

Depending on the EEE parts manufacturer, the designation of “radiation hard” may or may not include SEE hardness. SMDs / spec sheets must be inspected for both total dose and SEE. TID characteristics are given as a dose tolerance level, for example 50 krad(Si). The TID guarantee must meet project specification. SEE characteristics are typically given as an LET threshold for destructive effects, for example SEL immune to LET = 60 MeV-cm<sup>2</sup>/mg. Susceptibility to non-destructive SEE may be given as a (separate) LET threshold and/or an average SEU/SET/SEE rate per bit in typical environment such as GEO. The designation of SEE “radiation tolerant” typically refer to complex parts such as processors / FPGAs that are immune to destructive SEE but susceptible to non-destructive SEE. Recovery after non-destructive SEE should not be assumed to be trivial. In many cases, the “upset” part has to be reconfigured, reprogrammed, re-activated etc. requiring ground and/or crew time. Excessive susceptibility of “radiation tolerant” parts may be a nuisance that effectively renders them as failing to meet performance requirements. Radiation engineering can provide projects support down-selecting parts candidates and advise on potential issues.

Using commercial parts in the design poses inherent risks. Unless specifically designed for radiation tolerance, new technology and high speed commercial parts are typically significantly more susceptible to radiation effects including destructive SEE and total dose degradation. Radiation test data available for commercial parts is inherently less reliable as manufacturing process changes may affect key radiation properties. These changes may not even be advertised by the manufacturers, and/or lot traceability may not be possible. Radiation testing performed on prototype units after the design is mostly completed is useful to identify the risk posture. In rare cases, extensive testing at this stage may identify mitigation strategy, but it is a costly process to provide “band-aids” in limited instances and not a panacea for incorrect designs.

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="a13a4831ce80e432d758981c17bdcd24_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 48 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

## 12.2 SEE Rate calculations

### 12.2.1 Heavy ion rates

First, test data representing SEE cross-sections as function of LET are fitted with a 4-parameter Weibull curve of the form:

$$\sigma(L) = \sigma_0 \left[ 1 - e^{-\left(\frac{L-L_0}{W}\right)^s} \right]$$

where  $\sigma_0$  = saturation cross section ( $\mu\text{m}^2/\text{bit}$ ),  $L$  = LET ( $\text{MeV-cm}^2/\text{mg}$ ),  $L_0$  = threshold LET ( $\text{MeV-cm}^2/\text{mg}$ ) such that  $\sigma(L) = 0$  for  $L < L_0$ ,  $W$  = width parameter ( $\text{MeV-cm}^2/\text{mg}$ ), and  $s$  = shape parameter (dimensionless).

Then, rates are calculated using tools-of-the-trade using as input the mission environment and the previously fitted parameters. The most popular software tool is CRÈME 96, which is found on the internet at <https://crème.isde.vanderbilt.edu/>. This tool is available to the public. Other tools are SPENVIS (web-based, public), OMERE (downloadable freeware) and Space Radiation (SpaceRad) (downloadable w/ purchase required).

### 12.2.2 Proton rates

Similar to heavy ions, SEE cross-sections a function of energy are first fitted with Weibull or Bendel curves. Then proton-induced SEE rates for proton environments can be calculated using tools such as CRÈME 96. The functional form for Bendel curves are described on the CRÈME website.

### 12.2.3 Proton rates derived from heavy ion data

Proton rates can be estimated from the heavy ion test. The estimations are inaccurate (typically, conservative) and subject to requirements in this document. EV radiation effects engineers can help with the calculations.

### 12.2.4 Heavy ion rates derived from proton data

An empirical approach was developed by E. Petersen in 1995 to correlate a part's heavy ion and proton SEE susceptibility by a single quantity referred as the Figure of Merit (FOM). The FOM approach was subsequently implemented in the ProTest tool developed by Dr. P. O'Neill at JSC. ProTest specifically assumes ISS environment (500 km altitude, 51.6 degrees inclination orbit) and 100 mils Aluminum-equivalent shielding. Historically, the method has proven conservative for deriving SEU and SET. The method is not considered reliable for DSEE rate predictions due to limited range /

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 203" src="d0871c645f74b81d0ef4dbbc3fd009a5_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 49 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

average LET of secondary particles, and limited statistics / physical coverage of the device features. Heavy ion rate determination from proton data is only accepted for non-critical hardware and contingent upon IRP approval.

## 12.3 Radiation susceptibility of different EEE part types and technologies

Understanding parts' susceptibilities to different types of radiation effects is critical to part selection and testing. Table 18 provides guidance on effects typically expected from different EEE part types and technologies for HSF type mission environments but it is not comprehensive.

**TABLE 18. TYPICAL RADIATION EFFECTS FOR VARIOUS PART TECHNOLOGIES**

| Device Type               | SEL | SET<br>SEU | SEB | SEGR <sup>1</sup> | SEDR | SEFI | SBU<br>MBU | TID | ELDRS | TNID<br>DDD |
|---------------------------|-----|------------|-----|-------------------|------|------|------------|-----|-------|-------------|
| Linear Bipolar            |     | X          |     |                   | X    |      |            | X   | X     | X           |
| Bi-CMOS                   | X   | X          |     |                   | X    |      |            | X   | X     | X           |
| CMOS                      | X   | X          |     |                   |      |      |            | X   |       | X           |
| Pwr MOSFET                |     |            | X   | X                 |      |      |            | X   |       |             |
| Power BJT                 |     |            | X   |                   |      |      |            | X   | X     | X           |
| Low voltage & current BJT |     | X          |     |                   |      |      |            | X   | X     | X           |
| FPGAs                     | X   | X          |     |                   |      | X    |            | X   |       |             |
| Memory                    | X   |            |     |                   |      | X    | X          | X   |       |             |
| Voltage Reg/f             | X   | X          |     |                   |      |      |            | X   |       |             |
| Optoelectronic            | X   | X          | X   |                   |      |      |            | X   |       | X           |
| Schottky                  |     |            | X   |                   |      |      |            |     |       |             |
| Xtal Oscillators          | X   | X          |     |                   |      |      |            | X   |       |             |
| GaAs RF                   |     | X          | X   |                   |      |      |            |     |       | X           |
| GaN HEMT                  |     |            | X   | X                 | X    |      |            |     |       |             |
| SiC                       |     |            | X   | X                 |      |      |            | X   |       | X           |
| Flash ROM                 | X   |            |     |                   |      |      | X          | X   |       |             |
| CPU/GPU                   | X   | X          | X   |                   |      | X    | X          | X   |       |             |

<sup>1</sup> And/or non-catastrophic damage e.g., lss leakage

## 12.4 SET signatures

SET signatures are traditionally determined by radiation testing. Often times, the circuit design pre-dates the availability of test data. For such cases, SET signature guidelines are provided in Table 19. These are to be interpreted as enveloping 90% of the applications. An initial design assessment should be performed by the circuit designer using the maximum SEE signatures and circuit simulation software. Per RAD029, radiation characterization testing specific for the application may be required based on circuit analysis results (e.g., when insufficient margin exists in the circuit mitigation and

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 203" src="e1fecf7627897191f471ea45e46d3bd6_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 50 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

design changes are not possible) in order to confirm actual SEE signatures, rates and impacts.

**TABLE 19. SET SIGNATURE GUIDELINES**

| Device Types                                           | SET signature at the device output                                                                     |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Op-Amps                                                | $V_{\max} = +/- V_{cc}$ , $T_{\max} = 200 \mu s$                                                       |
| Comparators<br>Voltage Regulators<br>Voltage Reference | $V_{\max} = +/- V_{cc}$ , $T_{\max} = 10 \mu s$                                                        |
| Optocouplers                                           | $V_{\max} = +/- V_{cc}$ , $T_{\max} = \text{rise time} + \text{fall time from the vendor data sheet.}$ |

## 12.5 Radiation design recommendations for non-critical hardware

The following recommendations are provided for design of non-critical hardware. EV radiation effects engineers strongly recommend 1-7 on all new or COTS designs. If the mission is deep space and of a long duration, 11 and 12 are strongly recommended.

- a. Purchase the most radiation tolerant parts that are feasible to buy (short enough lead time and within the budget.)
- b. Choose parts with some history of space usage.  
Although the data is not complete, it is better than nothing and cuts down the potential test items.
- c. De-rate the parts  
Temperature and power are stressful to most parts.
- d. Proton testing
  1. Relatively inexpensive test that finds really troublesome parts.
  2. Useful for down-select tests due to costs/schedule
  3. Testing at board level is recommended.
- e. Add strings/redundancy  
If the parts are not tested or characterized, another string or two can help to reduce the risk of failure.
- f. Assess and mitigate potential radiation effects propagation through interfaces (do no harm to the vehicle)
- g. Implement radiation tolerant power converters and over-current protection to control hazards.
- h. Use operational controls to minimize SEE (turn off the unit when possible or power cycle before some operations).
- i. Implement current monitoring, limiting and autonomous power cycling ability to increase chance of surviving SEL.
- j. Implement health monitoring (e.g., watch-dog timers) and autonomous reset / power cycling ability to mitigate SEFI.

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 210" src="ec607b096ccbc23661be18061b13dc5c_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 51 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

- k. Perform Survivability testing at NASA Space Radiation Laboratory at Brookhaven National Laboratory

This is a board level test that determines survivability. No characterization is performed.

- l. Heavy ion testing

Appropriate method for characterizing electronic piece parts for deep space.

## 12.6 SEE heavy ion testing: High energy (NSRL) vs. low energy (TAMU, LBNL); part-level characterization vs. card-level testing

Traditional heavy ion testing is performed at part level. Due to the short range of the particles, testing in low energy beams such as TAMU and Berkeley (LBNL) require parts to be delidded. Heavy ion testing as NSRL (Brookhaven, BNL) is considered attractive by many projects because it allows testing at card level, and without the need to de-lid parts. This convenience comes with limitations. The projects must coordinate with ASD ionizing radiation engineering to assess the most appropriate test method given the project criticality, parts list, make vs. buy, and other constraints.

As a starting point, the following tables summarize the advantages (denoted by "+") and disadvantages (denoted by "-") of different test methods. In general, low energy testing is performed at part level, and high energy testing at card level. For clarity however, the comparisons of low energy vs. high-energy testing, and part level vs. card level are presented separately.

**TABLE 20. ADVANTAGES AND DISADVANTAGES OF LOW-ENERGY- VS. HIGH-ENERGY HEAVY ION TESTING**

| Low Energy (TAMU, LBNL)                                  | High Energy (BNL NSRL)                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Beam time cost (+)                                       | 8x more expensive (NSRL vs TAMU) (-)                                                                                                                                                                                                                                                                                                                                                   |
| DC beam (+)                                              | Pulsed beam; duty factor 10% (-)                                                                                                                                                                                                                                                                                                                                                       |
| Parts de-lidding required (-)                            | No de-lidding required (+)                                                                                                                                                                                                                                                                                                                                                             |
| Flip-chip testing difficult or unfeasible (-)            | Flip-chip testing possible (+)                                                                                                                                                                                                                                                                                                                                                         |
| Test LET known a priori (+)                              | Test LET not known a priori (-) <ul style="list-style-type: none"> <li>- VDBP applicable to select parts only</li> <li>- Part sectioning analysis may be required</li> <li>- Min LET guarantee limited by thickest part and applicable to entire card if card-level test</li> <li>- For card level test, each part is subject to different LET given variable lid thickness</li> </ul> |
| High fluence / LET data point guarantees good statistics | For VDBP, lower fluence / LET data point is driven by TID concerns                                                                                                                                                                                                                                                                                                                     |

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                  |                                                                 |                        |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="103 77 245 203" src="d7c12954c40e29c6aae7d6b51dc848fd_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                  | Date: 16 April 2021                                             | Page 52 of 53          |
|                                                                                                                  | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

**TABLE 21. ADVANTAGES AND DISADVANTAGES OF PART- VS. CARD- (OR BOX) LEVEL HEAVY ION TESTING**

| Part level                                                                                  | Card level                                                                                                                       |
|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Requires dedicated test board (-)                                                           | Does not require test board (+)                                                                                                  |
| Instrumented for full characterization (+)                                                  | Limited test observables (-)                                                                                                     |
| Enables SEE criticality analysis (+)                                                        | No SEE criticality analysis (-)                                                                                                  |
| High statistical confidence in error modes (+)                                              | More frequent error modes “swamp” the test data. Rare critical error modes may not be caught due to test fluence limitations (-) |
| Enables “designing out” SEE (+)                                                             | Provides limited data toward mitigation (-)                                                                                      |
| Test data are application independent* (+)                                                  | Test data are circuit specific (-)                                                                                               |
| Intrinsic part susceptibility only (-)                                                      | Reflects FW / SW effects (+)                                                                                                     |
| Intrinsic part susceptibility allows analytic derivation of SW mitigation effectiveness (+) | Incorrect assessment of SW mitigation effectiveness due to high test flux (-)                                                    |
| Allows compliant derating (+)                                                               | Inherently non-compliant for derating (-)                                                                                        |

\*In many cases

See Cover for full disclosure. Verify correct revision before use at

<https://qmsmasterlist.jsc.nasa.gov/Home.aspx/Index>

|                                                                                                                   |                                                                 |                        |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------|
| <img alt="JSC Engineering NASA logo" data-bbox="77 999 208 1139" src="1fbb8334969e24e3f15a60c0ed5c1b4a_img.jpg"/> | Revision: Basic                                                 | Document No: JSC-67551 |
|                                                                                                                   | Date: 16 April 2021                                             | Page 53 of 53          |
|                                                                                                                   | Title: JSC Avionics Ionizing Radiation Effects Standard (AIRES) |                        |

# APPENDIX A: NSPAR TEMPLATE

![Small JSC Engineering NASA logo](4c8721520bc36623aa6c19562146bab9_img.jpg)

Small JSC Engineering NASA logo

## Part Number and Function

![NASA logo](7c166dd7ef469f2cddf2fc4025f9188b_img.jpg)

NASA logo

---

|                                                                                                                                                            |                        |                            |                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|----------------------------|---------------------------------------------|
| ➤ <b>IRP Date:</b>                                                                                                                                         |                        |                            |                                             |
| ➤ <b>Project Name:</b>                                                                                                                                     | Project Engineer Name: | Responsible Engineer Name: |                                             |
| ➤ <b>System name:</b> <i>Next/larger assembly</i>                                                                                                          | Criticality:           | Effectivity:               | <i>Which flights will this NSPAR cover.</i> |
| ➤ <b>Part Number / Manufacturer / Description:</b>                                                                                                         |                        |                            |                                             |
| ➤ <b>Application assessment:</b>                                                                                                                           |                        |                            |                                             |
| ➤     Function of the part: <i>What is the impact of radiation effects (recoverable and/or non-recoverable as applicable), include all applications.</i>   |                        |                            |                                             |
| ➤ <b>Compliance Assessment:</b>                                                                                                                            |                        |                            |                                             |
| ➤     What requirement(s) is (are) not met, non-compliance details                                                                                         |                        |                            |                                             |
| ➤ <b>Rationale/Justification:</b>                                                                                                                          |                        |                            |                                             |
| ➤     Rationale why the part is usable as-is, or determine the rates for risk quantification. Include any flight history, testing, similarity, rates, etc. |                        |                            |                                             |

- **Disposition:**
- **NSPAR** number as needed.

Export Control Designation

Download Template: [http://ea.isc.nasa.gov/eawebfiles/EA-ISO9000/JSC-67551\\_NSPAR\\_Template.pptx](http://ea.isc.nasa.gov/eawebfiles/EA-ISO9000/JSC-67551_NSPAR_Template.pptx)

See Cover for full disclosure. Verify correct revision before use at  
<https://qmsmasterlist.isc.nasa.gov/Home.aspx/Index>