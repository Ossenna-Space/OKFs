

# Compendium of Radiation Effects Test Results from NASA Goddard Space Flight Center

Alyson D. Topper, Megan C. Casey, Edward P. Wilcox, Michael J. Campola, Donna J. Cochran, Martha V. O'Bryan,  
Jonathan A. Pellish, and Peter J. Majewicz

**Abstract-- Total ionizing dose, displacement damage dose, and single event effects testing were performed to characterize and determine the suitability of candidate electronics for NASA space utilization. Devices tested include optoelectronics, digital, analog, and bipolar devices.**

## I. INTRODUCTION

NASA spacecraft are subjected to a harsh space environment that includes exposure to various types of radiation. The performance of electronic devices in a space radiation environment is often limited by its susceptibility to single event effects (SEE), total ionizing dose (TID), and displacement damage dose (DDD). Ground-based testing is used to evaluate candidate spacecraft electronics to determine risk to spaceflight applications. Interpreting the results of radiation testing of complex devices is quite difficult. Given the rapidly changing nature of technology, radiation test data are most often application-specific and adequate understanding of the test conditions is critical [1].

These test results show sensitivities of candidate spacecraft and electronic devices to SEE including single-event upset (SEU), single-event functional interrupt (SEFI), single-event latchup (SEL), single-event burnout (SEB), single-event gate rupture (SEGR), single-event transient (SET), TID, and DDD effects. All tests were performed between March 2020 and February 2021.

## II. TEST TECHNIQUES AND SETUP

### A. Test Method

TID testing was performed using MIL-STD-883, Test Method 1019.9 [2] unless otherwise noted as research. All tests were performed at room temperature and with nominal power supply voltages, unless otherwise noted. Based on the application, samples would be tested in a biased and/or unbiased configuration. Functionality and parametric changes were measured after step irradiations (for example: every 10 krad(Si)).

Unless otherwise noted, SEE testing was performed in accordance with JESD57A test procedures [3]. Depending on the DUT and the test objectives, one or two SEE test methods were typically used:

- a) *Dynamic* – The DUT was exercised and monitored continuously while being irradiated. The type of input stimulus and output data capture methods are highly device- and application-dependent. In all cases the power supply levels were actively monitored during irradiation. These results are highly application-dependent and may only represent the specific operational mode tested.
- b) *Static/Biased* – The DUT was provided basic power and configuration information (where applicable), but not actively operated during irradiation. The device output may or may not have been actively monitored during irradiation, while the power supply current was actively monitored for changes.

In SEE experiments, DUTs were monitored for soft errors, such as SEUs, and for hard errors, such as SEGR. Detailed descriptions of the types of errors observed are noted in the individual test reports.

SET testing was performed using high-speed oscilloscopes controlled via NI LabVIEW® [4]. Individual criteria for SETs are specific to the device and application being tested. Please see the individual test reports for details.

Heavy ion SEE sensitivity experiments include measurement of the linear energy transfer threshold ( $LET_{th}$ ) and cross section at the maximum measured LET. The  $LET_{th}$  is defined as the maximum LET value at which no effect was observed at an effective fluence of  $1 \times 10^7$  particles/cm<sup>2</sup>. In the case where events are observed at the smallest LET tested,  $LET_{th}$  will either be reported as less than the lowest measured LET or determined approximately as the  $LET_{th}$  parameter from a Weibull fit.

---

This work was supported in part by the NASA Electronic Part and Packaging Program (NEPP) and NASA Flight Projects.

Alyson D. Topper, Martha V. O'Bryan, and Donna J. Cochran, are with SSAL work performed for NASA Goddard Space Flight Center, Code 561.4, Greenbelt, MD 20771 (USA), phone: 301-286-5489, email: alyson.d.topper@nasa.gov.

Edward P. Wilcox, Michael J. Campola, Megan C. Casey, Jonathan A. Pellish, and Peter J. Majewicz are with NASA/GSFC, Code 561.4, Greenbelt, MD 20771 (USA), phone: 301-286-5427, email: michael.j.campola@nasa.gov.

### B. Test Facilities – TID

TID testing was performed using a gamma source. Dose rates used for testing were between 10 mrad(Si)/s and 2.6 krad(Si)/s.

### C. Test Facilities – DDD

Neutron DDD tests were performed at the University of Massachusetts Lowell's (UML) Fast Neutron Irradiation Facility (FNI) [5].

### D. Test Facilities – SEE

Heavy ion experiments were conducted at the Texas A&M University Cyclotron (TAMU) [6] and Brookhaven National Laboratory's NASA Space Radiation Laboratory (NSRL). Energies and Linear Energy Transfers (LETs) available varied slightly from one test date to another.

TID electron testing was performed at Goddard Space Flight Center using the 2-MeV Van de Graaff. [7]

## III. TEST RESULTS OVERVIEW

Abbreviations for principal investigators (PIs) are listed in Table I. Abbreviations and conventions are listed in Table II. Summary of TID, DDD, and SEE test results from February 2020 through February 2021 are listed in Table III. Please note that these test results can depend on operational conditions.

TABLE I  
LIST OF PRINCIPAL INVESTIGATORS

| Principal Investigator (PI) | Abbreviation |
|-----------------------------|--------------|
| Megan C. Casey              | MCC          |
| Michael J. Campola          | MJC          |
| Edward (Ted) Wilcox         | TW           |

TABLE II  
ACRONYM LIST

| Acronym | Definition                              |
|---------|-----------------------------------------|
| <       | SEE observed at lowest tested LET       |
| >       | No SEE observed at lowest tested LET    |
| CMOS    | Complementary Metal Oxide Semiconductor |
| COTS    | Commercial Off the Shelf                |
| DDD     | Displacement Damage Dose                |
| DUT     | Device Under Test                       |
| FNI     | Fast Neutron Irradiation Facility       |
| GSFC    | Goddard Space Flight Center             |
| HDR     | High Dose Rate                          |
| LDC     | Lot Date Code                           |
| LDR     | Low Dose Rate                           |
| LET     | Linear Energy Transfer                  |
| NEPP    | NASA Electronics Parts and Packaging    |
| NSRL    | NASA Space Radiation Laboratory         |
| PI      | Principal Investigator                  |
| REAG    | Radiation Effects & Analysis Group      |
| SEB     | Single-Event Burnout                    |
| SEE     | Single-Event Effect                     |
| SEFI    | Single-Event Functional Interrupt       |
| SEGR    | Single-Event Gate Rupture               |
| SEL     | Single-Event Latchup                    |
| SET     | Single-Event Transient                  |
| SEU     | Single-Event Upset                      |
| SRAM    | Static Random-Access Memory             |
| TAMU    | Texas A&M University                    |
| TID     | Total Ionizing Dose                     |
| UML     | University of Massachusetts Lowell      |

TABLE III  
SUMMARY OF TEST RESULTS

| Part Number                                | Manufacturer            | LDC: (REAG ID#) | Device Function            | Technology | PI  | Sample Size | Test Env. | Test Facility (Test Date) | Test Results (Effect, Dose Level/Energy, Results)                                                                                                                                                                                                                                                         |
|--------------------------------------------|-------------------------|-----------------|----------------------------|------------|-----|-------------|-----------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 22FDX SRAM-based Line-Monitor Test Vehicle | GlobalFoundries         | n/a; (18-007)   | 22 nm SRAM                 | CMOS       | MCC | 2           | Electron  | GSFC (Oct 2020)           | Measured SEUs due to direct ionization of low-energy electrons. Upsets were measured at all electron energies tested from 130 keV to 1.6 MeV. [8]                                                                                                                                                         |
| 61055-305                                  | Micropac                | 2018; (21-003)  | Phototransistor            | Si         | TW  | 12          | Neutron   | UML (Dec 2020)            | Unbiased irradiation; No degradation noted to $4.55 \times 10^{11}$ n/cm <sup>2</sup> .                                                                                                                                                                                                                   |
| 62087-305                                  | Micropac                | 2018; (21-004)  | LED                        | GaAs       | TW  | 12          | Neutron   | UML (Dec 2020)            | Unbiased irradiation; No degradation noted to $4.55 \times 10^{11}$ n/cm <sup>2</sup> .                                                                                                                                                                                                                   |
| 80SCLQ060SCS                               | International Rectifier | 1839; (20-007)  | Schottky Diode             | Si         | TW  | 3           | Heavy Ion | TAMU (Dec 2020)           | SEB LET <sub>th</sub> > 42.7 (Vr: 61.5 V, 25 MeV/amu Xe, normal incidence, range: 220 $\mu$ m, fluence: $1 \times 10^7$ /cm <sup>2</sup> ) SEB LET <sub>th</sub> > 60 (Vr: 65 V, 25 MeV/amu Xe, normal incidence with beam degraders, range: 88 $\mu$ m, fluence: $1 \times 10^7$ /cm <sup>2</sup> ). [9] |
| ACPL-785E                                  | Avago                   | 1649; (17-047)  | Analog Isolation Amplifier | Bipolar    | MJC | 2           | Heavy Ion | NSRL (Dec 2020)           | No destructive SEEs or SETs observed. Largest observed transient was 5V, 40 $\mu$ s with a DC input. A varied response was seen using an input square wave including delays in one and/or both output channels. [10]                                                                                      |
| AD9814                                     | Analog Devices          | 1531A; (19-051) | Processor                  | CMOS       | MCC | 8           | Gamma     | GSFC (Sep 2020)           | TID LDR, All parameters tested remained within specification up to 16.3 krad(Si).                                                                                                                                                                                                                         |
| ADG201                                     | Analog Devices          | 1635; (21-002)  | Analog Switch              | CMOS       | TW  | 1           | Heavy Ion | TAMU (Dec 2020)           | SEL LET <sub>th</sub> > 75 (VDD: 16.5 V, Temp: 90 °C, 25 MeV/amu Xe at 45 degrees, fluence: $1 \times 10^7$ /cm <sup>2</sup> ). [11]                                                                                                                                                                      |
| DS25BR100                                  | Texas Instruments       | n/a; (20-016)   | LVDS Buffer                | CMOS       | TW  | 3           | Heavy Ion | TAMU (Dec 2020)           | SEL Observed: $20 < \text{LET}_{th} < 31$ MeV-cm <sup>2</sup> /mg. Parts failed catastrophically.                                                                                                                                                                                                         |
| JANS2N2222                                 | Semicoa                 | 2013; (20-012)  | NPN Transistor             | Bipolar    | TW  | 22          | Gamma     | GSFC (Jan 2021)           | TID LDR, All parts within specification at 20 krad(Si) h <sub>FE3</sub> below specification at 30 krad(Si) (minimum gain observed: 94)                                                                                                                                                                    |
|                                            |                         | 2006; (20-013)  |                            |            |     | 22          |           |                           | TID LDR, All parts within specification at 20 krad(Si) h <sub>FE3</sub> below specification at 30 krad(Si) (minimum gain observed: 96)                                                                                                                                                                    |
|                                            |                         | 2006A; (20-014) |                            |            |     | 22          |           |                           | TID LDR, All parts within specification at 20 krad(Si) h <sub>FE3</sub> below specification at 30 krad(Si) (minimum gain observed: 91)                                                                                                                                                                    |

| Part Number     | Manufacturer           | LDC; (REAG ID#) | Device Function           | Technology  | PI  | Sample Size | Test Env. | Test Facility (Test Date) | Test Results (Effect, Dose Level/Energy, Results)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------|------------------------|-----------------|---------------------------|-------------|-----|-------------|-----------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LP2951          | Texas Instruments      | 1911A; (19-049) | Voltage Regulator         | Bipolar     | MCC | 8           | Gamma     | GSFC (Aug 2020)           | TID LDR, Tested to 16.3 krad(Si), Output voltage went out of spec between 2.5 and 5.9 krad(Si) when biased with 5 V and between 5.9 and 7.5 krad(Si) when biased with 3.3 V. The load regulation went out of spec between 12.4 and 14 krad(Si) (5 V and $I_L = 100$ mA) and 10.8 and 12.4 krad(Si) (3.3 V and $I_L = 100$ mA). The load regulation for the unbiased parts also went out of spec for 3.3 V and 75 mA between 14 and 16.3 krad(Si), but all of the other parts stayed in spec. Ground current went out of spec (5 V and $I_L = 100$ mA) between 8.5 and 12.4 krad(Si) and (3.3 V and $I_L = 100$ mA) between 8.5 and 10.8 krad(Si). |
| MAX4651EUE      | Maxim                  | 1831; (21-001)  | Analog switch             | CMOS        | TW  | 12          | Gamma     | GSFC (Feb 2021)           | TID HDR, All parameters tested remained within specification up to 50 krad(Si). [12]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| QI-SWIR-VGA15XS | Semi Conductor Devices | n/a; (20-008)   | Camera Electronics Module | InGaAs/CMOS | MCC | 1           | Gamma     | GSFC (Sep 2020)           | TID HDR, All parameters tested remained within specification up to 17.7 krad(Si).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## IV. TEST RESULTS AND DISCUSSION

As in our past workshop compendia of GSFC test results, each device under test has a detailed test report available online at <http://radhome.gsfc.nasa.gov> [13] and at <http://nepp.nasa.gov> [14] describing in further detail the test method, conditions and monitored parameters, and test results. This section contains a summary of testing performed on a selection of featured parts.

### A. LP2951, Texas Instruments, Voltage Regulator

Texas Instruments' LP2951 is an adjustable micropower voltage regulator. It can accommodate a wide input supply voltage range up to 30 V. This voltage regulator can output either a fixed or adjustable voltage. [15]

The LP2951 was TID tested at GSFC's gamma chamber with a low dose rate (LDR) up to 16.3 krad(Si). Eight parts were irradiated with two used as controls. Three DUTs were biased at 5 V, three were biased at 3.3 V, and the remaining two were unbiased during irradiation. Output voltage went below specification between 2.5 and 5.9 krad(Si) when biased with 5 V (see Fig. 1.) and between 5.9 and 7.5 krad(Si) when biased with 3.3 V. The load regulation (with conditions 5 V and  $I_L = 100$  mA) went above specification between 12.4 and 14 krad(Si) and 10.8 and 12.4 krad(Si) with the conditions 3.3 V and  $I_L = 100$  mA. The load regulation for the unbiased parts also went above specification (for conditions 3.3 V and  $I_L = 75$  mA) between 14 and 16.3 krad(Si), but all of the other parts stayed in specification. Ground current (with conditions 5 V and  $I_L = 100$  mA) went above specification between 8.5 and 12.4 krad(Si) and (with conditions 3.3 V and  $I_L = 100$  mA) between 8.5 and 10.8 krad(Si). All remaining measured specifications stayed within specification up to 16.3 krad(Si).

![Figure 1: LP2951 Output Voltage (V) vs. Total Ionizing Dose (krad(Si)). The graph shows four data series: CTRL Avg (blue circles), Biased (5 V) Avg (red squares), Biased (3.3 V) Avg (magenta diamonds), and Unbiased Avg (green triangles). The y-axis ranges from 4.4 to 5.1 V, and the x-axis ranges from 0 to 18 krad(Si). Dashed lines indicate the specification minimum (approx. 4.95 V) and maximum (approx. 5.05 V). The CTRL Avg remains constant at 5.0 V. The Biased (5 V) Avg starts at 5.0 V and drops to ~4.75 V at 16 krad(Si). The Biased (3.3 V) Avg starts at 5.0 V and drops to ~4.7 V at 16 krad(Si). The Unbiased Avg starts at 5.0 V and drops to ~4.55 V at 16 krad(Si).](6bbc398f520a7bcc5491cab18d3e4cac_img.jpg)

| Total Ionizing Dose [krad(Si)] | CTRL Avg [V] | Biased (5 V) Avg [V] | Biased (3.3 V) Avg [V] | Unbiased Avg [V] |
|--------------------------------|--------------|----------------------|------------------------|------------------|
| 0                              | 5.00         | 5.00                 | 5.00                   | 5.00             |
| 2                              | 5.00         | 5.00                 | 5.00                   | 5.00             |
| 4                              | 5.00         | 5.00                 | 5.00                   | 5.00             |
| 6                              | 5.00         | 4.98                 | 4.98                   | 4.95             |
| 8                              | 5.00         | 4.95                 | 4.95                   | 4.85             |
| 10                             | 5.00         | 4.90                 | 4.90                   | 4.75             |
| 12                             | 5.00         | 4.85                 | 4.85                   | 4.60             |
| 14                             | 5.00         | 4.78                 | 4.78                   | 4.58             |
| 16                             | 5.00         | 4.75                 | 4.70                   | 4.55             |

Figure 1: LP2951 Output Voltage (V) vs. Total Ionizing Dose (krad(Si)). The graph shows four data series: CTRL Avg (blue circles), Biased (5 V) Avg (red squares), Biased (3.3 V) Avg (magenta diamonds), and Unbiased Avg (green triangles). The y-axis ranges from 4.4 to 5.1 V, and the x-axis ranges from 0 to 18 krad(Si). Dashed lines indicate the specification minimum (approx. 4.95 V) and maximum (approx. 5.05 V). The CTRL Avg remains constant at 5.0 V. The Biased (5 V) Avg starts at 5.0 V and drops to ~4.75 V at 16 krad(Si). The Biased (3.3 V) Avg starts at 5.0 V and drops to ~4.7 V at 16 krad(Si). The Unbiased Avg starts at 5.0 V and drops to ~4.55 V at 16 krad(Si).

Fig. 1. LP2951 Output Voltage (V) vs. Total Ionizing Dose (krad(Si)).

### B. DS25BR100, Texas Instruments, LVDS Buffer

This BiCMOS, COTS, LVDS buffer was tested at the Texas A&M Cyclotron with a 25 MeV/amu tune. The highest nominal LET was 25 MeV/amu Xe, at 42.7 MeVcm<sup>2</sup>/mg. Worst case conditions for single-event latchup were tested with VDD = 3.6 V and case temperature greater than 85°C. Power supply current was monitored for high current states. For most testing, all three devices on the evaluation board were attached in series, with only a single buffer actively irradiated. Testing was also performed with individual devices isolated to ensure the effects observed were not influenced by the attached buffers. Fig. 2 is a photograph of the evaluation board.

![Figure 2: Photograph of the COTS evaluation board for DS25BR100 buffer. The board is blue with multiple gold-plated connectors along the top and bottom edges. Various electronic components, including integrated circuits and resistors, are visible on the surface. A red probe is connected to one of the bottom connectors.](04519be9bd73b202914a1bb3da732edd_img.jpg)

Figure 2: Photograph of the COTS evaluation board for DS25BR100 buffer. The board is blue with multiple gold-plated connectors along the top and bottom edges. Various electronic components, including integrated circuits and resistors, are visible on the surface. A red probe is connected to one of the bottom connectors.

Fig. 2. COTS evaluation board for DS25BR100 buffer (top device)

The DS25BR100 was first irradiated with 42.7 MeVcm<sup>2</sup>/mg Xe, with a range of 220  $\mu$ m in silicon. At ambient temperature and nominal voltage (3.3 V), single-event latchup was observed. The power supply current jumped to the hardware limit of 500 mA (see Fig 2). This was repeated on several runs and several devices, and for the four runs on which fluence-to-failure was noted, the average cross-section was  $2.18 \times 10^{-6}$  cm<sup>2</sup>. A sample was heated to 85°C and exposed to greater than  $1 \times 10^7$  /cm<sup>2</sup> at an effective LET of 60.4 MeVcm<sup>2</sup>/mg by use of beam degraders to reduce energy. Single-event latchup was again observed, limited by the 500mA power supply compliance. No parts were catastrophically damaged during this phase of testing. At an LET of 30.8 MeVcm<sup>2</sup>/mg and ambient temperature, SEL was observed. After one test to  $2.3 \times 10^6$  /cm<sup>2</sup>, the device was catastrophically destroyed and could not be restored to functionality (current remained high). Finally, at an LET of 21.3 MeVcm<sup>2</sup>/mg, three tests to a total of  $5 \times 10^6$  /cm<sup>2</sup> at ambient temperature did not result in any single-event latchup, but time did not allow for additional testing at elevated temperature.

Single-event upset data was a secondary objective of this test. Many runs were obscured by SEL that caused a near-infinite number of errors to be recorded. No clear cross-

section vs LET curve is possible from the limited dataset, but it may be useful in understanding the relative magnitude of possible errors from this device (see test report).

![Figure 3: A line graph showing Current (A) on the y-axis (ranging from 0.1 to 0.55) versus Elapsed Time (s) on the x-axis (ranging from 0 to 400). The current is constant at approximately 0.15 A until about 240 seconds, where it spikes sharply to approximately 0.5 A and remains constant until about 380 seconds, after which it returns to the baseline of approximately 0.15 A.](c54b3ca7603d65d4589151bc3a49d054_img.jpg)

Figure 3: A line graph showing Current (A) on the y-axis (ranging from 0.1 to 0.55) versus Elapsed Time (s) on the x-axis (ranging from 0 to 400). The current is constant at approximately 0.15 A until about 240 seconds, where it spikes sharply to approximately 0.5 A and remains constant until about 380 seconds, after which it returns to the baseline of approximately 0.15 A.

Fig. 3. DS25BR100 SN2 power supply current spike.

## V. SUMMARY

We have presented data from recent TID, DDD, and SEE tests on a variety of devices. It is the authors' recommendation that this data be used with caution due to many application- or lot-specific test conditions. We also highly recommend that lot-specific testing be performed on any commercial devices, or any devices that are suspected to be sensitive. As in our past workshop compendia of GSFC test results, each DUT has a detailed test report available online describing in further detail, test method, test conditions/parameters, test results, and graphs of data.

## VI. ACKNOWLEDGMENT

The authors would like to acknowledge the sponsors of this effort: NASA Electronic Parts and Packaging Program (NEPP) and NASA Flight Projects. The authors thank members of the Radiation Effects and Analysis Group (REAG) who contributed to the test results presented here; Stephen K. Brown, Martin A. Carts, Yevgeniy Geraschenko, Kenny O'Connor, James Forney, Anthony Phan, Jason Osheroﬀ, Thomas Carstens, Hak Kim, Kenneth LaBel, Jean-Marie Lauenstein, Paige Karras, Ray Ladbury, Stephen R. Cox, Landen Ryder, Christina M. Seidleck, Scott Stansberry, Craig Stauffer, Carl Szabo, and Mike Xapsos.

## VII. REFERENCES

1. Kenneth A. LaBel, Lewis M. Cohn, and Ray Ladbury, "Are Current SEE Test Procedures Adequate for Modern Devices and Electronics Technologies?," [http://radhome.gsfc.nasa.gov/radhome/papers/HEART08\\_LaBel.pdf](http://radhome.gsfc.nasa.gov/radhome/papers/HEART08_LaBel.pdf)
2. Department of Defense "Test Method Standard Microcircuits," MIL-STD-883 Test Method 1019.9 Ionizing radiation (total dose) test procedure, June 7, 2013, <https://landandmaritimeapps.dla.mil/Downloads/MilSpec/Docs/MIL-STD-883/std883.pdf>.
3. JEDEC Government Liaison Committee, Test Procedure for the Management of Single-Event Effects in Semiconductor Devices from Heavy Ion Irradiation," JESD57A, <https://www.jedec.org/standards-documents/docs/jesd-57>, Nov. 2017.
4. National Instruments LabVIEW System Design Software, <http://www.ni.com/labview/>
5. University of Massachusetts Lowell <https://www.uml.edu/Research/RadLab/Neutron-Facilities.aspx>
6. B. Hyman, "Texas A&M University Cyclotron Institute, K500 Superconducting Cyclotron Facility," <http://cyclotron.tamu.edu/facilities.htm>, Jul. 2003.
7. NASA Goddard Space Flight Center Radiation Effects Facility [https://radhome.gsfc.nasa.gov/radhome/ref/GSFC\\_REF.html](https://radhome.gsfc.nasa.gov/radhome/ref/GSFC_REF.html)
8. Megan Casey, "Direct Ionization from Low-Energy Electrons in a Highly-Scaled CMOS Process" presented at NSREC, Dec 3, 2020. <https://nepp.nasa.gov/docs/tasks/043a-Scaled-CMOS/NEPP-CP-2020-Casey-NSREC-Presentation-Low-Energy-Electrons-CMOS-20205010699.pdf>
9. Ted Wilcox, Michael Campola, and Matt Joplin, "Single-Event Effect Test Report International Rectifier 80SCLQ060SCS Schottky Diode", NASA GSFC, Greenbelt, MD, USA, Greenbelt, MD, USA, Dec. 2020. [Online]. Available: <https://nepp.nasa.gov/docs/tasks/070-Test-Reports/NEPP-TR-2020-Wilcox-NASA-TM-TR-20-007-80SCLQ060SCS-Schottky-Diode-2020Dec08-20210009916.pdf>
10. L. D. Ryder, T. A. Carstens, A. M. Phan, C. M. Seidlick, M. J. Campola, "Single Event Effects Testing of a Vertical Optocoupler with Unmodified Packaging," in *IEEE Radiation Effects Data Workshop (REDW)*, Jul. 2021
11. Ted Wilcox and Michael Campola, "Single-Event Effect Test Report Analog Devices ADG201 Quad SPST Analog Switch," NASA GSFC, Greenbelt, MD, USA, Greenbelt, MD, USA, Dec. 2020. [Online]. Available: <https://radhome.gsfc.nasa.gov/radhome/papers/2020-Wilcox-TR-21-002-ADG201-NASA-TM-20210010191.pdf>
12. Jason Osheroﬀ and Ted Wilcox, "Total Ionizing Dose Test Report MAX4651 Quad SPST Analog Switch," NASA GSFC, Greenbelt, MD, USA, Greenbelt, MD, USA, Apr. 2021. [Online]. Available: <https://radhome.gsfc.nasa.gov/radhome/papers/Osheroﬀ-TR-21-001-MAX4651-2021Mar09-TID-NASA-TM-20210011180.pdf>
13. NASA/GSFC Radiation Effects and Analysis home page, <http://radhome.gsfc.nasa.gov>.
14. NASA Electronic Parts and Packaging Program home page, <http://nepp.nasa.gov>.
15. LP2951 datasheet, rev. I Nov 2014, <https://www.ti.com/lit/ds/symlink/lp2951.pdf?ts=1621385650664>