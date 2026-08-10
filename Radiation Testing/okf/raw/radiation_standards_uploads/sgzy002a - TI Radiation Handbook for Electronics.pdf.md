

# Radiation Handbook for ElectronicsA satellite in space with Earth in the background and circuitry overlaid on the right side.The background of the cover is a composite image. On the left, a curved horizon of the Earth is visible against the blackness of space, with a few stars scattered in the distance. On the right, a satellite is shown in detail, featuring several large, white, parabolic dish antennas and long, rectangular solar panel arrays. The solar panels have a rainbow-colored gradient. Overlaid on the right side of the image is a faint, glowing blue circuit board pattern with various electronic symbols and traces.

A compendium of radiation effects topics for space,  
industrial and terrestrial applications

![Texas Instruments logo](30a26f2d17ca95672702bf50fb4f0242_img.jpg)

The Texas Instruments logo, consisting of a stylized white 'TI' inside a red square, followed by the words 'TEXAS INSTRUMENTS' in white, uppercase, sans-serif font.

Texas Instruments logo

## CONTENTS

## Foreword: Texas Instruments space flight history

## Chapter 1: Radiation environments

|                                           |    |
|-------------------------------------------|----|
| 1.1 The space radiation environment       | 4  |
| 1.2 The terrestrial radiation environment | 9  |
| 1.3 Artificial radiation environments     | 16 |

## Chapter 2: Radiation effects in matter

|                                     |    |
|-------------------------------------|----|
| 2.1 Radiation basics                | 25 |
| 2.2 Particle interactions in matter | 28 |
| 2.3 Linear energy transfer          | 34 |
| 2.4 Radiation shielding             | 35 |

## Chapter 3: Radiation effects in electronics – dose effects

|                                 |    |
|---------------------------------|----|
| 3.1 Total ionizing dose effects | 38 |
| 3.2 Displacement damage         | 42 |

## Chapter 4: Radiation effects in electronics – single-event effects

|                                                                        |    |
|------------------------------------------------------------------------|----|
| 4.1 Destructive and nondestructive<br>single-event effects             | 47 |
| 4.2 Archetype for all single-event effects:<br>single-event transients | 47 |
| 4.3 Digital and analog single-event transients                         | 49 |
| 4.4 Single-event upsets                                                | 51 |
| 4.5 Single-event functional interrupt                                  | 54 |
| 4.6 Single-event latchup                                               | 55 |
| 4.7 Single-event gate ruptures and<br>single-event burnouts            | 57 |
| 4.8 Prompt-dose effects                                                | 59 |

## Chapter 5: Radiation sensitivity by technology

|                          |    |
|--------------------------|----|
| 5.1 Total ionizing dose  | 63 |
| 5.2 Single-event effects | 67 |

## Chapter 6: Mitigating radiation effects in electronics

|                                                                         |    |
|-------------------------------------------------------------------------|----|
| 6.1 Radiation robustness by serendipity                                 | 75 |
| 6.2 Radiation hardening by process                                      | 77 |
| 6.3 Radiation hardness by design –<br>component configuration solutions | 79 |
| 6.4 Radiation hardness by design –<br>component layout solutions        | 82 |
| 6.5 Radiation hardness by design –<br>circuit redundancy solutions      | 83 |

## Chapter 7: Radiation testing and qualification

|                                                           |     |
|-----------------------------------------------------------|-----|
| 7.1 Total ionizing dose testing                           | 88  |
| 7.2 Single-event effect testing                           | 95  |
| 7.3 Displacement damage dose testing –<br>neutron testing | 101 |
| 7.4 Dose-rate or prompt-dose testing                      | 101 |
| 7.5 Terrestrial neutron and<br>alpha-particle testing     | 102 |
| 7.6 Texas Instruments' radiation<br>test philosophy       | 102 |

## Chapter 8: Texas Instruments' space product advantage

|                                         |     |
|-----------------------------------------|-----|
| 8.1 Product and process changes         | 108 |
| 8.2 Lot-to-lot variation                | 108 |
| 8.3 Wafer-lot date codes                | 109 |
| 8.4 Radiation qualification by process  | 109 |
| 8.5 Using published radiation test data | 109 |

## Glossary 113

## Acronyms 115

![Portrait of Robert Baumann](7ee2d12e8cbaacaf65b0c332d1c76daf_img.jpg)

A headshot of Robert Baumann, a middle-aged man with short, light-colored hair, wearing a light-colored collared shirt under a dark jacket. He is smiling slightly and looking towards the camera.

Portrait of Robert Baumann

### Robert Baumann

Early in his 29 year career at TI, Robert Baumann discovered that the reaction of  $^{10}\text{B}$  with low-energy cosmic neutrons was a dominant reliability risk in digital electronics and developed mitigation schemes that reduced product failure rates nearly ten-fold. From 1993-1998, He was involved in transistor and radiation effects reliability and advanced failure analysis at TI's Mihomura Fab and

Tsukuba R&D Center in Japan. When he returned to Dallas he led radiation effects programs for the advanced technology reliability group. He co-led the SIA's expert panel, which successfully negotiated with the U.S. Government to change ITAR export control laws that posed a serious risk of export restriction to advanced commercial technologies. Baumann was one of the primary authors of the JEDEC (JESD89, 89A) industry standard for radiation characterization in the terrestrial environment for which he was awarded the JEDEC Chairman's Award. In 2012 he moved to the high reliability product group focused on improving the characterization, modeling and reporting of radiation effects. Baumann was elected TI and IEEE Fellow. He has coauthored and presented more than 90 papers and presentations, two book chapters and has fifteen U.S. patents. Baumann retired from TI in 2018.

![Portrait of Kirby Kruckmeyer](89337b7d31e8913d0af346758554070a_img.jpg)

A headshot of Kirby Kruckmeyer, a middle-aged man with short, light-colored hair, wearing a dark and light striped polo shirt. He is smiling slightly and looking towards the camera.

Portrait of Kirby Kruckmeyer

### Kirby Kruckmeyer

Kirby Kruckmeyer started his career at National Semiconductor (acquired by Texas Instruments in 2011) as a process engineer, developing processes for the world's first 5-inch analog wafer fab. During this time, Kruckmeyer gained experience with semiconductor physics, passivation charging effects and radiation-hardened processing. From 1990-1992, Kruckmeyer was an assignee from

National Semiconductor to Semiconductor Manufacturing Technology (SEMATECH), an industry consortium established to improve processing technology in the United States. There, he supervised engineers from other companies in the development of 150-mm process technologies. After finishing his assignment, Kruckmeyer returned to National, where he moved into product development and eventually was the product line manager for National's Automotive Systems group. In 2005, Kruckmeyer moved in the High Reliability product group. He was instrumental in developing National Semiconductor's leadership in space-grade data converters, enhanced low dose rate sensitivity-free products and radiation testing. At Texas Instruments, Kruckmeyer continues to support space applications, radiation testing and space product development. He has authored and presented over 20 papers, sits on radiation testing standards committees, and participates in radiation conferences.

## Foreword: Texas Instruments space flight history

Texas Instruments has one of the longest space-flight histories of any semiconductor vendor. Even before Texas Instruments engineer Jack Kilby conceived and built the first integrated circuit (IC) in September 1958, Texas Instruments transistors had flown into space on the U.S.'s first satellite, Explorer 1, which launched on Jan. 31 that same year.

Since then, products from Texas Instruments have flown on many space missions. Notable and historic missions with Texas Instruments products on board include:

- Telstar 1, the first broadcast TV satellite
- Apollo 11, marking the first man on the moon
- Mariner 2, the first successful interplanetary spacecraft
- Voyager 1, still traveling after 40 years and now the farthest human-made object from Earth
- Every Space Shuttle mission from 1981-2011
- Navigational satellites supporting GPS and the Global Navigation Satellite System (GLONASS)
- The Hubble space telescope
- The International Space Station
- Rosetta and Philae, the European Space Agency comet orbiter and lander, respectively
- The Mars Rover

- Mangalyaan, the Indian Space Research Organization Mars orbiter
- KickSat, a group of 104 microsatellites launched on a single rocket into low Earth orbit in 2014

Former Texas Instruments researcher Mary Ellen Weber served as an astronaut on Discovery Space Shuttle mission space transportation system (STS)-70.

Numerous commercial, scientific and governmental satellites using Texas Instruments products have launched since 1958 and continue to launch weekly.

Through its acquisitions of Unitrode in 1999 and National Semiconductor in 2011, Texas Instruments added significant product breadth, expertise and technology to its internal space-grade semiconductor capabilities. Building on this long heritage in space flight, Texas Instruments continues to innovate and bring new products to the space ecosystem. Texas Instruments offers one of the industry's broadest portfolios of ICs for space applications, covering a wide range of device types. Power management, data converters, amplifiers, clocks and timing, interface, processors, and sensors are just a few of the device types Texas Instruments provides for space electronics systems. Texas Instruments' portfolio includes both Class-V qualified manufacturer list (QML) and radiation-hardness assured (RHA) ICs, demonstrating the company's long-standing commitment to the space electronics market.

![Texas Instruments' space heritage timeline from 1958 to present.](2db53d6ef524be5cde118e647f73ed90_img.jpg)

**Texas Instruments' space heritage**  
1958 - present

The timeline illustrates the company's contributions to space exploration from 1958 to the present. It features a central horizontal axis with major milestones marked by icons and labels. The background is a deep space scene with stars, planets, and spacecraft. Key milestones include the launch of Explorer 1 in 1958, Mariner 2 in 1962, Apollo 11 in 1969, Voyager 1 and 2 in 1977, the Hubble Telescope in 1990, the International Space Station in 1998, the Mars Rover in 2001, and the Mars Orbiter Mission in 2013. The timeline also includes a section for 'Other spacecrafts' and 'The first space shuttle & following shuttles'.

**Other spacecrafts**

- Mariner Missions
- Ranger Missions
- Explorer Missions
- Discovery Missions

**The first space shuttle & following shuttles**

- Apollo Missions & Vehicles
- IRS
- GLONASS
- AlphaSat
- ROSAT
- MUNIN
- and many more

© 2018 Texas Instruments Incorporated. All rights reserved.

Texas Instruments' space heritage timeline from 1958 to present.

# Chapter 1: Radiation environments

The type and magnitude of radiation effects observed in electronics are largely defined by specific device properties and the radiation environment in which the devices are used. In this chapter, we review three of the primary radiation environments: the natural space environment encountered outside the protective shielding of the Earth's atmosphere; the natural terrestrial radiation environment in which most electronic applications operate; and the specialized man-made radiation environments encountered in some medical, industrial and military applications. In later chapters, we will deal with the different radiation effects and how they manifest in different device types.

### 1.1 The space radiation environment

Three sources of radiation define the space environment in our solar system:

- Galactic cosmic rays (GCRs), a nearly isotropic flux (same in all directions) predominantly comprising extremely energetic protons impacting the Earth from outside our solar system.
- Solar radiation, comprising a stream of lower-energy photons, plasma and magnetic flux that the sun emits continuously in all directions, like an ever-present “wind” of particles. This solar wind is punctuated by sporadic emissions from solar storms.

Solar flares and coronal mass ejections (CMEs) generate localized intense particle bursts with much higher energies and fluxes than the steady-state solar wind.

- Radiation belts, accumulations of energetic particles diverted and trapped into toroidal-shaped regions around planets in response to their magnetic fields.

The reliability of microelectronic components in the harsh space radiation environment is characterized by the accumulation of ionizing and displacement damage dose (DDD), as well as a high rate of single-event effects (SEEs). The radiation exposure that on-board electronics receive is a function of the orbit that the spacecraft follows, the mission duration, the amount of shielding, and the number and magnitude of solar flares or CMEs that might have also occurred during the mission.<sup>[1-3]</sup>

The Earth's magnetic field has a varying effect on shielding space radiation, depending on the mission orbit.<sup>[4]</sup> Figure 1-1 shows the different orbit types and their properties. Leaving the Earth's surface, Figure 1-1 shows the low Earth orbit (LEO), a geocentric orbit with an altitude ranging from 0 to 2,000 km (1,240 miles). In order to keep a satellite in orbit with minimum energy, it is crucial to eliminate atmospheric drag, so practical Earth orbits begin at approximately 167 km (100 miles), and have an orbital period between one and two hours.

#### Types of Earth orbit

![Figure 1-1: Illustration of orbit types, shapes and properties. The figure is divided into three main sections: 'By inclination', 'By shape', and 'By altitude'. 'By inclination' shows three types of orbits: Inclined orbit (tilted relative to the equator), Equatorial orbit (in the plane of the equator), and Polar orbit (passing over the poles). 'By shape' shows two types: Elliptical orbit (oval-shaped with perigee and apogee) and Circular orbit (perfect circle). 'By altitude' shows three types: Geostationary orbit (GEO) at 35,800 km, Medium Earth orbit (MEO) between 5,000-10,000 km, and Low Earth orbit (LEO) between 100-2,000 km. Each section includes a diagram of the Earth with the orbit path and a satellite icon.](1a6d75c94d3fd49936527eadd25e9278_img.jpg)

**By inclination**

- Inclined orbit**  
Satellite track covers range of altitudes in Northern and Southern Hemispheres
- Equatorial orbit**  
Satellite track over equator
- Polar orbit**  
Satellite track covers all parts of Earth as planet rotates

**By shape**

- Elliptical orbit**  
Earth at one focus of ellipse  
Perigee (closest distance)  
Apogee (farthest distance)
- Circular orbit**  
Earth at center  
All points of satellite orbit at about the same altitude

**By altitude**

- Geostationary orbit (GEO)**  
35,800 km (22,300 miles) altitude
- Medium Earth orbit (MEO)**  
5,000-10,000 km (3,100-6,200 miles) altitude (typical)
- Low Earth orbit (LEO)**  
About 100-2,000 km (60-1,200 miles) altitude

Orbital period of satellite equal to rotational period of Earth  
Satellite orbit inequatorial plane

Figure 1-1: Illustration of orbit types, shapes and properties. The figure is divided into three main sections: 'By inclination', 'By shape', and 'By altitude'. 'By inclination' shows three types of orbits: Inclined orbit (tilted relative to the equator), Equatorial orbit (in the plane of the equator), and Polar orbit (passing over the poles). 'By shape' shows two types: Elliptical orbit (oval-shaped with perigee and apogee) and Circular orbit (perfect circle). 'By altitude' shows three types: Geostationary orbit (GEO) at 35,800 km, Medium Earth orbit (MEO) between 5,000-10,000 km, and Low Earth orbit (LEO) between 100-2,000 km. Each section includes a diagram of the Earth with the orbit path and a satellite icon.

Figure 1-1. Illustration of orbit types, shapes and properties.

LEOs are relatively low-altitude orbits and thus the least expensive in terms of energy expended to achieve orbit. In LEO, round-trip signal distances are the shortest; signal communication delays are minimal, and surface details are better resolved than for higher orbits. The orbital periods of LEO satellites range from approximately 1 1/2 hours to a bit more than two hours.

Medium Earth orbit (MEO) is defined between LEO and geostationary orbit (GEO) at 35,786 km (22,236 miles). MEO is usually used for navigation (GPS), communication and science observation missions. The orbital periods of MEO satellites range from approximately two to nearly 24 hours.

Geosynchronous orbit (GSO) and GEO both match the Earth's rotation, and thus complete one full orbit every 24 hours. A satellite in GSO stays exactly above the equator, while a satellite in GEO will swing north to south during its orbit. Any orbiting spacecraft with an altitude above GEO is considered to be in high Earth orbit (HEO). HEOs are orbits usually reserved for missions that need to get away from the heavy electromagnetic traffic present in lower orbits, such as those focused on monitoring deep space.

LEO – particularly equatorial orbits, where the magnetic shielding effect is maximized – provides the greatest benefit in terms of minimizing radiation effects. At higher altitudes, orbits such as MEO or GEO, and/or highly inclined orbits or polar orbits, the shielding provided by the Earth's magnetic field is significantly reduced, leading to higher particle fluxes and a higher probability of more disruptive events. Missions with high inclinations or polar orbits will be exposed to higher fluxes and higher energy particles since the Earth's magnetic shielding becomes less effective at higher/lower latitudes away from the equator. For interplanetary flights far from the Earth's protective magnetic field, the spacecraft is exposed to the high fluxes of energetic particles.

#### Galactic cosmic rays

Before focusing on the local space environment of our solar system, consider the environment on a bigger scale. "Outer space" is often portrayed as a complete absence of material (empty space), but in actuality, even the vast seemingly empty spaces between the stars are filled with matter and energy. The material that occupies the space between the stars, called the interstellar medium, mostly consists of hydrogen, with a smaller fraction of helium and trace amounts of heavier elements, plus a smattering of dust. The interstellar medium is not a perfect vacuum, but has an extremely low density from  $10^{-4}$  to  $10^6$  atoms/cm<sup>3</sup>. In stark contrast, our atmosphere has a density of  $\sim 10^{19}$  atoms/cm<sup>3</sup>.

The interstellar gas usually forms large "clouds" of neutral atoms or molecules. Near stars or other energetic bodies plus the dilute gas clouds become ionized. The gas in the interstellar medium is not static but moving, compressing or dissipating in response to the local interplay of magnetic, thermodynamic, gravitational and radiation processes. This turbulence drives the dynamic evolution of the interstellar gas, slowing or halting collapse over larger ranges while initiating local compression and star formation at more localized smaller ranges. Interstellar gas is both the substrate and the source of galaxies and stars.

The interplanetary medium of our solar system begins where the interstellar medium ends. The solar wind, or flux of energetic particles emitted continuously and spreading radially away from the sun, eventually slows down to subsonic velocities at a distance about twice the distance of Pluto's orbit in a region known as the termination shock. In this region, the solar wind density is so low that it is effectively impeded by the "force" of the interstellar medium. The heliopause is the outer extent of the sun's magnetic field and solar wind. Within the heliopause is the heliosphere, a spherical bubble that encompasses the sun and planets. The heliosphere acts as a giant electromagnetic shield, protecting the planets from some of the incident GCR flux. Cosmic-ray particles with less than  $\sim 50$  MeV of kinetic energy are unable to penetrate within the heliosphere due to the energy of the solar wind within this volume, such that nearly 75% of the incoming GCR particles are stopped.

Figure 1-2 shows the heliosphere, heliopause and solar system. GCRs are a major part of the space radiation environment. As their name implies, GCRs originate outside of the solar system and consist of high-energy electrons and ions.

![Diagram of the heliosphere and solar system. The diagram shows the Sun at the center with planets (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto) in elliptical orbits. The solar wind flows outwards from the Sun, creating a bow shock and a termination shock. The heliopause is the outer boundary of the solar wind. Voyager 1 and Voyager 2 are shown crossing the heliopause. The interstellar wind is shown flowing from the left. The heliosphere is the volume defined by the termination shock, and the heliopause is the boundary where the solar wind velocity ceases being supersonic.](130ce5fbe21d11939cd4419d3e7ff044_img.jpg)

Diagram of the heliosphere and solar system. The diagram shows the Sun at the center with planets (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto) in elliptical orbits. The solar wind flows outwards from the Sun, creating a bow shock and a termination shock. The heliopause is the outer boundary of the solar wind. Voyager 1 and Voyager 2 are shown crossing the heliopause. The interstellar wind is shown flowing from the left. The heliosphere is the volume defined by the termination shock, and the heliopause is the boundary where the solar wind velocity ceases being supersonic.

**Figure 1-2. The heliopause represents the boundary where the sun's influence ends. The heliosphere is the volume defined by the boundary where solar wind velocity ceases being supersonic (termination shock) and is no longer able to filter out the interstellar medium.<sup>[5]</sup>**

Scientists believe that GCRs accelerate due to high kinetic energies caused by shock waves from supernova explosions propagating in the interstellar medium. GCR composition consists of 89% ionized hydrogen (protons) and 9% ionized helium (alpha particles), with the remaining 2% consisting of heavier ions and electrons. The galactic magnetic field deflects the charged GCRs, thus accelerating them around circular paths – confining them to the disk of the galaxy.

Radioisotope dating has determined that most GCRs have been traveling in our galaxy for tens of millions of years. Their direction has been randomized over time such that they are isotropic. GCRs are traveling at a large fraction of the speed of light, with the majority of particles having kinetic energies of  $\sim 1$  GeV. The GCR flux below  $\sim 100$  MeV is deflected by the heliosphere. Above 1 GeV, the cosmic ray flux decreases fairly consistently with an increase in particle energy: the higher the energy of the particle, the rarer it is. The highest-energy cosmic rays measured have kinetic energies in excess of  $10^{20}$  eV!

Figure 1-3 shows the differential flux of GCRs as a function of particle energy. In comparison, protons emitted from the sun seldom exceed kinetic energies of 1 GeV. The interplanetary magnetic field also influences GCRs within the heliosphere, making it difficult for them to reach the inner solar system. The lower energy range of the GCR flux is modulated by the 11-year solar activity cycle, dropping during maximum solar flux when increased ionization deflects the incoming GCR flux and increasing when the sun is at its minimum activity levels and has less deflective power. The GCR flux varies by a factor of five between solar maximum and minimum conditions.

#### Flux of cosmic rays

![Figure 1-3: Spectrum of galactic cosmic rays. A log-log plot showing Flux (m² or GeV sec)⁻¹ on the y-axis (ranging from 10⁻²⁵ to 10⁴) versus Energy (eV) on the x-axis (ranging from 10⁹ to 10²¹). The curve shows a steep decline with two distinct features: the 'Knee' at approximately 10¹⁵ eV and the 'Ankle' at approximately 10¹⁸ eV. Annotations indicate '1 particle per m² - second' at high flux/low energy, 'Knee (1 particle per m² - year)' at the knee, and 'Ankle (1 particle per km² - year)' at the ankle.](c0843c6d138705289960d9f53a6e72a1_img.jpg)

Figure 1-3: Spectrum of galactic cosmic rays. A log-log plot showing Flux (m² or GeV sec)⁻¹ on the y-axis (ranging from 10⁻²⁵ to 10⁴) versus Energy (eV) on the x-axis (ranging from 10⁹ to 10²¹). The curve shows a steep decline with two distinct features: the 'Knee' at approximately 10¹⁵ eV and the 'Ankle' at approximately 10¹⁸ eV. Annotations indicate '1 particle per m² - second' at high flux/low energy, 'Knee (1 particle per m² - year)' at the knee, and 'Ankle (1 particle per km² - year)' at the ankle.

Figure 1-3. Spectrum of galactic cosmic rays.<sup>69</sup>

Image courtesy of W. Bietenholz, "Cosmic Rays and the Search for a Lorentz Invariance Violation"

#### Solar radiation

Continually converting hydrogen into helium via nuclear fusion at its core, the sun is the most intense source of radiation in the solar system, emitting more than 60 MW/m². Two main visible features of the sun correlate with solar radiation: the photosphere and the corona. The photosphere is the visible layer of the sun that emits photons, with an estimated temperature of nearly 6,000 K. The solar corona is the roiling region of super-heated (~1 million K) plasma surrounding the photosphere.

The photosphere is a huge network of relatively small (~1,000 km), dynamic, cell-like granules formed by localized convection cells. Figure 1-4 shows the convection granules and sunspots (black areas) in the photosphere. Convection is driven by heated plasma rising up from the interior (brighter areas) and spreading out across the surface. As the plasma cools during the lateral spreading, it ultimately sinks back to the cooler interior (darker areas).

Sunspots, which appear as dark spots on the photosphere, are regions of high magnetic field strength. They usually form in pairs that constitute the two poles of a magnet. Sunspot activity is transient, usually lasting for days to weeks. Sunspot activity

follows an 11-year cycle characterized by approximately four years of relatively "inactive sun" where the number of sunspots is at a minimum, followed by seven years of "active sun" with increased numbers of sunspots. Sunspot activity is correlated to magnetic storms that produce the most harmful radiation.

![Figure 1-4: Image of two primary features of the photosphere surface: granules and sunspots. The image shows a highly textured, granular surface of the sun's photosphere, with bright, turbulent areas (granules) and dark, irregular patches (sunspots).](8a58f9778d09be5d0a0ae25e5393a583_img.jpg)

Figure 1-4: Image of two primary features of the photosphere surface: granules and sunspots. The image shows a highly textured, granular surface of the sun's photosphere, with bright, turbulent areas (granules) and dark, irregular patches (sunspots).

Figure 1-4. Image of two primary features of the photosphere surface: granules and sunspots.

Image courtesy of Institute for Solar Physics; observed with the Swedish 1-m Solar Telescope

Solar activity can be divided into three components: solar wind, solar flares and CMEs. The temperature of the sun's corona is so high that solar gravity cannot keep the energetic particles from escaping. These particles, called the solar wind, stream out of the corona continuously in all directions at speeds ranging from 300-800 km/s. The solar wind consists of highly energized photons, electrons, protons, helium ions and a small number of heavier ions. Solar wind couples to the Earth's magnetic field and produces storms in the Earth's magnetosphere. Compared to intense sporadic solar-storm phenomena, the solar wind tends to be significantly less harmful to spacecraft electronics and crews, because most of the flux consists of much lower-energy particles, with a significant portion of the lower-energy flux deflected and trapped by planetary magnetic fields.

In stark contrast, coronal shock waves, prominences, solar flares and CMEs can have a large impact on microelectronic reliability by accelerating solar particles to much higher energies. When viewed head-on, flares manifest as sudden, rapid and intense variations in brightness, which occur when built-up magnetic energy is suddenly released. Flares occur around sunspots where intense and spontaneous discontinuities in magnetic field strength precipitate sudden releases of magnetic energy and plasma stored in the corona, literally shooting large chunks of the coronal surface into space with high velocity. Figure 1-5 shows a photograph of a flare with Earth superimposed to show the scale of typical flare events.

During a flare event, radiation is emitted across the electromagnetic spectrum, from radio waves to gamma rays. As magnetic energy is released during the flare, electrons, protons and heavier nuclei are heated and accelerated to high kinetic energies. CMEs are often associated with solar flares and prominences. As with sunspot activity, the frequency of CMEs varies with the 11-year sunspot cycle. Flares and CMEs are much more frequent during the active phase of the solar cycle. For example, the frequency of CMEs at solar minimum is approximately one CME per week, while at solar maximum, the number of CMEs increases to a couple per day.

![Figure 1-5: Ultraviolet image of a solar flare, with Earth shown for scale. The image shows a bright, fiery orange and red solar flare erupting from the surface of the Sun. A small, dark silhouette of Earth is shown in the bottom left corner for scale, with the text 'Earth to scale' next to it.](c834b9abb4ddf70e5d10641f87d5ff5b_img.jpg)

Figure 1-5: Ultraviolet image of a solar flare, with Earth shown for scale. The image shows a bright, fiery orange and red solar flare erupting from the surface of the Sun. A small, dark silhouette of Earth is shown in the bottom left corner for scale, with the text 'Earth to scale' next to it.

**Figure 1-5. Ultraviolet image of a solar flare, with Earth shown for scale.** Image courtesy of NASA/Solar Dynamics Observatory/Atmospheric Imaging Assembly

Of key concern are the solar energetic particles (SEPs), electrons, protons and heavier ions accelerated during solar flares or CME-induced shock waves. During such events, the intensity of SEPs can increase by hundreds to millions of times. The maximum energy reached by SEPs is typically somewhere in the range of 1 MeV to 1 GeV.

Figure 1-6 shows example spectra comparing solar wind, SEP and GCR proton events. Since flare and CME events are highly directed, they affect a relatively small region of space, but are characterized by very high particle fluxes lasting hours to days.<sup>[7-12]</sup> The fluxes can exceed the normal space radiation levels by many orders of magnitude. For example, CMEs can generate in excess of 500,000 protons-cm<sup>-2</sup>sec<sup>-1</sup>. Being caught in a flare or CME is hazardous to crews and microelectronics in space vehicles – an example of being in the wrong place at the wrong time.

#### Representative proton energy spectra at 1 AU

![Figure 1-6: Differential proton flux as a function of proton energy for solar wind, SEPs and GCR distributions. The graph is a log-log plot showing the differential proton flux N(E) in particles cm^-3 keV^-1 on the y-axis (ranging from 10^-15 to 1) versus the proton energy E in nucleon eV on the x-axis (ranging from 10^1 to 10^9). Several curves are shown: Solar wind (highest flux at low energies), Interstellar pickup ions, Corotating particle events ions, SEP events (sharp peaks at various energies), and Galactic cosmic rays (highest flux at high energies).](7ff005f9556dc6518981bb92091d36ab_img.jpg)

Figure 1-6: Differential proton flux as a function of proton energy for solar wind, SEPs and GCR distributions. The graph is a log-log plot showing the differential proton flux N(E) in particles cm^-3 keV^-1 on the y-axis (ranging from 10^-15 to 1) versus the proton energy E in nucleon eV on the x-axis (ranging from 10^1 to 10^9). Several curves are shown: Solar wind (highest flux at low energies), Interstellar pickup ions, Corotating particle events ions, SEP events (sharp peaks at various energies), and Galactic cosmic rays (highest flux at high energies).

**Figure 1-6. Differential proton flux as a function of proton energy for solar wind, SEPs and GCR distributions.**

#### Radiation belts

Radiation belts can form around any planetary body that has a magnetic field (magnetosphere) of sufficient strength to divert and capture particles before they can enter the planet's atmosphere. The radiation belts consist of captured particles from the solar wind as well as lower-energy GCRs. Mercury, Venus and Mars have weak or insignificant planetary magnetic fields; thus, these planets do not trap appreciable radiation and do not appear to have belt structures.

Despite having magnetic fields similar to Earth's, Saturn and Uranus trap much less radiation in their belts. In contrast, Jupiter has an extremely powerful magnetic field – more than 10x that of Earth – that creates a radiation belt system considerably larger and more intense than Earth's. The Earth's magnetic field collects and traps protons and electrons, creating doughnut-shaped (toroidal) concentrated regions of trapped charged particles in the vicinity of Earth. These belts were discovered by Dr. James Van Allen and a team of scientists in a series of experiments starting with the Explorer I mission in 1958, the United States' first artificial satellite.

Figure 1-7 is a simplified illustration of the two concentric belts of radiation trapped by the Earth's magnetic field.

![Figure 1-7: Artist's conception of the two radiation belts surrounding the Earth. The diagram shows the Earth at the center, surrounded by two concentric, toroidal (doughnut-shaped) regions of radiation. The inner belt is closer to the Earth, and the outer belt is further out. The Earth's magnetic field lines are shown as curved lines passing through the belts, illustrating how they trap charged particles.](bfeb269e87832e1443c8d017e685dbc8_img.jpg)

Figure 1-7: Artist's conception of the two radiation belts surrounding the Earth. The diagram shows the Earth at the center, surrounded by two concentric, toroidal (doughnut-shaped) regions of radiation. The inner belt is closer to the Earth, and the outer belt is further out. The Earth's magnetic field lines are shown as curved lines passing through the belts, illustrating how they trap charged particles.

**Figure 1-7. Artist's conception of the two radiation belts surrounding the Earth. Referred to as the Van Allen belts, these toroidal inner and outer belts are formed by the Earth's magnetic field.**

The belts are thicker at the equator where the Earth's magnetic field is strongest (where it is parallel to the surface) and get thinner at higher and lower latitudes. They disappear totally at the poles where the Earth's magnetic field becomes oriented normal to the Earth's surface. At the equator, the inner belt ranges from an altitude of approximately 1,200 km to 6,000 km, while the outer belt ranges from approximately 13,000 km to 60,000 km above the Earth's surface.<sup>[13]</sup> The inner belt contains high concentrations of electrons with kinetic energies of ~1-5 MeV and protons with kinetic energies ~10 MeV. The outer belt consists mainly of electrons with kinetic energies of ~10-100 MeV. The outer belt's particle population fluctuates dramatically in response to solar activity.

In general, since the radiation belts are regions where radiation exposure will be greatly increased, travel through them is minimized or avoided whenever possible. LEOs are safely below the radiation belts and hence are the most benign, limited to a region of relatively low particle flux. LEOs are also partially shielded from GCRs by the belts.

An occasional transitory third radiation belt has been recently observed<sup>[14]</sup> that forms and dissipates by temporarily splitting off from the outer belt. The omnidirectional particle fluxes within the inner and outer belts peak at approximately  $10^4$ - $10^6$   $\text{cm}^{-2}\cdot\text{sec}^{-1}$ . In contrast, the flux of particles between the Earth's surface and inner belt is  $10$ - $100$   $\text{cm}^{-2}\cdot\text{sec}^{-1}$ , while in the region between the two belts, it is  $\sim 10^2$ - $10^4$   $\text{cm}^{-2}\cdot\text{sec}^{-1}$ . The Earth's magnetic field is tilted about 11 degrees from the rotation axis. As a result, the radiation belts do not align exactly with the Earth's surface. This asymmetry causes the inner belt, with a nominal altitude of 1.3 km, to drop to 200-800 km in a specific region. This extension of the inner belt to lower altitudes is located over South America off the coast of Brazil, and extends over much of South America (as shown in Figure 1-8), forming the so-called South Atlantic Anomaly (SAA).<sup>[15]</sup> While the particle fluxes in the SAA are significantly lower than at higher altitudes deeper within the belt, they are significantly higher than anywhere else in

the Earth's orbit at that altitude. For example, most of the radiation dose exposure that the International Space Station receives occurs while it flies through the SAA. The SAA is shown in the cross-section and external view in Figure 1-8.

While the electrons and protons trapped in the belts have much lower energies than most GCRs or SEPs, the much higher flux levels are dangerous to crew and electronics if they are exposed for extended periods. Mission orbits/paths are therefore specifically tailored to minimize the spacecraft's exposure time to radiation belts because of high particle fluxes. Minimizing exposure to the radiation belts greatly reduces the rate of SEEs and the accumulation of dose effects. Additionally, in some cases, electronics are powered down during the times when they are in the radiation belts to reduce total ionizing dose (TID) effects, which are made worse by the presence of electric fields.

![Figure 1-8: Cross-section and globe view of the South Atlantic Anomaly (SAA).](bedcca5cdf168e3508ef511d94ec514c_img.jpg)

The figure consists of two panels. The left panel is a cross-section view showing the Earth's surface as a dashed line and a 500-km altitude as a solid line. The South Atlantic Anomaly (SAA) is indicated by a dashed line and a red shaded region representing high particle flux. The right panel is a globe view showing the SAA as a red shaded region over the South Atlantic Ocean, centered near South America.

Figure 1-8: Cross-section and globe view of the South Atlantic Anomaly (SAA).

Cross-section view.

Figure 1-8. Cross-section showing the extent of inner-belt ingress at the SAA (left), and the location and extent of SAA relative to the globe (right).<sup>[15]</sup>

### 1.2 The terrestrial radiation environment

The terrestrial radiation environment exists within the Earth's atmosphere, from sea level to flight altitudes (typically up to a maximum of 13 miles or 22 km) and at all latitudes and longitudes. Three sources of radiation dominate microelectronic reliability failures in the terrestrial environment:

- Very localized alpha-particle radiation (<50  $\mu\text{m}$  from active silicon devices), emitted by the natural radioactive decay of unstable isotopes like uranium, thorium and their daughter isotopes.
- High-energy cosmic-ray neutron radiation, produced as a byproduct of nuclear reactions between galactic and solar high-energy protons with the nitrogen and oxygen nuclei in the Earth's atmosphere. The resulting neutron flux depends on the altitude, latitude, longitude and solar activity.
- The interaction of low-energy cosmic-ray neutrons with an unstable isotope of boron ( $^{10}\text{B}$ ) in a microelectronic device.

SEEs dominate microelectronic reliability in the terrestrial environment. Most reliability failures are related single-event upsets (SEUs) – the flipping of digital bits in memories and sequential logic and the occasional single-event latchup. Additionally, in high-voltage power devices, single-event burnout can be a reliability concern in the terrestrial environment.

TID and displacement damage (DD) are not considered major effects in the terrestrial environment because neutron and alpha-particle event rates are simply too low to cause an appreciable accumulation of dose for typical electronic product lifetimes (decades). The reliability of microelectronics in the terrestrial environment is thus the sum of failures induced by the three natural radiation mechanisms: alpha particles, which are localized within a few tens of microns from active device areas; nuclear reactions between nuclei in the device and penetrating high-energy cosmic-ray neutrons; and nuclear reactions induced by low-energy cosmic-ray neutrons and  $^{10}\text{B}$ . In order to accurately determine the reliability impact of SEEs on any device, you must account for the contribution of each of the three components in the terrestrial environment.

#### Alpha particles

A significant source of ionizing radiation in microelectronic devices comes from alpha particles emitted by the decay of naturally occurring radioactive impurities.<sup>[17,18]</sup> Radioactive impurities are present in trace amounts in the materials used to manufacture and package microelectronic devices. The natural radioactive decay process that produces alpha particles is the result of a spontaneous breakdown of heavy nuclei that do not have enough nuclear binding energy to hold the nuclei together, rendering these nuclei unstable.

The ratio of neutrons to protons must fall within a certain range for an element to be stable. Unstable nuclei emit radiation usually in a multistep process, until a stable ratio of nucleons is reached. Nuclear decay occurs with the emission of an alpha particle, a beta particle, a gamma photon, a positron or the nuclear capture of an inner electron.

Of these processes, the emission of alpha particles is the primary radiation of concern because alpha particles are the most highly ionizing and therefore the most potentially damaging to the operation of microelectronic devices. Although there are many radioactive isotopes, uranium and thorium and their associated daughter products have the highest activities of the naturally occurring radioactive species. They are therefore the dominant source of alpha particles in materials. Uranium and thorium are both heavy elements, and it takes multiple decays into successive unstable daughter products to ultimately shed enough excess nuclear mass for them to become stable isotopes of lead.

Figure 1-9 shows the full decay chain for the  $^{232}\text{Th}$  thorium isotope.

![Radioactive decay chain for the 232Th parent isotope. The chain starts with 232Th (1.41e+10 years) and proceeds through several isotopes: 228Th (1.9 years), 228Ac (6.1 minutes), 228Ra (5.7 years), 224Ra (3.6 days), 220Rn (55 seconds), 216Po (0.14 seconds), 212Bi (61 minutes), 212Po (0.296 seconds), 208Pb (stable), 208Tl (3.1 minutes), and 208Pb (stable). The chain is organized by element: Thorium, Actinium, Radium, Francium, Radon, Astatine, Polonium, Bismuth, Lead, and Thallium.](b0211cee4b20034939d883ac0d70f696_img.jpg)

```

graph TD
    Th232["232Th  
1.41e+10 years"] --> Th228["228Th  
1.9 years"]
    Th232 --> Ra228["228Ra  
5.7 years"]
    Th228 --> Ac228["228Ac  
6.1 minutes"]
    Ac228 --> Ra228
    Ra228 --> Ra224["224Ra  
3.6 days"]
    Ra224 --> Rn220["220Rn  
55 seconds"]
    Rn220 --> Po216["216Po  
0.14 seconds"]
    Po216 --> Bi212["212Bi  
61 minutes"]
    Bi212 --> Po212["212Po  
0.296 seconds"]
    Bi212 --> Pb212["212Pb  
10.6 minutes"]
    Po212 --> Pb212
    Pb212 --> Tl208["208Tl  
3.1 minutes"]
    Tl208 --> Pb208["208Pb  
stable"]
    Pb212 --> Pb208
    
```

Radioactive decay chain for the 232Th parent isotope. The chain starts with 232Th (1.41e+10 years) and proceeds through several isotopes: 228Th (1.9 years), 228Ac (6.1 minutes), 228Ra (5.7 years), 224Ra (3.6 days), 220Rn (55 seconds), 216Po (0.14 seconds), 212Bi (61 minutes), 212Po (0.296 seconds), 208Pb (stable), 208Tl (3.1 minutes), and 208Pb (stable). The chain is organized by element: Thorium, Actinium, Radium, Francium, Radon, Astatine, Polonium, Bismuth, Lead, and Thallium.

Figure 1-9. Radioactive decay chain showing all daughters of a  $^{232}\text{Th}$  parent isotope.

The time listed below each isotope in [Figure 1-9](#) is the time that it would take for half of a large population of that isotope to decay. An equilibrium population of  $^{232}\text{Th}$  will emit six alpha particles with energies from 4.081-8.955 MeV. The decay chain for the  $^{238}\text{U}$  uranium isotope is similar (although the daughters are different), emitting eight different alpha particles with kinetic energies ranging from 4.270-7.833 MeV.

When considering a large population of a specific unstable isotope, one key characteristic of the rate of decay is the average decay time. It is impossible to predict when a single specific unstable nucleus will undergo decay because it is a completely random process defined by quantum mechanics. However, when a large ensemble of unstable nuclei is present, the time for a specific fraction to decay is very well-defined.

The fraction of interest is set to 50%, indicating the time for 50% of the initial population of nuclei to decay. This is referred to as the half-life. Radioactive decay is a simple exponential decay process; after a time period of one half-life, only 50% of the original population remains. After two half-lives, 50% of the remaining 50% decays, so the population is 25% of its initial size, and so on.

The longer the half-life, the longer it takes for an isotope population to decay. A longer half-life therefore implies a lower activity, measured in decays/time. [Equation 1-1](#) is a simple equation for the exponential decay of an initial population,  $N_0$ , of unstable nuclei. [Equation 1-2](#) relates the activity,  $\lambda$ , to the half-life,  $\tau_{1/2}$ :

$$N(t) = N_0 \cdot e^{-\tau_{1/2}t}$$

[Equation 1-1.](#)

$$\lambda = \frac{\ln 2}{\tau_{1/2}}$$

[Equation 1-2.](#)

The alpha particle emitted during a decay event consists of two neutrons and two protons – a doubly ionized helium atom ( $^4\text{He}^{2+}$ ) – emitted with an energy in the range of 4 MeV to 9 MeV. The original unstable nucleus is therefore transformed by the emission of the alpha particle into a nucleus whose mass number is reduced by four (a loss of four nucleons) and whose atomic number is reduced by two (a loss of two protons).

The alpha-particle emission energy is specific to the nucleus that is emitting it, with each unstable isotope having a single unique alpha-particle emission energy (and in a few cases, several closely spaced emission energies). For a sample of  $^{232}\text{Th}$  in equilibrium, a single alpha-emission energy or set of energies will be observed for each alpha decay. [Figure 1-10](#) shows the alpha-emission spectrum from a thin film of  $^{232}\text{Th}$ .

![Figure 1-10: Simulation of the alpha emission from a thin layer of 232Th source material illustrating the discrete alpha energies. The graph shows Intensity (arbitrary units) on the y-axis (0 to 100) versus Alpha energy (MeV) on the x-axis (0 to 10). The spectrum consists of six distinct vertical lines at approximately 4.08, 4.4, 5.4, 5.8, 6.0, and 8.9 MeV, representing the discrete energy levels of the 232Th decay chain.](2f73c3f1961c12d27d0d18fe7befbf0c_img.jpg)

Figure 1-10: Simulation of the alpha emission from a thin layer of 232Th source material illustrating the discrete alpha energies. The graph shows Intensity (arbitrary units) on the y-axis (0 to 100) versus Alpha energy (MeV) on the x-axis (0 to 10). The spectrum consists of six distinct vertical lines at approximately 4.08, 4.4, 5.4, 5.8, 6.0, and 8.9 MeV, representing the discrete energy levels of the 232Th decay chain.

[Figure 1-10.](#) Simulation of the alpha emission from a thin layer of  $^{232}\text{Th}$  source material illustrating the discrete alpha energies.<sup>[19]</sup>

Of course, in a real situation in which the alpha emitter is a trace impurity in the die or packaging materials, it will be distributed in different layers, materials and concentrations. Thus, the distinct energy “lines” shown in [Figure 1-10](#) will not be visible because the emission can occur anywhere within the metal film. The distinct lines are broadened to lower energies because energy is lost as the alpha travels from where it was emitted. [Figure 1-11](#) shows the alpha-particle energy spectrum as it would look at the silicon surface after having been emitted from various locations within a complex package representing a distributed alpha source.

![Figure 1-11: Simulation of the alpha-particle spectrum at the active device surface from all sources within a packaged device. The graph shows Intensity (arbitrary units) on the y-axis (0 to 600) versus Alpha energy (MeV) on the x-axis (0 to 10). The spectrum is a broad, jagged red line starting around 150 MeV, peaking at approximately 500 MeV around 5.5 MeV, and then dropping off towards 10 MeV, representing the broadened energy distribution due to energy loss within the package.](fef288b92fc7299b718bb8d6107421c0_img.jpg)

Figure 1-11: Simulation of the alpha-particle spectrum at the active device surface from all sources within a packaged device. The graph shows Intensity (arbitrary units) on the y-axis (0 to 600) versus Alpha energy (MeV) on the x-axis (0 to 10). The spectrum is a broad, jagged red line starting around 150 MeV, peaking at approximately 500 MeV around 5.5 MeV, and then dropping off towards 10 MeV, representing the broadened energy distribution due to energy loss within the package.

[Figure 1-11.](#) Simulation of the alpha-particle spectrum at the active device surface from all sources within a packaged device.<sup>[19]</sup>

Alpha emissions from impurities in package mold compound or underfill, which are essentially “thick” sources, produce a broadened alpha-particle spectrum. A notable exception of this broadening occurs if the alpha source is confined to a thin layer, so that all of the alpha-particle emission essentially occurs at or very near the surface. One example of a thin source would be the residue of alpha-emitting impurities left after a wet-etch with certain batches of phosphoric acid<sup>[12, 13]</sup> or surface emission from solder bumps. It has been<sup>[14]</sup> reported that the primary alpha-emitting impurity (<sup>210</sup>Po) in standard lead-based solders segregates to the surface of solder bumps.<sup>[14]</sup> This effect would also lead to a sharp spectrum.

Comprehending the shape of the energy spectrum of the alpha particles incident on a silicon device is crucial in accurately determining the type and rate of SEEs. Indeed, the probability that an alpha particle causes a soft error is based largely on its energy and trajectory. The wrong assumption about the alpha-particle energy spectrum can lead to a significant overestimation or underestimation of the SEE rate from accelerated experiments. The activity of a particular isotope is directly proportional to its natural abundance and inversely related to its half-life. Secular equilibrium is only valid if the material has not undergone any chemical separation, because under such conditions, the various isotope concentrations can become depleted or enriched.

Because virtually all semiconductor materials are highly purified, in general, alpha-emitting impurities will not be in secular equilibrium (a situation in which a quantity of a radioactive daughter product remains constant because its production rate by decay of a parent is equal to its decay rate). Simply accounting for the amount of <sup>238</sup>U and <sup>235</sup>Th trace impurities present in the material will not guarantee that the alpha emission rate is below a certain level, because the daughter concentrations can be very far from equilibrium, and in many cases undetectable. In other words, low <sup>238</sup>U and <sup>235</sup>Th levels are necessary but **not** sufficient to ensure that a material has low alpha emissions. Thus, alpha-counting investigations are necessary to determine the alpha-particle flux from materials. Bateman equations can be used to calculate nonequilibrium daughter concentrations.

**Table 1-1** summarizes alpha-particle emissions from some key production materials determined by high-sensitivity (large-area) alpha counting. The alpha emission rates are reported at a 90% confidence level. Depending on grade and type of material, a large range of alpha-emission rates exists.

| Material                   | Emissivity (a/cm <sup>2</sup> -hr) |
|----------------------------|------------------------------------|
| Fully processed wafers     | <0.001                             |
| 30-μm-thick Cu metal (UBM) | <0.002                             |
| 20-μm-thick AlCu metal     | <0.001                             |
| Packaging mold compound    | <0.024 - <0.001                    |
| Flip-chip underfill        | <0.002 - <0.001                    |
| Eutectic Pb-based solder   | <7,200 - <0.002                    |

**Table 1-1. Typical alpha-emission rates from various materials.**

In general, the primary source of alpha particles is the package material (mold compound, underfill, solder), not the materials used to fabricate the semiconductor device. In the early 1980s, when the industry realized that alpha particles were a dominant reliability problem, material manufacturers came up with the low-alpha specification of <0.01 a/cm<sup>2</sup>-hr. As device technologies scaled and power-supply voltages dropped, sensitivity to alpha particles grew. A new standard was established in the 1990s: the ultra-low-alpha (ULA) emission of <0.002 a/cm<sup>2</sup>-hr.<sup>[22-24]</sup>

Assuming an attempt to minimize a microelectronic product's failure rate from alpha-particle-induced SEEs by using low-alpha-emission materials, an emissivity of ~0.001 a/hr-cm<sup>2</sup> for a packaged device seems to be a limit that is possible today. This emissivity limit equates to less than one-tenth of a part per billion for many materials! While such event rates may seem quite low, every alpha particle is directly ionizing, so each alpha particle that reaches active device silicon can potentially cause an SEE.

In contrast, neutron events must instigate a nuclear reaction to produce any charge; thus, the event rate is much smaller than the actual flux of neutrons. If every alpha emitted from a surface in a 1-cm<sup>2</sup> device caused AN EVENT, even at a low-emission rate of 0.001 a/hr-cm<sup>2</sup>, the observed failure rate would be about a million failures in time (FIT). Obviously, many alpha events will not cause an SEE due to the small amount of charge being deposited. In typical microelectronic technologies, assuming the control of alpha-particle emission to ULA levels, the resulting SEE rate will be somewhere in the range of 1,000 to 100 FIT/cm<sup>2</sup>.

An SEE caused by alpha particles can constitute a large fraction of the failure rate observed in terrestrial applications. However, at flight altitudes, where the neutron flux is several orders of magnitude higher, alpha-particle SEEs become a negligible portion because they are independent of altitude and based only on the intrinsic impurity levels in the materials. For applications where an alpha-particle SEE is a significant fraction of the observed failure rate, the impact of alpha particles can be mitigated in several ways:

- Using extremely high-purity materials and screening them to validate their low alpha-particle emission.
- Using design rules so that packaging components with the highest alpha emissions are physically separated from sensitive circuit components. (This approach is only effective if there is a big difference in the alpha-induced SEE sensitivity. This was used effectively in the days when static random access memory (SRAM) was much more sensitive than sequential logic. Digital devices were laid out with keep-out zones, where flip-chip bumps with high alpha emissions could not be placed over SRAM.
- Shielding the die from materials with high alpha emissions. This is difficult, since layers must be many tens of microns thick to ensure efficacy. Using a shield that is not thick enough can actually increase the SEE failure rate above unshielded units<sup>[25]</sup> due to the large nonlinearity in the alpha particle's linear energy transfer (LET) as a function of energy.

#### High-energy cosmic-ray neutrons

The second significant source of SEEs in microelectronics in the terrestrial environment is related to high-energy cosmic-ray neutrons. “High energy” in this case defines neutrons with energy  $\geq 1$  MeV.<sup>[26]</sup> As noted in the section on space radiation, the Earth’s upper atmosphere is bathed in radiation from primary GCRs with  $E_{\text{max}} > 1$  GeV and SEPs with  $E_{\text{max}} < 1$  GeV. They consist of 92% protons, 6% alpha particles (He), and 2% gamma photons and heavier nuclei.

Coulombic interactions in the upper atmosphere quickly stop the alpha particles and heavier ions, leaving only the high-energy protons to react in the upper atmosphere. The protons undergo nuclear reactions via strong force, with oxygen and nitrogen nuclei producing huge and complex cascades of “secondary” particles that shower down through the atmosphere to the Earth’s surface. The reaction products or secondaries include short-lived pions and kaons that decay into muons, neutrinos and gamma rays, as well as electrons and positrons produced by muon decay and follow-on interactions between gamma-ray photons and other atmospheric atoms. **Figure 1-12** illustrates a schematic of a cascade.

![Figure 1-12: Particle cascade or 'shower' diagram. An incoming cosmic ray (red dot) strikes a nucleus (N), creating a cascade of secondary particles. The cascade includes pions (pi+, pi-, pi0), muons (mu+, mu-, mu0), protons (p), neutrons (n), electrons (e-), and positrons (e+). The diagram shows the branching of particles as they travel downwards, with a legend indicating: P: Proton, n: Neutron, pi: Pion, e: Electron, mu: Photon.](ff0952ef692c9d960ce5f6708bcc9711_img.jpg)

Figure 1-12: Particle cascade or 'shower' diagram. An incoming cosmic ray (red dot) strikes a nucleus (N), creating a cascade of secondary particles. The cascade includes pions (pi+, pi-, pi0), muons (mu+, mu-, mu0), protons (p), neutrons (n), electrons (e-), and positrons (e+). The diagram shows the branching of particles as they travel downwards, with a legend indicating: P: Proton, n: Neutron, pi: Pion, e: Electron, mu: Photon.

**Figure 1-12. Particle cascade or “shower” created when a high-energy cosmic-ray proton interacts with a nitrogen or oxygen nucleus in the upper atmosphere.**<sup>[27]</sup>

Image courtesy of International Business Machines Corp., © International Business Machines Corp.

Less than 1% of the primary flux reaches sea level. The predominant particle fluxes at sea level include muons, protons, electrons, neutrons and pions. Due to their relatively high flux and stability, the neutrons are the most likely cosmic radiation to cause SEEs in devices at terrestrial altitudes. Pions and muons are short-lived, and the lower-energy protons and electrons are effectively attenuated by Coulombic interactions.

**Figure 1-13** shows the differential energy spectra for the primary cosmic-ray particles encountered at sea level. These curves define the number of particles at any given energy that are incident on a microelectronic device (or anything else) at sea level. Ultimately, the Earth’s atmosphere can be considered a thick filter layer of reactive matter that converts the high flux of incident cosmic-ray protons into a lower flux of lower-energy terrestrial neutrons. Significant numbers of cosmic-ray muons and protons are also produced, but their impact on microelectronics is much less significant.

![Figure 1-13: Differential flux for the primary cosmic-ray particles at sea level. A log-log plot of Flux/(cm²·MeV·s) vs Particle energy (GeV). The plot shows curves for Neutrons (red), Muons (light blue), Protons (dark blue), and Pions (cyan). The total flux is also shown. The plot includes location and atmospheric data: Latitude: 42.35° N (GM=54.03°), Longitude: 288.95° E (GM=357.37°), Altitude: 0 ft, Press.: 1033 g/cm², Temp.: 0°C, GMR: 1.7 GV. Total flux/cm²·s: Neutrons = 0.0142, Muons = 0.0207, Pions = 0.0000153, Protons = 0.000114.](303b94716b6713757d1fdf940a6b345f_img.jpg)

Figure 1-13: Differential flux for the primary cosmic-ray particles at sea level. A log-log plot of Flux/(cm²·MeV·s) vs Particle energy (GeV). The plot shows curves for Neutrons (red), Muons (light blue), Protons (dark blue), and Pions (cyan). The total flux is also shown. The plot includes location and atmospheric data: Latitude: 42.35° N (GM=54.03°), Longitude: 288.95° E (GM=357.37°), Altitude: 0 ft, Press.: 1033 g/cm², Temp.: 0°C, GMR: 1.7 GV. Total flux/cm²·s: Neutrons = 0.0142, Muons = 0.0207, Pions = 0.0000153, Protons = 0.000114.

**Figure 1-13. Differential flux for the primary cosmic-ray particles at sea level. The total flux of muons is actually higher than that of neutrons, but muons are less able to generate errors.**<sup>[28]</sup>

Image courtesy of International Business Machines Corp., © International Business Machines Corp.

If the neutron curve in **Figure 1-13** is replotted as the neutron flux times the neutron energy, then the areas under the spectral peaks represent similar fluxes. The replotted neutron spectrum shown in **Figure 1-14** has three broad peaks:

- A high-energy peak centered around 100 MeV, which is defined by the highest-energy cosmic-ray neutrons reaching sea level.
- A peak centered around 2 MeV and attributed to nuclear reactions between secondary and tertiary cosmic-ray particles and oxygen and nitrogen nuclei – the so-called nuclear evaporation peak.
- A neutron peak at the lowest energy that comprises neutrons that have been slowed down by scattering and are in thermal equilibrium with atoms in surrounding materials.

![Figure 1-14: Measured cosmic-ray neutron spectrum for five locations. The graph plots Energy x differential (cm-2 s-1) on the y-axis (0 to 1.5 x 10^-3) against Neutron energy (MeV) on a logarithmic x-axis (10^-8 to 10^4). Five curves are shown: Fremont Pass (light blue), Leadville (medium blue), Mt. Washington (dark blue), Yorkton Hts. (black), and Houston (red). All curves show a sharp peak around 10^-7 MeV and a broader peak around 10^1 MeV, with the peaks increasing in magnitude from Houston to Fremont Pass.](7c1f9e78e0f033d391b687f1652f6e47_img.jpg)

Figure 1-14: Measured cosmic-ray neutron spectrum for five locations. The graph plots Energy x differential (cm-2 s-1) on the y-axis (0 to 1.5 x 10^-3) against Neutron energy (MeV) on a logarithmic x-axis (10^-8 to 10^4). Five curves are shown: Fremont Pass (light blue), Leadville (medium blue), Mt. Washington (dark blue), Yorkton Hts. (black), and Houston (red). All curves show a sharp peak around 10^-7 MeV and a broader peak around 10^1 MeV, with the peaks increasing in magnitude from Houston to Fremont Pass.

Figure 1-14. Measured cosmic-ray neutron spectrum for five locations.<sup>[26]</sup>

The thermal neutron distribution is only important in devices that contain concentrations of  $^{10}\text{B}$ , because in general, most thermal neutron reactions with other isotopes only produce a gamma-ray photon, which usually does not generate sufficient charge to cause an SEE. In contrast, neutrons with  $>100$  keV of energy and those in the middle peak are highly effective at generating relatively large charge transients that translate into detectable SEEs. Neutrons in the high-energy peak portion will cause spallation reactions that are less likely to produce SEEs, because the emitted nucleon will either generate only a small amount of charge through proton direct ionization or no charge at all. The neutron has no charge, so there is no Coulombic charge production. Additional nuclear reactions are required to generate a sizable event capable of generating an SEE.

Three primary factors define the cosmic-ray neutron flux at any terrestrial location. The most dominant factor is by far the altitude, with neutron flux increasing nearly 20x from sea level to 4,000 m (13,000 feet).<sup>[26]</sup> At commercial flight altitudes, the neutron flux can be hundreds of times higher than it is at sea level. Eventually, the neutron-flux increase – as a function of increasing altitude – saturates at about 17 km (55,000 feet). Figure 1-15 shows the effect of altitude on neutron flux.

![Figure 1-15: Neutron-flux increase as a function of altitude. The graph plots Relative neutron flux on the y-axis (0 to 400) against Altitude (feet) on the x-axis (0 to 80k). A red curve shows the flux increasing sharply from 0 at sea level to a plateau of about 350 at 60k feet. The area under the curve is shaded light blue and labeled 'Flight altitudes'. The area before the curve starts to rise is labeled 'Terrestrial altitudes'.](411fa16c3211377525ba37c57784fee0_img.jpg)

Figure 1-15: Neutron-flux increase as a function of altitude. The graph plots Relative neutron flux on the y-axis (0 to 400) against Altitude (feet) on the x-axis (0 to 80k). A red curve shows the flux increasing sharply from 0 at sea level to a plateau of about 350 at 60k feet. The area under the curve is shaded light blue and labeled 'Flight altitudes'. The area before the curve starts to rise is labeled 'Terrestrial altitudes'.

Figure 1-15. Neutron-flux increase as a function of altitude.

Altitude can have a significant impact on the rate of SEEs. For microelectronic devices used at flight altitudes, the cosmic-ray flux can be hundreds of times higher than it is at sea level; thus, neutron-induced events dominate reliability in avionics.

Latitude, or, more specifically, geomagnetic rigidity as a function of geographical location, is a secondary factor that can modulate the neutron flux by about 2x at terrestrial altitudes and ~5x at commercial flight altitudes. The neutron flux increases from equatorial to polar regions. The Earth's magnetic field deflects incoming cosmic-ray protons from equatorial regions where the field is parallel to the Earth's surface. But in areas where the field orientation approaches normal incidence at the poles, the magnetic field provides only weak shielding at north/south magnetic latitudes in excess of 55 degrees. Figure 1-16 shows the neutron flux as a function of latitude.

![Figure 1-16: Cosmic-ray neutron flux as a function of latitude for sea level and at flight altitudes. The graph plots Relative neutron flux on the y-axis (0 to 6.0) against Latitude (degrees) on the x-axis (0 to 90). Two curves are shown: a red curve for 'Flight altitudes' and a blue curve for 'Sea level'. Both curves show an increase in flux from equatorial (0 degrees) to polar (90 degrees) latitudes, with the flight altitude curve reaching a much higher plateau (around 5.5) than the sea level curve (around 2.0).](b8261918596971c3801af23435c5ea50_img.jpg)

Figure 1-16: Cosmic-ray neutron flux as a function of latitude for sea level and at flight altitudes. The graph plots Relative neutron flux on the y-axis (0 to 6.0) against Latitude (degrees) on the x-axis (0 to 90). Two curves are shown: a red curve for 'Flight altitudes' and a blue curve for 'Sea level'. Both curves show an increase in flux from equatorial (0 degrees) to polar (90 degrees) latitudes, with the flight altitude curve reaching a much higher plateau (around 5.5) than the sea level curve (around 2.0).

Figure 1-16. Cosmic-ray neutron flux as a function of latitude for sea level and at flight altitudes.<sup>[27]</sup>

The third and weakest variable modulating the terrestrial neutron flux is the solar activity cycle. Solar activity usually accounts for  $<\pm 30\%$  variations in neutron flux. Because the neutron flux at terrestrial altitudes is linked to the proton flux incident on the upper atmosphere, it follows that solar activity will have some impact on the neutron flux at sea level. In times of "normal" solar activity, where the activity increases relatively slowly, the upper atmosphere has time to respond to changes in conditions and becomes more highly ionized, thereby creating an electrostatic repulsion field that actually deflects a greater number of incoming protons.

As might be expected, the increased shielding effect during high solar activity reduces the number of protons that get into the atmosphere, thus producing fewer neutrons (muons, etc.). So for typical high solar activity, the neutron flux at terrestrial altitudes is reduced.

Occasionally, sporadic flares and CMEs can occur so suddenly that the Earth's ionosphere cannot respond quickly enough. The ionospheric charging and resulting screening effect do not have time to respond, so the terrestrial neutron flux actually increases during such short-lived events. Figure 1-17 shows the terrestrial neutron flux as a function of solar activity cycle under longer-term variations.

![Figure 1-17: A line graph showing the percentage change in neutron flux as a function of the 11-year solar-activity cycle. The y-axis is labeled '% Change in neutron flux' and ranges from 0% to -30% in increments of 5%. The x-axis is labeled 'Time' and shows dates from 11/1997 to 9/2004, with major ticks at 3/1999, 8/2000, 12/2001, 5/2003, and 9/2004. A blue line with high-frequency noise represents the neutron flux data, and a red dashed line represents the 11-year sun-spot cycle. The text 'Solar eruptions follow the "11-year sun-spot cycle"' is written in the upper right area of the plot.](71ab4df17511d75261da8d462d643b1a_img.jpg)

Figure 1-17: A line graph showing the percentage change in neutron flux as a function of the 11-year solar-activity cycle. The y-axis is labeled '% Change in neutron flux' and ranges from 0% to -30% in increments of 5%. The x-axis is labeled 'Time' and shows dates from 11/1997 to 9/2004, with major ticks at 3/1999, 8/2000, 12/2001, 5/2003, and 9/2004. A blue line with high-frequency noise represents the neutron flux data, and a red dashed line represents the 11-year sun-spot cycle. The text 'Solar eruptions follow the "11-year sun-spot cycle"' is written in the upper right area of the plot.

**Figure 1-17. Cosmic-ray neutron flux as a function of the 11-year solar-activity cycle. During periods of active sun, the neutron flux decreases.**

High-energy neutron interactions with silicon and other chip materials are extremely complicated and depend on the energy of the incident neutrons. One of the primary reactions by which cosmic-ray events induce SEEs in microelectronics is the neutron-induced silicon recoil (elastic and inelastic). When neutrons with kinetic energies in excess of about 100 keV collide with silicon nuclei, enough of their energy can transfer to the nucleus to knock it from its position within the silicon lattice (this is also an example of DD discussed in Chapter 3, although in this case the event rate is simply too low to produce a dose effect), generating enough charge through Coulombic interactions to upset many microelectronic technologies.

For incident neutrons with energies above about 2 MeV, a host of nuclear reaction pathways become viable. In these reactions, the silicon nucleus absorbs the neutron in an inelastic reaction that produces a burst of highly ionizing secondary products. The original nucleus breaks apart into energetic fragments, including a heavy recoil nucleus and lighter ions and/or nucleons, each of which can potentially induce SEEs or other nuclear reactions. As neutron energies increase above 100 MeV, the wavelength of the neutron is so small that it no longer interacts with the entire nucleus, but actually exchanges its energy with single nucleons in a process called spallation. In spallation, the secondaries produced are individual nucleons ejected by an incoming neutron. All neutron reactions occur at a rate defined by the neutron flux, the energy of each neutron and the neutron reaction cross-section, which is also a function of neutron energy for the material in which the neutron is traveling. For microelectronic devices, the primary materials are silicon and silicon oxide, where the active components reside.<sup>[30,31]</sup>

SEE rates caused by the high-energy cosmic-ray neutron flux depend on the location (altitude, latitude) and to a small degree on solar activity, as previously mentioned. Using the default terrestrial neutron – as specified by the JESD89A test standard to allow comparison across results – creates a model where the baseline standard neutron flux is defined at 0 m, New York City (NYC) latitude/longitude and equal to 1. Any geographical position and any solar-activity level can be modeled as a multiplicative factor of this standard neutron flux. (Geographical factor as a

function of key variables can be found at <http://www.seutest.com/cgi-bin/FluxCalculator.cgi> for sea-level NYC neutron flux [ $>10$  MeV] of  $13 \text{ n/cm}^2\text{-hr}$ .<sup>[32]</sup> Assuming an area of  $1 \text{ cm}^2$  for the device, you can expect 13 neutron events per hour or 0.0036 neutrons per second at sea level – much more if the device operates at higher altitudes or latitudes.

If every neutron caused an SEE, the microelectronic device would suffer a failure rate of approximately 3.6 million FIT. However, since neutrons do not have charge, they cannot directly ionize silicon. In other words, the actual event rate will be defined by the flux of neutrons and the neutron reaction cross-section for the materials through which the neutrons are traveling. Cross-sections vary tremendously with neutron energy and material, but in general for silicon (assuming a rough cross-section for reactions that can cause secondary products with enough energy to create SEEs), an estimated one SEE is observed per 1,000 to 10,000 neutrons. Thus, the neutron-induced SEE rate drops to approximately 3,600 to 360 FIT for a  $1\text{-cm}^2$  device.

Unlike alpha-particle mitigation schemes focused on the purification of materials, keep-out zones and/or shielding layers, the ever-present cosmic-ray neutron flux cannot easily be reduced at chip level with die shields, keep-out zones or high-purity materials. Simulation has shown that hydrogen-rich materials such as concrete (due to its relatively high moisture content) can offer some reductions in cosmic-ray neutron flux – approximately a fourfold reduction per meter<sup>[33]</sup> of concrete thickness.

Neutron detector studies confirm that in the basements of concrete buildings, reductions of cosmic-ray neutron flux as high as an order of magnitude are possible.<sup>[34]</sup> While hiding out in a basement location may be a viable option for mainframes, server farms and supercomputer clusters, for personal desktop applications or portable electronics, little can be done to reduce SEEs produced by high-energy neutron events. Designers must therefore deal with cosmic-ray SEEs by reducing the sensitivity of microelectronics, either by design or process modifications.

#### Low-energy cosmic-ray neutrons and $^{10}\text{B}$

The third significant source of ionizing particles in some microelectronic devices is the secondary radiation induced from the interaction of low-energy cosmic-ray neutrons and  $^{10}\text{B}$ .<sup>[35-37]</sup> While the previous discussion focused on high-energy neutron reactions, this reaction is dominated by low-energy neutrons that have been thermalized by numerous interactions with materials around them ( $\sim 0.025 \text{ eV}$ ).<sup>[38,39]</sup> This affects only devices with large concentrations of a certain isotope of boron. Boron is used extensively as a P-type diffusion and implant species in silicon, in the formation of boron-doped phosphosilicate glass (BPSG) (2%-8% by weight) dielectric layers.<sup>[40]</sup> Borane is used as a formation or carrier gas for several processes.

While implantation processes tend to be fairly mass-specific and usually implant  $^{11}\text{B}$ , diffusion and gas processes typically use boron that has not been isotopically separated. Boron consists of two isotopes:  $^{11}\text{B}$  (80.1% abundance) and  $^{10}\text{B}$  (19.9% abundance). The  $^{10}\text{B}$  is unstable when exposed to neutrons.  $^{11}\text{B}$  also reacts with

neutrons; however, its reaction cross-section is nearly 1 million times smaller, and its reaction products (gamma rays) generally do not cause problems. The thermal neutron capture cross-section of  $^{10}\text{B}$  is extremely high compared to most other isotopes present in semiconductor materials (three to seven orders of magnitude higher), as illustrated in [Figure 1-18](#).

![Figure 1-18: Bar chart comparing thermal neutron capture cross-sections (σ_th in barns) for various materials. The y-axis is logarithmic, ranging from 10^-3 to 10^4. Boron-10 has the highest cross-section at approximately 3,800 barns. Other materials include Tungsten (~15 barns), Titanium (~6 barns), Arsenic (~4 barns), Copper (~3 barns), Nitrogen (~1 barn), Aluminum (~0.3 barns), Silicon (~0.2 barns), Phosphorus (~0.1 barns), Oxygen (~0.0001 barns), and Boron-11 (~0.0001 barns).](b05fbb6a015ea153c1e25245772b1a1b_img.jpg)

| Material   | $\sigma_{th}$ (barns) |
|------------|-----------------------|
| Boron-10   | ~3,800                |
| Tungsten   | ~15                   |
| Titanium   | ~6                    |
| Arsenic    | ~4                    |
| Copper     | ~3                    |
| Nitrogen   | ~1                    |
| Aluminum   | ~0.3                  |
| Silicon    | ~0.2                  |
| Phosphorus | ~0.1                  |
| Oxygen     | ~0.0001               |
| Boron-11   | ~0.0001               |

Figure 1-18: Bar chart comparing thermal neutron capture cross-sections (σ\_th in barns) for various materials. The y-axis is logarithmic, ranging from 10^-3 to 10^4. Boron-10 has the highest cross-section at approximately 3,800 barns. Other materials include Tungsten (~15 barns), Titanium (~6 barns), Arsenic (~4 barns), Copper (~3 barns), Nitrogen (~1 barn), Aluminum (~0.3 barns), Silicon (~0.2 barns), Phosphorus (~0.1 barns), Oxygen (~0.0001 barns), and Boron-11 (~0.0001 barns).

**Figure 1-18. Comparison of thermal neutron capture cross-sections for  $^{10}\text{B}$  and several common semiconductor materials. This plot demonstrates the anomalously high thermal neutron reaction cross-section of  $^{10}\text{B}$ . Note, a “barn” is a nuclear physics unit of area equivalent to  $10^{-24} \text{ cm}^2$ .**

Unlike most isotopes that emit relatively harmless gamma photons, after absorbing a thermal neutron, the  $^{10}\text{B}$  nucleus breaks apart with an accompanying release of energy in the form of an excited  $^7\text{Li}$  recoil nucleus and an alpha particle. A prompt gamma photon is also emitted from the lithium recoil soon after fission occurs. In the  $^{10}\text{B}(n,\alpha)^7\text{Li}$  reaction, the alpha particle and lithium nucleus are emitted in opposite directions to conserve momentum. The lithium nucleus is emitted with a kinetic energy of 0.840 MeV 94% of the time and 1.014 MeV 6% of the time. The alpha particle is emitted with an energy of 1.47 MeV, as shown in [Figure 1-19](#).

![Figure 1-19: Diagram illustrating the capture of a thermal neutron by a 10B nucleus. A thermal neutron (represented by a blue dot) strikes a 10B nucleus (represented by a cluster of red and blue spheres). The reaction produces an alpha particle (4He, represented by a blue cloud) with 1.47 MeV energy and a lithium recoil nucleus (7Li, represented by a blue cloud) with 0.84 MeV energy. A prompt gamma photon (represented by a wavy line) is also emitted.](16152cf1d84aea10848758f51a91ff6a_img.jpg)

Figure 1-19: Diagram illustrating the capture of a thermal neutron by a 10B nucleus. A thermal neutron (represented by a blue dot) strikes a 10B nucleus (represented by a cluster of red and blue spheres). The reaction produces an alpha particle (4He, represented by a blue cloud) with 1.47 MeV energy and a lithium recoil nucleus (7Li, represented by a blue cloud) with 0.84 MeV energy. A prompt gamma photon (represented by a wavy line) is also emitted.

**Figure 1-19. Capture of a thermal neutron by a  $^{10}\text{B}$  nucleus and the secondary products: an alpha particle, a lithium recoil nucleus and prompt gamma photon.**

The lithium recoil has a peak LET of 25 fC/ $\mu\text{m}$ , while that of the alpha particle is 16 fC/ $\mu\text{m}$ . In most cases, calculations have shown that the range of the alpha particle and lithium recoils in silicon and silicon oxide is very limited: less than 1.5  $\mu\text{m}$ . If the reaction occurs more than 1 mm away from sensitive device nodes (deeper in the substrate or in the layers over the silicon), neither the lithium recoil nor alpha particle will have sufficient energy to induce SEEs.

[Figure 1-20](#) shows the lineal charge generation and range of both secondary products. Generally, only  $^{10}\text{B}$  in close proximity to the active silicon layer needs to be considered. For conventional semiconductor processes, BPSG is the dominant source of boron reactions, and in some cases can be the primary cause of soft errors.<sup>[41-43]</sup> The alpha and the lithium recoils are both capable of inducing SEEs in microelectronics, particularly in advanced low-voltage technologies. The event rate from the  $^{10}\text{B}(n,\alpha)^7\text{Li}$  mechanism is a function of the thermal neutron flux, the thermal neutron cross-section for the reaction and the amount of  $^{10}\text{B}$  in the device close to the active silicon device layers. Several groups have measured the terrestrial thermal neutron flux and it is between 4-20 n/ $\text{cm}^2\text{-hr}$ , basically a little less or similar in magnitude to the high-energy neutron flux. The  $^{10}\text{B}(n,\alpha)^7\text{Li}$  reaction has a thermal neutron cross-section of 3,838 barns (1 barn =  $10^{-24} \text{ cm}^2$  per nucleus).

![Figure 1-20: Graph showing differential charge generation (dQ/dx in fC/μm) and range in silicon (μm) as a function of particle energy (MeV) for the 10B(n,α)7Li reaction. The x-axis is ion energy (MeV) from 0.0 to 1.5. The left y-axis is dQ/dx (fC/μm) from 0 to 20. The right y-axis is Range in silicon (μm) from 0 to 5. Four curves are shown: Li dQ/dx in silicon (red), He dQ/dx in silicon (teal), Li range in silicon (light blue), and He range in silicon (dark blue).](0bd23f00e0632855cfef9274f1ab93d8_img.jpg)

Figure 1-20: Graph showing differential charge generation (dQ/dx in fC/μm) and range in silicon (μm) as a function of particle energy (MeV) for the 10B(n,α)7Li reaction. The x-axis is ion energy (MeV) from 0.0 to 1.5. The left y-axis is dQ/dx (fC/μm) from 0 to 20. The right y-axis is Range in silicon (μm) from 0 to 5. Four curves are shown: Li dQ/dx in silicon (red), He dQ/dx in silicon (teal), Li range in silicon (light blue), and He range in silicon (dark blue).

**Figure 1-20. Differential charge generation and range in silicon as a function of particle energy from the alpha particle and lithium recoil produced by the  $^{10}\text{B}(n,\alpha)^7\text{Li}$  reaction.<sup>[44]</sup>**

Assuming a 1- $\text{cm}^2$  device area covered with a 1-mm layer of BPSG doped with 8% boron, an upper bound for the SEE event rate can be calculated by assuming that one of the two secondary products will produce a detectable SEE. Because the secondaries are emitted in opposite directions, only one of them will traverse the active devices. Actually, since the secondary products will be emitted in or near the active silicon device volumes, it is very likely that each event will be capable of upsetting a sensitive volume. In any case, using the assumptions above, an event rate of 0.0126 reactions/hr- $\text{cm}^2$  is the upper bound, or, assuming that each event is an upset, a failure rate of 17 kFIT. Clearly, this is an overestimation, but compared to

the other two mechanisms (the terrestrial thermal neutron flux and the alpha particles), the  $^{10}\text{B}(n,\alpha)^7\text{Li}$  mechanism can cause reliability issues in microelectronics that have BPSG layers close to the silicon substrate, or those that use borane-based fabrication processes and leave  $^{10}\text{B}$  residue near the active silicon.

It's possible to mitigate SEEs caused by the activation of  $^{10}\text{B}$  in BPSG in several ways. The first and most direct is simply to eliminate BPSG, borane or other boron-containing compounds from the process flow. Due to the limited range of the alpha and lithium recoil emitted during the  $^{10}\text{B}(n,\alpha)^7\text{Li}$  reaction, there is no need to replace or modify concentrations of  $^{10}\text{B}$  outside this range because the secondary products will never reach active silicon. In cases where the unique reflow and gettering properties of boron are needed, or the boron compound is required in the process, the boron source material should be replaced with one enriched with a  $^{11}\text{B}$ , thereby mitigating  $^{10}\text{B}$  without changing the desired physical or chemical properties and without requiring new equipment or processing steps.

Finally, if the process cannot be changed, such as in the case of a foundry process, the packaging materials can use materials rich in  $^{10}\text{B}$  to provide a thermal neutron shield. For example, in a plastic molded package, the silica filler could be doped with  $^{10}\text{B}$ , thus providing effective shielding for thermal neutrons. Because the resultant secondary alpha-particle and lithium recoils only have a range of  $<2\text{ }\mu\text{m}$ , they would be completely absorbed by the silica and mold compound or die materials long before any of the radiation would reach the sensitive active silicon device volume.

### 1.3 Artificial radiation environments

This section focuses on man-made artificial radiation environments, situations where microelectronics are exposed to – and must function in – radiation environments produced in a host of medical, industrial and defense applications. In medical applications, the radiation exposure occurs most often in diagnostic or treatment equipment such as X-ray and proton-beam therapy machines. High doses of electron-beam (e-beam) or gamma-ray irradiation are also used for sterilizing surgical instruments and implantable electronics in operating rooms.

There are numerous industrial uses of radiation. A wide range of applications rely on X-ray, gamma- and e-beam irradiation, from waste treatment to inspection to security screening. Microelectronics are exposed to doses of neutrons and gamma rays when used in high-radiation areas inside nuclear power plants. In the defense environment, electronics must be hardened against brief but intense gamma-ray and neutron exposures, as well as against follow-on electromagnetic pulse (EMP) effects from nuclear detonations. For microelectronics in most medical and industrial applications, TID is the primary radiation effect concern, while in the defense environment, the concern includes the full spectrum of SEEs, TID, DDD and prompt-dose (high-dose-rate) effects.

### Medical radiation environments

In the medical field, devices that produce X-rays are ubiquitous, from simple dental X-ray machines to full-body scanners (dental X-rays, fluoroscopes, computerized axial tomography [CAT] scanners, etc.). **Figure 1-21** shows an evacuated tube with electrodes at each end producing X-rays. One electrode, the filament, is heated by running a high current through the wire filament. The filament current is the source of electrons for the acceleration process that produces the X-rays. The heated wire emits electrons from the surface of the wire, which is excited by thermionic emission.

![Figure 1-21: Cross-sectional diagram of an X-ray tube. The diagram shows a vacuum tube with a glass envelope. Inside, there is a tungsten target (anode) and a filament (cathode). The filament is connected to a high-voltage anode and a grounded cathode shield. Accelerated electrons are shown moving from the filament towards the tungsten target, producing X-rays. A filament current is also shown flowing through the filament.](43837b056625d3d6ce615e4c02f163bb_img.jpg)

The diagram illustrates the internal components of an X-ray tube. A vacuum tube is shown with a glass envelope. Inside, a tungsten target (anode) is positioned at one end, and a filament (cathode) is at the other. The filament is connected to a high-voltage anode and a grounded cathode shield. Accelerated electrons are shown moving from the filament towards the tungsten target, producing X-rays. A filament current is also shown flowing through the filament.

Figure 1-21: Cross-sectional diagram of an X-ray tube. The diagram shows a vacuum tube with a glass envelope. Inside, there is a tungsten target (anode) and a filament (cathode). The filament is connected to a high-voltage anode and a grounded cathode shield. Accelerated electrons are shown moving from the filament towards the tungsten target, producing X-rays. A filament current is also shown flowing through the filament.

**Figure 1-21.** Cross-sectional diagram of an X-ray tube.

In this process, the electrons gain enough kinetic energy from heating to be able to overcome the work function of the material, which is the energy required to liberate an electron from inside a material. The filament itself is surrounded by a grounded metal cup with an aperture at the end, facing the other electrode. The other electrode, the target, is biased with a high positive voltage with respect to the filament cup (usually 10-150 KeV) such that the high electric field immediately sweeps the electrons emitted through the aperture in the cup toward the target electrode. Because the electrons are traveling in a vacuum, they suffer no energy-robbing collisions with gas molecules and thus are accelerated to high energies by the field.

When these energetic electrons collide with the target (usually a high-z metal such as tungsten), various scattering effects (see Chapter 2) produce X-rays. The target is usually canted at an angle to enable the X-ray radiation to radiate out of the side of the tube, unobstructed. The amount of radiation exposure in diagnostic applications near the equipment or in the patient is not high enough to pose a risk to microelectronics because the X-ray dose is tightly controlled (humans are much more sensitive to radiation exposure than electronics), and the X-ray equipment is heavily shielded so that no X-rays radiate outside the target treatment area.

As an example of a typical patient dose, consider the very popular computer tomography (CT) or CAT scanner, which provides cross-sectional images of the body constructed from a series of multiple X-ray exposures from different radial positions, as illustrated in **Figure 1-22**.<sup>[45]</sup> This type of diagnostic will usually give a maximum X-ray dose, as a large number of X-ray exposures is required to build up the image.

![Diagram of a CT scanner showing a patient lying on a motorized table. A rotating X-ray source at the top emits a fan-shaped X-ray beam through the table. Rotating detectors are positioned around the table. Arrows indicate the rotating direction of the source and detectors.](fbfaa723129f8b8e3be651c6fe7cfab7_img.jpg)

Diagram of a CT scanner showing a patient lying on a motorized table. A rotating X-ray source at the top emits a fan-shaped X-ray beam through the table. Rotating detectors are positioned around the table. Arrows indicate the rotating direction of the source and detectors.

**Figure 1-22. Diagram of a CT scanner. Because the image is built up from numerous X-ray “shots,” the radiation exposure from a CT scan can be many times higher than that of a single X-ray.**

Table 1-2 shows a comparison of the patient dose received as a function of the type of X-ray diagnostic. The unit of millisieverts (mSv) defines an “effective dose” received from radiation exposure based on different tissue types and their relative sensitivity to specific types of radiation. To put this into perspective, with regards to doses relevant to microelectronics, 1 mSv is equivalent to 0.1 rad(Si).

|                                                       |           |
|-------------------------------------------------------|-----------|
| CT-abdomen and pelvis, repeated with/without contrast | 20 mSv    |
| CT – colonography                                     | 6 mSv     |
| Coronary computed tomography angiography (CTA)        | 12 mSv    |
| Radiograph – lower GI tract                           | 8 mSv     |
| Radiograph – spine                                    | 1.5 mSv   |
| Radiograph – extremity                                | 0.001 mSv |
| CT – chest                                            | 7 mSv     |
| CT – lung cancer screening                            | 1.5 mSv   |
| Radiograph – chest                                    | 0.1 mSv   |
| Dental intraoral X-ray                                | 0.005 mSv |
| Bone densitometry (DEXA)                              | 0.001 mSv |
| Mammography                                           | 0.4 mSv   |

**Table 1-2. The effective doses of various diagnostic X-ray procedures.**<sup>[46]</sup>

For a microelectronic device implanted in a patient, given a single CT abdomen scan, you would expect a maximum dose of ~2 rad(Si). Even the weakest commercial electronics would not be sensitive to such a low dose.

What about SEEs occurring during irradiation? To be certain that CT scans do not interfere with implanted devices, several medical studies used CT scanner X-rays to directly irradiate the electronics of pacemakers and cardio defibrillators (simulating a coronary CT angiography or multipass abdomen CT scan). While some did report “electronic interference,” the probability that this interference would cause clinically significant adverse events was deemed extremely low.

For example, the interference observed on an internal node did not translate into a functional interruption during irradiation.

It is possible to completely avoid the risk of any interference when the implantable device is outside the primary X-ray beam of the CT scanner. In general, microelectronics implanted in patients are unlikely to be exposed to any radiation that would damage them because of the high-dose sensitivity of the human body compared to silicon devices.

The one medical environment where microelectronics may be exposed to high chronic doses of X-rays is in the solid-state detectors and supporting electronics housed inside of an X-ray machine. In these locations, the patient receives an X-ray dose; therefore, a single exposure will represent a relatively low dose. However, the fact that the machine is used on many patients over hours, days, months and years of service means that internal electronics can accumulate high TIDs.

Vendors of such equipment alleviate this problem by ensuring that metal of sufficient density/thickness shields all microelectronics that are not physically part of the actual imaging, so that X-ray exposure is minimized or eliminated completely. Image sensors will necessarily be exposed to X-rays and will accumulate significant doses over time.<sup>[47-49]</sup> In cases such as these, even well-designed or radiation-hardened imagers and support circuits will likely suffer dose effects and will need to be replaced occasionally. Since dose failures involve the shifting of device parameters over dose (time), self-test startup routines can detect when an imager is reaching its end of life and alert users that a replacement is required.

In the medical environment, there is an increasing use of ionizing radiation to sterilize surgical instruments and implantable devices that would otherwise be damaged by the high temperature and humidity of autoclave sterilization.<sup>[50-52]</sup> Sterilization by irradiation with e-beams, X-rays and gamma rays works because the radiation has sufficient energy to ionize atoms. Ionization directly damages DNA and creates reactive free radicals. One major free radical forms when the ionizing radiation breaks the covalent bond between two oxygen atoms in an oxygen molecule (O<sub>2</sub>). The two oxygen-free radicals are energetically predisposed to find an additional electron, causing them to become highly reactive. The free radicals cause additional damage to the cell and further degrade its DNA.

Figure 1-23 shows the DNA of the cell’s control and reproduction mechanism being affected by radiation. With a sufficient dose, enough damage accumulates such that the cell no longer functions properly, cannot reproduce and ultimately dies.

![Microscopic image showing various bacteria and viruses, illustrating the effect of sterilization radiation.](a538e783a7a6643b5a333e04fe07615d_img.jpg)

Microscopic image showing various bacteria and viruses, illustrating the effect of sterilization radiation.

**Figure 1-23. Sterilization of bacteria and viruses is possible by using high doses of ionizing radiation that irrevocably damage their DNA/RNA such that the cells can no longer function or reproduce and ultimately die off.**

Studies on inactivating viruses and bacteria by ionizing radiation indicate that a single exposure is sufficient to sterilize a sample, provided that the dose is high enough. Because no patient is involved and the bacteria and viruses must be neutralized to a very high degree (usually to  $10^{-6}$  or better), sterilization using radiation is performed at extreme dose levels – a maximum dose considered to fully sterilize a sample is ~50 kGy (5 Mrad). This type of dose actually exceeds most defense and space application requirements and thus poses a real challenge for any microelectronics located in a piece of equipment that must be sterilized. However, most electronics in devices being sterilized will be powered down during irradiation, which can significantly reduce the amount of charge trapped and somewhat lessen the effective dose.

The medical radiation environment is primarily limited to X-ray, gamma-ray or e-beam exposures. Proton-beam therapy is also used for cancer treatments, but these are characterized by highly focused, targeted exposures that deliberately steer clear of implanted electronics. It is unlikely that medical microelectronics implanted in a patient would suffer permanent dose-related damage because the irradiation is limited by dose allowances that patients can tolerate (very low dose levels). Even microelectronics inside X-ray machines or other devices that produce ionizing radiation are usually shielded to keep the dose to a manageable level.

Electronics that must be in a radiation beam (like imagers) constitute the primary exception. They will eventually accumulate enough doses that they may need to be replaced occasionally. The radiation doses encountered in medical sterilization applications are also extremely challenging, and most microelectronics will not be able to tolerate these dose levels without being shielded or radiation-hardened. TID effects are the primary concern for microelectronics used in medical instrumentation or implantable devices sterilized with ionizing radiation.

#### Industrial radiation environments

Industrial applications use radiation extensively: in the processing of materials to induce chemical/physical changes, in the sterilization of food and waste, for the inspection and monitoring of physical properties of materials, for the mitigation of static in assembly processes, in the defect inspection of manufactured components, and in security screening applications.<sup>[53-58]</sup> Some examples of industrial radiation applications are shown in [Figure 1-24](#).

Radiation sources for industrial applications include many types and geometries of sealed sources containing radioactive materials that emit radiation continuously and machines that produce radiation by accelerating particles (e-beam and X-ray machines). The sealed sources are usually encapsulated in metal shields, with a shuttered port or window that allows the radiation out. Sealed gamma-ray sources most commonly use cobalt-60 (half-life ~5.2 years) and have an advantage in that they do not require external power to generate radiation.

The spontaneous fission of Californium-252 or sources that combine a source of alpha particles with light (low- $z$ ) metals such as lithium or beryllium will emit neutrons (for example, plutonium-beryllium, americium-beryllium, americium-lithium) when bombarded by alpha particles.

![A person viewing an X-ray image of a bag's contents on a computer monitor.](67af94a7c462e85f3a310c9a45c0980d_img.jpg)

A person is seen from the back, looking at a computer monitor. The monitor displays an X-ray image of a bag, showing internal structures and a security line. The person is wearing a dark jacket.

A person viewing an X-ray image of a bag's contents on a computer monitor.

![A portable X-ray machine scanning a large pipe for defects.](0adfe2c1a73ed4d130777d83dd16321d_img.jpg)

A portable X-ray machine, which is blue and black, is positioned on a wooden stand. It is scanning a large, dark, cylindrical pipe that is lying on the ground. The background shows a dirt embankment and some power lines in the distance.

A portable X-ray machine scanning a large pipe for defects.

**Figure 1-24.** X-ray image of the contents of a bag in an airport security line (top); a portable X-ray machine to scan for pipe defects (bottom).

The main issue with many sealed source applications is that the source intensity decays with time, because the source isotope produces the radiation as a byproduct of the natural decay. Dose-rate correction is necessary on a regular basis, with the time interval defined by the half-life of the isotope. Other issues with sealed sources include the potential for contamination – the release of the radioactive material into the environment if the seal is breached – and ultimately their disposal when the radiation intensity has decayed below a useful flux, even though the source is still radioactive.

Accelerators and other powered devices energize charged particles such as ions (most commonly protons) or electrons by using very high accelerating voltages to give these particles a high kinetic energy. At this point, they are used directly as a radiation source or directed onto a target material converting the incident radiation into secondary radiation.

Accelerated protons incident on metal targets generate neutrons, while accelerated electrons on metal targets produce X-rays. Accelerators require lots of energy to produce radiation, so they tend to be large and in-place installations. Unlike sealed sources, accelerators do not pose a portable contamination risk.

Particle beams, however, especially ion and neutron beams, induce nuclear reactions within any materials in the beam, potentially making them radioactive. For lighter materials, the degree of activation is usually not a concern, as the amount of radiation produced is short-lived, but some heavier elements that can have longer-lived radioactivity require caution. The activation produces gamma-ray radiation, as the unstable isotopes created by the nuclear reactions in the target material decay to stable ones.

Microelectronics are present in most industrial applications, either as an integral part of the equipment producing the radiation or embedded in equipment being irradiated. In places where operators or other personnel are present, the radiation sources must be well-shielded and controlled such that radiation emission and contamination is either eliminated or constrained to levels deemed safe for humans. Microelectronics in these types of areas are usually not at risk. Additionally, microelectronics inside accelerators (e-beams and proton beams), X-ray machines or sealed sources that produce ionizing radiation are generally heavily shielded to keep dose exposures low. The doses encountered in industrial applications are extremely well-controlled.

There are two exceptions where dose exposure can accumulate to levels that will damage or destroy microelectronics:

- In industrial applications, where the microelectronics are part of the imaging or detection systems and must be in the radiation field during operation. This applies to X-ray imagers as well as radiation, liquid-level and other detectors used in nuclear power plants.
- In processing/sterilization applications, where the electronics will be irradiated and will accumulate dose; for example, in electronic radio-frequency identification (RFID) tags used to label foods and drugs.

Nuclear fission reactors operated by the power industry to produce electricity also create high radiation areas rich in neutrons and gamma rays from both the reactor vessel and spent fuel in the storage pools. All power plants – whether nuclear-, coal-, oil- or gas- driven – boil water to produce steam that activates turbines, which in turn produce electricity. In nuclear reactors, the process of nuclear fission produces the heat needed to obtain steam.

Most reactors are based on isotopes of uranium ( $^{238}\text{U}$  and  $^{235}\text{U}$ ) that have a high-fission cross-section.<sup>[59]</sup> Fission or splitting of the uranium nucleus can occur spontaneously, albeit at a very low rate, or if it is exposed to neutrons. The absorption of an extra neutron renders the uranium nucleus much less stable. The excess energy of the uranium nucleus is released when it splits into two energetic fission fragments, emitting additional neutrons and gamma rays. This is a key point, because fission of the nucleus without the production of additional neutrons would not allow subsequent fissions to occur. So uranium nuclei fissions release neutrons that feed follow-on fission reactions such that the process can be self-sustaining, usually referred to as a controlled chain reaction. The uranium fuel consists of small pellets assembled into long fuel rods placed in the main reactor vessel in vertical bundles, as illustrated in [Figures 1-25 and 1-26](#).

Interspersed between the array of uranium fuel bundles are rods of neutron absorbers. They consist of elements that are capable of absorbing many neutrons without themselves undergoing fission. These control rods slow down or speed up the rate of fission

![Figure 1-25: Nuclear reaction core cross-section diagram. The diagram shows a vertical cross-section of a reactor core. At the top, a 'Control rod (Neutron catchers)' is shown with a downward arrow. Below it, 'Hot coolant' is indicated with a pink arrow pointing left. The central region contains 'Nuclear fuel' rods (colored red, orange, and yellow) and a 'Moderator' (colored green). At the bottom, a 'Radiation protection barrier' is shown. 'Cold coolant' is indicated with a blue arrow pointing right, returning to the bottom of the fuel assembly.](1fd4fda95d22e337df091dfa8fa80f90_img.jpg)

Figure 1-25: Nuclear reaction core cross-section diagram. The diagram shows a vertical cross-section of a reactor core. At the top, a 'Control rod (Neutron catchers)' is shown with a downward arrow. Below it, 'Hot coolant' is indicated with a pink arrow pointing left. The central region contains 'Nuclear fuel' rods (colored red, orange, and yellow) and a 'Moderator' (colored green). At the bottom, a 'Radiation protection barrier' is shown. 'Cold coolant' is indicated with a blue arrow pointing right, returning to the bottom of the fuel assembly.

**Figure 1-25. Nuclear reaction core cross-section.**

reactions by modifying the number of neutrons available to drive the fission process. By adjusting the height of the control rods within the reactor vessel, the fission rate adjusts, as does the rate of steam production and ultimately the power output of the reactor.

The heat energy is actually derived from the kinetic energy of the fission fragments created during the reaction. The entire fuel assembly is submersed in a deep pool of water. The water itself absorbs some neutrons, but its main purpose is to keep the core below melting temperatures while converting the waste heat by turning water into steam, which in turn drives a turbine and generator to create electricity. While uranium fuel is used in the reactor, it gradually accumulates fission products – transuranic elements (the production of nonfissile isotopes by neutron absorption) that cause an increase in the neutron absorption of the reactor components. The control rods can be adjusted to compensate, but after several years, the increasing neutron absorption, along with the structural changes

![Figure 1-26: Photograph of a nuclear reactor core in operation. The image shows a large, circular reactor vessel filled with water. Numerous vertical fuel rods are visible, and a bright blue glow (Cherenkov radiation) is visible throughout the water, indicating high-speed charged particles passing through it.](a251a846ffb8c1750262be87b489eeec_img.jpg)

Figure 1-26: Photograph of a nuclear reactor core in operation. The image shows a large, circular reactor vessel filled with water. Numerous vertical fuel rods are visible, and a bright blue glow (Cherenkov radiation) is visible throughout the water, indicating high-speed charged particles passing through it.

**Figure 1-26. Photograph of a nuclear reactor core in operation. The blue color is Cherenkov radiation given off as charged particles pass through the water at speeds greater than the speed of light in water, an effect analogous to the sonic boom produced by aircraft traveling faster than the speed of sound in air.**

in the fuel rods and assemblies induced by displacement damage, requires replacing the spent fuel rods. The fuel assemblies are removed and stored in spent fuel pools and replaced with fresh fuel rods. Approximately half of the fissile material remains, and thus the rods are still highly radioactive.

The radiation environment in a nuclear reactor comes from two sources:

- The fission reaction itself bathing the reactor vessel area with a high flux of gamma rays and neutrons.
- The alpha, beta and gamma radiations emitted from the products of fission; the primary radiation, unstable fission fragments and radioactive isotopes created by transmutation in fuel; and reactor vessel materials from the high neutron flux.

The primary areas in the nuclear facilities are the reactor and the spent fuel containment area, as illustrated in **Figures 1-27 and 1-28**. Both areas use a large volume of water to shield neutrons and to some extent gamma rays emitted from the core and the spent fuel assemblies (alphas and betas do not have enough energy to escape the pool). In addition, thick concrete and metal shields help keep operators safe.

![Figure 1-27: Diagram of a typical nuclear reactor system. The diagram shows a 'Containment structure' housing a 'Control' rod and a 'Water pump'. A primary loop of water circulates from the pump to a 'Steam generator' and back. The steam generator heats a secondary loop of water, which turns a 'Turbine' connected to an 'Electric generator'. The turbine drives the water pump. The secondary loop's water then goes to a 'Condenser' which is cooled by a 'Cooling tower' (labeled 'Cooling tower' with a large plume of steam). The condenser's output returns to the steam generator. A 'Spent fuel pool' is also shown, containing fuel rods and connected to the primary loop. A power transmission tower is shown receiving power from the electric generator.](a3472689858b068ef469213682965325_img.jpg)

Figure 1-27: Diagram of a typical nuclear reactor system. The diagram shows a 'Containment structure' housing a 'Control' rod and a 'Water pump'. A primary loop of water circulates from the pump to a 'Steam generator' and back. The steam generator heats a secondary loop of water, which turns a 'Turbine' connected to an 'Electric generator'. The turbine drives the water pump. The secondary loop's water then goes to a 'Condenser' which is cooled by a 'Cooling tower' (labeled 'Cooling tower' with a large plume of steam). The condenser's output returns to the steam generator. A 'Spent fuel pool' is also shown, containing fuel rods and connected to the primary loop. A power transmission tower is shown receiving power from the electric generator.

**Figure 1-27. Diagram of the different areas in a typical nuclear reactor.** High radiation areas include the reactor vessel where the controlled fission occurs and the handling pool where spent fuel rods are kept. The water creates steam to turn turbines (generating electrical power) and acts as a coolant and radiation shield.

![Figure 1-28: A photograph of a spent fuel rods storage pool. The pool is filled with water and contains many spent fuel rods. A bright blue glow is visible in the water, which is due to Cherenkov radiation. The pool is surrounded by a concrete structure with various pipes and equipment.](6b29ab7e77b37eb167c955b26206c169_img.jpg)

Figure 1-28: A photograph of a spent fuel rods storage pool. The pool is filled with water and contains many spent fuel rods. A bright blue glow is visible in the water, which is due to Cherenkov radiation. The pool is surrounded by a concrete structure with various pipes and equipment.

**Figure 1-28. A spent fuel rods storage pool filled with water. Because the spent fuel is radioactive, the blue glow is due to Cherenkov radiation, just as in the reactor core.**

Image courtesy of the Nuclear Regulatory Commission

Microelectronics used in detection and monitoring equipment that is installed or sent into the high radiation areas of nuclear reactors will also be exposed to high doses of gamma rays and neutrons.<sup>[60]</sup> For these applications, TID effects are the primary concern. In high-dose applications where the electronics cannot be shielded, specifically designed radiation-hardened devices are necessary. The combination of proximity to high-radiation fluxes and the long lifetime requirement (years) implies the need for a high level (Mrads) of TID robustness.

One critical application in nuclear reactors is the monitoring of water levels in the pools that house the active reactor vessel and spent fuel rods, because a loss of water in either of these areas could expose workers to critical radiation levels and lead to a meltdown of both operating and spent fuel rods. Based on issues that occurred following the tsunami damage to the Fukushima power plant in 2011, the U.S. Nuclear Regulatory Commission issued an order directing U.S. facilities to install fail-safe and redundant water-level monitoring instrumentation in each pool.<sup>[61, 62]</sup>

In general, the industrial-radiation environment includes X-ray, gamma-ray, e-beam or neutron exposures. TID effects are the primary concern for microelectronics used in industrial radiation environments. Most inspection applications use X-rays, and the doses are fairly limited such that under regular circumstances, most microelectronics will not be affected.

Similarly, for most electronics inside the sealed source or accelerator equipment that produces ionizing radiation, shielding keeps the doses to a manageable level. Microelectronics that must operate in a radiation beam or field (like imagers, dosimeters, etc.) or in high-radiation areas (like detectors and gauges in nuclear power plants) pose a challenge. In such industrial applications, electronics will not be able to tolerate the high accumulated dose levels unless they are radiation-hardened. In many cases, even with robust design, certain applications will ultimately accumulate enough dose that the electronics will need to be periodically replaced to ensure that the end equipment operates reliably.

### Defense radiation environments

In addition to the reactor environment in nuclear power plants installed in some navy vessels, the primary defense radiation environment is created during and after the detonation of a nuclear weapon. The physical consequences of detonating a fission or fusion weapon include blast, thermal, ionizing radiation and residual radiation effects. The level of destruction is defined by the total energy released by the weapon (this is based on the specific design and the reaction mass of the weapon) and the environment in which it detonates. Many of the physical damage effects of a nuclear weapon detonation are similar to those of conventional explosives, but the fission/fusion processes release millions of times more energy per reaction mass.

Nuclear weapons can be detonated on the ground, in air, underground, underwater or in space, all with differing effects. The volume of material around the detonation (usually air) is filled with intense radiation, raising temperatures to tens of millions of degrees. The vaporized material forms a fireball (~1 km in diameter for a 1-megaton device) of incredibly high-temperature plasma, which in turn creates a high-pressure shockwave. For detonations in air, **Figure 1-29** shows that at least half of the weapon's energy is converted into the physical blast.

![Figure 1-29: Pie chart showing the output energy partitioning for a nuclear weapon. The chart is divided into five segments: Blast (50%, red), Thermal radiation (35%, teal), Residual radiation (fallout) (10%, light blue), Initial radiation (gamma-rays, neutrons) (5%, dark grey), and Prompt (5%, black).](60e9207be66a64332619bb4b667fe67b_img.jpg)

| Category                                 | Percentage |
|------------------------------------------|------------|
| Blast                                    | 50%        |
| Thermal radiation                        | 35%        |
| Residual radiation (fallout)             | 10%        |
| Initial radiation (gamma-rays, neutrons) | 5%         |
| Prompt                                   | 5%         |

Figure 1-29: Pie chart showing the output energy partitioning for a nuclear weapon. The chart is divided into five segments: Blast (50%, red), Thermal radiation (35%, teal), Residual radiation (fallout) (10%, light blue), Initial radiation (gamma-rays, neutrons) (5%, dark grey), and Prompt (5%, black).

Figure 1-29. Output energy partitioning for a nuclear weapon.  
Image courtesy of Department of Defense

Two concurrent mechanisms cause blast damage: damage from the drastic increase in air pressure exerted by the shockwave and additional damage caused by the high-velocity winds created by dynamic pressure changes in the wake of the shockwave. The shockwave creates overpressures capable of destroying concrete walls and collapsing buildings (~5-10 psi), and the dynamic pressure variations cause wind speeds in excess of 1,000 km/hr. The range of shockwave and wind effects capable of destroying concrete structures is 5 to 7 km from the detonation of a 1-megaton device. Another 30-40% of a nuclear weapon's energy is converted into thermal radiation (including visible and ultraviolet radiation), which causes localized heating and can ignite combustible materials at significant distances from the detonation (for example, thermal radiation from a 1-megaton explosion will have a range of ~10 km).

Concurrent with the thermal radiation, ~5% of the detonation energy is emitted as an intense burst of initial radiation comprising X-rays, gamma rays and neutrons. Since the gamma rays and neutrons can travel great distances through the air in a general direction away from the detonation point, they are the primary radiation threat to sensitive microelectronics.

Figure 1-30 shows the energy-rate output as a function of time after a nuclear detonation. The peak prompt-gamma dose occurs rapidly, in this case within tens of nanoseconds. Obviously, the timescale is a function of the distance between the detector and the point of detonation – the further away the detector, the more expanded the timescale. The magnitude of the gamma-energy rate increases with increasing kilotonnage. The emitted gamma rays expand from the detonation point at the speed of light, while the neutrons travel outward more slowly. Most of the neutrons released by the fission process will be fast neutrons with a peak kinetic energy of 12-14 MeV, corresponding to a velocity that is ~15% the speed of light.

The radiation emission from a detonation follows the inverse-square law, so the gamma-ray and neutron flux will drop with the square of the distance; in other words, a target that is twice as far away as another target will receive only a quarter of the radiation of the closer target. About 10% to 15% of the blast energy is in the form of residual radiation and consists of radioactive fission products and secondary

neutron-activated products that “fall out” of the upper atmosphere hours, days and weeks after the explosion. For surface or low-air burst nuclear detonations, residual radiation comes from two sources:

- Some of the neutrons emitted as initial radiation react with metals in the soil and become radioactive isotopes. The induced radiation is generally created in a circular area centered at the detonation point. The intensity decreases over time, as the newly formed radioisotope decays to safe levels within about a week.
- The radioactive dust (or fallout) falls out of the sky hours, days and weeks after a nuclear explosion. Fallout consists of a combination of radioactive materials, including carbon-14 created by neutrons, radioactive fission fragments (spent nuclear material), unspent fissile material and weapons-casing materials activated by neutrons. The various radioactive species have different decay half-lives.

![Figure 1-30: Log-log plot of Gamma-ray energy output rate per kiloton as a function of time after detonation. The y-axis is Energy rate (mev/sec/kt) from 10^18 to 10^30. The x-axis is Time (sec) from 10^-8 to 10. The solid line represents the high-altitude airburst, and the dotted line represents the airburst. Key features include: Prompt (peak at ~10^-7 sec), Inelastic scattering of neutrons by nuclei of air atoms, Isomeric decays, Neutron capture in nitrogen, and Fission product.](c7c1a2a04d07232ca372d3ea08fb19fc_img.jpg)

Figure 1-30: Log-log plot of Gamma-ray energy output rate per kiloton as a function of time after detonation. The y-axis is Energy rate (mev/sec/kt) from 10^18 to 10^30. The x-axis is Time (sec) from 10^-8 to 10. The solid line represents the high-altitude airburst, and the dotted line represents the airburst. Key features include: Prompt (peak at ~10^-7 sec), Inelastic scattering of neutrons by nuclei of air atoms, Isomeric decays, Neutron capture in nitrogen, and Fission product.

Figure 1-30. Gamma-ray energy output rate per kiloton as a function of time after detonation for an airburst (solid line) and high-altitude airburst (dotted line).<sup>[63]</sup> Image courtesy of Department of Defense.

The intense radiation emission during a nuclear detonation interacts with the Earth's atmosphere, ionosphere and magnetic field to produce a secondary radiation effect called the EMP. As opposed to direct radiation effects by neutron and gamma irradiation suffered by microelectronics within a few kilometers of a nuclear weapon detonation, the EMP manifests as spurious currents in conductors and overvoltage transients (electrical effects only), but over a range of hundreds and even thousands of kilometers.

Figure 1-31 shows a diagram of an EMP generated by a high-altitude (400-km) detonation, which is represented by the black dot on the map. The initial radiation absorbed by the air creates a large region of highly ionized gas: the excited electrons spiral in the geomagnetic field, which produces a very high pulse of electromagnetic energy to be radiated to ground level.

![Diagram illustrating the ionized electrons from a nuclear detonation being deflected by Earth's magnetic field, radiating EMP over a large area. The top part shows a spiraling electron, a magnetic field line, a gamma ray, and a burst. The bottom part shows a map of the United States with concentric circles representing the radius of the EMP effect, ranging from 20 km to 40 km. A legend indicates the intensity of the EMP in V/m: 5,000, 12,500, 25,000, 37,500, 50,000, and 25,000.](0f79a59f3766fc341ff688a23692c1d9_img.jpg)

The diagram illustrates the process of an EMP event. The top portion shows a 'Spiraling electron' moving along a 'Magnetic field line', which results in a 'Gamma ray' and a 'Burst'. Distances of 20 km and 40 km are marked. The bottom portion is a map of the United States with concentric circles representing the radius of the EMP effect. A legend on the right indicates the intensity of the EMP in V/m: 5,000, 12,500, 25,000, 37,500, 50,000, and 25,000.

Diagram illustrating the ionized electrons from a nuclear detonation being deflected by Earth's magnetic field, radiating EMP over a large area. The top part shows a spiraling electron, a magnetic field line, a gamma ray, and a burst. The bottom part shows a map of the United States with concentric circles representing the radius of the EMP effect, ranging from 20 km to 40 km. A legend indicates the intensity of the EMP in V/m: 5,000, 12,500, 25,000, 37,500, 50,000, and 25,000.

**Figure 1-31. Ionized electrons from the initial radiation from a 400-km-high nuclear detonation that are deflected sideways and in spirals by the Earth's magnetic field, radiating EMP over a large area.** <sup>[64]</sup>  
Image courtesy of Department of Defense

This transient burst of electromagnetic energy couples to the power grid via long transmission lines, damaging or destroying power infrastructures and control electronics. The EMP has three phases that occur over different timescales, with differing effects:

- The first phase, characterized by a narrow electromagnetic spike, is caused when oxygen and nitrogen atoms in the atmosphere absorb a large fraction of the gamma rays and are consequently ionized. This effect is maximized in high-altitude detonations: the excess electronic charge spirals in the geomagnetic field, radiating electromagnetic radiation over a large region. This radiated electromagnetic field produces high currents and overvoltages that can destroy transformers, breakdown junctions and insulators. The transient peaks within a few nanoseconds and dissipates within  $<1 \mu\text{s}$ .

- The second phase of the EMP is produced by scattered gamma rays and those produced during reactions between nuclei in the air and neutrons emitted by the detonation. This phase starts after the dissipation of the first transient and lasts approximately 1 s after the detonation, producing effects similar to lightning strikes. While many electronics and power systems are designed to handle lightning strikes, the first transient can degrade or destroy the protection circuits, thus allowing additional damage from this second phase.
- The last phase of the EMP event manifests in a relatively slow pulse lasting from seconds to minutes. The radiation emitted during a nuclear detonation causes a large ionization disturbance in the upper atmosphere, ionosphere and magnetosphere, similar to that caused by solar flares and CMEs. The ionization temporarily distorts the Earth's magnetic field, producing geomagnetic transients that couple to and create current transients in long power distribution lines, temporarily overloading or permanently burning out transformers in the power grid.

The gamma-ray and neutron radiation emitted by a nuclear detonation and the subsequent EMP are the primary concerns for microelectronics outside the blast damage zone. Both dose-rate (prompt-dose or prompt-gamma) and dose effects are a concern for microelectronics operating in a nuclear detonation environment. EMP is not a direct particle-radiation effect but a coupled electromagnetic disturbance, usually manifesting in microelectronics as high transient overvoltages on the inputs or power rails.

### References

- 1 E. G. Stassinopoulos and J. P. Raymond, "The space radiation environment for electronics," *Proc. of the IEEE* 76(11), Nov. 1988, pp. 1423-1442.
- 2 J. L. Barth, C. S. Dyer and E. G. Stassinopoulos, "Space, atmospheric and terrestrial radiation environments," *IEEE Trans. Nuclear Sci.*, 50(3), 2003, pp. 466-482.
- 3 H. C. Koons and J. F. Fennell, "Space weather effects on communications satellites," *URSI Radio Science Bulletin*, 2006 (316), pp. 27-41.
- 4 <https://earthobservatory.nasa.gov/Features/OrbitsCatalog/>
- 5 <http://planetfacts.org/heliopause/>
- 6 W. Bietenholz, "Cosmic Rays and the Search for a Lorentz Invariance Violation," *Physics Report* 505, 2011, pp. 145-185. doi: arXiv:0806.3713 [hep-ph] DESY-08-072.
- 7 D. L. Chenette and W. F. Dietrich, "The Solar Flare Heavy Ion Environment for Single-Event Upsets: A Summary of Observations over the Last Solar Cycle, 1973-1983," *IEEE Trans. Nuclear Sci.* 31(6), Dec. 1984, pp. 1217-1222.
- 8 J. H. Adams and A. Gelman, "The Effects of Solar Flares on Single Event Upset Rates," *IEEE Trans. Nuclear Sci.* 31(6), Dec. 1984, pp. 1212-1216.
- 9 M. S. Gussenhoven, D. H. Brautigam and E. G. Mullen, "Characterizing solar flare high energy particles in near-Earth orbits," *IEEE Trans. Nuclear Sci.*, 35(6), Dec. 1988, pp. 1412-1419.
- 10 <https://solarscience.msfc.nasa.gov>
- 11 <https://hesperia.gsfc.nasa.gov/sftheory/flare.htm>
- 12 S. Bowler, "Record-breaking solar flares," *Astronomy & Geophysics* 44(6), June 2003, pp. 6.4-6.4.
- 13 S. P. Plunkett and S. T. Wu, "Coronal mass ejections (CMEs) and their geoeffectiveness," *IEEE Trans. Plasma Sci.* 28(6), June 2000, pp. 1807-1817.
- 14 E. G. Stassinopoulos, "World Maps of Constant B, L and Flux Contours," NASA SP-3054, Office of Technology Utilization, NASA, Washington, D.C., 1970.
- 15 G. P. Ginot, D. Madden, B. K. Dichter and D. H. Brautigam, "Energetic Proton Maps for the South Atlantic Anomaly," *IEEE Rad. Effects Data Workshop*, Dec. 2007, pp. 1-8.
- 16 <https://image.gsfc.nasa.gov/poetry/ask/q525.html>
- 17 T. C. May and M. H. Woods, "A New Physical Mechanism for Soft Error in Dynamic Memories," *Proc. 16th Annual International Reliability Physics Symp. (IRPS)*, 1978, pp. 33-40.
- 18 J. T. Nelson, L. L. Vanskike and D. S. Yaney, "Alpha particle tracks in silicon and their effect on dynamic MOS RAM reliability," *IEEE International Electron Dev. Meeting (IEDM)* 24, 1978, pp. 693-693.
- 19 Output from RadSim alpha-particle transport code, Texas Instruments, 1989-2012.
- 20 R. C. Baumann, "Effectiveness of Polyimide for Stopping of Alphas in Memory Development," Texas Instruments Technical Report, Sept. 1991, pp. 1-37.
- 21 Z. Hasnain and A. Ditali, "Building-in reliability: soft errors – a case study," *Proc. 30th Annual International Reliability Physics Symp. (IRPS)*, 1992, pp. 276-280.
- 22 R. C. Baumann and T. Z. Hossain, "Investigation of U and Th in 16 Mb DRAM Metals by NAA," *Texas Instruments Technical Report*, May 1991, pp. 1-20.
- 23 M. W. Roberson, "Soft error rates in solder bumped packaging," *Proc. 4th International Symp. Advanced Packaging Materials Processes, Properties and Interfaces* (Cat. No. 98EX153), 1998, pp. 111-116.
- 24 W. K. Warburton, B. Dwyer-McNally, M. Momayezi and J. E. Wahl, "Ultra-low background alpha particle counter using pulse shape analysis," *IEEE Symp. Conf. Record Nuclear Sci* 1, 2004, pp. 577-581.
- 25 R. C. Baumann, "Effectiveness of Polyimide for Stopping of Alphas in Memory Development," Texas Instruments Technical Report, Sept. 1991, pp. 1-24.
- 26 J. F. Ziegler and W. A. Lanford, "The Effect of Sea Level Cosmic Rays on Electronic Devices," *J. Appl. Phys.* 52, 1981, pp. 4305-4318.
- 27 J. F. Ziegler, "Terrestrial cosmic ray intensities," *IBM J. Res. Develop.* 42(1), 1998, pp. 117-139.
- 28 P. Goldhagen, "Cosmic-Ray Neutrons on the Ground and in the Atmosphere," *Mater. Res. Soc. Bulletin* 28, Feb. 2003, pp. 131-135.
- 29 E. Normand, "Single Event Effects in Avionics," *IEEE Trans. Nuclear Sci.* 43(2), April 1996, pp. 461-474.
- 30 F. Wrobel, J. M. Palau, M. C. Calvet, O. Bersillon and H. Duarte, "Incidence of multi-particle events on soft error rates caused by n-Si nuclear reactions," *IEEE Trans. Nuclear Sci.* 47(6), Dec. 2000, pp. 2580-2585.
- 31 F. Wrobel, J. M. Palau, M. C. Calvet and P. Iacconi, "Contribution of SiO<sub>2</sub> in neutron-induced SEU in SRAMs," *IEEE Trans. Nuclear Sci.* 50(6), Dec. 2003, pp. 2055-2059.
- 32 Measurement and Reporting of Alpha Particle and Terrestrial Cosmic Ray-Induced Soft Errors in Semiconductor Devices, JESD89A, Oct. 2006, JEDEC test standard.
- 33 J. F. Ziegler, "The effect of concrete shielding on cosmic ray induced soft fails in electronic systems," *IEEE Trans. Electron Dev.* 28(5), May 1981, pp. 560-565.
- 34 S. H. Jiang et al., "A study on natural background neutron dose," *IEEE Trans. Nuclear Sci.* 41(4), Aug. 1994, pp. 993-998.
- 35 R. Fleischer, "Cosmic ray interactions with boron: a possible source of soft errors," *IEEE Trans. Nuclear Sci.* 30(5), Oct. 1983, pp. 4013-4015.
- 36 R. C. Baumann, T. Z. Hossain, S. Murata, and H. Kitagawa, "Boron Compounds as a Dominant Source of Alpha Particles in Semiconductor Devices," *Proc. 33rd Annual International Reliability Physics Symp. (IRPS)*, 1995, pp. 297-302.

- 37 R. C. Baumann and E. B. Smith, "Neutron-Induced Boron Fission as a Major Source of Soft Errors in Deep Submicron SRAM Devices," *Proc. 38th Annual International Reliability Physics Symp. (IRPS)*, 2000, pp. 152-157.
- 38 J. D. Dirk, M. E. Nelson, J. F. Ziegler, A. Thompson and T. H. Zabel, "Terrestrial thermal neutrons," *IEEE Trans. Nucl. Sci.* 50(6), Dec. 2003, pp. 2060-2064.
- 39 M. S. Gordon, P. Goldhagen, K. P. Rodbell, T. H. Zabel, H. H. K. Tang, J. M. Clem and P. Bailey, "Measurement of the flux and energy spectrum of cosmic-ray induced neutrons on the ground," *IEEE Trans. Nucl. Sci.* 51(6), Dec. 2004, pp. 3427-3434.
- 43 S. M. Sze, VLSI Technology, New York, McGraw Hill, 1983, pp. 113-125.
- 41 E. Normand, K. Vranish, A. Sheets, M. Stitt and R. Kim, "Quantifying the double-sided neutron SEU threat, from low energy (thermal) and high energy (>10 MeV) neutrons" *IEEE Trans. Nucl. Sci.* 53(6), Dec. 2006, pp. 3587-3595.
- 42 S. J. Wen, S. Y. Pai, R. Wong, M. Romain and N. Tam, "B10 findings and correlation to thermal neutron soft error rate sensitivity for SRAMs in the sub-micron technology," *Proc. IEEE International Integrated Reliability Workshop (IIRW)*, 2010, pp. 31-33.
- 43 M. Olmos, R. Gaillard, A. Van Overberghe, J. Beaucour, S. Wen and S. Chung, "Investigation of thermal neutron induced soft error rates in commercial SRAMs with 0.35  $\mu\text{m}$  to 90 nm technologies," *Proc. IEEE Int. Reliab. Phys. Symp.*, 2006, pp. 212-216.
- 44 Simulated output from [Stopping and Range of Ions in Matter \(SRIM\)](#) 2013 software, downloaded at [www.srim.org](http://www.srim.org).
- 45 "Computed Tomography (CT)," <https://www.nibib.nih.gov/science-education/science-topics/computed-tomography-ct>.
- 46 "Radiation Dose in X-Ray and CT Exams," <https://www.radiologyinfo.org/en/info.cfm?pg=safety-xray>.
- 47 M. Esposito, T. Anaxagoras, O. Diaz, K. Wells and N. M. Allinson, "Radiation hardness of a large area CMOS active pixel sensor for bio-medical applications," *IEEE Nuclear Sci. Symp. and Medical Imaging Conf. Record (NSS/MIC)*, 2012, pp. 1300-1304.
- 48 A. C. Konstantinidis et al., "Evaluation of a novel wafer-scale CMOS APS X-ray detector for use in mammography" *IEEE Nuclear Sci. Symp. and Medical Imaging Conf. Record (NSS/MIC)*, 2012, pp. 3254-3260.
- 49 V. Goiffon, C. Virmontois, P. Magnan, S. Girard and P. Paillet, "Analysis of Total Dose-Induced Dark Current in CMOS Image Sensors from Interface State and Trapped Charge Density Measurements," *IEEE Trans. Nuclear Sci.* 57(6), Dec. 2010, pp. 3087-3094.
- 50 M. A. Moore, "Inactivation of enveloped and non-enveloped viruses on seeded human tissues by gamma irradiation," *Cell and Tissue Banking* 13 (3), Aug. 2012, pp. 401-407.
- 51 T. S. Dunn and J. L. Williams, "Comparison of Cobalt-60 and Electron Accelerators for Radiation Sterilization," *IEEE Trans. Nuclear Sci.* 26 (1), Feb. 1979, pp. 1776 -1783.
- 52 R. A. Potyrailo et al., "Passive gamma-resistant RFID tags integrated into gamma-sterilizable pharmaceutical components," *IEEE Proc. International Conf. RFID*, 2010, pp. 110-117.
- 53 Y. Wang, B. Li, L. Chen and Z. Jiang, "Region segmentation based radiographic detection of defects for gas turbine blades," *IEEE International Conf. Mechatronics and Automation (ICMA)*, 2015, pp. 1681-1685.
- 54 R. Huang, A. Sorini and J. McNulty, "Quantitative solder inspection with computed tomography," *IEEE Symp. Product Compliance Engineering (ISPCe)*, 2014, pp. 82-85.
- 55 Y. Chen, N. Lin and P. Lai, "Three-dimensional X-ray laminography as a tool for detection and characterization of package on package (PoP) defects," *10th International Conf. Reliability, Maintainability and Safety (ICRIMS)*, 2014, pp. 275-278.
- 56 M. Firsching et al., "3-D scanning of sea freight containers using MeV X-rays," *IEEE Nuclear Sci. Symp. and Medical Imaging Conf. Record (NSS/MIC)*, 2013, pp. 1-5.
- 57 K. Alfonso, M. Elsalim, M. King, D. Strellis and T. Gozani, "MCNP Simulation Benchmarks for a Portable Inspection System for Narcotics, Explosives and Nuclear Material Detection," *IEEE Trans. Nuclear Sci.* 60(2), April 2013, pp. 520-527.
- 58 H. Bomsdorf, T. Klostermann, F. Scherwinski, and J. Stein, "Detector pulse shape analysis for X-ray scatter based baggage inspection systems," *IEEE Nuclear Sci. Symp. and Medical Imaging Conf. Record (NSS/MIC)*, 2007, pp. 1125-1129.
- 59 K. S. Krane, *Introductory Nuclear Physics*, New York, New York: John Wiley & Sons, 1988, pp. 501-516.
- 60 D. J. Fitzgerald and E. H. Snow, "Comparison of surface and bulk effects of nuclear reactor radiation on planar devices," *IEEE Trans. Elec. Dev.* 15(3), March 1968, pp. 160-163.
- 61 S. Rizzolo, J. Périssé, A. Boukenter, Y. Ouerdane, E. Marin et al., "Real time monitoring of water level and temperature in storage fuel pools through optical fibre sensors," *Scientific Reports*, published online Aug. 18, 2017, pp. 1-10. doi: 10.1038/s41598-017-08853-7
- 62 A. Giraud and J. Veau, "Full Autonomous Monitoring Tools Inside Nuclear Reactor Building," *IEEE Trans. Nuclear Sci.* 57(5), Oct. 2010, pp. 2662-2669.
- 63 "Test Operations Procedure (TOP): 1-2-612 Nuclear Environment Survivability," *Survivability, Vulnerability, & Assessment Directorate (TEDT-W-S-SV-N)*, Appendix A. General Nuclear Weapon Effects, Oct. 2008, pp. 61.
- 64 "Test Operations Procedure (TOP): 1-2-612 Nuclear Environment Survivability," *Survivability, Vulnerability, & Assessment Directorate (TEDT-W-S-SV-N)*, Appendix D. Electromagnetic Environment and Effects, Oct. 2008, pp. 75-81.

## 2.1 Radiation basics

Radiation is energy transport from one location to another. The “carriers” of this energy are photons, ions, electrons, muons and/ or nucleons (neutrons or protons). Early in the 20th century, it was discovered that the classical concept of “particles” and “waves” did not fully describe the properties of quantum-scale particles, and that intrinsically, such particles actually exhibit particle-like or wave-like behavior (“particle-wave duality”), depending on the situation.<sup>[1]</sup> One aspect of this duality is that every particle can be viewed as having a characteristic wavelength that is inversely proportional to its momentum (or alternatively, the square root of its kinetic energy) according to [Equation 2-1](#) (using the nonrelativistic form to keep things simple):

$$\lambda = \frac{h}{p} = \frac{h}{mv} = \frac{h}{\sqrt{2mE_k}}$$

Equation 2-1.

where h is the Planck’s constant, p is the particle momentum, m is its mass, v is its velocity and E<sub>k</sub> is its kinetic energy.

Basically, as a particle’s energy increases, its velocity and momentum also increase, while its wavelength gets smaller. This is an important property, as the wavelength of the incoming particle defines what types of interactions are possible with matter.

A physical effect of this law is readily demonstrable in optics. The Abbe diffraction limit (the more complex form is known as Rayleigh’s criterion<sup>[2-3]</sup>) says that the minimum resolvable feature size, t, is one-half a wavelength of the light used to observe an object – below this limit, diffraction dominates such that a clear, focused image cannot form. As visible light has its smallest wavelengths at ~400 nm (the violet end of the spectrum), the smallest object that can be resolved optically is ~200 nm. Indeed, optical microscopes can easily form images of bacteria and structures within cells, but viruses, proteins, etc., are too small, as shown in [Figure 2-1](#).

In a similar fashion, if electrons are used to probe an object, a higher accelerating voltage allows smaller features to be resolved, since the electron wavelength decreases as the electron kinetic energy increases. A typical scanning electron microscope (SEM) uses accelerating voltages in the range of 1-20 keV, enabling visualization of semiconductor device features that would not be visible using light. In a transmission electron microscope (TEM), where electrons are accelerated to hundreds of kiloelectron volts, resolution to atomic scales is possible, as illustrated in [Figure 2-2](#).

![Figure 2-2: Comparison of the resolution of the wavelength of the imaging particle. The figure shows three images side-by-side. The first image is labeled 'OM' (Optical Microscope) with a wavelength 'λ_ph ~ 500 nm' above it. The second image is labeled 'SEM' (Scanning Electron Microscope) with a wavelength 'λ_e ~ 0.01 nm' above it. The third image is labeled 'TEM' (Transmission Electron Microscope) with a wavelength 'λ_e ~ 0.004 nm' above it. The images show increasing levels of detail from left to right, from a low-magnification view of a circuit to a high-magnification view of atomic-scale features.](9887cf85c05205c57271d28ecc108b32_img.jpg)

Figure 2-2: Comparison of the resolution of the wavelength of the imaging particle. The figure shows three images side-by-side. The first image is labeled 'OM' (Optical Microscope) with a wavelength 'λ\_ph ~ 500 nm' above it. The second image is labeled 'SEM' (Scanning Electron Microscope) with a wavelength 'λ\_e ~ 0.01 nm' above it. The third image is labeled 'TEM' (Transmission Electron Microscope) with a wavelength 'λ\_e ~ 0.004 nm' above it. The images show increasing levels of detail from left to right, from a low-magnification view of a circuit to a high-magnification view of atomic-scale features.

Figure 2-2. Comparison of the resolution (based on the wavelength of the imaging particle) obtained with an optical microscope (OM), SEM and TEM. Using particles of smaller wavelengths (higher energy) enables resolving of much smaller features. The SEM image – Courtesy of Insight Analytical Labs, the TEM image – Courtesy of Hitachi Technologies, taken on a Hitachi HF-3300

The same principle applies to particle accelerators, where electron or ion acceleration energies have increased over the years to enable collisions with such high energies (small wavelengths) that interactions at the deep subatomic scale are revealed – enabling the discovery of quarks, leptons and, most recently the Higgs boson, which makes up the basic building blocks of matter.

Radiation propagating unabated in a vacuum is a key source of the radiation environment encountered in space (hard cosmic rays are considered to be of galactic and extra-galactic origins), but it is the

![Figure 2-1: Demonstration of Abbe's diffraction limit. The figure shows a horizontal scale from 1 mm down to 1 nm. Above the scale are icons for various objects: Ant (1 mm), Hair (100 μm), Mammalian cell (10 μm), Bacterium (1 μm), Mitochondrion (1 μm), Virus (100 nm), Protein (10 nm), and Small molecule (1 nm). A vertical dashed red line is positioned at 100 nm, representing the Abbe's diffraction limit (0.2 μm). Objects to the left of the line are larger than the limit and can be resolved, while objects to the right are smaller and cannot be resolved by visible light.](90d8516930bb8334d7898604aee1bb58_img.jpg)

Figure 2-1: Demonstration of Abbe's diffraction limit. The figure shows a horizontal scale from 1 mm down to 1 nm. Above the scale are icons for various objects: Ant (1 mm), Hair (100 μm), Mammalian cell (10 μm), Bacterium (1 μm), Mitochondrion (1 μm), Virus (100 nm), Protein (10 nm), and Small molecule (1 nm). A vertical dashed red line is positioned at 100 nm, representing the Abbe's diffraction limit (0.2 μm). Objects to the left of the line are larger than the limit and can be resolved, while objects to the right are smaller and cannot be resolved by visible light.

Figure 2-1. Demonstration of Abbe’s diffraction limit showing the minimum features that visible radiation can resolve. When an object is large with respect to the wavelength of light, a good image is possible; however, if an object is the same order as half a wavelength, diffraction effects obliterate the formation of an image.

interaction between radiation and matter that ultimately creates the radiation effects that must be contended with in microelectronics. When a flux of particles is incident on a slab of matter (referred to as the target), each incident particle will encounter one of three possible outcomes:

- The particle will travel through the target material without interacting in any way, emerging from the other side of the slab unchanged (no directional change or energy loss).
- The particle will lose some of its kinetic energy (usually over a large number of small energy-draining interactions) while traveling through the target material, emerging with its direction changed and its kinetic energy reduced.
- The particle will lose all of its energy in the target slab and will be absorbed in the material.

Radiation comes in many flavors, including electromagnetic waves and various energetic particle radiations.

Electromagnetic waves are defined by three physical properties: frequency, wavelength and photon energy (photons are particles of electromagnetic energy). The wavelength is inversely proportional to the frequency; photon energy is proportional to the frequency. Thus, longer wavelengths have lower frequencies and lower photon energies, while shorter wavelengths have higher frequencies and higher photon energies. The behavior of electromagnetic radiation with matter depends on its wavelength.

As illustrated in [Figure 2-3](#), the electromagnetic spectrum is classified by wavelength into the following loosely defined categories, from radio wave to microwave, infrared, visible, ultraviolet, X-ray and finally to short-wavelength and high-energy gamma rays. From a susceptibility point of view, the typical electromagnetic radiation challenge for microelectronics in industrial, medical and defense applications is primarily constrained to X-ray and/or gamma-ray exposures (although some exposed die are sensitive to optical wavelengths).

Radio-frequency and electromagnetic-interference radiation effects are effectively mitigated by standardized commercial design, layout and packaging practices (and thus are not discussed further).

In addition to photons, other particle radiations include a number of different atomic and subatomic particles commonly encountered in natural, industrial and defense environments. From largest to smallest, the primary radiations of interest are heavy and light ions (ionized atoms), nucleons (neutrons and protons), and electrons

and muons. In a macroscopic sense, if energetic particles are incident on a slab of matter (target material), there are several possible outcomes, as illustrated in [Figure 2-4](#).

![Diagram of possible outcomes for particle radiation incident on a thin slab of matter.](356eb99ab9489bbd647223390a913903_img.jpg)

The diagram shows a light blue vertical rectangle labeled 'Slab of matter'. Six horizontal grey arrows, labeled 'a' through 'f', represent incident particles from the left. 
 - Arrow 'a' passes straight through to the right, labeled '100% transmission'.
 - Arrow 'b' is stopped at the slab, labeled '100% absorption'.
 - Arrow 'c' passes through but is shorter, labeled 'Attenuated transmission'.
 - Arrow 'd' is deflected downwards at an angle, labeled 'Forward scattering'.
 - Arrow 'e' is deflected upwards at an angle, labeled 'Back scattering'.
 - Arrow 'f' is stopped at the slab with a small arrow pointing to the interior, labeled 'Absorption with conversion'.

Diagram of possible outcomes for particle radiation incident on a thin slab of matter.

**Figure 2-4.** Diagram of the possible outcomes for particle radiation incident on a thin slab of matter.

In some cases, especially if the slab is thin relative to the typical range of the incident particle in that material, the particle may traverse the slab without any interactions at all and thus be fully transmitted ([Figure 2-4a](#)). For example, neutrinos (chargeless and nearly massless subatomic particles) have such a weak interaction with matter that most neutrinos will traverse large thicknesses of dense materials without interacting at all; hence, these are typically not a reliability concern for microelectronics, since they will pass through devices without any interactions. In stark contrast, alpha particles emitted from natural radioactive decay will be completely absorbed in a thin sheet of paper ([Figure 2-4f](#)). But these particles, emitted from the decay of naturally occurring radioactive uranium and thorium in chip materials, can cause reliability problems if not controlled to very low emission levels. Thus, higher levels of interaction between an incident radiation and the target matter usually lead to more pronounced effects in microelectronics.

From the extremes of full transmission to full absorption, there are several other possible outcomes, all dependent on interactions

![Electromagnetic spectrum diagram showing energy, frequency, and wavelength relationships.](6722729cda068c0bd8c4df61c38501d8_img.jpg)

The figure shows a horizontal bar divided into seven sections: Gamma ray, X-ray, Ultraviolet, Visible (represented by a rainbow), Infrared, Microwave, and Radio. 
 - Below the bar, on the left, text reads: 'Higher photon energy', 'Higher frequency', 'Shorter wavelength'.
 - Below the bar, on the right, text reads: 'Lower photon energy', 'Lower frequency', 'Longer wavelength'.
 - Below the bar is a diagram of a wave. The wavelength increases from left to right, corresponding to the sections of the spectrum.

Electromagnetic spectrum diagram showing energy, frequency, and wavelength relationships.

**Figure 2-3.** Electromagnetic spectrum

between the incident particle and the electrons and nuclei in the target material (Figure 2-4b-e). Specific interactions will be covered later, but for now we acknowledge that the incident particle will often be partially attenuated; that is, the number of particles exiting the opposite surface of the target material will be reduced from the original number of particles incident on the front surface. This absorption of some of the particles or collisions with the electrons and nuclei in the target material can cause this attenuation. As a result of the collision, some particles will be redirected, or scattered.

The angle at which an incident particle is scattered depends on a lot of parameters (particle energy, angle, type of material, etc.), but in a very basic way, particles reversing the direction of motion after the collision are considered to be back-scattered (Figure 2-4d), while those that deviate from their original path but still maintain forward direction are considered to be forward-scattered (Figure 2-4e). In some cases, a particle other than the original incident particle exits, due to the absorption of the original particle with conversion to another particle type (Figure 2-4f).

Now, let's focus on the specifics of the types of interactions between incident radiation and materials that affect the macroscopic transmission, absorption or attenuation. At a more detailed level, an incoming particle can be fully absorbed in a single interaction (in some interactions, photons are completely absorbed in the creation of a single electron-hole [e-h] pair). But for incident ions, nucleons and electrons, almost all of the possible interactions transfer a fraction of the incident particle's kinetic energy to the target electrons or nuclei. In other words, it takes many successive interactions to slow and eventually stop the incident particle (to reduce its kinetic energy to zero). The distance that the particle travels between each successive interaction is called a free path, and the average distance between all interactions is known as the mean free path.

Figure 2-5. Illustrates a particle and its path through matter, suffering successive multiple collisions with electrons and/or nuclei. If the probability of interactions goes up, the mean free path will decrease. Consequently, since the particle will expend more of its energy within a smaller distance traveled, its range in the material will decrease. This situation is analogous to comparing the path of an incident particle in a material that has low density to one with higher density (density here is used loosely to denote the number of interaction sites within a given volume of material).

![Figure 2-5: A diagram showing the path of an energetic particle through a target material. The material is represented by a grid of blue circles (atoms). A red dot on the left represents the incident particle. A black line shows the particle's path, which is deflected multiple times by the atoms. The path ends at a red dot on the right, indicating the particle has stopped. The deflections are labeled 'Multiple collisions rob the particle of its kinetic energy while also redirecting it.'](0eb742ed939b1846d05da644664fa9b7_img.jpg)

Figure 2-5: A diagram showing the path of an energetic particle through a target material. The material is represented by a grid of blue circles (atoms). A red dot on the left represents the incident particle. A black line shows the particle's path, which is deflected multiple times by the atoms. The path ends at a red dot on the right, indicating the particle has stopped. The deflections are labeled 'Multiple collisions rob the particle of its kinetic energy while also redirecting it.'

Figure 2-5. Path of an energetic particle through a target material. Multiple collisions rob the particle of its kinetic energy while also redirecting it.

As material density increases, the interactions a particle suffers in traveling a specific distance increase, so the mean free path between collisions is reduced – and so is the range of the particle in that denser material. Since the energy of the incident particle is not absorbed in a single interaction but via many smaller interactions with target nuclei and electrons, the actual physical path will be unique for each ion.

The ion paths can be visualized in a Monte-Carlo simulation<sup>[6]</sup> of 1,000 identical 50-MeV iron ions incident on a slab of silicon in Figure 2-6. The ions are incident normal to the surface from the left side, and are traveling to the right through the silicon target. In this case, the thickness of the slab and the energy of the ions were adjusted such that all ions are absorbed within the slab. In other words, the **range** of the ions is less than the thickness of the target material through which they are traveling.

![Figure 2-6: A simulation plot showing the paths of 1,000 50-MeV iron ions incident on a silicon target. The x-axis is 'Depth in silicon (μm)' from 0 to 13. The y-axis is 'Depth vs. y-axis'. A horizontal line at y=0 represents 'Ion-beam incidence'. Multiple blue lines represent the paths of individual ions, showing 'Longitudinal straggling' (spread along the x-axis) and 'Lateral straggling' (spread along the y-axis). A vertical double-headed arrow indicates the 'Mean range in silicon'.](9c8070d46f1d2480a875239e792f1ef6_img.jpg)

Figure 2-6: A simulation plot showing the paths of 1,000 50-MeV iron ions incident on a silicon target. The x-axis is 'Depth in silicon (μm)' from 0 to 13. The y-axis is 'Depth vs. y-axis'. A horizontal line at y=0 represents 'Ion-beam incidence'. Multiple blue lines represent the paths of individual ions, showing 'Longitudinal straggling' (spread along the x-axis) and 'Lateral straggling' (spread along the y-axis). A vertical double-headed arrow indicates the 'Mean range in silicon'.

Figure 2-6. Simulation of 1,000 50-MeV iron ions incident (from left) on a silicon target. Each ion has a unique path defined by random multiple interactions with target nuclei and electrons. Each interaction reduces the ion energy by a small amount and can change its trajectory. Ultimately, all of the ions were “stopped” or absorbed.<sup>[9]</sup>

The process is clearly stochastic (probabilistic) – while it is the same ion being shot at the same slab of silicon repeatedly, no two paths are identical. In this example, a mean depth (range) in the material is ~12 μm, but there is clearly variation in the lateral and longitudinal extent of the path. This “straggling” behavior occurs because the number and type of interactions over the depth for each ion are different. Thus, for example, an ion that suffers more scattering-type interactions will tend to be deflected off its initial path.

The concept of a reaction cross-section<sup>[7]</sup> can be considered in terms of a characteristic interaction area, outside of which the interaction/collision probability drops to zero. Since matter is largely “empty space,” imagine the reaction cross-section comprising a large number of tiny reactive areas distributed uniformly through a much larger, inert volume of material.

Interactions only occur if the particle impinges on one of these small reaction areas. A larger cross-section implies a larger area and a larger probability of interaction. Cross-section, typically denoted as  $\sigma$ , is measured in units of area.

In some cases, like certain types of reactions between neutrons and nuclei, the two particles essentially only interact upon contact. In such cases, the cross-section is defined largely by the actual physical size of the target – in this case the cross-sectional area of the nucleus. For other interactions, where forces can act on the particles at a distance, cross-sections will be significantly larger than the physical area of the particles (like charged particles interacting via Coulombic force), since the force acts over longer distances. The probability for any given reaction is proportional to its reaction cross-section.

At the heart of all scattering and absorption interactions is the concept of collisions. Particle-particle collisions are the basic mechanism for how radiation interacts with matter. These collisions can be defined as either elastic or inelastic. Actually, all collisions involve both elastic and inelastic energy loss, but we classify the process as one or the other based on the dominant energy-loss mechanism.

Elastic collisions between an incident and a target particle end with both particles separating after the collision (no particles created, breaking apart or annihilated during the collision, and no energy lost into excitation). Billiard balls colliding is the classic physics example of hard objects interacting elastically. The amount of kinetic energy and momentum that the incident and target particles have after the collision can differ, but the total kinetic energy and momentum of the system must be conserved in elastic collisions.

In contrast, in an inelastic collision, the total kinetic energy in the system is not conserved. A collision is inelastic when some of the kinetic energy is converted into another form of energy (and hence the overall total kinetic energy is reduced). Additionally, in inelastic collisions, particles can be created or destroyed, so incoming and outgoing particles may be different. An example of this would be a nuclear reaction where the incoming neutron or proton is actually absorbed by the nucleus – where the incoming kinetic energy and mass of the nucleon is converted into secondary particles when the nucleus breaks up into pieces to shed the excess energy. In this case, excitation or some other process “uses up” some of the kinetic energy to create particles.

Particle interactions with matter are all about energy loss from the energetic particle to the target material. They represent a number of unique and diverse pathways that depend on the particle, its energy and the properties of the matter in which it is traveling.<sup>[8]</sup> The key concept is that radiation loses energy in matter through these interaction processes. In some cases, the energy of a single particle is completely absorbed in a single interaction. In other cases, it takes numerous successive interactions to “bleed off” the particle’s energy and bring it to rest (absorb it). The more energy that a particle loses per unit distance, the less range it will have. Similarly, the more energy a particle has, the farther it will travel in a given material. Also, the denser a material is, the more energy loss occurs per distance traveled and thus the lower the range of the particle.

The key issue for microelectronics is that most of the energy absorbed from radiation is converted into the production of charge. Since proper operation of microelectronics is based on the controlled modulation, storage and transportation of charge, the nonequilibrium (excess) charge created by localized energy deposited by radiation events can cause transients and/or quasi-permanent charging that can lead to parametric and functional failures.

### 2.2 Particle interactions in matter

### Photons

The photon is the fundamental carrier of electromagnetic energy (radiation), spanning from low to high energy and long to short wavelengths across the electromagnetic spectrum: radio waves, microwaves, visible light, ultraviolet light, X-rays and gamma rays.

The photon’s lack of electric charge eliminates many of the interactions observed between charged particles and atomic electrons and nuclei. There are three major mechanisms<sup>[9–11]</sup> in which a photon loses energy to matter, as illustrated in [Figure 2-7](#). If the incident photon has sufficient energy to free an electron from the valence band or bound state, the photon is destroyed and its entire energy is completely absorbed, creating an excited photoelectron and leaving a positively charged vacancy or “hole.” At higher photon energies, the photon can excite a tightly bound inner electron. In such cases, a secondary “characteristic” X-ray photon is produced when an outer-shell electron fills the vacancy created during the original photon absorption event.

![Diagram illustrating the three primary mechanisms of photon interaction with matter: Photoelectric effect, Pair production, and Compton scattering.](1c29dadab94c3fa552d270434db09c81_img.jpg)

The diagram illustrates three primary mechanisms of photon interaction with matter, centered around a nucleus (represented by a cluster of red and blue spheres). 
1. **Photoelectric effect**: An incident photon (wavy line) is absorbed by an inner-shell electron, ejecting it as a 'Photoelectron' and leaving a vacancy. An outer-shell electron then fills this vacancy, emitting a 'Characteristic X-ray photon'.
2. **Pair production**: An incident photon interacts with the nucleus, converting its energy into an electron-positron pair.
3. **Compton scattering**: An incident photon interacts with a free or loosely bound electron, transferring part of its energy to the electron (labeled 'Recoil electron') and scattering the remaining energy as a lower-energy photon. The energy of the scattered photon is labeled  $E_2 < E_1$ .

Diagram illustrating the three primary mechanisms of photon interaction with matter: Photoelectric effect, Pair production, and Compton scattering.

**Figure 2-7. The three primary mechanisms in which incident photons lose energy in matter: the photoelectric effect, Compton scattering and pair production.**

Like a fingerprint, each element has a unique energy between its L- and K-shell electrons; thus the energy of the X-rays emitted is characteristic of a particular element. These characteristic X-rays thus appear as very sharp and well-defined spectral lines.

The photoelectric effect is inelastic (since all incoming energy is converted into excitation) and proportional to the photon frequency, with higher-frequency photons providing a larger amount of energy. In cases where photon energy is insufficient to create an e-h pair, the material through which it is traveling is “transparent,” since the photon will travel through the material unabsorbed. This quantum-mechanical process is called the photoelectric effect.

The probability of a photoelectric interaction occurring strongly depends on the energy of the incident photon with respect to the binding energy of the electrons in the target material. In silicon, the photoelectric effect is the dominant way in which photons interact with matter, from optical frequencies to X-rays up to ~100 keV.

At higher photon energies, another mechanism begins to take over. In Compton scattering, the photon loses some of its energy in a collision with a single electron. The scattering reaction produces a free recoil electron and a “scattered” photon that is diverted in another direction with less energy (lower frequency) than it had before the collision. Depending on the energy transferred, the electron is either raised to a higher energy-bound state, or, in cases where the transferred energy exceeds the binding energy, the electron is freed with kinetic energy so that it can interact with other electrons and nuclei.

At even higher photon energies, pair production becomes possible and ultimately becomes the dominant energy-loss mechanism for high-energy gamma rays. Pair production can occur between incoming gamma-ray photons and a nucleus, resulting in the creation of two particles: an electron and a positron (a positively charged electron). For pair production to occur, the photon energy must be at least equivalent to the total resting mass of the two particles created. Any extra energy beyond the threshold is converted into kinetic energy of the two newly created particles. The probability of pair production is zero until the threshold energy is reached. Above this threshold, pair production increases with increasing photon energy. The pair production rate increases approximately as the square of the atomic number (the number of protons in an atom, or “Z”; in an uncharged atom, also the number of electrons) of the target. Heavier, denser nuclei are better at absorbing gamma rays.

These three energy-loss mechanisms define what fraction of an incident beam of photons can pass through a specific thickness of target material.<sup>[12]</sup> The photon beam intensity is reduced exponentially by the product of the target thickness and the attenuation coefficient,  $\mu$ , in units of  $\text{cm}^{-1}$ .

The attenuation coefficient is dependent on the photon energy and the target material, since this will determine which absorption mechanism dominates. It is usually more convenient to consider the mass attenuation coefficient,  $\mu_m$ , which is the linear attenuation coefficient divided by the density of the target. The mass attenuation coefficient has units of square centimeter per gram.

**Figure 2-8.** plots the mass attenuation coefficient of silicon as a function of photon energy. The total response is defined by the

![Figure 2-8: A log-log plot showing the total mass attenuation coefficient (solid red curve) and its components (photoelectric absorption, Compton scattering, and pair production) for iron as a function of photon energy. The x-axis is 'Energy in MeV' ranging from 10^-3 to 10^4. The y-axis is 'Attenuation in (cm^2 g^-1)' ranging from 10^-4 to 10^4. The photoelectric absorption curve (blue) starts at 10^4 at 10^-3 MeV and drops sharply. The Compton scattering curve (green) peaks around 0.05 MeV and then decreases. The pair production curves (cyan) start at 1.02 MeV and increase. The total attenuation curve (red) is the sum of these three components.](d04ba66e3c0eccfd8fd2b0d176d3c941_img.jpg)

Figure 2-8: A log-log plot showing the total mass attenuation coefficient (solid red curve) and its components (photoelectric absorption, Compton scattering, and pair production) for iron as a function of photon energy. The x-axis is 'Energy in MeV' ranging from 10^-3 to 10^4. The y-axis is 'Attenuation in (cm^2 g^-1)' ranging from 10^-4 to 10^4. The photoelectric absorption curve (blue) starts at 10^4 at 10^-3 MeV and drops sharply. The Compton scattering curve (green) peaks around 0.05 MeV and then decreases. The pair production curves (cyan) start at 1.02 MeV and increase. The total attenuation curve (red) is the sum of these three components.

**Figure 2-8.** Total mass attenuation coefficient (in iron) vs. energy (solid curve) illustrating the contributions from three different energy-absorbing mechanisms: the photoelectric effect, Compton scattering and pair production.<sup>[12]</sup>

addition of terms corresponding to the three primary energy-loss mechanisms: the photoelectric effect, Compton scattering and pair production.

Since most microelectronics are encapsulated in opaque packages (plastic, ceramic and/or metal), photons in the visible spectrum are typically not a concern. Photons of higher energy, such as X-ray and gamma photons, can easily penetrate packaging materials and are thus the primary photons of concern from the microelectronics point of view. In industrial and medical environments, where X-rays or gamma rays are the dominant radiation, the photon energy is in the range of 10-1,000 keV, so charge production is dominated by the photoelectric effect, and to a lesser degree, Compton scattering. In the terrestrial and space environments, direct X-ray and gamma-ray fluxes are usually not significant compared to those from other radiation types.

#### Electrons

Incident electrons interact with orbital electrons and nuclei in target matter via the Coulomb force. The result of each interaction is always a redirected electron with or without the emission of a photon.<sup>[14-16]</sup> In the case of electron-electron interactions, a repulsive force grows between two negatively charged electrons as the distance between them shrinks. This force deflects the incoming electron off its initial trajectory (presuming that the target electron stays in orbit around the nucleus). The incident electron leaves the collision area at a different angle.

In the case of electron-nucleus interactions, an attractive force grows between the negatively charged electron and the positively charged nucleus as the distance between them shrinks. This attractive force decelerates the electron and causes it to change its trajectory (the nucleus is much less affected, since it is much more massive than the electron). The incident electron leaves the collision area at a different angle. Occasionally, the electron can displace a target nucleus, creating displacement damage (see Chapter 3), although ionizing energy loss is far more prevalent. Both of these events are known as scattering; the key types of electron scattering are shown in **Figure 2-9**.

The two most likely interactions are electron-electron and electron-nucleus scattering. The scattering angles (the angle between the trajectory of the incoming electron and its new trajectory after the collision) in electron-electron collisions are smaller than electron-nucleus collisions, since less mass is involved. Elastic electron-electron scattering usually results in smaller scattering angles, while electron-nucleus interactions cause higher-angle scattering and involve inelastic processes. In electron-nucleus collisions, the scattering angle is strongly dependent on the atomic number of the target material.

![Diagram of three primary mechanisms for electron-matter interactions: elastic electron-electron scattering, inelastic electron-electron scattering, and inelastic electron-nucleus scattering.](5d3455c6c2a37cb3aff761fedeb8644e_img.jpg)

The diagram illustrates three primary mechanisms for electron-matter interactions within an atom. 
 1. **Elastic electron-electron scattering:** An incident electron (red arrow) collides with a bound electron (blue dot), resulting in both electrons changing direction without energy loss. 
 2. **Inelastic electron-electron scattering:** An incident electron (red arrow) collides with a bound electron (blue dot), causing the bound electron to be ejected (recoil electron) and a photon (characteristic X-ray photon) to be emitted. 
 3. **Inelastic electron-nucleus scattering:** An incident electron (red arrow) is deflected by the nucleus, resulting in the emission of Bremsstrahlung (braking radiation). 
 The atom is shown with a central nucleus (red and blue spheres) and concentric electron shells (blue dots).

Diagram of three primary mechanisms for electron-matter interactions: elastic electron-electron scattering, inelastic electron-electron scattering, and inelastic electron-nucleus scattering.

**Figure 2-9. Diagram of the three primary mechanisms for electrons interacting with matter: elastic electron-electron, inelastic electron-electron and inelastic electron-nucleus scattering.**

Since higher  $Z$  atoms tend to have higher electron densities, electron scattering effects are larger in such materials. In inelastic electron-electron collisions, the bound target electron absorbs some or all of the incident electron kinetic energy and is excited to a higher energy level. When an inner electron is ejected by a collision with an incoming electron, it leaves a vacancy. This vacancy is immediately filled by an electron from a higher energy-bound state – with a concurrent emission of a photon whose energy is defined by the difference between the higher energy state and lower energy state.

In higher  $Z$  elements, the emitted photon is an X-ray. This characteristic X-ray is analogous to the X-rays emitted due to the creation of a vacancy during the absorption of a photon by the photoelectric effect. When the same inelastic electron-electron reaction occurs in a lighter (low- $Z$ ) atom with weakly bound electrons, the photon emission is in the visible spectrum. In some interactions, if the target electron absorbs more energy, it may become “unbound” or “free.” If it has sufficient kinetic energy, the excited electron can cause further ionizations before it loses its energy and is recaptured (an energetic electron is often referred to as a delta-ray).

One primary inelastic interaction between an incoming electron and a target nucleus results in the direct emission of a photon. As the electron is attracted to the nucleus, it changes direction by decelerating. Bremsstrahlung, or braking radiation, is emitted when a charged particle is decelerated. This deceleration causes the electron to lose kinetic energy, which is emitted in the form

of a photon. The closer the high-speed electron approaches the nucleus, the greater the electrostatic attraction and the greater the deceleration of the electron, so the greater the energy of the emitted photon.

Since the energy of photons is proportional to how close the electron and nucleus were when the interaction occurred, and because there is a semi-infinite number of possible trajectories, Bremsstrahlung is characterized by a continuous spectrum of photon energies, with a maximum energy determined by the maximum kinetic energy of the incident particles. **Figure 2-10** plots the range of electrons as a function of their kinetic energy for silicon (blue curve) and tungsten (red curve).

![Graph of electron range in cm versus electron energy in eV for silicon and tungsten.](fbfbd4dd5363c5bd548a8e871d0fce40_img.jpg)

The graph plots the range of electrons in centimeters (cm) on a logarithmic y-axis (from 0.001 to 100) against electron energy in eV on a logarithmic x-axis (from 1.E+04 to 1.E+08). Two curves are shown: a blue curve for silicon and a red curve for tungsten. Both curves show that the range of electrons increases with energy, but the range in tungsten is significantly lower than in silicon for the same energy level.

| Electron energy (eV) | Range in silicon (cm) | Range in tungsten (cm) |
|----------------------|-----------------------|------------------------|
| 1.E+04               | ~0.001                | ~0.0005                |
| 1.E+05               | ~0.01                 | ~0.005                 |
| 1.E+06               | ~0.1                  | ~0.02                  |
| 1.E+07               | ~1                    | ~0.1                   |
| 1.E+08               | ~10                   | ~0.5                   |

Graph of electron range in cm versus electron energy in eV for silicon and tungsten.

**Figure 2-10. Electron range in silicon (blue) and tungsten (red) as a function of electron energy. Tungsten is both denser and has higher  $Z$  than the silicon; consequently, the range of electrons in tungsten is much lower.<sup>[7]</sup>**

Since most microelectronics are encapsulated in opaque packages (plastic, ceramic and/or metal), only electrons with kinetic energies in excess of ~300 keV can penetrate the packaging materials and reach the die. In industrial and medical environments, where accelerated electron beams or radioisotopes emit beta particles, the electron energy is in the range of 0.01–4 MeV. Clearly, at higher energies, the electrons are capable of penetrating microelectronics packages and irradiating the microelectronics inside. In terrestrial environments, there are usually not enough high-energy electrons (or beta particles) to have a significant effect on the reliability of microelectronics. In space environments, electron fluxes can be significant, particularly near radiation belts where the flux of electrons can be very high. In these belts, the electrons have energy in the range of 0.1 to 10 MeV, so electrons in the space environment will clearly penetrate the package and cause total ionizing dose (TID) effects.

### Nucleons and nuclear reactions

Nucleons are the building blocks of nuclei: the protons and neutrons that populate the nuclei of all atoms. Nucleons comprise three specific types of quarks held together by gluons (carriers of the strong force), but for the physics of radiation effects in microelectronics, you really don't need to go beyond proton and neutron reactions with the nuclei of matter.<sup>[18,19]</sup>

Neutrons and protons have nearly identical mass. The mass of a neutron is 1.0 atomic mass units (AMUs), while a proton has a mass of 0.9986 AMUs. In contrast, the mass of an electron is 2,000x smaller, with a mass of about 0.0005 AMUs. The key differentiator between a proton and a neutron is that neutrons are electrically neutral, while protons are positively charged. This difference has an impact on the types of interactions with target nuclei and electrons.

Since neutrons have no charge, Coulomb interactions do not occur, so the neutron is incapable of producing direct ionization as it travels through a target material. Said another way, the only way a neutron can lose energy in matter is through elastic and inelastic nuclear reactions (and rare magnetic interactions with unpaired electrons). As a result, neutrons are quite penetrating, since their interactions with matter are limited. A neutron can have two types of nuclear reactions, elastic and inelastic, as shown in [Figure 2-11](#).<sup>[20]</sup>

![Figure 2-11: Elastic and inelastic nuclear reactions. The top diagram shows an elastic collision where an incoming neutron strikes a silicon target nucleus, resulting in an outgoing neutron and a recoiling silicon nucleus. The bottom diagram shows an inelastic collision where an incoming neutron strikes a silicon nucleus, causing nuclear excitation and leaving the nucleus in a highly excited state.](9f9386d5b3d6cbeb1ed104a799320ebf_img.jpg)

The diagram consists of two parts. The top part, labeled 'Elastic nuclear collision', shows an 'Incoming neutron' (blue circle) approaching a 'Silicon target nucleus' (cluster of red and blue spheres). After the collision, an 'Outgoing neutron' (blue circle) moves away, and the 'Silicon recoil nucleus' (cluster of red and blue spheres) is displaced. The bottom part, labeled 'Inelastic nuclear collision', shows an 'Incoming neutron' (blue circle) approaching a 'Silicon nucleus' (cluster of red and blue spheres). The result is 'Nuclear excitation', represented by a larger, more vibrant blue sphere.

Figure 2-11: Elastic and inelastic nuclear reactions. The top diagram shows an elastic collision where an incoming neutron strikes a silicon target nucleus, resulting in an outgoing neutron and a recoiling silicon nucleus. The bottom diagram shows an inelastic collision where an incoming neutron strikes a silicon nucleus, causing nuclear excitation and leaving the nucleus in a highly excited state.

**Figure 2-11. Elastic (top) and inelastic (bottom) nuclear reactions between a silicon target nucleus and an energetic incoming neutron. In the elastic collision, the neutron “bounces off” the nucleus and no change creates a recoil. In the inelastic case, the neutron actually gets absorbed, causing the nucleus to be in a highly excited state.**

In the case of elastic reactions, the neutron collides with a target nucleus and transfers some of its kinetic energy to that nucleus. The neutron then leaves the scene of the collision with less kinetic energy. From a microelectronics point of view, if enough of the incident neutron's kinetic energy transfers to the nucleus (this usually occurs at neutron energies in excess of 100 keV), it becomes a recoil nucleus and is displaced from its normal position within the target.

In semiconductor devices, neutron-induced defects induce dramatic localized changes in the electrical properties of a device. An accumulation of these defects over repeated neutron or proton events creates the displacement damage dose effects explained in Chapter 3. Additionally, each neutron-induced recoil nucleus is a heavy ion, producing a lot of direct ionization as it travels away from the collision site. Each recoil nuclei is therefore potentially capable of causing a single-event effect (SEE).

Inelastic nuclear reactions occur when the neutron is absorbed by the target nucleus – this implies that the mass and energy of the neutron are converted into excitation of the nucleus. There are several pathways for releasing this excess energy, all leading to the emission of secondary radiation by the target nucleus that depends on the type of nucleus and the kinetic energy of the incident neutron. These are illustrated in [Figure 2-12](#). With incident neutrons at thermal energies up to a few tens of kiloelectron volts, the incident neutron is typically absorbed and the excess energy is released in the form of gamma-ray photons.

![Figure 2-12: Pathways for energy release from an excited silicon nucleus. The diagram shows four possible outcomes: 1) Emission of a gamma ray, 2) Spallation (ejection of a neutron or proton), 3) Nuclear fission (splitting into two heavy recoils and neutrons), and 4) Fragmentation (splitting into light fragments and a recoil nucleus).](1c9a5a80a4ed18fdfda1c8ae915966bf_img.jpg)

The diagram shows a central 'Silicon nucleus' (cluster of red and blue spheres) with a dashed line indicating it is 'Immediately after inelastic collision with neutron'. Four arrows point outwards to different outcomes: 1) 'Gamma ray' (a wavy line), 2) 'Ejected neutron or proton (spallation)' (a single red or blue sphere), 3) 'Two heavy recoils + neutron(s) (Nuclear fission)' (two clusters of spheres and a neutron), and 4) 'Light fragments + recoil' (small clusters of spheres and a larger recoil nucleus).

Figure 2-12: Pathways for energy release from an excited silicon nucleus. The diagram shows four possible outcomes: 1) Emission of a gamma ray, 2) Spallation (ejection of a neutron or proton), 3) Nuclear fission (splitting into two heavy recoils and neutrons), and 4) Fragmentation (splitting into light fragments and a recoil nucleus).

**Figure 2-12. Immediately after an inelastic nuclear reaction, the nucleus is left in a highly excited state. The excess energy is released as radiation in one of four pathways dependent on the energy of the neutron and the type of target nucleus.<sup>[21]</sup>**

At low to intermediate energies, from one to several tens of megaelectron volts, the usual result is that the captured neutron's energy is shared among all nucleons. The nucleus' response is to break apart, usually into one or more light fragments (nucleons or light ions) with a heavier recoil nucleus (gamma rays are also emitted). All emitted fragments usually have energy in the megaelectron range and thus are directly ionizing. This secondary radiation is the dominant source of SEEs from neutrons in microelectronics (the exception is emitted neutrons that are not directly ionizing but that can cause further follow-on nuclear reactions that do produce ionizing radiation).

The nuclei of certain elements will split into two nearly equal mass recoil fragments while emitting one or more neutrons. Such nuclear reactions are known as nuclear fission and are the basis for nuclear reactors. In microelectronics, such heavy compounds are found in impurity levels (parts per billion); thus fission is not a significant source of TID or SEEs.

As the incident neutron energy increases above 100 MeV, its wavelength is reduced such that it no longer interacts with the whole nucleus but actually transfers most or all of its energy to single nucleons within the nucleus. The result of these higher-energy reactions is called spallation. The incident neutron interacts with a single neutron or proton within the nucleus, ejecting it with a high kinetic energy. The ejected nucleon can then go on and cause further nuclear reactions as it travels through the target material.

Even though protons have a mass that is nearly identical to that of the neutron, they behave differently in matter since they have a positive charge. In addition to inducing many of the same nuclear effects as neutrons, protons also interact via Coulombic forces and thus can – and do – directly ionize materials. The actual charge generated by protons within typical device-sensitive volumes is relatively small, but in some advanced digital circuits with low critical charge, SEEs have been observed.<sup>[22]</sup>

Protons will attract electrons and be repulsed by the positive charge of nuclei. For protons with kinetic energies <50 MeV, the Coulombic effect will tend to dominate over nuclear effects – the protons will be repulsed from the nuclei before the strong force can take over and cause a nuclear reaction. Above 50 MeV, the protons have sufficient energy to exceed the repulsive effects such that nuclear reactions will occur similarly to those induced by neutrons.

One last important aspect of nuclear reactions is the concept of nuclear reaction cross-section. Cross-section is a measure of the probability that a specific nuclear reaction will occur when protons or neutrons traverse a thin slab of target material. Cross-section is usually reported as a cross-sectional area, in units of barn, where one barn =  $10^{-28} \text{ m}^2 = 10^{-24} \text{ cm}^2$ . The barn is based on the typical physical nuclear radius ( $\sim 10^{-14} \text{ m}$ ) and cross-sectional area ( $10^{-28} \text{ m}^2$ ).

**Figure 2-13** is a nuclear cross-section for neutrons incident on a slab of silicon as a function of the neutron energy, and shows both the elastic (red curve) and inelastic (blue curve) contributions to the overall cross-section. The very distinct resonances in the curves are due to the different quantized nuclear states. An incoming particle that can deposit exactly the mass/energy of these discrete states is much more likely to be captured – these resonances reveal aspects of the specific quantum structure of specific nuclei.

For microelectronics, the cross-section curve is important because with a knowledge of the fluence and spectrum of neutrons or protons incident on a target material, the cross-section determines the actual number of nuclear reactions expected to occur within that target slab. Ultimately, this type of information can help determine single-event rates and doses in microelectronics.

Protons are the primary radiation encountered in space, and a significant fraction of these protons have sufficient energy to easily traverse shielding and packaging materials, depositing significant energy in microelectronics. Thus, protons are a major source of SEEs and can occur in high-enough fluences to potentially induce TID and displacement damage dose effects as well.

Neutrons are one of the primary particles in the terrestrial environment, from sea level to flight altitudes. The natural terrestrial neutron spectrum (which is a direct result of cosmic-ray protons interacting with the Earth's atmosphere) includes neutrons with

kinetic energies of tens and hundreds of megaelectron volts, so shielding the neutron flux is not practical for most applications (large supercomputers, data centers, etc., are often built in basements surrounded by thick concrete walls – with at least a few meters of concrete precisely to reduce neutron-induced errors). Neutron effects produce significant SEEs in terrestrial applications. TID and displacement damage effects from terrestrial neutrons are usually not a concern, due to the relatively low fluences encountered over typical product lifetimes.

![Figure 2-13: Nuclear reaction cross-section for neutrons in a silicon target as a function of neutron energy. The graph plots Cross-section (barns) on a logarithmic y-axis (from 0.00001 to 100) against Incident neutron energy (MeV) on a logarithmic x-axis (from 0.01 to 100). Three curves are shown: 28Si(n,tot) in blue, 28Si(n,elastic) in red, and 28Si(n,inelastic) in cyan. The total cross-section (blue) shows numerous sharp resonances, particularly between 0.1 and 10 MeV. The elastic cross-section (red) is relatively smooth and decreases from about 2 barns at 0.01 MeV to about 0.5 barns at 100 MeV. The inelastic cross-section (cyan) starts at approximately 0.05 MeV and increases to about 1 barn at 100 MeV.](e75b47d0ac4bd181879bc6abdf215d33_img.jpg)

Figure 2-13: Nuclear reaction cross-section for neutrons in a silicon target as a function of neutron energy. The graph plots Cross-section (barns) on a logarithmic y-axis (from 0.00001 to 100) against Incident neutron energy (MeV) on a logarithmic x-axis (from 0.01 to 100). Three curves are shown: 28Si(n,tot) in blue, 28Si(n,elastic) in red, and 28Si(n,inelastic) in cyan. The total cross-section (blue) shows numerous sharp resonances, particularly between 0.1 and 10 MeV. The elastic cross-section (red) is relatively smooth and decreases from about 2 barns at 0.01 MeV to about 0.5 barns at 100 MeV. The inelastic cross-section (cyan) starts at approximately 0.05 MeV and increases to about 1 barn at 100 MeV.

**Figure 2-13. Nuclear reaction cross-section for neutrons in a silicon target as a function of neutron energy. Elastic reactions are shown in red and inelastic reactions in blue.<sup>[23]</sup>**

#### Ions

Energetic ions are positively charged, since they are basically nuclei that have lost some or all of their electrons and travel at high velocities defined by their kinetic energy. When an energetic ion traverses matter, the primary energy-loss mechanism is via electronic and nuclear interactions with target atoms.<sup>[24, 25]</sup>

A simulation of the linear energy transfer (LET) of a Xenon ion in a silicon target as a function of the ion's energy is shown in **Figure 2-14**. The larger peak at higher ion energies is LET due to electronic effects (direct ionization). The smaller peak at lower ion energies is LET due to “nuclear” stopping – energy loss by the displacement of target nuclei by an incoming ion. Along its trajectory through the target, the ion will continuously be losing kinetic energy (slowing down) to successive elastic and inelastic interactions with nuclei and electrons. The energetic ion's positive charge ejects nearby electrons out of their orbits (ionizes them), creating a mass of electrons and holes in its wake. “Heavier” ions with more positive charge are much more effective at causing direct ionization. Indeed, at any given energy, the heavier the ion, the more charge generated over the trajectory of that ion (higher LET).

Energetic ions also interact with target nuclei. As a positive ion approaches an atom, the bound electrons around the atom screen the positive nuclear charge, reducing the repulsive force generated between the ion and the nucleus.

![Figure 2-14: Linear energy transfer (LET) as a function of ion energy for Xenon ion in a silicon target. The graph shows two curves: 'Energy loss via direct ionization' (solid blue line) and 'Nuclear reactions, displacement damage' (dashed blue line). The x-axis is 'Ion energy (MeV)' on a log scale from 0.001 to 10000. The y-axis is 'LET (MeV-cm²/mg)' on a linear scale from 0 to 80. The direct ionization curve peaks at approximately 70 MeV-cm²/mg around 100 MeV. The nuclear reactions curve peaks at approximately 20 MeV-cm²/mg around 0.1 MeV.](9ac04bd96ff7aa9e60639b5f5a63ed40_img.jpg)

Figure 2-14: Linear energy transfer (LET) as a function of ion energy for Xenon ion in a silicon target. The graph shows two curves: 'Energy loss via direct ionization' (solid blue line) and 'Nuclear reactions, displacement damage' (dashed blue line). The x-axis is 'Ion energy (MeV)' on a log scale from 0.001 to 10000. The y-axis is 'LET (MeV-cm²/mg)' on a linear scale from 0 to 80. The direct ionization curve peaks at approximately 70 MeV-cm²/mg around 100 MeV. The nuclear reactions curve peaks at approximately 20 MeV-cm²/mg around 0.1 MeV.

**Figure 2-14. Linear energy transfer (LET) as a function of ion energy for Xenon ion in a silicon target illustrating the two types of energy loss, electronic and nuclear.** [29]

Ultimately, as the ion gets closer to the nucleus, the screening force drops off and the full ion-nuclei Coulomb repulsive force is generated (proportional to the inverse of the distance between two objects with the same charge polarity). Thus, the ion will be scattered or redirected to a new trajectory while also losing kinetic energy during the scattering event. When the ion has lost all of its kinetic energy through a multitude of interactions with the target, it is at rest (stopped) in the target material.

In contrast to photons, electrons and nucleons, energetic ions deposit high densities of energy, leaving localized filamentary cylindrical distributions of highly ionized charge in their wake. [27–29] A comparison of different particle radiation types and the amount of charge they deposit along their paths is shown in **Figure 2-15**. Clearly, heavy ions (iron) are the most disruptive events, generating hundreds of femtocoulombs per micron of travel. Lighter ions and electrons are much less disruptive. This is one reason why SEEs are usually dominated by heavy ion events versus other radiation types.

Very small volumes of silicon can suffer very large infusions of excess charge, especially for heavy-ion events. Typical events occur over a very short duration compared with device dynamic response times. An energetic ion traverses sensitive volumes of silicon in tens of femtoseconds and has been completely stopped within a picosecond.

From a device dynamics perspective, for all but the very smallest and fastest technologies, the silicon device “sees” the ion event as creating a time-zero excess ambipolar charge distribution along its path through sensitive volumes (with e-h pairs in close proximity to each other so the overall charge disturbance is quasi-neutral prior to charge separation). The huge number of excess e-h pairs created by the ion’s passage is completed before recombination, drift and diffusion effects start to reduce, separate and collect the charge.

Heavy-ion events can be pictured as the instantaneous creation of cylindrical volumes of excess charge randomly injected within microelectronics. These excess charge filaments, or cylinders, have

a length defined by the range of the particle in the target material (tens or hundreds of microns), while the radius is typically on the order of nanometers.

If the ion trajectory is such that it is located deep within the substrate or constrained to the back end of the line (metal and dielectric layers above the active devices), then its impact is usually negligible and the ion event will go unnoticed. If, however, the ion occurs in active device layers, the injected charge will usually cause device malfunctions.

![Figure 2-15: Comparison of the linear charge generated per distance traveled (dQ/dx) by various radiation types in silicon as a function of the incident particle energy. The graph shows three curves: 'Iron ions' (red solid line), 'Protons' (blue solid line), and 'Electrons' (cyan dashed line). The x-axis is 'Incident particle energy (MeV)' on a linear scale from 0 to 100. The y-axis is 'LET (MeV-cm²/mg)' on a log scale from 0.01 to 1000. Iron ions show a sharp increase in LET from 0 to about 100 MeV-cm²/mg, then plateau. Protons show a sharp decrease in LET from about 100 MeV-cm²/mg at low energy to about 0.1 MeV-cm²/mg at high energy. Electrons show a very low LET, increasing slightly with energy.](7b080ccb895acb922759b1643910b3fb_img.jpg)

Figure 2-15: Comparison of the linear charge generated per distance traveled (dQ/dx) by various radiation types in silicon as a function of the incident particle energy. The graph shows three curves: 'Iron ions' (red solid line), 'Protons' (blue solid line), and 'Electrons' (cyan dashed line). The x-axis is 'Incident particle energy (MeV)' on a linear scale from 0 to 100. The y-axis is 'LET (MeV-cm²/mg)' on a log scale from 0.01 to 1000. Iron ions show a sharp increase in LET from 0 to about 100 MeV-cm²/mg, then plateau. Protons show a sharp decrease in LET from about 100 MeV-cm²/mg at low energy to about 0.1 MeV-cm²/mg at high energy. Electrons show a very low LET, increasing slightly with energy.

**Figure 2-15. Comparison of the linear charge generated per distance traveled ( $dQ/dx$ ) by various radiation types in silicon as a function of the incident particle energy. Note that heavier ions are orders of magnitude more disruptive than other particles.**

In low-voltage technologies, charge transients will induce spurious voltages and current, which can corrupt digital data or induce glitches on the outputs of analog devices. In CMOS devices where complementary well structures are in close proximity, the injected charge can turn on parasitic bipolar mechanisms and induce single-event latchup. In higher-voltage power and interface technologies, heavy ions can induce junction and gate-oxide breakdown.

In addition to huge fluxes of protons (hydrogen ions) and alpha particles, heavier ions are primarily encountered only in space, mostly from extra-solar cosmic rays. These heavier ions have sufficient energy to easily traverse shielding and package materials, and deposit the most energy (generate the most charge) of any particle type.

In the space environment, heavy ions are a major source of SEEs; due to their very high LET characteristics, heavy ions can induce a host of nondestructive and destructive SEEs. That being said, even in space, heavy ions are relatively rare and do not occur in high-enough fluences to induce TID and displacement damage dose effects in microelectronics. Since heavy ions are rapidly absorbed by the atmosphere, they are not a concern in the terrestrial environment.

### 2.3 Linear energy transfer

One of the most common terms when dealing with particle radiation and microelectronics is the concept of linear energy transfer, or LET. The term linear refers to the fact that LET is a function that provides the energy loss **per unit length** and does not imply that energy loss is a linear function of particle energy. LET is strongly nonlinear as a function of particle energy and is typically reported in units of megaelectron volts-square centimeters per milligram, or megaelectron volts per millimeter.

Simulations of LET and range for an ion of iron in silicon as a function of its energy are shown in **Figure 2-16**. As the iron ion loses kinetic energy, it moves more slowly and has more time to generate more charge through more interactions with the matter through which it is traversing. Thus, going from high ion energy to lower energy, the ion LET peaks at low energy. Once the kinetic energy has been reduced to zero, the ion is considered stopped in the target material and is no longer an issue from a device reliability standpoint. The amount of target material required to stop an ion of a particular kinetic energy is the range of that ion in the material.

![Figure 2-16: A dual-axis line graph showing the relationship between ion energy, linear energy transfer (LET), and ion range for an iron ion in a silicon target. The x-axis represents ion energy in MeV, ranging from 0 to 1000. The left y-axis represents linear energy transfer in MeV-cm²/mg, ranging from 0 to 30. The right y-axis represents ion range in silicon in micrometers (µm), ranging from 0 to 300. A red solid line, labeled 'Fe ion LET', shows a highly nonlinear curve that starts at 0, rises to a peak of approximately 29 MeV-cm²/mg at an energy of about 100 MeV (the Bragg peak), and then decreases as energy increases further. A blue dashed line, labeled 'Fe ion RANGE', shows a linear relationship that starts at 0 and increases steadily to approximately 230 µm at 1000 MeV.](8f38356601e137ac471fc4771b9c5a5c_img.jpg)

Figure 2-16: A dual-axis line graph showing the relationship between ion energy, linear energy transfer (LET), and ion range for an iron ion in a silicon target. The x-axis represents ion energy in MeV, ranging from 0 to 1000. The left y-axis represents linear energy transfer in MeV-cm²/mg, ranging from 0 to 30. The right y-axis represents ion range in silicon in micrometers (µm), ranging from 0 to 300. A red solid line, labeled 'Fe ion LET', shows a highly nonlinear curve that starts at 0, rises to a peak of approximately 29 MeV-cm²/mg at an energy of about 100 MeV (the Bragg peak), and then decreases as energy increases further. A blue dashed line, labeled 'Fe ion RANGE', shows a linear relationship that starts at 0 and increases steadily to approximately 230 µm at 1000 MeV.

**Figure 2-16.** SRIM 2013<sup>[30]</sup> simulation of the LET (red) and range (blue) of an iron ion in a silicon target as a function of the ion's energy. Note that LET is highly nonlinear; the iron ion loses most of its energy at the end of its range when it has the least kinetic energy remaining. This peak in the LET curve is often referred to as the Bragg peak.

Referring to the blue curve, for example, an iron ion of 1 GeV will have a range of ~230 µm in a silicon target. Both LET and range are statistical in nature, since the actual path and the number and types of interactions will vary from ion event to ion event, so there is variation in range (known as straggling) and LET for any given number of identical ion events. The pronounced peak in a LET curve is known as the Bragg peak.<sup>[31,32]</sup>

The nonlinear property of LET implies that unless a shield is sufficiently thick enough to completely stop a particle, it will reduce the particle energy. But this will actually increase the LET, thus

creating more radiation-induced charge. This effect was found in dynamic random access memories (DRAMs) using a 5-µm polyimide film as an overcoat, mechanical stress relief and "alpha shield." Experiments revealed that the shield did not completely block alpha particles but actually stopped them closer to the active device layers with higher LET, thus making alpha-particle soft errors worse than in DRAMs without any shielding.<sup>[33]</sup>

Since most of the energy is lost in the production of ionization charge (so-called electronic stopping), for microelectronics LET is a direct measure of an event's ability to upset these devices. The amount of charge produced can be determined by dividing the energy loss within a given trajectory segment by the energy required to create an e-h pair in that particular material (in silicon, each 3.6 eV of energy lost produces a single e-h pair).

Most microelectronics have areas and volumes that are extremely sensitive to charge injection. If an energetic particle comes close or traverses one or more of these sensitive volumes, the circuit may be corrupted or destroyed. The severity of the circuit response depends on its design, layout, biasing and process, but in large part is actually determined by the LET of the particle. SEEs are largely dependent on LET.

Another related energy-loss mechanism is called stopping power – again, a function describing particle energy loss along a linear trajectory. But stopping power is actually a bit more accurate, as it considers all energy-loss mechanisms, including radiative energy loss (Bremsstrahlung), the production of delta rays (secondary electrons) and the creation of atomic defects, while LET does not. In actuality, though, the terms are nearly interchangeable for heavier ions, as LET and stopping power are nearly equal for these types of particles.

LET describes the amount of incremental energy, dE, lost by a particle (due to electronic ionization processes) in a specific target material as the particle travels an incremental distance, dx, through that material. LET is not constant but varies as a function of particle energy and is a strong function of particle type (proton, electron, light ion, heavy ion, etc.); energy; and the material through which the particle is traveling.

Ions are often separated into light and heavy categories – typically a heavy ion means anything bigger than carbon – but for some this divider is at iron. The key point is that heavier ions have higher Z (larger numbers of protons) and hence a larger positive charge. The heavier an ion is, the more positive charge it carries, and the more energy it will lose and the more ionization it will create as it travels through a target.

For LET, the particle mass is actually less important than its charge, since it is the charge and not the mass that determines the amount of energy lost by Coulombic forces (particle mass is important for energy loss due to scattering events, particularly those that cause displacement damage). Here are a few rules of thumb regarding LET and ranges of particles in matter:

- The heavier, higher Z (also more highly charged) the particle, the higher the LET.
- At the same energy and in the same material, lighter/lower charge particles will have a lower LET.
- Lighter particles will have a larger range than heavier particles.

- The LET of particles traversing denser materials will usually be higher than the LET of ions in less-dense materials.
- The range of ions will be shorter in denser materials.

LET is independent of the actual ion trajectory (ignoring crystallographic effects such as channeling). However, since active layers in most semiconductor devices and their charge-sensitive volumes are constrained to thin surface layers, ions with trajectories closer to the surface (trajectories at higher angles of incidence) will create much more charge in proximity to active areas. Thus, the same LET value becomes more effective at generating the charge that disrupts semiconductor devices.<sup>[34]</sup>

To account for this effect, Equation 2-2 expresses the concept of effective LET ( $LET_{EFF}$ ):

$$LET_{EFF} = \frac{LET}{\cos \theta}$$

Equation 2-2.

where  $\theta$  is the angle of incidence (0 degrees for normal incidence).

Figure 2-17 shows two identical ion strikes: one at normal incidence (left) and one at a glancing angle of 60 degrees (right). Since most of the energy is lost at the end of the ion's path, the glancing ion event creates much more charge near the sensitive junction areas; hence, its ability to disrupt the device function is significantly enhanced.

Figure 2-17 shows a SRIM simulation of  $LET_{EFF}$  as a function of ion angle. Generally, when LET is mentioned in the context of its effect on electronic devices, assume that the angle term is included and that it is the  $LET_{EFF}$ .  $LET_{EFF}$  is an engineering approximation and is not accurate for very small geometries or high-voltage products with deep sensitive areas.

### 2.4 Radiation shielding

In industrial and medical radiation environments that employ radiation-producing equipment, or where exposure to radioactive substances is likely, three methods minimize dose exposure for people and equipment: limiting time near the source of radiation, maximizing the distance between the user and the source, and shielding the source of radiation. Since radiation exposure depends directly on the duration of radiation, dose can be reduced by limiting exposure time.

The amount of radiation exposure depends on the distance from the source of radiation – for an isotropic source (emitting radiation in all directions), the flux will decrease with the square of the distance from the source. Thus, maximizing distance from the sources minimizes the exposure. Lastly, a barrier can shield the source of radiation.

When microelectronics must function in a space environment – and where the mission dictates time and distance in the radiation environment – the only recourse is to mitigate or reduce the exposure levels is to shield the electronics. Radiation shielding usually consists of single or multiple barriers of metal, ceramic plates or enclosures. The type of shielding depends on the type

![Diagram (a) showing two ion strikes on a P substrate. The left strike is normal (θ = 0) and the right strike is at an angle (θ ~ 60°). Both strikes are labeled 'N+' and show the ion path and the resulting charge distribution near the surface.](537ca37419783394e9b8ab64dd4da754_img.jpg)

Diagram (a) showing two ion strikes on a P substrate. The left strike is normal (θ = 0) and the right strike is at an angle (θ ~ 60°). Both strikes are labeled 'N+' and show the ion path and the resulting charge distribution near the surface.

(a)

#### SRIM 2013 Fe in silicon

![Figure 2-17(b) is a line graph showing Effective LET (MeV-cm²/mg) versus Iron ion energy (MeV) on a logarithmic scale. The graph displays five curves for different angles of incidence: Normal (0°), 30°, 45°, 60°, and 75°. The Effective LET increases with increasing angle of incidence, with the 75° curve reaching the highest peak of approximately 110 MeV-cm²/mg at 100 MeV.](2665a19f156c09460b6b2df4eeb3c2c0_img.jpg)

Figure 2-17(b) is a line graph showing Effective LET (MeV-cm²/mg) versus Iron ion energy (MeV) on a logarithmic scale. The graph displays five curves for different angles of incidence: Normal (0°), 30°, 45°, 60°, and 75°. The Effective LET increases with increasing angle of incidence, with the 75° curve reaching the highest peak of approximately 110 MeV-cm²/mg at 100 MeV.

(b)

Figure 2-17. A diagram of identical ions hitting a junction at normal incidence (left) and at a glancing incidence (right) – much more charge will be collected by the junction in the glancing case (a); plot of  $LET_{EFF}$  of an iron ion as a function of ion energy. Each curve represents a different angle of incidence, with  $LET_{EFF}$  increasing with increasing angle (b).<sup>[35]</sup>

of radiation to be shielded and its energy. For microelectronics placed in high-radiation environments – medical diagnostic equipment, scanners or most aerospace applications – shielding can help reduce the amount of radiation reaching the microelectronics and thus reduce the severity of radiation effects. Radiation-shielding properties of matter are based on the material's attenuation of the specific radiation of concern.

Attenuation is a measure of the reduction in radiation intensity as a function of the thickness of the shielding material. Shielding materials are selected based on maximizing attenuation while minimizing the required mass of the shield (or its thickness). Additionally, shielding materials should not generate a high flux of secondary particles when exposed to environmental radiation. Shielding reduces the incident flux of radiation on microelectronics and thus impacts both dose and SEEs.

The actual impact of shielding depends not only on the shield material and thickness, but also on the type and energy spectrum of the radiation being shielded against. As an example, electrons are shielded relatively easily by thin metal shields, while neutrons require meters of shield material to reduce their numbers.

In the space environment, shielding can help mitigate dose effects in electronics and human body doses in space crews. However, space radiation extends to extremely high energies, so shielding is never completely effective.

Another severe constraint in spacecraft is the mass and size of the final payload or vehicle. Large, heavy shielding is often not a viable option due to mass/space constraints. In typical spacecraft applications, the shield material is usually aluminum, with thicknesses of 100-300 mils (2.5-7.6 mm). Aluminum shielding does attenuate low-energy ions and electrons, but has a minimal effect on high-energy radiation from galactic cosmic rays.

Aluminum thicknesses in excess of ~50 mils absorb the majority of incident electrons. However, increasing the shielding thickness beyond that renders diminishing returns. **Figure 2-18** illustrates the TID in low Earth orbit as a function of aluminum shield thickness for three space radiation sources (electrons, protons and Bremsstrahlung radiation).<sup>[36]</sup> The saturation in the curve means that adding additional shielding thickness is of limited effectiveness in further reducing TID. The saturation occurs because a large fraction of the incident proton radiation is of such high energy that several millimeters of aluminum are insufficient to significantly reduce their numbers.

In natural terrestrial environments, shielding is usually not necessary or constrained by the application. In early DRAM production, polyimide was used as a shielding material in an effort to protect sensitive devices from alpha particles emitted from impurities in packaging materials.<sup>[37]</sup> But trends in using ultra-low alpha emission materials negated the effectiveness of such in-package shielding.

#### Low Earth orbit

![Figure 2-18: Plot of TID in low Earth orbit as a function of aluminum shielding thickness for three space radiations: protons, electrons and Bremsstrahlung.](1cd6a2d6e58e0e6d75c879a999be06ef_img.jpg)

A line graph showing the Total Ionizing Dose (TID) in rad(AI) on a logarithmic y-axis (from 10<sup>1</sup> to 10<sup>6</sup>) versus Aluminum (Al) shield thickness in mils on a linear x-axis (from 0 to 300). Three curves are plotted: 'Total' (the highest curve, starting at ~10<sup>5.5</sup> and decreasing to ~10<sup>3.5</sup> at 300 mils), 'Protons' (starting at ~10<sup>5.5</sup> and decreasing to ~10<sup>3.5</sup> at 300 mils), and 'Electrons' (starting at ~10<sup>5.5</sup> and decreasing to ~10<sup>2.5</sup> at 300 mils). A fourth curve, 'Bremsstrahlung', starts at ~10<sup>2.5</sup> and decreases to ~10<sup>1.5</sup> at 300 mils.

Figure 2-18: Plot of TID in low Earth orbit as a function of aluminum shielding thickness for three space radiations: protons, electrons and Bremsstrahlung.

**Figure 2-18.** Plot of TID in low Earth orbit as a function of aluminum shielding thickness for three space radiations: protons, electrons and Bremsstrahlung.<sup>[36]</sup>

For microelectronics used in aviation, the radiation environment is high enough to be a major reliability concern, but the key component of the commercial flight-altitude environment is cosmic-ray neutrons, which are not easily shielded. Other means address the reliability, such as redundancy and architectural resilience.

The main types of artificial radiation environments that require shielding in specific industrial and medical applications are X-ray and gamma photons, neutrons, protons, and alpha and beta particles, as shown in **Figure 2-19**. In most cases, shields for absorbing gamma and X-ray radiation are based on high-density, high-Z metals that are more effective than lower-density material. "More effective" here means that a shield made with a denser, high-Z material will require less material thickness. Lead is often used as a shielding material for gamma rays and X-rays due to its high density, high Z number and low cost. Neutrons have no charge and hence do not interact via Coulomb forces, so they easily pass through most high-Z and dense shielding materials. Materials comprising low atomic number elements usually have fairly high neutron-capture cross-sections and are more effective at stopping neutrons.

![Figure 2-19: Effective shielding materials for different specific particle radiations encountered in industrial/medical environments.](15143cc30398cac09dbe6cdf9bfceeed_img.jpg)

A diagram showing four types of shielding materials represented by vertical bars of increasing thickness and density from left to right: 'Paper', 'Thin plates made of wood, aluminum, etc.', 'Lead, iron and other thick metal plates', and 'Water, concrete, etc.'. Red arrows indicate the penetration of different radiation types: 'Alpha' is stopped by paper; 'Beta' is stopped by thin plates; 'X-ray' and 'Gamma' are stopped by lead/iron plates; 'Neutron' passes through all three but is stopped by the water/concrete block.

Figure 2-19: Effective shielding materials for different specific particle radiations encountered in industrial/medical environments.

**Figure 2-19.** Effective shielding materials for different specific particle radiations encountered in industrial/medical environments.<sup>[39]</sup>

Hydrogen and hydrogen-based materials are often used as neutron shielding. Targets with a high concentration of hydrogen atoms, such as plastics and concrete (high water content), can form efficient neutron shields. In nuclear reactor and accelerator environments with high neutron fluxes, shielding is often in the form of thick (meters-thick) concrete and steel shields.

Proton shielding has similar requirements, since a lot of neutrons are generated when protons impact heavy high-Z targets.

For blocking alpha and beta radiation, thickness is less of a concern. A thin sheet of metal or other material is sufficient for shielding against alpha particles (~0.1 mm). Heavy metals are not good candidates for stopping beta particles (energetic electrons emitted from unstable nuclei) because they can produce a large amount of secondary radiation via Bremsstrahlung when traveling through high-Z materials. Plastic or low-Z materials a few millimeters thick can efficiently shield beta radiation.

### References

- 1 A. P. French and E. F. Taylor, "An Introduction to Quantum Physics," New York, W. W. Norton & Co., 1978, pp. 55-64.
- 2 E. Hecht, "Optics," 2nd edition, Reading, Addison Wesley Publishing Co., 1987, pp. 422-424.
- 3 W. J. Smith, "Modern Optical Engineering: The Design of Optical Systems," 2nd edition, New York, McGraw-Hill, 1990, pp. 151-154.
- 4 N. Tsoulfanidis, "Measurement and Detection of Radiation," 2nd edition, New York, Taylor & Francis, 1995, pp. 122-139.
- 5 J. F. Ziegler, J. P. Biersack and U. Littmark, "The Stopping and Range of Ions in Matter," Volume 1, New York, Pergamon, 1985.
- 6 Simulated output from SRIM 2013 software downloaded at [www.srim.org](http://www.srim.org).
- 7 K. S. Krane, "Introductory Nuclear Physics," New York, John Wiley & Sons, 1988, pp. 392-394.
- 8 N. Tsoulfanidis, "Measurement and Detection of Radiation," 2nd edition, New York, Taylor & Francis, 1995, pp. 145-150.
- 9 A. P. French and E. F. Taylor, "An Introduction to Quantum Physics," New York, W. W. Norton & Co., 1978, pp. 18-23.
- 10 G. F. Knoll, "Radiation Detection and Measurement," 2nd edition, New York, John Wiley & Sons, 1979, pp. 50-54.
- 11 N. Tsoulfanidis, "Measurement and Detection of Radiation," 2nd edition, New York, Taylor & Francis, 1995, pp. 153-158.
- 12 G. F. Knoll, "Radiation Detection and Measurement," 2nd edition, New York, John Wiley & Sons, 1979, pp. 31-34.
- 13 M. J. Berger, J. H. Hubbell, S. M. Seltzer, J. Chang, J. S. Coursey et al., "XCOM: Photon Cross Sections Database," National Institute of Standards and Technology.
- 14 G. F. Knoll, "Radiation Detection and Measurement," 2nd edition, New York, John Wiley & Sons, 1979, pp. 44-49.
- 15 N. Tsoulfanidis, "Measurement and Detection of Radiation," 2nd edition, New York, Taylor & Francis, 1995, pp. 122-142.
- 16 Texas A&M University presentation, "Interaction of Electrons with Matter," [https://moreira.tamu.edu/BAEN625/TOC\\_files/chapt4b08.pdf](https://moreira.tamu.edu/BAEN625/TOC_files/chapt4b08.pdf).
- 17 M. J. Berger, J. S. Coursey, M. A. Zucker and J. Chang, "ESTAR: Stopping Powers and Ranges for Electrons," National Institute of Standards and Technology.
- 18 M. Veltman, "Facts and Mysteries in Elementary Particle Physics," New Jersey, World Scientific, 2003, p. 12.
- 19 W. N. Cottingham and D. A. Greenwood, "An Introduction to the Standard Model of Particle Physics," Cambridge, Cambridge University Press, 1998, pp. 1-14.
- 20 "Elastic and Inelastic Collisions." <http://hyperphysics.phy-astr.gsu.edu/hbase/elacol.html>.
- 21 K. S. Krane, "Introductory Nuclear Physics," New York, John Wiley & Sons, 1988, pp. 378-520.
- 22 K. P. Rodbell, D. F. Heidel, H. K. Tang, M. S. Gordon, P. Oldiges et al., "Low-Energy Proton-Induced Single-Event-Upsets in 65 nm Node Silicon-on-Insulator, Latches and Memory Cells," *IEEE Trans. Nuclear Sci.* 54(6), Dec. 2007, pp. 2474-2479.
- 23 "ENDF/B-VII Incident-Neutron Data," T2.lanl.gov, July 2007.
- 24 G. F. Knoll, "Radiation Detection and Measurement," 2nd edition, New York, John Wiley & Sons, 1979, pp. 31-34.
- 25 S. R. Messenger, E. A. Burke, G. P. Summers, M. A. Xapsos, R. J. Walters et al., "Nonionizing energy loss (NIEL) for heavy ions," *IEEE Trans. Nuclear Sci.* 46(6), Dec. 1999, pp. 1595-1602.
- 26 Simulated output from SRIM 2013 software downloaded at [www.srim.org](http://www.srim.org).
- 27 R. N. Hamm, J. E. Turner, H. A. Wright and R. H. Ritchie, "Heavy-Ion Track Structure in Silicon," *IEEE Trans. Nuclear Sci.* 26(6), Dec. 1979, pp. 4892-4895..
- 28 W. J. Stapor, P. T. McDonald, A. R. Knudson, A. B. Campbell and B. G. Glagola, "Charge collection in silicon for ions of different energy but same linear energy transfer (LET)," *IEEE Trans. Nuclear Sci.* 35(6), Dec. 1988, pp. 1585-1590.
- 29 M. Murat, A. Akkerman and J. Barak, "Electron and Ion Tracks in Silicon: Spatial and Temporal Evolution," *IEEE Trans. Nuclear Sci.* 55(6), Dec. 2008, pp. 3046-3054.
- 30 Simulated output from SRIM 2013 software downloaded at [www.srim.org](http://www.srim.org).
- 31 G. F. Knoll, "Radiation Detection and Measurement," 2nd edition, New York, John Wiley & Sons, 1979, pp. 33-37.
- 32 D. S. Yaney, J. T. Nelson and L. L. Vanskike, "Alpha-particle tracks in silicon and their effect on dynamic MOS RAM reliability," *IEEE Trans. Electron Dev.* 26(1), Feb. 1979, pp. 10-16.
- 33 R. C. Baumann, "Investigation of the Effectiveness of Polyimide Films for the Stopping of Alpha Particles in Megabit Memory Devices," MOS Memory QRA, Texas Instruments Technical Report, 1991, pp. 1-22.
- 34 T. P. Ma and P. V. Dressendorfer, "Ionizing Radiation Effects in MOS Devices and Circuits," New York, John Wiley & Sons, 1989, pp. 524-526.
- 35 Simulated output from SRIM 2013 software downloaded at [www.srim.org](http://www.srim.org).
- 36 J. W. Keller and N. M. Schaeffer, "Radiation shielding for space vehicles," *Electrical Engineering* 79(12), 1960, pp. 1049-1054.
- 37 M. Kojima, H. Sekine, H. Suzuki, H. Satou, D. Makino et al., "Photosensitive polyimide for IC devices," Proc. 39th *Electronic Components Conference*, 1989, pp. 920-924.
- 38 W. C. Fan, C. R. Drumm, S. B. Roeske and G. J. Scrivner, "Shielding considerations for satellite microelectronics," *IEEE Trans. Nuclear Sci.* 43(6), Dec. 1996, pp. 2790-2796.
- 39 B. F. Maskewitz, D. K. Trubey and R. W. Roussin, "Materials Information in the Radiation Shielding Information Center," CONF. 740424-2, April 1974, pp. 1-10.

# Chapter 3: Radiation effects in electronics – dose effects

As illustrated in **Figure 3-1**, radiation effects impact semiconductor devices in three fundamental ways:

- Single-event effects (SEEs) are random, instantaneous disruptions triggered by the passage of a single particle or photon. One radiation event equals one upset occurrence. An upset could lead to failures in more than one device or bit for each individual radiation event.
- Dose effects are characterized by lasting parametric shifts that accumulate over time due to chronic radiation exposure (a large number of radiation events), ultimately leading the semiconductor device to drift out of tolerance and eventually fail.
- Dose-rate effects entail the delivery of extremely high dose rates (HDRs) over a brief time interval, inducing SEE-like effects.

The focus of this chapter is dose effects. There are two categories of dose effects: total ionizing dose (TID) caused by radiation-induced charge generation/trapping and neutron dose/proton dose (ND/PD) related to the accumulation of physical damage (commonly called displacement damage [DD]) such that electrical properties degrade as the dose increases.

![Venn diagram showing the relationship between Dose effects, Dose-rate effects, and Single-event effects.](b58cedaf15ad4f0edee5621820865ccc_img.jpg)

A Venn diagram with three overlapping circles. The left circle is red and labeled 'Dose effects'. The right circle is blue and labeled 'Single-event effects'. The intersection of these two circles is shaded light blue and labeled 'Dose-rate effects'.

Venn diagram showing the relationship between Dose effects, Dose-rate effects, and Single-event effects.

**Figure 3-1.** A diagram showing the ways in which radiation causes reliability failures in semiconductor devices exposed to radiation.

### 3.1 Total ionizing dose effects

In response to radiation exposure, TID sensitivity can limit product reliability and functionality. At a high level, the key mechanism driving TID is the generation, transport and trapping of holes in the insulation used as gate and isolation oxides in metal-oxide semiconductor (MOS) and bipolar devices at or near the silicon-oxide interface. At a sufficiently high absorbed dose, isolation leakage in complementary MOS (CMOS) circuits will lead to functional failures. In bipolar transistors, oxide charge and interface states in the isolation increase the recombination rate, forcing the base current to increase for a given collector current. In bipolar transistors, TID leads to a reduction in the current gain of the device.

As described in previous chapters, the creation of electronic charge is one of the primary manifestations of radiation's interaction with

matter. Each type of radiation (photons, ions, neutrons, electrons, etc.) loses energy in a variety of different ways and at different rates while traversing matter. The quantity and distribution of excess charge generated in the material is a function of the type of radiation, its energy, its trajectory and its properties. TID is defined as the energy absorbed by a unit mass of material when exposed to ionizing radiation. The overall exposure is quantified in units of radiation-absorbed dose, or rad. A rad is a measure of the absorbed energy per unit mass of a specific material. Originally defined in centimeter-gram-second (cgs) units, a rad is the dose that causes the absorption of 100 ergs by one gram of matter.

Most semiconductor applications report TID as absorbed dose in silicon or rad. The International System of Units uses grays (Gy), with  $1 \text{ Gy} = 100 \text{ krad} = 1 \text{ J/kg}$ . Since most specification and military standards use the older unit of rad, we report all TID in rad(Si) or krad(Si).

In conductor and semiconductor materials such as metals or silicon, respectively, any excess charge generated by the passage of an ionizing radiation event will be largely compensated by recombination, and/or dissipated by drift and diffusion. In other words, in conducting and semiconducting materials, excess charge is effectively transported so that all excess-generated charge is removed from the device in a short time interval. This short-lived charge transient can cause a multitude of SEEs, but from a TID perspective, no charge is accumulated or stored.

The case is radically different for insulating materials. Insulators are characterized by wide band gaps, low free-carrier densities and low carrier mobility, at least for holes. Frequently, the material has a lot of bulk traps. In semiconductor devices, the most common insulator is silicon dioxide ( $\text{SiO}_2$ ), which is used to form the gates of MOS transistors and as isolation material in both MOS and bipolar technologies. The absorption of energy from radiation exposure creates a number of effects in the oxide that degrade device performance and potentially its functionality.

**Figure 3-2** is a band diagram of the MOS stack that forms metal-oxide semiconductor field-effect transistors (MOSFETs) and bipolar junction transistors (BJTs), illustrating excess charge generation by exposure to radiation, and the subsequent transport and trapping of that excess charge at or near the interface in  $\text{SiO}_2$  on silicon. The diagram represents distance (or depth) on the horizontal axis and electron energy on the vertical axis. More energetic electrons appear higher on the diagram, and a positive voltage pulls the energy bands down. The positively biased polysilicon (or metal) gate electrode is shown on the left, with the insulator layer in the middle. The insulator energy bands are slanted electric field from the gate and silicon electrodes. Energy from incident radiation is absorbed in the insulator by the formation of electron-hole (e-h) pairs. Approximately 17 eV of energy is required for the production of each single e-h pair in oxide. The creation of excess charge occurs on the femtosecond timescale.

![Figure 3-2: Band diagram of a MOS device with positive gate bias showing the effect of ionizing radiation on carrier generation, transporting and trapping. The diagram shows energy levels for SiO2 and Si. (1) E-h pairs generated by ionized radiation. (2) Hopping transport of holes through localized states in SiO2 bulk. (3) Deep hole trapping near Si/SiO2 interface. (4) Radiation-induced interface traps within Si bandgap. A 1.1 eV energy gap is indicated between the Si valence band and the Si/SiO2 interface.](157e8c1d80a02c8eee893c2ea60a77a8_img.jpg)

Figure 3-2: Band diagram of a MOS device with positive gate bias showing the effect of ionizing radiation on carrier generation, transporting and trapping. The diagram shows energy levels for SiO2 and Si. (1) E-h pairs generated by ionized radiation. (2) Hopping transport of holes through localized states in SiO2 bulk. (3) Deep hole trapping near Si/SiO2 interface. (4) Radiation-induced interface traps within Si bandgap. A 1.1 eV energy gap is indicated between the Si valence band and the Si/SiO2 interface.

**Figure 3-2. Band diagram of a MOS device with positive gate bias showing the effect of ionizing radiation on carrier generation, transporting and trapping.<sup>[1]</sup>**

The initial concentration of excess carriers produced by the radiation is reduced, as the e-h pairs begin to recombine immediately after their formation. If the charges were truly immobile, all of the excess e-h pairs would recombine before transporting; the pairs would be trapped and TID would not be a problem, because there would be no trapped charge or interface states. However, in oxides, electron mobility is much higher than that of holes, so transport by diffusion – and especially drift in cases where an electric field is present – will rapidly remove excess electrons from the oxide film.

Within picoseconds, all of the remaining electrons are removed from the oxide, effectively shutting off any further charge loss by recombination. The fraction of unrecombined hole charge remaining (known as the fractional yield) after the electrons have been removed is a strong function of the type of radiation and the electric field in the gate oxide.

TID effects in MOSs are typically exacerbated in the presence of a strong electric field, since this maximizes the charge yield, as shown in **Figure 3-3**. Note also that gamma-ray radiation is the most effective in terms of creating TID by virtue of its high fractional yield. The next most effective type is radiation from X-rays, followed by electrons and light ions. Heavy ions are the least effective in generating TID effects.

Fractional yield is inversely proportional to the linear energy transfer (LET) (or charge density) generated within the oxide volume, primarily because the e-h recombination rate is a strong function of the amount of excess charge present. Heavier, more highly charged particles generate much more charge per unit distance because they have a higher LET. Compared to photons and electrons, the recombination rate is greatly increased for ions, and a larger fraction of the generated e-h pairs recombine after the event.

This implies that testing with gamma-ray photons will actually generate the worst-case TID response in a MOS structure. The rapid removal of the highly mobile electrons from the oxide leaves a number of excess positively charged holes. The holes themselves actually create a local distortion in the insulator bond structure surrounding them.

These localized structural deformations are called small polarons. The holes are effectively self-trapped in the oxide by virtue of the polaron formation. The holes do migrate – by drift and diffusion – but relatively slowly, “hopping” from adjacent shallow traps in the valence band and carrying the polaron with them as they move.

The hopping process breaks chemical bonds, releasing trapped protons (H<sup>+</sup>). These protons are free to diffuse or “drift” in the same direction as the holes. The migration of holes and protons to the oxide interface occurs over a time frame of seconds. Ultimately, holes that migrate toward the SiO<sub>2</sub>-silicon interface get captured by mid-band-gap traps near the interface – initially causing a positive charge buildup – or are captured at the interface itself, where they create interface states that are positive, neutral or negative. The deep-hole traps reside in the oxide one or more atomic spacings away from the SiO<sub>2</sub>-silicon interface.

![Figure 3-3: Graph showing Fractional yield (Y-axis, 0 to 1.0) versus Electrified field (MV/cm) (X-axis, 0 to 5). The graph plots data for 12-MeV electrons and 60Co (solid blue line), 10-keV X-rays (dashed red line), 5-keV electrons (dashed green line), 700-keV protons (dashed cyan line), Positive bias (dashed magenta line), and 2 MeV alpha particles (dashed black line). The fractional yield increases with both the electrified field and the energy of the ionizing radiation. Higher energy radiation (like 12-MeV electrons and 60Co) results in a higher fractional yield compared to lower energy radiation (like 2 MeV alpha particles).](f52d4f86fa07f74697e9e428413833ab_img.jpg)

Figure 3-3: Graph showing Fractional yield (Y-axis, 0 to 1.0) versus Electrified field (MV/cm) (X-axis, 0 to 5). The graph plots data for 12-MeV electrons and 60Co (solid blue line), 10-keV X-rays (dashed red line), 5-keV electrons (dashed green line), 700-keV protons (dashed cyan line), Positive bias (dashed magenta line), and 2 MeV alpha particles (dashed black line). The fractional yield increases with both the electrified field and the energy of the ionizing radiation. Higher energy radiation (like 12-MeV electrons and 60Co) results in a higher fractional yield compared to lower energy radiation (like 2 MeV alpha particles).

**Figure 3-3. This diagram shows charge-yield fraction as a function of the oxide electric field for different types of ionizing radiation.<sup>[1]</sup> Note that more highly charged particles have a lower fractional yield.**

Hole traps are created by naturally occurring defects that appear when excess silicon from the substrate diffuses into the oxide and creates oxygen vacancies (oxygen-depleted oxide = SiO<sub>x</sub>, where x < 2). These oxygen vacancies form hole traps that are energetically deep so that at room temperature, the thermal energy is not large enough to cause hole release from the traps. The trapped holes are relatively stable and generally immobile.

Holes trapped at the oxygen vacancies are responsible for an accumulated positive charge in MOS and bipolar devices during irradiation. Tunneling or thermalized electrons injected from the silicon that neutralize the hole charge compensate for the positive hole charge. In such cases, the hole can recombine with the injected electron and permanently remove the charge. The normal bonding structure is re-established to an unoccupied oxygen vacancy; thus the defect is considered to be “annealed out.”

In other cases, the hole and electron do not recombine but form a dipole pair that can be polarized. Often referred to as border traps, these oxide traps exchange charge with the silicon substrate and can act as a neutral, positive or negative charge.

This complex set of charge states explains “rebound behavior” – the instability in the TID-induced threshold voltage shift – observed in MOS transistors as a function of bias and temperature after radiation exposure.  $\text{SiO}_2$ , grown even under the best conditions, has a certain density of surface structural defects at the interface between the oxide and the silicon.

In bulk silicon, every silicon atom is covalently bonded to each of its four nearest neighbors. At the transition between pure silicon and  $\text{SiO}_2$ , a region of oxygen vacancies forms on the oxide side. At the actual surface where the silicon meets the oxide, less-stable trivalent silicon complexes form where the silicon atom only bonds to three other silicon atoms, leaving one of its four available bonds free or dangling. This dangling bond is electrically active and can interact with carriers in the silicon substrate near the interface. In normal semiconductor processing, hydrogen passivation hides these defects when hydrogen forms a stable bond. Released during hole transport, protons reaching the interface depassivate the bonded hydrogen, re-establishing dangling bonds that once again become electrically active.

Radiation-induced interface traps at the silicon- $\text{SiO}_2$  interface induce voltage-dependent threshold shifts – positive or negative depending on bias – just like the trapped-hole charge. In addition, these shifts increase surface recombination rates while decreasing carrier mobility. Both the trapped-hole charge and interface-state charge cause dose-dependent device marginalities in both MOS and bipolar devices.

Rebound or super-recovery is the reduction and eventual reversal of the initial threshold voltage shift induced immediately after a radiation exposure. It is primarily a concern in MOS devices, where strong bias (a high electric field) is usually present in the gate oxide.

![Figure 3-4: A line graph showing the time dependence of threshold voltage (VT) in an N-channel MOS (NMOS) transistor. The x-axis is 'Time (hrs) (x10^6 rads)' on a logarithmic scale from PRE to 1000. The y-axis is 'Voltage' from -3 to 4. Three curves are shown: Vt (solid red line with triangles), Vt (dashed blue line with squares), and Vt (dotted green line with circles). All curves show a sharp drop during irradiation and a subsequent recovery during anneal. The Vt curve (solid red) shows the most significant recovery, reaching a plateau around 3.5V. The Vt curve (dashed blue) shows a smaller recovery, reaching a plateau around 1.5V. The Vt curve (dotted green) shows the least recovery, reaching a plateau around 0.5V. The graph is divided into 'Irradiation' and 'Anneal' regions.](74448f9178da618d823e5a5dadc56fb5_img.jpg)

Figure 3-4: A line graph showing the time dependence of threshold voltage (VT) in an N-channel MOS (NMOS) transistor. The x-axis is 'Time (hrs) (x10^6 rads)' on a logarithmic scale from PRE to 1000. The y-axis is 'Voltage' from -3 to 4. Three curves are shown: Vt (solid red line with triangles), Vt (dashed blue line with squares), and Vt (dotted green line with circles). All curves show a sharp drop during irradiation and a subsequent recovery during anneal. The Vt curve (solid red) shows the most significant recovery, reaching a plateau around 3.5V. The Vt curve (dashed blue) shows a smaller recovery, reaching a plateau around 1.5V. The Vt curve (dotted green) shows the least recovery, reaching a plateau around 0.5V. The graph is divided into 'Irradiation' and 'Anneal' regions.

**Figure 3-4.** This plot illustrates time dependence of  $V_T$  in an N-channel MOS (NMOS) transistor during and after a 1-Mrad(Si) high-dose-rate exposure. Note the strong bias and temperature effect on the annealing rates.<sup>[2]</sup>

Figure 3-4 illustrates the time evolution of the threshold voltage,  $V_T$ , and the change in  $V_T$  due to changes in the number of deep-oxide hole traps and interface states ( $\Delta V_{OT}$  and  $\Delta V_{IT}$ , respectively). This experiment was repeated at two different annealing temperatures. During irradiation, interface-state charge and oxide-trapped charge accumulate. Immediately after exposure, the positive trapped-hole charge dominates and the NMOS  $V_T$  decreases. Leakage increases, and the transistor is easier to turn on. After irradiation with a positive gate bias, electrons from the silicon tunnel into the oxide and neutralize the trapped-hole charge through the recombination of electrons that tunnel to the holes and the formation of trapped dipoles. The annealing process is defined by compensation of the positive hole charge such that the typically negative interface-state charge dominates, thereby increasing  $V_T$ .

This radiation-induced shift, followed by a shift the other way during annealing, is known as rebound. Rebound is really limited to older (thick) oxide processes and does not occur in modern MOSFET processes. The magnitude of the rebound depends on temperature and bias. Increasing temperature increases the annealing rate of oxide-trapped charge, but generally has a much less pronounced effect on surface-state annealing. The rebound effect is minimized in oxide processes where the density of interface states is inherently low.

As part of the standard radiation-hardness-assured (RHA) flow, Texas Instruments tests for rebound according to military standard MIL-STD-883, TM1019 (see Chapter 7), with 168-hour annealing at 100°C under worst-case bias conditions after post-irradiation characterization to determine the magnitude of the rebound if it occurs.

Degradation due to TID presents one additional complication primarily affecting bipolar devices. Dose-rate sensitivity effects are not usually associated with MOSFETs, which can typically be accurately characterized at HDRs. Some bipolar devices suffer significantly more degradation when radiation exposure occurs at a low dose rate (LDR). In other words, dose rates that accumulate slowly cause more degradation than if the same device had been exposed at an HDR.

This LDR effect or enhanced low-dose-rate sensitivity (ELDRS) is a feature observed in some bipolar devices and thus requires validation on any new device.<sup>[4-7]</sup> Understanding if a device has ELDRS is critical because the actual dose rates encountered in most radiation environments, including space environments, are very low. Conducting HDR tests only on devices with ELDRS would lead to significantly underestimated TID sensitivity. A device thought to be robust to TID would actually fail long before it was expected to based on HDR results alone.

The plot in Figure 3-5 shows several bipolar devices tested to the same TID level using a large range of dose rates. Clearly, there is a wide range of ELDRS sensitivity for different devices: LM324 devices are very dose-rate sensitive, while LM108 devices appear to have no sensitivity to dose rate at all.

ELDRS and TID are extremely sensitive to the process used to form and anneal the oxides; thus the same device from two different vendors (even two devices from the same vendor but manufactured at two different sites) can have altogether different TID and dose-rate dependencies. One of the onerous aspects of ELDRS testing is the long irradiation times required. HDR testing, with a typical dose rate in the range of ~100 rad/s, takes approximately 20 minutes to

reach 100 krad(Si). In contrast, the same 100-krad(Si) target dose takes approximately 116 days, or nearly four months at the typical LDR of  $\sim 0.01$  rad(Si)/s specified for ELDRS tests in MIL-STD-883 TM1019 (see Chapter 7).

There were many competing theories upon EDLRS' initial discovery; even now, there is not yet full agreement about some of the specific mechanisms. The basic cause of dose-rate dependence is related to the fact that there is a higher density of radiation-induced excess e-h pairs at HDRs. Since the recombination rate increases with excess carrier density, enhanced recombination claims many more holes at HDR exposures. This is especially true in bipolar transistors, where the oxide is used as isolation. The external electric field is weak, so excess electrons will not be removed as quickly as in strongly biased MOS devices.

![Figure 3-5: Plot showing TID degradation as a function of dose rate for several different bipolar devices. The y-axis is 'Relative damage (normalized to 50 (rad(Si)/s))' ranging from 0 to 6. The x-axis is 'Dose rate (rad(Si)/s)' on a log scale from 0.001 to 100. Data series include LM324 (pnp), LM111 (pnp), LM101 (npn), and LM108 (npn). A shaded region at the bottom is labeled 'Discrete transistors'.](1c2028183a35357e7238438a4af9cab7_img.jpg)

Figure 3-5: Plot showing TID degradation as a function of dose rate for several different bipolar devices. The y-axis is 'Relative damage (normalized to 50 (rad(Si)/s))' ranging from 0 to 6. The x-axis is 'Dose rate (rad(Si)/s)' on a log scale from 0.001 to 100. Data series include LM324 (pnp), LM111 (pnp), LM101 (npn), and LM108 (npn). A shaded region at the bottom is labeled 'Discrete transistors'.

**Figure 3-5.** Plot showing TID degradation as a function of dose rate for several different bipolar devices. All devices were tested to the same TID level, but the variable was the dose rate.<sup>[6]</sup>

The removal of a larger number of holes leads to a concurrent reduction in the number of protons as well. Because the holes are responsible for the liberation of trapped protons, and it is the protons reacting with passivated interface sites that create the electrically active interface states, it follows that reducing the number of protons reaching the interface will reduce the amount of parametric device degradation. Thus, the degradation is lower at HDRs than at LDRs, where more trapped holes and released protons cause greater degradation at the interface. Since the actual space environment exposure to radiation is at very low effective dose rates (Figure 3-6), it is crucially important to determine if a device has ELDRS. As part of the RHA specification for bipolar technologies, Texas Instruments follows ELDRS characterization procedures as required by MIL-STD-883 test method (TM) 1019.

The high-quality gate oxides in today's advanced CMOS technologies – much thinner than 10 nm – have minimized TID-induced threshold voltage shifts in individual transistors for most applications. TID can still have some impact in low-noise or very-high-speed switching applications. Even in these technologies,

however, the field isolation for adjacent transistors remains relatively thick and will exhibit sensitivity to TID-induced charge.

Isolation oxides are often fabricated with different growth/deposition techniques that lead to different properties and quality. Although these oxides meet the electrical isolation and reliability performance for which they are optimized, their trapping properties are considerably poorer than those of the gate oxides. These oxides generally have a higher trap density, and thus degrade more from TID damage when exposed to radiation.

![Figure 3-6: Plot showing radiation-induced input bias current increases in bipolar devices as a function of total dose at several different dose rates. The y-axis is 'Input bias current (nA)' on a log scale from 10^1 to 10^3. The x-axis is 'Total dose (rad(Si)/s)' on a log scale from 10^2 to 10^5. Data series include 'Substrate PNP input transistor', 'Spacecraft data* (dose rate varies)', '0.01 rads/s', '10 rads/s', and '60Co-gamma data'.](e51f9764097b236acbf8f544491dd24f_img.jpg)

Figure 3-6: Plot showing radiation-induced input bias current increases in bipolar devices as a function of total dose at several different dose rates. The y-axis is 'Input bias current (nA)' on a log scale from 10^1 to 10^3. The x-axis is 'Total dose (rad(Si)/s)' on a log scale from 10^2 to 10^5. Data series include 'Substrate PNP input transistor', 'Spacecraft data\* (dose rate varies)', '0.01 rads/s', '10 rads/s', and '60Co-gamma data'.

**Figure 3-6.** This plot shows that radiation-induced input bias current increases in bipolar devices as a function of total dose at several different dose rates. Degradation from actual spacecraft data correlates with  $^{60}\text{Co}$  results at the lowest dose-rate exposure.<sup>[19]</sup>

The two most common types of field-isolation oxides found in CMOS commercial products are local oxidation of silicon (LOCOS) and shallow-trench isolation (STI). The predominant failure mode for commercial MOS technologies is increased leakage current induced by positive hole charge trapping in the isolation oxides. Electric field fringing effects concentrate in the tapered bird's beak region at the edge of the LOCOS or at the top edge of the STI structure.<sup>[10]</sup> In these high-field regions, the P-type surface is depleted and/or inverted, reducing the turn-on voltage. Cases where surface inversion forms a parasitic conductive channel between the source and drain or neighboring n-well will result in excessive leakage. The I-V plot shown in Figure 3-7 illustrates the changes in NMOS characteristics after irradiation.

Note that while the threshold voltage of the gate structure shifts a bit (lowered threshold voltage), a large reduction in the isolation threshold voltage has occurred. This TID-induced parasitic leakage in the field isolation increases the static power-supply current. At higher doses, the increase in parasitic leakage can increase to the point where the device exceeds its rating or fails. The positive charge trapping tends to reduce leakage and increases threshold voltage in PMOS transistors, so TID failures are not usually linked to PMOS.

![Figure 3-7: I-V plot of NMOS transistor pre- and post-radiation exposure. The plot shows drain current I_DS (A) on a logarithmic y-axis (from 10^-12 to 10^-2) versus gate voltage V_GS (V) on a linear x-axis (from -6 to 14). Four curves are shown: 'Pre-rad (gate)' (dark blue), 'Post-rad (gate)' (light blue), 'Pre-rad (field or gate)' (dark blue), and 'Post-rad (field or gate)' (light blue). The 'Post-rad (field or gate)' curve shows a significant increase in leakage current at low V_GS compared to the 'Pre-rad (field or gate)' curve. The 'Post-rad (gate)' curve is slightly higher than the 'Pre-rad (gate)' curve at higher V_GS.](5fdd55201f3f090a54d10ffe9de2f068_img.jpg)

Figure 3-7: I-V plot of NMOS transistor pre- and post-radiation exposure. The plot shows drain current I\_DS (A) on a logarithmic y-axis (from 10^-12 to 10^-2) versus gate voltage V\_GS (V) on a linear x-axis (from -6 to 14). Four curves are shown: 'Pre-rad (gate)' (dark blue), 'Post-rad (gate)' (light blue), 'Pre-rad (field or gate)' (dark blue), and 'Post-rad (field or gate)' (light blue). The 'Post-rad (field or gate)' curve shows a significant increase in leakage current at low V\_GS compared to the 'Pre-rad (field or gate)' curve. The 'Post-rad (gate)' curve is slightly higher than the 'Pre-rad (gate)' curve at higher V\_GS.

**Figure 3-7. I-V plot of NMOS transistor pre- and post-radiation exposure.** Note the large increase in field-isolation leakage (light blue curves) that dominates most MOS TID failures.<sup>[70]</sup>

In general, the HDR TID response of MOS devices is the worst case. Although rebound can be an issue and requires characterization, it is generally related to older legacy processes and is usually not an issue for advanced MOS production processes. A secondary failure mode is related to the interface-state charge induced by the radiation exposure, which impacts channel-carrier mobility and noise margin in both PMOS and NMOS transistors used in low-noise or high-speed switching applications.

TID-induced damage in bipolar transistors usually manifests as a reduction in bipolar gain ( $h_{FE}$ ) with increasing total dose exposure.  $h_{FE}$  is defined as the ratio of the collector current and the base current. An increase in base current is usually the cause of TID-induced damage, but in devices with lightly doped collectors, decreases in collector current can also contribute to gain degradation.

**Figure 3-8** shows the gain of two bipolar transistors used in the Cassini spacecraft: the 2N3700 clearly failed due to large gain reductions. There are two primary TID-induced degradation mechanisms in bipolar transistors: an increase in the density of silicon-SiO<sub>2</sub> interface traps in the base region that affect the surface recombination rate, and the accumulation of positive oxide charge buildup that increases the surface recombination rate and changes the size of the emitter-base depletion region.

As the absorbed dose increases, the increase in both types of traps leads to increases in the surface recombination rate. The increased loss of minority carriers due to surface recombination in the base region requires a concurrent increase in the base current to produce the same output collector current, thus degrading the common-emitter current gain. The interface trap density and surface recombination rate typically track with increasing dose.

Oxide charge works primarily by modifying the area of the emitter-base region near the surface as dose increases. Because the trapped hole charge in the oxide is positive, the emitter-base surface area increases in NPN transistors, while decreasing in PNP transistors.

Lateral transistors typically exhibit more degradation than vertical devices at the same total dose, since more of the transistor action is located in close proximity to the oxide interface and surface, where the radiation-induced trapped charge has a more pronounced effect. LDR or ELDRS effects are important considerations for bipolar devices in space environments, because some devices degrade more at LDRs and require an exposure time of many months for proper characterization.

![Figure 3-8: Plot of bipolar gain h_FE as a function of dose. The y-axis is h_FE (0 to 125) and the x-axis is Total dose (krad[Si]) (0 to 50). Two data series are shown: 2N918 (I_C = 0.5 mA) represented by a dashed cyan line with circular markers, and 2N3700 (I_C = 0.1 mA) represented by a solid blue line with circular markers. The 2N918 gain remains relatively stable around 110-115, while the 2N3700 gain drops sharply from about 110 at 0 krad to near 0 by 20 krad.](79bd707e4636b9a1d4dbd443ef857814_img.jpg)

Figure 3-8: Plot of bipolar gain h\_FE as a function of dose. The y-axis is h\_FE (0 to 125) and the x-axis is Total dose (krad[Si]) (0 to 50). Two data series are shown: 2N918 (I\_C = 0.5 mA) represented by a dashed cyan line with circular markers, and 2N3700 (I\_C = 0.1 mA) represented by a solid blue line with circular markers. The 2N918 gain remains relatively stable around 110-115, while the 2N3700 gain drops sharply from about 110 at 0 krad to near 0 by 20 krad.

**Figure 3-8. Plot of bipolar gain as a function of dose (delivered at extreme LDRs) in devices used in the Cassini spacecraft.** Note the 10x gain reduction suffered by the 2N3700 due to ELDRS, while the gain of the 2N918 remains stable under ELDRS.<sup>[71]</sup>

### 3.2 Displacement damage

As mentioned at the beginning of this chapter, DD is another term that describes ND/PD effects related to the accumulation of physical damage to a crystal structure. Electrical properties degrade as ND/PD increases (electrons can also cause damage, although the cross-section is much smaller). This section limits the discussion to DD and its effects on semiconductor devices.

In response to prolonged ND/PD exposure, in addition to TID effects, increased levels of DD can limit semiconductor reliability/functionality. The key mechanism driving DD is the gradual degradation of semiconductor properties due to accumulated physical damage in the semiconductor's crystal structure. Unlike TID, which is a surface accumulation of trapped charge and interface states, DD is a volumetric effect in that the entire silicon volume is accumulating damage, which ultimately changes the electrical and optical properties of the bulk.

Virtually all microelectronics are based on the electrical properties of semiconductors like silicon. The silicon substrate on which most of the technology is based is single-crystal material grown and processed specifically to have extremely low defect densities, both in the volume and at the surface.

Defects in the crystal introduce local asymmetry in the crystal structure or lattice. These asymmetries change e-h pair interactions, thus causing changes in lifetime or scattering rates affecting mobility. They can drastically change the electrical/thermal/optical properties in the neighborhood of the crystal defect. If enough of these defects accumulate in a volume of silicon, its macroscopic properties can shift, leading to device shifts or a loss of functionality.

The damage increases incrementally each time an incident particle knocks a silicon nucleus off from its correct physical location within the crystal lattice. In these events, sufficient kinetic energy transfers from the incident particle to the silicon nucleus such that the binding energy is exceeded – freeing the silicon nucleus from its lattice site. This single dislocation produces a localized (low-mobility) vacancy; a gap in the structure where the silicon nucleus was; and a mobile interstitial defect, which is the displaced silicon nucleus between lattice positions.

Both of these defects can be electrically active, creating traps in the silicon band gap. While a single trap will generally not affect the macroscopic properties, just like dopants, the accumulation of a larger number of traps within a volume degrades critical semiconductor properties like carrier recombination, generation and transport properties.

In BJTs, the increased recombination rate in the base area increases the base current required for a given collector current, reducing current gain. MOS circuits are generally fairly robust against DD effects up to fairly high DD doses. At sufficiently high absorbed NDs/PDs, mobility degradation and free-carrier reductions caused by DD ultimately lead to reductions in MOSFET device drive strength and switching speed.

The creation of defects in device volumes is one of several manifestations of radiation's interaction with matter. The quantity and distribution of DD generated in the material is a function of the accumulated dose and type of radiation, its energy, its trajectory, and its material properties. Energy-loss mechanisms in matter can be divided into two general categories: those that produce charge (ionizing) and those that do not produce charge (nonionizing). Both ionizing and nonionizing effects work in concert to diminish the energy of radiation events traveling through matter. The ionization effect is relatively short-lived due to the drift and diffusion of the excess nonequilibrium charge. The recombination of charge then eliminates it. In contrast, nonionizing processes create some level of permanent damage. The temperature to anneal out DD is somewhere around 900°C.

Radiation-induced DD effects are referred to as nonionizing energy loss (NIEL) mechanisms. Since most radiations that cause DD traverse the bulk of active device regions, the damage occurs throughout the device volume as opposed to being restricted to surface or interface regions.

The primary radiations responsible for producing DD are energetic electrons, protons and/or neutrons. Heavy ions can also produce DD, but their rarity implies that they will not occur in sufficient numbers to create sizable device shifts. Energetic photons (in the million electron volts [eV] range) such as gamma rays or very-high-energy X-rays produce secondary electrons with sufficient kinetic energy to cause DD.

In stark contrast to ionizing mechanisms, where most radiations directly produce ionization, the crystal damage created by NIEL mechanisms is indirect and involves nuclear-scale cross-sections that are smaller than that of direct ionization mechanisms. Additionally, more energy is required to form a vacancy by displacement (~15 eV in silicon) than to create e-h pairs (~3.6 eV in silicon). Energy loss in matter from NIEL represents about 0.1% of the energy lost to ionizing mechanisms.

NIEL mechanisms create DD in four ways:

- At lower particle energy levels, the incident-charged particle (not applicable to neutrons) can scatter off a silicon atom via the Coulomb interaction, transferring enough of its kinetic energy to free the silicon atom.<sup>[12-16]</sup> The Coulomb scattering effect drops off exponentially as a function of increasing particle energy.
- The incident particle (including neutrons) interacts with silicon nuclei in nuclear elastic reactions – a billiard ball-like reaction that conserves momentum – transferring enough kinetic energy to produce silicon recoils. Coulomb and elastic reactions displace the silicon atom from its lattice site, creating a localized vacancy as well as a mobile interstitial silicon atom, as illustrated in [Figure 3-9](#).
- The incident particle interacts through inelastic reactions with the silicon nuclei, where some or all of the particle energy transfers to the nucleus, thus creating an excited nuclear state and ultimately decay. This decay is caused by either nuclear recoil or through the creation of secondary particles comprising ejected nucleons and larger nuclear fragments.
- Energetic secondary particles stop. As particle energy drops, it is better able to interact with phonons (lattice vibrations). By more effectively transferring its energy to phonons, the atoms nearby vibrate at higher amplitudes and frequencies as they absorb energy. This enhanced localized atomic vibration is equivalent to a higher temperature.

At some point, the local energy absorption causes localized areas of the silicon to melt. When this occurs, the electrical properties completely change, since areas that used to be crystalline silicon have transformed into amorphous silicon, with different band structure and defect states. These defect clusters have a large impact on generation/recombination, and if they occur in an active device layer (such as the MOSFET channel region or BJT base region), they can cause significant device degradation.

![Diagram illustrating the creation of a vacancy and an interstitial defect in a silicon crystal lattice by an energetic particle. An incident particle (red arrow) strikes a silicon atom (blue circle), displacing it from its lattice site. The displaced atom becomes an interstitial defect (dark gray circle), and the original lattice site becomes a vacancy (light gray circle).](4ca62688976b4bef770a81683f9d9eef_img.jpg)

The diagram shows a 2D grid of blue circles representing silicon atoms in a crystal lattice. A red arrow labeled 'Incident particle' enters from the top right and strikes one of the atoms. This atom is shown being displaced from its regular grid position. The new position it occupies is labeled 'Interstitial' and is represented by a dark gray circle. The original position it left behind is labeled 'Vacancy' and is represented by a light gray circle. The displacement is indicated by a curved arrow showing the path of the atom.

Diagram illustrating the creation of a vacancy and an interstitial defect in a silicon crystal lattice by an energetic particle. An incident particle (red arrow) strikes a silicon atom (blue circle), displacing it from its lattice site. The displaced atom becomes an interstitial defect (dark gray circle), and the original lattice site becomes a vacancy (light gray circle).

**Figure 3-9. Vacancy (light gray) and Interstitial defect (dark gray) created in a silicon crystal lattice by an energetic particle.<sup>[17]</sup>**

Coulomb scattering dominates at lower energies, with nuclear reactions dominating at incident particle energies in excess of ~10 MeV. **Figure 3-10** shows an example of NIEL created during proton irradiation of silicon as a function of proton energy.

![Figure 3-10: A log-log plot showing NIEL (MeV-cm²/g) versus Energy (MeV) for silicon. The y-axis ranges from 10⁻⁴ to 10², and the x-axis ranges from 10⁻³ to 10³. Four curves are shown: 'Total' (solid red), 'Coulomb' (dashed blue), 'Nuclear (elastic + nonelastic)' (dotted green), and 'Summers' (solid cyan). The Coulomb curve is dominant at low energies, while the nuclear curve becomes dominant at higher energies. The 'Total' curve is the sum of the other two.](f2c40bfbb63eaf7fd84888bdbf1a0a51_img.jpg)

Figure 3-10: A log-log plot showing NIEL (MeV-cm²/g) versus Energy (MeV) for silicon. The y-axis ranges from 10⁻⁴ to 10², and the x-axis ranges from 10⁻³ to 10³. Four curves are shown: 'Total' (solid red), 'Coulomb' (dashed blue), 'Nuclear (elastic + nonelastic)' (dotted green), and 'Summers' (solid cyan). The Coulomb curve is dominant at low energies, while the nuclear curve becomes dominant at higher energies. The 'Total' curve is the sum of the other two.

**Figure 3-10.** NIEL in silicon as a function of incident proton energy. Note that Coulomb scattering dominates damage up to ~10 MeV, after which nuclear processes dominate.<sup>[17]</sup>

**Figure 3-10** also shows the contribution from the two different mechanisms, with Coulombic interactions dominant for protons up to ~10 MeV and nuclear processes dominating for higher proton energies. Neutrons lack charge, but no NIEL will be generated by Coulomb scattering, since neutrons lack charge. A single incident particle will lose significant energy by both ionizing and NIEL mechanisms. Indeed, a single energetic particle incident on a material typically suffers multiple collisions with nuclei, producing additional secondary reactions, each of which loses energy by further downstream collisions and displacements.

A material absorbing all of the incident energy results in a particle that is “stopped” within the material. In the wake of this burst of collisions, a “cascade tree” structure forms, creating multiple individual displacements (point defects) and interstitial atoms, as well as larger defect clusters. See **Figure 3-11**.

Exposing devices to specific neutron or proton fluences reveals DD effect characteristics, which are reported in units of particle per square centimeter. These target fluences are based on estimations of the specific environment and mission length. Energy loss via NIEL causes displacement damage dose (DDD), as described earlier. This simple DDD formulation applies when NIEL does not change appreciably as the particle traverses the device volume. If the particle is near the end of its range, where NIEL will change drastically, determining DDD becomes more complex.<sup>[21]</sup>

The magnitude of DDD in spacecraft electronics will be a strong function of the specific orbit (inclination, altitude, etc.) with respect to the radiation belts, the amount of shielding and the mission lifetime. **Figure 3-12** shows an example of DDD accumulated from proton and electron dose in an 11-year geosynchronous orbit (GSO). For this orbit, and with typical shielding in the 100- to 300-mils range, DDD by electrons dominates. In low Earth orbit, proton

![Figure 3-11: A diagram illustrating a ‘damage cascade’ caused by an incident energetic particle. The x-axis is Distance (nm) from -36 to 36, and the y-axis is Distance (nm) from 0 to 80. A central vertical line represents the path of the incident particle, with branches extending outwards, each ending in a shaded oval labeled ‘Defect cluster’.](4bff5f22997753bcf1997c715118012d_img.jpg)

Figure 3-11: A diagram illustrating a ‘damage cascade’ caused by an incident energetic particle. The x-axis is Distance (nm) from -36 to 36, and the y-axis is Distance (nm) from 0 to 80. A central vertical line represents the path of the incident particle, with branches extending outwards, each ending in a shaded oval labeled ‘Defect cluster’.

**Figure 3-11.** “Damage cascade” caused by an incident energetic particle (at zero on the x-axis and aimed upward). A single incident particle creates multiple individual displacements as well as larger defect clusters.<sup>[18]</sup>

![Figure 3-12: A log-log plot of Displacement damage dose (MeV/g) versus Thickness (mil) for satellite electronics. The y-axis ranges from 1.E+02 to 1.E+16, and the x-axis ranges from 0.01 to 10000. Four curves are shown: 'DDD, Kinchin' (solid blue), 'Isc' (dashed blue), 'Voc' (solid red), and 'Pmax' (solid cyan). The 'Total DDD' curve is the sum of the other three. The 'Electron DDD' curve is also shown, and the 'GPS-type orbit' is indicated.](37a96d647a34d2c514364514c7f85f41_img.jpg)

Figure 3-12: A log-log plot of Displacement damage dose (MeV/g) versus Thickness (mil) for satellite electronics. The y-axis ranges from 1.E+02 to 1.E+16, and the x-axis ranges from 0.01 to 10000. Four curves are shown: 'DDD, Kinchin' (solid blue), 'Isc' (dashed blue), 'Voc' (solid red), and 'Pmax' (solid cyan). The 'Total DDD' curve is the sum of the other three. The 'Electron DDD' curve is also shown, and the 'GPS-type orbit' is indicated.

**Figure 3-12.** A plot of DDD for satellite electronics as a function of aluminum-shield thickness for electrons/protons found in GSO.<sup>[20]</sup>

effects dominate DD, illustrating the complex way in which orbital properties and shielding define the dominant radiation and cause NIEL effects in space applications.

DDD and TID performance are important in other environments:

- In the nuclear battlefield, nuclear weapons emit a brief but extremely high dose of gamma rays and neutrons immediately after they are detonated (see Chapter 1).
- In medical and industrial accelerator (protons) and nuclear reactor (neutrons) applications, where the electronics are exposed to chronic, high doses of radiation limit their useful operating life compared to other reliability mechanisms.

As described previously, a key feature of interactions between radiation and matter is that some or all of the radiation's energy is absorbed by the matter through which it is traveling and converted into excess charge generation (producing SEEs and TID) or causing physical damage via NIEL. Radiation-induced DD in semiconductors leads to the formation of bulk traps in the volume. The number of traps and the degradation they cause to the bulk transport properties increase with increasing DDD. Figure 3-13 shows a silicon band diagram with various DD-induced trap types. These DD-induced traps create new trap-assisted "pathways" that can significantly alter the free-carrier properties of the semiconductor and change device characteristics dramatically. Figure 3-13 represents deep or mid-band bulk traps that enhance thermal carrier recombination and generation, and hence directly affect free carrier density.

![Figure 3-13: Band-gap traps in silicon produced by DDD. The diagram shows four scenarios (a, b, c, d) of energy levels in a silicon band gap. (a) shows a deep mid-band trap (E_M) between the conduction band (E_C) and valence band (E_V). (b) shows shallow traps (E_R, E_T) near the conduction band (E_C) edge. (c) shows localized donor-acceptor trap pairs (E_D, E_CR) that reduce free-carrier concentration. (d) shows a deep mid-band trap (E_M) between the conduction band (E_C) and valence band (E_V).](734487b0336ba703328f4484af34e77d_img.jpg)

Figure 3-13: Band-gap traps in silicon produced by DDD. The diagram shows four scenarios (a, b, c, d) of energy levels in a silicon band gap. (a) shows a deep mid-band trap (E\_M) between the conduction band (E\_C) and valence band (E\_V). (b) shows shallow traps (E\_R, E\_T) near the conduction band (E\_C) edge. (c) shows localized donor-acceptor trap pairs (E\_D, E\_CR) that reduce free-carrier concentration. (d) shows a deep mid-band trap (E\_M) between the conduction band (E\_C) and valence band (E\_V).

Figure 3-13. Band-gap traps in silicon produced by DDD. Mid-band traps increase thermal carrier generation (a); increase recombination (b); and enhance free-carrier trapping (c); localized donor-acceptor trap pairs reduce free-carrier concentration (d).<sup>[29]</sup>

The energy of the deep mid-band trap ( $E_M$ ) within the band gap ( $E_G$ ) – which is its distance from the conduction ( $E_C$ ) and valence band ( $E_V$ ) – will largely determine its cross-section for capture and emission processes. Shallow traps ( $E_R$ ,  $E_T$ ) near the conduction band ( $E_C$ ) edge provide increased trapping of free carriers, potentially enhancing recombination, while trap pairs ( $E_D$ ,  $E_{CR}$ ) lead to changes in free-carrier concentrations by partial compensation of donor-acceptor carrier concentrations.

Since minority carrier concentrations in the base and emitter-base depletion regions mediate the primary action in a BJT, they are intrinsically sensitive to DDD-induced changes in free-carrier properties, as described previously. The defects increase the input bias current required to produce a specific collector current, causing increased recombination and thus BJT gain degradation.

Due to their larger base regions, lateral BJTs can be more sensitive than vertical devices. It has been observed that PNP transistors are usually more sensitive to DD than NPN devices.<sup>[21]</sup> This is related to the fact that the base doping in PNP devices is typically much lower than NPN devices. Generally, the effects of both displacement damage and TID must be addressed for BJT devices.

Other devices that tend to be highly sensitive to DDD include image sensors, light-emitting diodes, photodiodes, solar cells and phototransistors. Figure 3-14 illustrates the sensitivity of PNP devices that suffer little output voltage reduction (~2%) from TID but do exhibit a large output reduction (~12%) from proton exposure, indicating that the device is sensitive to DDD accumulation.

![Figure 3-14: Output voltage shifts induced in PNP devices by TID from gamma rays and protons. The graph plots 'Change in output voltage (V)' on the y-axis (from -0.15 to 0) against 'Equivalent total dose [krad(Si)]' on the x-axis (from 0 to 140). Two data series are shown: 'Cobalt -60 gamma rays' (red squares) and '50 MeV protons' (red diamonds). The gamma rays show a very small decrease in voltage, while the protons show a significant decrease, reaching approximately -0.12 V at 100 krad(Si). A horizontal dashed line indicates a '5% change in voltage' at approximately -0.0625 V. A note states 'Nominal initial voltage = 1.25 Volts (bandgap reference)'.](930335a43c8196e391f87e6860db4d45_img.jpg)

Figure 3-14: Output voltage shifts induced in PNP devices by TID from gamma rays and protons. The graph plots 'Change in output voltage (V)' on the y-axis (from -0.15 to 0) against 'Equivalent total dose [krad(Si)]' on the x-axis (from 0 to 140). Two data series are shown: 'Cobalt -60 gamma rays' (red squares) and '50 MeV protons' (red diamonds). The gamma rays show a very small decrease in voltage, while the protons show a significant decrease, reaching approximately -0.12 V at 100 krad(Si). A horizontal dashed line indicates a '5% change in voltage' at approximately -0.0625 V. A note states 'Nominal initial voltage = 1.25 Volts (bandgap reference)'.

Figure 3-14. Output voltage shifts induced in PNP devices by TID from gamma rays and protons. The PNPs showed little TID sensitivity, so most of the observed gain degradation is related to accumulated DDD.<sup>[22]</sup>

In contrast to BJT and optical devices, MOSFET devices are much less sensitive to DDD and can usually tolerate significantly higher particle doses before their performance is compromised. There are two primary reasons for the robustness of MOSFETs in DDD environments:

- The fact that they are majority carrier devices means that much more damage is required to significantly alter device properties, since carrier densities are so much higher under normal operation.
- Since the active region of MOSFETs is the channel formed between the source and drain, and since this channel region is very thin, the actual volume through which the active current flows is very small.

Thus, it takes very high DDD to ensure that the channel has enough defects to significantly impact MOSFET characteristics. Enhanced recombination from DDD in the channel region will tend to reduce the drive current in MOSFETs.

### References

- 1 T. R. Oldham and F. B. McLean, "Total ionizing dose effects in MOS oxides and devices," *IEEE Trans. Nuclear Sci.* 50(3), June 2003, pp. 483-499.
- 2 J. R. Schwank et al., "Radiation Effects in MOS Oxides," *IEEE Trans. Nuclear Sci.* 55(4), Aug. 2008, pp. 1833-1853.
- 3 MIL-STD-883J with Change-4, Department of Defense TM Standard: Microcircuits (03-Jul-2014), Department of Defense, [http://everyspec.com/MIL-STD/MIL-STD-0800-0899/MIL-STD-883J\\_CHG-4\\_51849/](http://everyspec.com/MIL-STD/MIL-STD-0800-0899/MIL-STD-883J_CHG-4_51849/).
- 4 A. Wu, R. D. Schrimpf, H. J. Barnaby, D. M. Fleetwood, R. L. Pease et al., "Radiation-induced gain degradation in lateral PNP BJTs with lightly and heavily doped emitters," *IEEE Trans. Nuclear Sci.* 44(6), Dec. 1997, pp. 1914-1921.
- 5 R. L. Pease, R. D. Schrimpf and D. M. Fleetwood, "ELDRS in bipolar linear circuits: A review," *2008 European Conference on Radiation and Its Effects on Components and Systems*, 2008, pp. 18-32.
- 6 S. C. Witczak et al., "Gain degradation of lateral and substrate pnp bipolar junction transistors," *IEEE Trans. Nuclear Sci.* 43(6), Dec. 1996, pp. 3151-3160.
- 7 R. L. Pease, "Total ionizing dose effects in bipolar devices and circuits," *IEEE Trans. Nuclear Sci.* 50(3), June 2003, pp. 539-551.
- 8 A. H. Johnston, B. G. Rax and C. I. Lee, "Enhanced damage in linear bipolar integrated circuits at low dose rate," *IEEE Trans. Nuclear Sci.* 42(6), Dec. 1995, pp. 1650-1659.
- 9 J. L. Titus, D. Emily, J. F. Krieg, T. Turlfing, R. L. Pease et al., "Enhanced low dose rate sensitivity (ELDRS) of linear circuits in a space environment," *IEEE Trans. Nuclear Sci.* 46(6), Dec. 1999, pp. 1608-1615.
- 10 J. R. Schwank et al., "Radiation Effects in MOS Oxides," *IEEE Trans. Nuclear Sci.* 55(4), Aug. 2008, pp. 1833-1853.
- 11 A. H. Johnston, G. M. Swift and B. G. Rax, "Total dose effects in conventional bipolar transistors and linear integrated circuits," *IEEE Trans. Nuclear Sci.* 41(6), Dec. 1994, pp. 2427-2436.
- 12 S. R. Messenger et al., "NIEL for heavy ions: an analytical approach," *IEEE Trans. Nuclear Sci.* 50(6), Dec. 2003, pp. 1919-1923.
- 13 I. Jun, "Effects of secondary particles on the total dose and the displacement damage in space proton environments," *IEEE Trans. Nuclear Sci.* 48(1), Feb. 2001, pp. 162-175.
- 14 S. R. Messenger, E. A. Burke, M. A. Xapsos, G. P. Summers and R. J. Walters, "The simulation of damage tracks in silicon," *IEEE Trans. Nuclear Sci.* 51(5), Oct. 2004, pp. 2846-2850.
- 15 V. A. J. van Lint, R. E. Leadon and J. F. Colwell, "Energy Dependence of Displacement Effects in Semiconductors," *IEEE Trans. Nuclear Sci.* 19(6), Dec. 1972, pp. 181-185.
- 16 I. Jun et al., "Proton nonionizing energy loss (NIEL) for device applications," *IEEE Trans. Nuclear Sci.* 50(6), Dec. 2003, pp. 1924-1928.
- 17 J. R. Srour and J. W. Palko, "Displacement Damage Effects in Irradiated Semiconductor Devices," *IEEE Trans. Nuclear Sci.* 60(3), June 2013, pp. 1740-1766.
- 18 J. R. Srour, C. J. Marshall and P. W. Marshall, "Review of displacement damage effects in silicon devices," *IEEE Trans. Nuclear Sci.* 50(3), June 2003, pp. 653-670.
- 19 C. Dale, P. Marshall, B. Cummings, L. Shamey and A. Holland, "Displacement damage effects in mixed particle environments for shielded spacecraft CCDs," *IEEE Trans. Nuclear Sci.* 40(6), Dec. 1993, pp. 1628-1637.
- 20 C. Inguibert and S. Messenger, "Equivalent Displacement Damage Dose for On-Orbit Space Applications," *IEEE Trans. Nuclear Sci.* 59(6), Dec. 2012, pp. 3117-3125.
- 21 H. J. Barnaby, R. D. Schrimpf, A. L. Sternberg, V. Berthe, C. R. Cirba et al., "Proton radiation response mechanisms in bipolar analog circuits," *IEEE Trans. Nuclear Sci.* 48(6), Dec. 2001, pp. 2074-2080.
- 22 B. G. Rax, A. H. Johnston and T. Miyahira, "Displacement damage in bipolar linear integrated circuits," *IEEE Trans. Nuclear Sci.* 46(6), Dec. 1999, pp. 1660-1665.

# Chapter 4: Radiation effects in electronics – single-event effects

Once again, radiation effects impact semiconductor devices in three fundamental ways:

- Single-event effects (SEEs)
- Dose effects
- Dose-rate effects

The focus of this chapter is SEEs and their many subcategories. The definitions and acronyms used for these subcategories have been fluid and changed over time. Different standards, publications and radiation test reports may use different names for the same effect, or a different definition for the same SEE acronym. Texas Instruments generally uses the definitions in the latest revision of JESD57, although deviation is possible from time to time as needed to explain a new effect or conform with a long-standing definition.

We are also including dose-rate effects in this chapter given their similarity to SEEs. Dose-rate effects, often called prompt-dose events, are induced by the detonation of a nuclear weapon, which among other effects generates a high-intensity pulse of gamma radiation and neutrons. The irradiation of the entire device from this very high flux of ionizing radiation produces photocurrents that can temporarily overwhelm on-chip power supplies. Dose-rate effects can be similar to SEEs, but since the whole device is irradiated, there could be several different effects during one event.

### 4.1 Destructive and nondestructive single-event effects

Nondestructive SEEs cause an observable event or corruption in an output or data state, but do not actually damage or destroy the actual circuit component itself. In combinational logic or analog circuits with no memory, the disruption is transient and self-recovering; by definition, circuit functionality returns after a short duration once the excess charge in the struck junctions has been removed. In such cases, no external input is required to restore the state of the system once recombination and transport have cleared the nonequilibrium charge and its effects.

When SEEs occur in digital sequential or memory components, or in analog systems with memory (such as sample-and-hold systems), the charge disruption caused by the radiation event can change the data state of the affected node. Subsequent writes to the device will clear the erroneous state, but until this happens, the data is erroneous and persistent in the system. Such errors can cause systemic failures if the corrupted data state is read and used in downstream circuits. In both the digital and analog scenarios, the radiation has not damaged the device in any way – only the data is corrupted. Thus, nondestructive SEEs are often lumped together under the term “soft errors.”

Nondestructive SEEs cover a number of different SEE types, including single-event transients (SETs), single-event upsets (SEUs), single-event functional interrupts (SEFIs) and some single-event

latchups (SELs), in which the maximum current is limited such that latent or permanent damage does not occur.

Destructive SEEs cause an observable corruption in an output or data state in which the actual circuit component itself is damaged or destroyed. The physical effects of a destructive SEE can be the same as those induced by nondestructive SEEs, with the exception that the device is permanently damaged or destroyed. Thus, destructive SEEs are often lumped together under the term “hard errors.”

In addition to SELs, power electronics can suffer from two additional effects related to their higher operating currents and voltages: the single-event gate rupture (SEGR) and single-event burnout (SEB), discussed later in this chapter.

### 4.2 Archetype for all single-event effects: single-event transients

An SET will always occur when an energetic ion traverses an electronic device, unless it does not have enough energy to reach the semiconductor substrate where the active devices are. The ion leaves a high density of ionized excess electron-hole (e-h) pairs (charge carriers) in its wake.

Two natural restorative mechanisms address the target material's response to this nonequilibrium condition: carrier recombination (a process that eliminates excess charge when electrons recombine with holes) and carrier transport.

Consider an unrealistic condition in which the generated excess electrons and holes are completely immobile and trapped where they were generated. The recombination process would quickly eliminate the excess charge.

When an electron and a hole are in the same physical region and their momentum is similar or identical, it's very likely that the hole will capture the electron. The electron's negative charge and the hole's positive charge cancel each other out. Thus, each recombination event removes charge incrementally. This process continues until all excess charge has recombined and equilibrium conditions have been restored in the material.

Of course, in real materials, carriers can move when forces act upon them. How easily the charge carriers are transported is defined by their mobility and the specific material over which they are traveling. There are two fundamental transport mechanisms that dominate the motion of charge carriers: diffusion and drift.

In diffusion, the local concentration gradient pushes away the high excess concentration of charge carriers, with carriers moving from regions where there are high-carrier concentrations to regions with lower concentrations – like a drop of ink in clear water (the ink drop represents the excess charge distribution that the ion generates). Eventually, the concentrated ink drop disperses throughout the volume of water.

With drift, the driving force for the transport is the local electric field. The anode (negative terminal) attracts positively charged holes and the cathode (positive terminal) attracts negatively charged electrons.

The restoration of carrier equilibrium in materials occurs whether or not there are sensitive active devices in the area. If an ion event occurs deep in the silicon substrate away from any active circuits, the substrate will simply collect the charge harmlessly. In microelectronics, diffusion and drift events obviously create charge transients. But since the excess charge is located far from sensitive devices, they have absolutely no impact on the functionality of the device and therefore can be discounted. On the other hand, if the ion passes near or across active device volumes, some or all of the generated charge can be collected and wreak havoc with the operation of microelectronics.

The type of event that manifests will depend on how the radiation-induced charge transient is transformed by the circuit, layout, process layers and biasing into a response that is either a nondestructive SEE or a destructive SEE. Nondestructive SEEs destroy data states but do not affect devices permanently, whereas destructive SEEs destroy the data state and permanently damage or destroy devices.

In **Figure 4-1**, the SET is an archetypal event from which all SEEs are ultimately derived – it will either manifest as an SET or be mapped into one of several different types of SEE responses depending on the ion linear energy transfer (LET), trajectory, energy, local layout, biasing, layers, and a myriad of other device and circuit details.

![Figure 4-1: A 'magic decoder ring' of SEEs and their acronyms. The diagram shows a central 'Single-event transient SET' branching into 'Single-bit upset SBU', 'Multiple-bit upset MBU', 'Single-event functional interrupt SEFI', 'Single-event latchup SEL', and 'Single-event gate rupture/burnout SEGR/SEB'. These are further categorized into 'Soft error' (Nondestructive single-event effects) and 'Hard error' (Destructive single-event effects).](0f1767577a073167eb9628d72034e083_img.jpg)

Figure 4-1 is a diagram titled "A 'magic decoder ring' of SEEs and their acronyms." It shows a central "Single-event transient SET" branching into five categories: "Single-bit upset SBU", "Multiple-bit upset MBU", "Single-event functional interrupt SEFI", "Single-event latchup SEL", and "Single-event gate rupture/burnout SEGR/SEB". These are further categorized into "Soft error" (Nondestructive single-event effects) and "Hard error" (Destructive single-event effects).

Figure 4-1: A 'magic decoder ring' of SEEs and their acronyms. The diagram shows a central 'Single-event transient SET' branching into 'Single-bit upset SBU', 'Multiple-bit upset MBU', 'Single-event functional interrupt SEFI', 'Single-event latchup SEL', and 'Single-event gate rupture/burnout SEGR/SEB'. These are further categorized into 'Soft error' (Nondestructive single-event effects) and 'Hard error' (Destructive single-event effects).

**Figure 4-1. A "magic decoder ring" of SEEs and their acronyms. An SET event occurs after every radiation event. However, the actual SEE mechanism depends on ion LET trajectory, energy, local layout, biasing, layers, and a myriad of other device and circuit details.**

The reverse-biased junction is the most charge-sensitive part of microelectronics. In fact, solid-state radiation detectors are large-area diodes that are reverse-biased. They also usually include a low-doped intrinsic layer to maximize depletion volume and boost charge-collection efficiency.

The reverse-biased diode is a great radiation detector for two reasons:

- Any excess charge injected from an ion event will make a noticeable impact because the typical reverse currents are small. In other words, it does not take much collected charge to change the junction voltage; most ion events will generate a transient current that is larger than the diode's nominal reverse-bias current.

- Because a large depletion region forms at the junction when it is reverse-biased, a high electric field present at the depletion region is particularly effective at separating electrons and holes before they can recombine, maximizing the charge collection at the junction. **Figure 4-2** illustrates a reverse-biased N+/P diode at different stages during the event.

The N+ contact is positively biased with respect to the P-substrate. At the onset of an ionizing radiation event, a cylindrical track comprising a high nonequilibrium concentration of e-h pairs with a submicron radius is left in the ion's wake (**Figure 4-2a**). When the resulting ionization track traverses or comes close to the depletion region, carriers are rapidly separated by the electric field created, with the positively biased P+ node attracting electrons and holes being repulsed toward the substrate.

The huge influx of electrons injected on the P+ node produces a large current/voltage transient at that node. A notable feature of the event is the concurrent distortion of the potential into a funnel shape.<sup>[1]</sup> This funnel-shaped potential distortion around the event greatly enhances the efficiency of the drift collection by extending the high field-depletion region deeper into the substrate (**Figure 4-2b**).

![Figure 4-2: Phases in a reverse-biased N+/P diode and the resulting current transient. The top part shows three diagrams (a, b, c) illustrating the ion track, drift, and diffusion of charge carriers. The bottom part is a graph of Current (a.u.) vs Time (seconds) showing the transient response.](47b554ac4587106dd53a7ba24cbadd40_img.jpg)

Figure 4-2 consists of two parts. The top part shows three diagrams (a, b, c) illustrating the ion track, drift, and diffusion of charge carriers. The bottom part is a graph of Current (a.u.) vs Time (seconds) showing the transient response.

Figure 4-2: Phases in a reverse-biased N+/P diode and the resulting current transient. The top part shows three diagrams (a, b, c) illustrating the ion track, drift, and diffusion of charge carriers. The bottom part is a graph of Current (a.u.) vs Time (seconds) showing the transient response.

**Figure 4-2. Phases in a reverse-biased N+/P diode and the resulting current transient caused by the passage of a high-energy ion through the junction.<sup>[2]</sup>**

The size of the funnel is a function of substrate doping – the funnel distortion increases as substrate doping decreases. This prompt collection phase is complete within a few nanoseconds and followed by a slower charge-collection phase, where diffusion begins to dominate the collection process (Figure 4-2c). Additional charge is collected as electrons diffuse into the depletion region on a longer time scale (hundreds of nanoseconds) until all excess carriers have been collected, recombined or diffused away from the junction area.

The diagram at the bottom of Figure 4-2 shows the corresponding current pulse resulting from the charge collection that occurs during these three phases. For most modern microelectronics, CMOS-based digital circuits in particular, the farther away from the junction that the event occurs, the smaller the amount of charge collected and the less likely it is that the event will cause an SEE. In more mature technologies with deeper wells, buried layers and larger junction areas, diffusion collection can play a significant and sometimes dominant role in the type and severity of SEEs.

Although the example in Figure 4-2 shows an N+/P diode, the basic charge collection and transport also occurs in complementary reverse-biased P+/N diodes. In the reverse-biased P+/N diode, the generation of excess charge by the ion is identical, but the collection due to drift is reversed; the P+ is held at ground or negative potential. The holes are transported by drift toward the junction, while the electrons are repulsed. SEEs can and do occur in both types of reversed-biased diodes, but the N+/P diode typically will collect more charge. In diodes with identical layout areas, the reverse-biased N+/P diode structure is more sensitive to radiation events than the P+/N diode. There is one caveat: The transient parasitic bipolar amplification can lead to excess charge collection for P+/N junctions formed in an N-well.

In real-world circuits, single-circuit nodes are never truly alone but are actually part of a complex “sea of nodes” in close proximity. While the nodes themselves may be electrically isolated from one another, each ion event creates a spatial charge distribution from tens to hundreds of microns. Thus, the occurrence of a single radiation event potentially affects multiple nodes.

Charge sharing among nodes can greatly influence the amount of charge individual nodes collect, and how this collected charge gets mapped into an SEE. In some cases, charge sharing can actually preclude a radiation event from causing a detectable SEE, as the initial charge the SET generated is dissipated and divided harmlessly across many nodes, as opposed to being collected as a much bigger event by a single node. In other cases, the charge injected across several nodes within the same circuit can induce an SEE response – whereas if a single node were hit, none would be observed.

### 4.3 Digital and analog single-event transients

The previous section presented the basic definition of an SET. Now, let's consider the differences between SETs in digital and analog systems. The LET that caused an event largely defines an SET's magnitude and duration – higher LET events generally create a higher density of localized charge disturbance, and thus larger SETs. SETs from higher LET events tend to create larger voltage excursions and have longer durations.

The natural radiation environment, whether space or terrestrial, consists of high event rates at low LETs, dropping exponentially to lower event rates at high LETs. Thus, there will be a high probability of small SETs occurring and decreasing probabilities of larger LET events within any time interval.

Figure 4-3 shows an SET that is generated in and propagates through digital logic, which is known as a digital single-event transient (DSET). DSETs occur in combinatorial logic (the assemblies of INV, BUFF, NOR, NAND, XOR, etc. making up simple control logic or the core logic of processors) or it can occur in and propagate in the clock tree.<sup>[3-5]</sup> A DSET will manifest as a narrow glitch that may propagate through various stages. Each stage will attenuate and/or broaden the DSET. Many SETs will be below the digital-voltage threshold. They will be rapidly attenuated and will not impact the system at all. Some of the larger SETs will cause spurious digital signals that can confuse downstream systems.

![Diagram illustrating DSET propagation in digital logic. It shows sequential logic blocks (DFFs) and combinatorial logic stages. A DSET is injected into the combinatorial logic, propagates through the clock tree, and can cause erroneous clock pulses. The diagram includes waveforms for the clock tree and sequential logic outputs.](9ed248b025d766251d58be10b01a1cc0_img.jpg)

The diagram illustrates the propagation of a Digital Single-Event Transient (DSET) through a digital circuit. At the top, 'N-stages of combinatorial logic' are shown between two 'Sequential logic' blocks (DFFs). A 'DSET injection in combinatorial' is shown as a red pulse entering the logic. This pulse propagates through the logic stages, becoming a 'Propagated DSET pulse'. Below the logic, a 'Clock tree (synchronous)' is shown. A 'DSET on clock tree' is shown as a red pulse entering the clock tree. This pulse propagates through the clock tree, causing 'Erroneous clock pulse' waveforms at the inputs of the sequential logic blocks. The sequential logic blocks are labeled 'DFF' with inputs 'D', 'Q', and 'CLK'. The clock tree is shown as a series of inverters and buffers. The 'Erroneous clock pulse' waveforms are shown as narrow spikes on the clock signal lines.

Diagram illustrating DSET propagation in digital logic. It shows sequential logic blocks (DFFs) and combinatorial logic stages. A DSET is injected into the combinatorial logic, propagates through the clock tree, and can cause erroneous clock pulses. The diagram includes waveforms for the clock tree and sequential logic outputs.

Figure 4-3. There are two ways in which a DSET injected by a particle event can become a persistent error in digital systems. If the event occurs in combinatorial logic and can propagate to the input of sequential logic, it may be latched in at the next clock. DSETs occurring in the clock tree need to be big events to cause rail-to-rail clock glitches, but these events can erroneously clock any or all of the components driven by that clock tree.

**Figure 4-4** shows examples of a DSET event that is attenuated and one that propagates. Attenuated DSETs or DSETs that do not get captured by sequential or memory elements have no impact on system reliability. DSETs captured in sequential or memory components transform into persistent errors and are indistinguishable from SEUs that occur in the sequential element themselves. Persistent errors captured in the sequential components can corrupt the downstream data.

Three conditions are necessary for a DSET to have any possibility of being captured in downstream sequential logic or memory

- The ion event must generate a transient capable of propagating through the circuit.
- There must be a valid logic path through which the DSET can propagate to a latch or to another memory element.
- When the DSET glitch arrives at a sequential or memory component, it must have sufficient voltage amplitude to cause an input error and be of a sufficient width (in synchronous logic, the DSET must arrive at the latch during a valid setup-and-hold time).

![Figure 4-4: Simulated DSET events. The top plot shows a low LET event (3 MeV-cm²/mg) in a 10-inverter chain, where the transient is quickly attenuated after 4 inverters. The bottom plot shows a higher LET event in an RS FF latch, where the transient propagates unchanged through multiple logic stages.](2d62ff2bded0c21414a0f40fdf8fd537_img.jpg)

The figure consists of two plots showing Node voltage (V) versus Time (ps). Both plots have a y-axis from 0.0 to 1.6 V and an x-axis from 0 to 400 ps. The top plot is for a 10-Inverter Chain with parameters: LET = 3 MeV-cm²/mg, 0.18-μm CMOS, V<sub>DD</sub> = 1.62 V. It shows a 'Struck node' (red) that drops from 1.6V to ~0.2V at 20ps. Subsequent nodes (blue) show the transient being attenuated, with the signal after 4 inverters returning to 1.6V by 100ps. The bottom plot is for an RS FF latch with parameters: LET = 3 MeV-cm²/mg. It shows a 'Struck node' (red) that drops from 1.6V to ~0.2V at 20ps. The latch output (blue) shows a transient that propagates through multiple stages, with the signal after broadening inverters returning to 1.6V by 200ps. A dashed line indicates the 'RS FF latches SET'.

Figure 4-4: Simulated DSET events. The top plot shows a low LET event (3 MeV-cm²/mg) in a 10-inverter chain, where the transient is quickly attenuated after 4 inverters. The bottom plot shows a higher LET event in an RS FF latch, where the transient propagates unchanged through multiple logic stages.

**Figure 4-4. Simulated DSET events caused by a low LET (top) event and a higher LET event (bottom). The DSET in the top plot is quickly attenuated and therefore unlikely to be captured by downstream sequential elements, whereas the DSET in the bottom plot shows that the transient is propagating unchanged over multiple logic stages.<sup>[6]</sup>**

The probability that a DSET will be captured as an SEU in downstream sequential components increases linearly with frequency because the number of clock edges increases with increasing clock frequency. When voltage scaling has occurred with advanced digital circuits (where the operating voltage has

decreased), it takes less injected charge to create rail-to-rail signals that can propagate. Thus, more advanced higher-speed technologies are potentially more sensitive to SEUs induced by DSETs, because both their occurrence probability and their ability to propagate over multiple stages has increased with each new subsequent technology node. The wider the DSET glitch, the greater the probability of falling within a setup-and-hold time of a downstream sequential component.

Another way in which DSETs can cause the capture of erroneous values is when they occur on a clock tree. If they are big enough to cause a full-scale transient on the clock, DSETs can cause false rising or falling edges that may erroneously clock sequential circuits outside of their legal setup-and-hold times when the data inputs may not be valid. In this case, the DSET has the potential to indirectly induce an SEU by causing the clocking or capturing of an invalid data input within a sequential component. This mode will only occur with higher LET events because clock trees often have much higher capacitance (due to the fact that they have multiple distributed nodes). Any collected charge will induce a smaller voltage transient for a given event size for a larger node capacitance.

In analog circuits, an SET is often referred to as an analog single-event transient (ASET). In analog components like amplifiers and comparators, ASETs will cause a short-lived transient disturbance on the output of the device. **Figure 4-5** shows an example of ASETs in several different locations and their impact on the voltage output of an amplifier.

The duration, shape and magnitude of ASETs depend highly on which part of the amplifier the ion event hits. Many analog circuits are designed to resist short-duration glitches, so you can simply ignore or filter many ASETs out of the signal. An incorrectly sampled value will result, even in analog systems with memory-like sample-and-hold circuits, where the ASET can generate an erroneous voltage level on the sampling capacitor when the capacitor is in hold mode. However, the next correct sample written to the sample-and-hold circuit will clear the error – thus the corruption will affect a single sample, which can be filtered out.

One additional area where SETs cause system-reliability issues is in power devices. Although most SETs are nondestructive SEEs, they do impact system availability. Should an SET occur at a critical time, it could have more serious implications in high-reliability applications. Both ASETs and DSETs in power components have the potential to cause issues. For example, an ASET in the output stage of a power transistor that is providing an output current to a load at a specific current and specified voltage can cause a glitch in the power output.

While small glitches (particularly ASET undershoots such as those shown in **Figure 4-6**) can be tolerated, some expensive space-qualified field-programmable gate arrays (FPGAs) require maximum over/undershoots of <5%. Large-magnitude (>5%) overshoots on the output of power devices are the most problematic because they can cause permanent damage (electrical overstress) in downstream circuits, while large-magnitude undershoots can lead to data corruption and/or resets in downstream systems.

![Figure 4-5: Simulated radiation-induced current and resulting ASETs on the output of an operational amplifier. The figure consists of three plots and a circuit diagram. The 'Input stage' plot shows output voltage (V) vs. time (seconds) for a double exponential pulse (red) and a square pulse (teal). The 'Output stage' plot shows output voltage (V) vs. time (seconds) for the same pulses. The 'Gain stage' plot shows output voltage (V) vs. time (seconds) for the same pulses. The circuit diagram shows the internal structure of the op-amp with nodes labeled Input, Set1, Set2, Set3, Gain, Q4, Q9, Q14, and Output. Red strikes indicate the location of radiation-induced current injection.](62039fd2a1ef7b03f84c0fe5d8911860_img.jpg)

Figure 4-5: Simulated radiation-induced current and resulting ASETs on the output of an operational amplifier. The figure consists of three plots and a circuit diagram. The 'Input stage' plot shows output voltage (V) vs. time (seconds) for a double exponential pulse (red) and a square pulse (teal). The 'Output stage' plot shows output voltage (V) vs. time (seconds) for the same pulses. The 'Gain stage' plot shows output voltage (V) vs. time (seconds) for the same pulses. The circuit diagram shows the internal structure of the op-amp with nodes labeled Input, Set1, Set2, Set3, Gain, Q4, Q9, Q14, and Output. Red strikes indicate the location of radiation-induced current injection.

Figure 4-5. Simulated radiation-induced current individually injected into the input, gain and output stages (red strikes) of an operational amplifier and the resulting ASETs on the output.<sup>[7]</sup>

DSETs in the digital control logic of power controllers can cause problems as well. For example, a DSET in the logic that causes the  $P_{\text{good}}$  signal (a signal that tells the devices tied to the power device when the output is valid) to flag a power-down situation will cause a reset in downstream devices tied to the power bus, even though the power itself is still functioning within target levels. Figure 4-6 shows such a DSET. In this case, because the power-supply output is functioning properly, filtering out this narrow DSET on  $P_{\text{good}}$  will keep it from having an effect on downstream electronics.

### 4.4 Single-event upsets

When radiation events occur within the node of a digital storage component, such as the bit of a dynamic or a static random access memory (DRAM or SRAM), a latch, or a flip-flop, the result is a persistent error called an SEU. The system impact of an SEU will depend on the type of error and its location, but since the erroneous state persists until it is over-written with new data, SEU are potential “time-bombs” for the reliability of digital systems, since the erroneous data can be used in down-stream processes without the

![Figure 4-6: Two different SETs caused during the heavy-ion testing of a power device. The left plot shows V_out2 voltage (V) vs. time (ms) with a sharp dip (undershoot) at approximately 0.1 ms. The right plot shows P_good2 voltage (V) vs. time (ms) with a sharp spike (glitch) at approximately 0.1 ms.](a96c7e19f53f2350db97a90738a6fb51_img.jpg)

Figure 4-6: Two different SETs caused during the heavy-ion testing of a power device. The left plot shows V\_out2 voltage (V) vs. time (ms) with a sharp dip (undershoot) at approximately 0.1 ms. The right plot shows P\_good2 voltage (V) vs. time (ms) with a sharp spike (glitch) at approximately 0.1 ms.

Figure 4-6. Two different SETs caused during the heavy-ion testing of a power device: an ASET causing power-output undershoot; a DSET in control logic causing a glitch on the  $P_{\text{good}}$  output pin. This is an erroneous signal because the actual power output is unaffected.<sup>[8]</sup>

system “knowing” that the data is bad (such errors can be detected or corrected using additional circuitry and extra code bits in systems where higher reliability is desired). The SEU is a persistent data corruption but the circuit itself is not damaged.

**Figure 4-7** shows commercial DRAM technology based on the compact one-transistor one-capacitor (1T-1C) design. The presence or absence of a voltage (charge) on the storage node of the capacitor defines the binary data state stored in the DRAM bit cell. The storage capacitor is accessed during read (R) or write (W) operations by turning on the pass-gate transistor with the wordline (WL).

With the pass gate turned on, charge is free to travel between the bitline (BL) and the storage capacitor. The data state (charge state) of an individual bit cell is determined with a differential amplifier called a sense amplifier. During an R or refresh operation, the sense amplifier measures the voltage difference between the BL connected to the cell capacitor and a reference BL pre-charged to half the power-supply voltage. Thus, if the capacitor is in a fully charged state, the BL's voltage will be higher than its reference level. If the capacitor is in an uncharged state, the BL's voltage will be lower than its reference level.

Once sensing is complete, the sense amplifier drives the BL to the voltage (either to 0 V or to the power-supply voltage), representing the data state it detected in the capacitor. This signal regeneration by the sense amplifier is crucial for keeping the DRAM bits refreshed. The bit cell is just a simple capacitor, so if not refreshed periodically, a fully charged capacitor would eventually discharge. DRAM bit cells are optimized such that the next refresh cycle always occurs long before the sense margin is drastically reduced.

Any charge disturbance that leads to the depletion of charge enhanced from the discharge data state has the ability to cause a bit error because the storage capacitor has no regeneration path. The occurrence of a single-ion event in the DRAM array can introduce charge that will corrupt the bit cell struck.<sup>[19]</sup>

The red lines in **Figure 4-7** show where SEUs can happen in a DRAM. Ion-event strikes can occur in three primary locations in the DRAM array and cause an SEU. The most likely SEU is caused by a single-event strike in or near the capacitor cell. It is the most likely source of SEUs because all cells in the array are basically sensitive all of the time, except during the short time when they are accessed during R/W operations and make up a majority of the DRAM area.

The most likely effect of the ion strike is to deplete a fully charged state. In contrast, the fully discharged state usually collects much less charge, since the electric field is diminished. This type of direct-cell SEU tends to favor one data state over the other.

In the case of Texas Instruments DRAMs, fully charged storage nodes represent the “1” data state, and SEU test results are heavily skewed toward “1” failures.

The passage of an ion along the surface of the silicon traversing the drain-and-source region of the pass gate creates a momentary conductive path that constitutes a second likely source of SEUs when it connects to the BL (usually pre-charged to ground potential) and drains the charge from the storage node.

![Diagram of a 1T-1C DRAM bit cell. The diagram shows a Wordline (WL) at the top, connected to a Pass gate transistor. The Pass gate transistor is connected to a Storage node, which is also connected to a Storage capacitor. A Bitline (BL) is shown on the left. Red arrows indicate where ion strikes are likely to inject charge: one arrow points to the Bitline (BL), another points to the Storage node, and a third points to the Storage capacitor. A dashed line separates the Wordline from the rest of the circuit.](42e18c25bfd455a5a57f207bacfcb970_img.jpg)

Diagram of a 1T-1C DRAM bit cell. The diagram shows a Wordline (WL) at the top, connected to a Pass gate transistor. The Pass gate transistor is connected to a Storage node, which is also connected to a Storage capacitor. A Bitline (BL) is shown on the left. Red arrows indicate where ion strikes are likely to inject charge: one arrow points to the Bitline (BL), another points to the Storage node, and a third points to the Storage capacitor. A dashed line separates the Wordline from the rest of the circuit.

**Figure 4-7.** Diagram of a 1T-1C DRAM bit cell. Red arrows indicate where ion strikes are likely to inject charge that will cause an upset.

These events are rare due to the specific ion path required. When the BL is floating during the actual sensing R cycle, SEUs can occur due to the collection of charge in one of the many diffusion regions that are electrically connected to the BLs – typical DRAM implementations place 64 or more bit cells on a single BL.

Spatially, the probability of such an event is high because any of the many access-transistor drains along the current-sensing BL or a strike to the sense amplifier itself can constitute a collection point. However, the likelihood of an event occurring during the brief sensing time means that it is more likely caused by direct storage-capacitor strikes than SEUs. SEUs from BL/sense-amplifier strikes do increase in proportion to the frequency of operation, however, because at higher frequencies (shorter cycle times), sensing becomes a larger fraction of the total memory cycle time.

The upset process in SRAMs is different than in DRAMs, due to the active feedback designed into the SRAM bit cell. The standard 6T SRAM cell shown in **Figure 4-8** comprises two pass transistors to allow connection of the BLs to the storage cell during R/W operations. The two pass transistors (activated by the WL signal) are normally shut off (high impedance) and serve to isolate the SRAM bit cell when it is in storage mode.

The portion of the SRAM bit cell that is actually providing data storage comprises two P-type MOS transistors (P1 and P2) and two N-type MOS transistors (N1 and N2) forming two cross-coupled inverters. The inset on the upper left side shows an output of one

inverter driving the input of the other inverter. The regenerative feedback loop maintains the data state latched in this configuration as long as power is applied. If a "1" data state is stored on the left, by definition, the opposite state or "0" state is stored on the right. Thus, in the left PMOS, P1 is on, as revealed by the presence of leakage current (the yellow arrow from  $V_{DD}$ ) keeping the left storage node high while also ensuring that the NMOS N2 is on, maintaining the right storage node at ground.

Having the right node pull down to 0 V in turn ensures that the left PMOS P1 gate is low. The PMOS is maintained in the on state, keeping the left node pulled high.

Suppose that an energetic ion traverses near the node storing the "1" data state. A large cloud of e-h pairs is produced along the wake of the particle's trajectory, and electrical fields separate and transport a large portion of them.

In this case, electrons will be collected by the reverse-biased drain node at N1, causing a rapid drop in the stored voltage of the left node. As the node voltage drops, the left PMOS P1 hole current will start to compensate. Whether or not the PMOS can supply enough current to compensate for the current induced by the event before the cell itself flips to the opposite data state will determine whether the SRAM bit will flip or not.

As the node voltage drops on the left, the right PMOS P2 starts turning on while the right NMOS starts turning off. This event further aggravates the situation because it will tend to turn the left PMOS P1 off while turning the left NMOS N1 on, actually further pulling the left node down. If the hole current from the left PMOS cannot quench the excess charge before the left node falls below some critical low-voltage value, switching will occur and an SEU will result.<sup>[10]</sup>

![Circuit diagram of a 6T SRAM bit cell in storage mode. The circuit consists of two PMOS transistors (P1, P2) and two NMOS transistors (N1, N2) connected in a cross-coupled configuration. The word line (WL) is shown as a horizontal line with a pulse. The bit lines (BL) are shown as vertical lines. The left storage node is labeled '1' and the right storage node is labeled '0'. Arrows indicate the flow of current and the state of the transistors. A yellow arrow indicates leakage current from VDD to the left node.](508bc574df81fa8d3027a374f6d155fc_img.jpg)

Circuit diagram of a 6T SRAM bit cell in storage mode. The circuit consists of two PMOS transistors (P1, P2) and two NMOS transistors (N1, N2) connected in a cross-coupled configuration. The word line (WL) is shown as a horizontal line with a pulse. The bit lines (BL) are shown as vertical lines. The left storage node is labeled '1' and the right storage node is labeled '0'. Arrows indicate the flow of current and the state of the transistors. A yellow arrow indicates leakage current from VDD to the left node.

**Figure 4-8. 6T SRAM bit cell in storage mode.** The WL is off, so both pass transistors are off. The "1" data state is maintained on the left side by the P1 pullup. The "0" data state on the right side is pulled down by N2. N1 and P2 are off.

Two regions within the SRAM bit cell are most sensitive to the charge injected during an ion strike. For the side storing the "1" state, it is the collection of electrons by the drain of the N1, and for the side storing the "0" state, it is the collection of holes by the

drain of P2. Two factors determine the robustness or weakness of an SRAM bit to an SEU: the drive strength of the transistors (determined mostly by their width) and the intrinsic switching speed of the bit cell (determined by parasitics and the transistor drive).

A higher drive strength means that a larger restoration current can neutralize the excess charge that an ion strike injects. Reducing the switching speed of the SRAM bit cell gives the pullup/pulldown transistors more time to compensate for the charge injected. Increasing the drive strength and reducing the switching speed both improve the radiation tolerance of SRAM cells. However, commercial pressure to increase density and speed while reducing power ensures that the SRAM bit cell will be more weakly driven and have a shorter switching speed, resulting in increased sensitivity to SEUs for commercial SRAMs.

Whether in a DRAM, SRAM or a set of sequential gates in close proximity (register file, input/output buffer), an SEU flipping the data state in a single memory bit or sequential component is known as a single-bit upset (SBU), while a larger event that flips several bits in the same data word at one time is known as a multiple-bit upset (MBU).<sup>[11-13]</sup>

**Figure 4-9** shows memory maps of two arrays suffering SBUs (left) and MBUs (right). In bigger, higher LET events, charge sharing among closely spaced nodes can end up upsetting multiple adjacent memory bits. Even lower LET events with trajectories close to the surface and at low angles (parallel to the silicon surface) can deposit charge in several sensitive regions, resulting in an MBU.

![Figure 4-9 shows two memory maps. The left map shows three single-bit upsets (SBUs) as red squares on a grid. The right map shows three multibit upsets (MBUs) as red and dark teal rectangles on a grid. A legend indicates 'Single-bit upsets (red)' and 'Multibit upsets (red) and Multicell upsets (dark teal)'. An arrow points to the right, labeled 'Logical word in row direction'.](333d579717c3e3a4de4afbc63cc31c7d_img.jpg)

Figure 4-9 shows two memory maps. The left map shows three single-bit upsets (SBUs) as red squares on a grid. The right map shows three multibit upsets (MBUs) as red and dark teal rectangles on a grid. A legend indicates 'Single-bit upsets (red)' and 'Multibit upsets (red) and Multicell upsets (dark teal)'. An arrow points to the right, labeled 'Logical word in row direction'.

**Figure 4-9. Memory bitmap (left) with three SBUs; error bits are shown in red. Under realistic conditions, it is exceedingly rare to have multiple SBUs. Memory bitmap (right) with three multicell upsets (MCUs) (red and dark teal bits) and two MBUs (2-bit and 4-bit).**

In the space environment, MBUs are much more likely to occur because of high LET heavy-ion events, as opposed to proton or electron events. In the terrestrial environment, high-energy neutron reactions are responsible for most MBUs, as opposed to lower LET alpha particles. Because a single event induces an MBU, the MBU fail pattern will be contiguous and follow the ion trajectory. However, in systems with different data-state sensitivities, some noncontiguous fail patterns may occur.

The recently coined MCU is a more general term associated with the total number of bits that fail from a single ion event irrespective of the logical arrangement of those bits, while an MBU considers multiple bit fails only within logical words.

From a reliability perspective, which bits are upset makes a big difference in what is detectable and/or correctable and what leads to an actual fail. Multiple-bit failures in the direction where actual words are stored (in this example, in rows) are what can cause redundancy solutions to fail. MBUs are usually caused by higher-energy ions and/or higher LET events that are far rarer than smaller events causing SBUs. For commercial DRAMs, the MBU rate is between 5-10% of the observed SBU rate. For commercial SRAMs, the MBU rate is between 5-15% of the observed SBU rate.

A computer's discrete and embedded SRAM and DRAM would be useless without the peripheral logic interconnecting them. While less sensitive than SRAM, sequential logic devices can also experience SEUs. Sequential logic elements include latches and flip-flops that hold system-event signals and buffer data before they go in or out of the microprocessor and interface to combinatorial elements that perform logical operations based on multiple inputs.

The SEU sensitivity of these devices and their impact on the system are harder to quantify, because their period of vulnerability (when they are actually doing something critical in the system versus simply waiting) varies widely depending on the circuit design, frequency of operation and the algorithm being executed.

Latches are fundamentally similar to a SRAM cell in that they use cross-coupled inverters to store the data state. The need for compact and high-speed latches ensures SEU sensitivity on par with that of SRAM bit cells.

Flip-flops are inherently more robust because they are usually made from two stages – an SEU in the output stage will be transmitted, while an SEU in the slave stage does not get transmitted to the output. Latches and especially flip-flops designed with larger transistors (with larger fanout) can more easily compensate for spurious charge during radiation events and will generally be more robust to SEUs.

**Figure 4-10** shows an SEU in a sequential logic component. SEUs in sequential logic are particularly a concern in high-reliability systems whose memory has been protected by error correction where the peripheral logic-failure rate may be the dominant reliability failure mechanism.<sup>[15, 16]</sup>

#### Single-event upset in sequential element

![Diagram illustrating a single-event upset (SEU) in a sequential logic component. A particle event (red lightning bolt) strikes the D input of a D flip-flop (DFF). The DFF has inputs D, CLK, and Q-bar, and output Q. The output Q is connected to the D input of a second DFF. The second DFF has inputs D, CLK, and Q-bar, and output OUT. The output OUT is connected back to the D input of the first DFF, forming a feedback loop. The diagram shows the SEU affecting the D input of the first DFF, which can lead to a persistent SEU in the digital system.](3e2dcee303cecdd31b7f9ec0d8942fed_img.jpg)

Diagram illustrating a single-event upset (SEU) in a sequential logic component. A particle event (red lightning bolt) strikes the D input of a D flip-flop (DFF). The DFF has inputs D, CLK, and Q-bar, and output Q. The output Q is connected to the D input of a second DFF. The second DFF has inputs D, CLK, and Q-bar, and output OUT. The output OUT is connected back to the D input of the first DFF, forming a feedback loop. The diagram shows the SEU affecting the D input of the first DFF, which can lead to a persistent SEU in the digital system.

**Figure 4-10.** A particle event in sequential logic can become a persistent SEU in digital systems. The erroneous bit has some chance of being transmitted downstream and can affect a machine state or be written into memory.

### 4.5 Single-event functional interrupt

As microelectronics have increased in density, computational power and complexity, so has the number and variety of failure modes that they experience in radiation environments. Quite simply, as the complexity increases, so does the number of ways in which the device can fail.

SEFIs are a type of nondestructive SEE. SEFIs can occur in digital devices when the bit that is flipped (by an SEU) is in a critical system register, such as those that control operations, modes or program execution in FPGAs, DRAMs, SRAMs, nonvolatile flash memories, or microcontrollers and processors.<sup>[17, 18]</sup>

For example, a SEFI occurs if the SEU in a control register erroneously initiates a built-in self-test sequence, triggers a system reset, or if some other mode causes the integrated circuit (IC) to lose functionality or execute incorrectly. SEFIs impact product failure rates and availability much more dramatically than SEUs. Each SEFI leads to a direct product malfunction as opposed to typical memory/logic SEUs that may or may not affect the final operation depending on the algorithm, data sensitivity, etc.

When a SEFI occurs in a DRAM or SRAM array (either stand-alone or embedded in a processor), the upset is usually a bit in the control logic for row or column decoding, multiplexing, etc., which involves moving data during R/W operations. The SEFI will cause a loss of many bits, usually appearing as whole blocks, bands, rows or columns of bit fails in the memory map, as illustrated in **Figure 4-11**.

One example of a SEFI occurs in memory redundancy circuits. Redundant rows or columns are often included in memory arrays to offset the impact of manufacturing defects on yield. When bad bits are found during production testing, the addresses can be rerouted to a redundant row or column. Thus, the defect is effectively removed from memory because any time the address comes up, it is rerouted to a fully functional row/column. That address rerouting is typically stored in fuses blown at test. On power up, the fuse values are read into redundancy latches. During operation, the latch value is used during addressing. An SEU in any redundancy latch will cause the original bad row/column to be addressed instead of the good redundant row/column. In addition to having a defective

bit or bits in the row/column, the value of the other bits on that row/column will be incorrect because they were never written in previous accesses when the latch had the correct value. The only way to recover from this issue is a full power reset so that the redundancy latches are correctly updated with the proper values. Most SEFIs in digital systems require some level of external intervention (reset or power-down reset) to restore the system.

![Figure 4-11: Schematic representation of a SEFI fail mode in a memory. The diagram shows a memory array with rows and columns. A single bit in the control logic (I/O control) is corrupted, leading to erroneous behavior that causes many failures in the memory array (red bits). The failures manifest as blocks, sections of rows or columns, depending on what logic was affected. The control logic includes I/O control, Row decoder, Data IN buffer, Data OUT buffer, Column decoder, Burst length, Program register, and Timing register. The memory array is represented by a grid of red and blue squares.](b2cc37ae1974ec7b87b91f54963b855d_img.jpg)

Figure 4-11: Schematic representation of a SEFI fail mode in a memory. The diagram shows a memory array with rows and columns. A single bit in the control logic (I/O control) is corrupted, leading to erroneous behavior that causes many failures in the memory array (red bits). The failures manifest as blocks, sections of rows or columns, depending on what logic was affected. The control logic includes I/O control, Row decoder, Data IN buffer, Data OUT buffer, Column decoder, Burst length, Program register, and Timing register. The memory array is represented by a grid of red and blue squares.

**Figure 4-11. Schematic representation of a SEFI fail mode in a memory.**  
A single bit corrupted in the control logic leads to erroneous behavior that causes many failures in the memory array (red bits) – SEFIs usually manifest as blocks, sections of rows or columns, depending on what logic was affected.

### 4.6 Single-event latchup

A latchup is a potentially catastrophic mechanism in which a low-impedance path develops suddenly between power and ground and remains after the triggering event dissipates. Once latched, the high-current state is maintained until power is removed or the device suffers a catastrophic episode. Latchup is a well-known reliability concern for semiconductor manufacturers of CMOS and BiCMOS bulk technologies. Well-isolated bipolar technologies are usually less sensitive to latchup.

The minimum anode-to-cathode spacing, well-contact (tap) number and maximum tap-spacing ( $L_{N+}$ ,  $L_{P+}$ ) are a standard part of CMOS design rules established to minimize latchup sensitivity. The fundamental difference between a latchup and an SEL is the unique trigger for initiating the SEL.

During an SEL event, the ion-generated charge is delivered all at once (in the picosecond range), with a very high concentration of electrons and holes generated within the device. Thus, the initial trigger conditions tend to be significantly worse than those induced by an external voltage transient on the anode/cathode. As a result, good latchup performance is necessary but not sufficient to guarantee good SEL performance. To say it another way, if a device has poor latchup performance, it will have poor SEL performance, but if a device is latchup-free, it will still need to be tested with heavy ions to determine if it has acceptable SEL performance.

**Figure 4-12** shows the parasitic bipolar junction transistors (BJTs) responsible for latchup. The P-epi/P-substrate, N-well and P+ contact (anode) form the collector, base and emitter of the parasitic vertical PNP BJT, respectively. Similarly, the N-well, P-epi/P-substrate and N+ contact (cathode) form the collector, base and emitter of the parasitic lateral NPN BJT, respectively. The biasing of the BJTs originates from the charge injected by the ion; the spreading resistance of the well and substrate; and the voltages on the anode, cathode and supply contacts. If triggered, the parasitic BJTs form a regenerative feedback loop, producing a low-impedance path between power and ground. Assuming that the structure has a high-enough gain product, the regenerative feedback can maintain the high current state – it is latched and can only be removed by powering down so that the parasitic BJTs shut off.

![Figure 4-12: Cross-section of a typical CMOS well structure with parasitic BJTs and the primary resistances involved in the process of initiating an SEL. The diagram shows a cross-section of a CMOS well structure with layers: VDD, Anode, Cathode, VSS, N+, P+, N+, P+. The parasitic BJTs are shown with their respective resistances: R_N-well and R_sub. The diagram also shows the lengths L_N+, L_Anode-cathode, and L_P+.](c59c57aa32d1de24f1b0cfca10bd7dd9_img.jpg)

Figure 4-12: Cross-section of a typical CMOS well structure with parasitic BJTs and the primary resistances involved in the process of initiating an SEL. The diagram shows a cross-section of a CMOS well structure with layers: VDD, Anode, Cathode, VSS, N+, P+, N+, P+. The parasitic BJTs are shown with their respective resistances: R\_N-well and R\_sub. The diagram also shows the lengths L\_N+, L\_Anode-cathode, and L\_P+.

**Figure 4-12. Cross-section of a typical CMOS well structure with parasitic BJTs and the primary resistances involved in the process of initiating an SEL.**  
Dark-gray regions are insulating isolation (shallow trench isolation).<sup>[19]</sup>

The parasitic BJTs are triggered when excess carriers injected by the ion event turn on the vertical PNP or lateral NPN BJTs.<sup>[18-21]</sup> The process occurs in several distinct stages. First, the excess injected charge is transported by drift, inducing hole and electron currents to flow into the well and substrate in opposite directions. The injected current produces voltage drops across the well and substrate-spreading resistance. The well and substrate resistivity, well depth and distance of the ion strike from the contacts define the magnitude of the voltage drops.

If the voltage drop in the well or substrate is large enough to forward-bias to the emitter base of either one of the two parasitic BJTs, the first BJT turns on, suddenly amplifying the current injection in the other parasitic BJT. Once the voltage forward-biases the emitter-base junction of the second BJT, it turns on, injecting current in the first BJT. At this point, a positive feedback loop has been initiated in which each parasitic BJT feeds the other.

Sustained latchup is only possible if the following four conditions are met:

- The emitter-base junctions of both parasitic BJTs become forward-biased.
- The current-gain product of the parasitic BJTs is greater than 1.
- The power supply can source a current greater than the holding current.
- The operating voltage,  $V_{DD}$ , is higher than the holding voltage.

The current-voltage characteristic of the PNP device responsible for latchup/SEL is shown in **Figure 4-13**. There are three distinct behavior modes for the PNP structure. Low operating current over the operating voltage range characterizes the normal operating region (1). Under normal operation, the emitter-base junctions of both BJTs are reverse-biased up to a maximum voltage where the electrical breakdown occurs.

Once a latchup or SEL is triggered, the device snaps into a high-current/lower-voltage state (3) determined by the intersection of the I-V curve and the load line (the load line is defined by the impedance between the power supply and the device). The region of negative resistance (2) connecting these two modes is indicative of the gain that the activation of the parasitic BJTs provides. The holding voltage,  $V_H$ , is the minimum voltage that can sustain a steady-state SEL condition. If the operating voltage exceeds  $V_H$ , the triggered SEL will be sustained until the device is powered down.

![Figure 4-13: I-V characteristic of normal and latchup conditions. The graph plots current (I) on the y-axis against voltage (V) on the x-axis. A red curve represents the device's I-V characteristic, showing three regions: 1 (normal operation), 2 (negative resistance), and 3 (latchup). A dashed blue line represents the load line. The intersection of the load line and the red curve in region 1 is the 'Hold point' at voltage V_H and current I_H. The intersection in region 3 is at a higher current level. The x-axis is labeled V_DD and the y-axis is labeled I_DD.](e999b14cdba9a4824937bb35d8489a03_img.jpg)

Figure 4-13: I-V characteristic of normal and latchup conditions. The graph plots current (I) on the y-axis against voltage (V) on the x-axis. A red curve represents the device's I-V characteristic, showing three regions: 1 (normal operation), 2 (negative resistance), and 3 (latchup). A dashed blue line represents the load line. The intersection of the load line and the red curve in region 1 is the 'Hold point' at voltage V\_H and current I\_H. The intersection in region 3 is at a higher current level. The x-axis is labeled V\_DD and the y-axis is labeled I\_DD.

**Figure 4-13.** I-V characteristic of normal and latchup conditions. Initially, the current injection causes an increase in the anode voltage. Once the first BJT is forward-biased (as  $V_H$  reaches the trigger voltage), it turns on the second BJT in a regenerative loop. The anode voltage drops while the circuit is held at a much higher current level.

The primary physical factors affecting the turn-on sensitivity of the parasitic BJT are the ion type, LET and trajectory, because these factors determine the amount of charge produced within the sensitive area and its spatial distribution. Higher LET events will

inject larger amounts of charge and thus increase SEL sensitivity because larger induced currents equate to higher induced voltages – thus increasing the probability that enough voltage will be generated across the emitter-base junction to initiate BJT turn-on.

Latchup/SEL sensitivity is also determined by the substrate and well doping, distance to the taps, actual operating voltage, and ambient temperature. The lower the substrate and well doping, the higher the resistance, and the less charge required to initiate the forward-biased condition. Similarly, the greater the distance between the closest tap and the event, the larger the well resistance and the more easily BJTs will turn on. Increasing the operating voltage puts a higher voltage across all of the resistances. Less charge is needed to trigger the BJT, again making an SEL more likely.

Operating at increased temperatures has two effects that increase the likelihood and severity of an SEL:

- As the temperature increases, the voltage required to forward-bias the emitter-base junction drops – less charge is needed to initiate the formation of the parasitic BJTs.
- The bipolar gain or beta increases with temperature, so the turn-on of the BJTs will happen more quickly (the higher gain provides more current). The BJTs will have a higher gain product, thus increasing the likelihood that the event results in a sustained latchup condition.

The occurrence of an SEL is bad news from a reliability standpoint in all scenarios, even if it is considered a nondestructive SEE and nothing appears permanently damaged. At the very least, the circuit loses functionality and requires a power shutdown to get rid of the latched state. In extreme cases, the SEL induces a parasitic structure with high gain and very low impedance, producing high currents that totally destroy the component.

Very often, electromigration damage in the metallization layers causes this catastrophic failure. In applications that require high reliability where SEL-free solutions are not available, adding external circuits can detect the occurrence of an SEL (usually by monitoring the supply current to the component, which increases significantly with an SEL onset) and rapidly initiate a power-down reset to minimize damage to the device.

One of the challenges of this approach is determining the supply-current detection level required and how to minimize the time during which an SEL condition persists before power reset. Additionally, latent damage caused by seemingly nondestructive SEL events sustained only for short durations has been shown to occur.<sup>[22]</sup> Latent damage manifests as structural damage that exhibits little to no electrically observable parametric sign; it can be detected only by microscopic surface analysis. The observed latent damage is predominantly electromigration artifacts: metal extrusions, metal bridges formed by melting and small cracks in isolation. **Figure 4-14** shows an example of a defect that is exhibiting all three artifacts. This defect was obtained from a device that was fully functional, based on electrical parameters after the SEL. These small latent defects do not cause the device to fail, but they do represent future hazards because the damage may degrade the device's expected lifetime.

If using non SEL-free parts with an external circuit to reset after an SEL, it is good engineering practice to do a physical failure analysis to ensure that latent damage did not occur. Because latent damage from an SEL seems to be primarily an electromigration challenge, it will depend on the interconnect-metallization layout and design of the circuit. In other words, latent damage depends not so much on technology but rather on the actual device design.

![Figure 4-14: Three grayscale SEM images showing latent defects. The left image shows a bright circular feature. The middle image shows a vertical crack in a metal line. The right image shows a bridge formation between two metal structures.](1edf00a8a0ad2faa21bedfd66e9323d7_img.jpg)

Figure 4-14: Three grayscale SEM images showing latent defects. The left image shows a bright circular feature. The middle image shows a vertical crack in a metal line. The right image shows a bridge formation between two metal structures.

**Figure 4-14.** Latent defect induced by an SEL that was thought to be nondestructive but shows classic signs of electromigration damage: extrusion of metal, bridge formation (keeping the two halves electrically connected), local changes in grain and cracking of the isolation.<sup>[22]</sup>

### 4.7 Single-event gate ruptures and single-event burnouts

Designed to conduct large currents in the on state and withstand large stand-off voltages in the off state, power transistors are often used on the output stage of power-switching circuits. They can be metal-oxide semiconductor field-effect transistors (MOSFETs) or BJTs, depending on the application.

A vertical double-diffused MOSFET (DMOSFET) and insulated gate bipolar transistor (IGBT) are two of the typical power transistors commonly employed. Most Texas Instruments power solutions for space are based on vertical power DMOSFETs, so the focus here will be on this type of power device.

**Figure 4-15** is a cross-section of a vertical DMOSFET. The DMOSFET can switch relatively high currents at high voltages from the top source contacts to the drain contact at the substrate. The high current capability of these transistors is obtained by using a large N+ source/substrate area (usually achieved with multiple smaller devices in parallel), while the high voltage capability is enabled by the lightly doped N-epitaxial drift region, which can sustain a large source-to-drain electric field without breaking down.

With the gate electrode grounded, the N-channels on each side of the neck region (P-) are both in accumulation, so they are turned off. When applying a positive gate voltage to the structure, the two channel regions go into inversion, enabling electron current from the two-source regions to flow laterally across the newly formed channels into the neck region and turning on the device.

With a positive drain-to-source voltage, electrons injected into the neck region are then transported vertically down through the N-drift region to the drain terminal. The DMOS doping is optimized such

that the drain breakdown voltage is sufficiently large for the target application. Minimizing the thickness of the drift region keeps the on-state drain resistance as low as possible.

![Figure 4-15: Cross-section diagram of a DMOSFET. It shows a GATE electrode at the top, connected to a Neck region. The Neck region is flanked by N+ source regions and P+ body regions. Below the Neck is an N- epilayer drift region, and at the bottom is an N+ substrate. The Drain (+voltage) terminal is connected to the N+ substrate. The Source (ground) terminal is connected to the N+ source regions.](fca567a61a8702807c7118f9bb373b61_img.jpg)

Figure 4-15: Cross-section diagram of a DMOSFET. It shows a GATE electrode at the top, connected to a Neck region. The Neck region is flanked by N+ source regions and P+ body regions. Below the Neck is an N- epilayer drift region, and at the bottom is an N+ substrate. The Drain (+voltage) terminal is connected to the N+ substrate. The Source (ground) terminal is connected to the N+ source regions.

**Figure 4-15.** Cross-section of DMOSFET and IGBT devices used for power applications.

Most power devices are robust enough that lower-Z, lower-LET ion events cannot inject enough charge to precipitate any SEEs. In many cases, even higher LET events will only cause a brief disruption and output transient. However, in some cases, a high-LET heavy-ion strike through the power DMOS device while it is in the off state can generate enough charge to induce catastrophic failure by one of two mechanisms: the SEB and the SEGR.

A heavy-ion strike traversing the P-body channel region, the P-body under the N+ source region or the neck region close to the P-body can initiate an SEB.<sup>[23]</sup> An SEB is similar to an SEL except that in an SEB, only a single parasitic bipolar device is turned on. If the LET of the incident heavy ion is high enough, the excess charge injected by the ion strike can induce a voltage drop. This voltage drop forward-biases the emitter-base junction of the parasitic NPN formed by the N+ source, the P base region and the N-drift region inherent in the IGBT MOSFET diode DMOS power transistor, as shown in **Figure 4-16**. This parasitic BJT then greatly increases the current flowing.

If the strike occurs while the DMOSFET is under a high-enough drain bias that avalanche carrier multiplication occurs, then a second breakdown of the parasitic NPN BJT occurs, leading to catastrophic failure (localized melting) of the DMOS device. Simulation studies have shown that DMOS sensitivity to an SEB is highest when the ion event occurs in the neck region, close to either one of the two channel regions.<sup>[24]</sup> An SEB heavily depends on the source-to-drain voltage because below a certain voltage (where avalanche multiplication is shut off), the turn-on of the parasitic BJT will be a transient event, lasting several nanoseconds before the BJT turns off. Without the additional carrier injection provided by the avalanche multiplication process, the BJT shuts off rapidly and the device does not suffer a catastrophic SEB.

![Figure 4-16: A cross-sectional diagram of a DMOSFET showing a parasitic BJT structure. The device has a Gate electrode, Source (ground), and Drain (+voltage). The structure includes N+ regions for the source and drain, P+ regions for the body, and an N- epilayer drift region on an N+ substrate. A 'Neck' is indicated at the top of the channel. A 'Parasitic PNP turned on during SEB' is shown with arrows indicating carrier movement. The diagram illustrates how a heavy-ion strike can activate this parasitic BJT.](082d0abee7c2c27ee2f41d423ca814ea_img.jpg)

Figure 4-16: A cross-sectional diagram of a DMOSFET showing a parasitic BJT structure. The device has a Gate electrode, Source (ground), and Drain (+voltage). The structure includes N+ regions for the source and drain, P+ regions for the body, and an N- epilayer drift region on an N+ substrate. A 'Neck' is indicated at the top of the channel. A 'Parasitic PNP turned on during SEB' is shown with arrows indicating carrier movement. The diagram illustrates how a heavy-ion strike can activate this parasitic BJT.

Figure 4-16. A DMOSFET with a parasitic BJT that causes an SEB during a heavy-ion strike.

Figure 4-17 illustrates this behavior. The figure is a plot comparing the response of a diode, MOSFET and IGBT to a heavy-ion event at two voltages: one below the threshold for avalanche multiplication and one above the threshold voltage, where all devices are driven to a sustained high-current SEB mode. Even a transient event can cause latent damage, as with a nondestructive SEL.

![Figure 4-17: A log-log plot of Current (A) versus Time (s). The y-axis ranges from 10^-8 to 10^1 A, and the x-axis ranges from 10^-12 to 10^-7 s. Three curves are shown: IGBT (blue), MOSFET (red), and Diode (green). The IGBT curve shows a sharp increase in current at approximately 10^-10 s, reaching a plateau around 10^0 A. The MOSFET and Diode curves show a similar sharp increase at approximately 10^-10 s, reaching a plateau around 10^-1 A. A dashed line labeled 'Nonmultiplication event' shows a much lower current level, around 10^-3 A, for the same time range.](730b6615db6d402580db1024a7f4e163_img.jpg)

Figure 4-17: A log-log plot of Current (A) versus Time (s). The y-axis ranges from 10^-8 to 10^1 A, and the x-axis ranges from 10^-12 to 10^-7 s. Three curves are shown: IGBT (blue), MOSFET (red), and Diode (green). The IGBT curve shows a sharp increase in current at approximately 10^-10 s, reaching a plateau around 10^0 A. The MOSFET and Diode curves show a similar sharp increase at approximately 10^-10 s, reaching a plateau around 10^-1 A. A dashed line labeled 'Nonmultiplication event' shows a much lower current level, around 10^-3 A, for the same time range.

Figure 4-17. DMOS, diode and IGBT responses to heavy-ion strikes with and without avalanche multiplication. Multiplication provides regenerative feedback for the parasitic BJT, driving much higher current levels that rapidly destroy the devices.<sup>[26]</sup>

Like an SEB, an SEGR only occurs when the DMOS device is in the off state when a heavy ion strikes the neck region of the device.<sup>[26-28]</sup> The energy deposited by the ion creates a high density of excess e-h pairs in both the oxide and the silicon.

With a positive bias on the drain and ground or a negative bias on the gate electrode, drift separates the excess electrons and holes in the silicon. The holes are driven upward toward the

silicon/silicon dioxide (Si/SiO<sub>2</sub>) interface where they accumulate, while the electrons are transported toward the drain, as illustrated in Figure 4-18 and 4-19.

While the electrons have been drawn toward the positively biased (with respect to the source) drain contact, the holes have transported toward the negatively biased gate electrode. Because the oxide blocks the transport of the holes, they accumulate at the interface, where they induce an increase in the gate-oxide electric field.

![Figure 4-18: A cross-sectional diagram of a DMOSFET showing hole accumulation during a heavy-ion strike. The device has a Gate electrode, Source (ground), and Drain (+voltage). The structure includes N+ regions for the source and drain, P+ regions for the body, and an N- epilayer drift region on an N+ substrate. A 'Neck' is indicated at the top of the channel. Red '+' signs represent accumulated holes at the gate oxide interface, and blue '-' signs represent electrons moving toward the drain. The diagram illustrates how a heavy-ion strike can lead to a gate-oxide breakdown.](0895c2157aef064af8117233df148319_img.jpg)

Figure 4-18: A cross-sectional diagram of a DMOSFET showing hole accumulation during a heavy-ion strike. The device has a Gate electrode, Source (ground), and Drain (+voltage). The structure includes N+ regions for the source and drain, P+ regions for the body, and an N- epilayer drift region on an N+ substrate. A 'Neck' is indicated at the top of the channel. Red '+' signs represent accumulated holes at the gate oxide interface, and blue '-' signs represent electrons moving toward the drain. The diagram illustrates how a heavy-ion strike can lead to a gate-oxide breakdown.

Figure 4-18. A DMOSFET collecting excess holes during a heavy-ion strike. The hole accumulation ultimately leads to a gate-oxide breakdown.

![Figure 4-19: A cross-sectional diagram of a DMOSFET showing the accumulation of holes under gate oxide and the formation of image charge. The device has a Gate electrode, Source (ground), and Drain (+voltage). The structure includes N+ regions for the source and drain, P+ regions for the body, and an N- epilayer drift region on an N+ substrate. A 'Neck' is indicated at the top of the channel. Red '+' signs represent accumulated holes at the gate oxide interface, and blue '-' signs represent electrons moving toward the drain. The diagram illustrates how a heavy-ion strike can lead to a gate-oxide breakdown.](a4bfac39bb68bb6761d17d9cefe479ec_img.jpg)

Figure 4-19: A cross-sectional diagram of a DMOSFET showing the accumulation of holes under gate oxide and the formation of image charge. The device has a Gate electrode, Source (ground), and Drain (+voltage). The structure includes N+ regions for the source and drain, P+ regions for the body, and an N- epilayer drift region on an N+ substrate. A 'Neck' is indicated at the top of the channel. Red '+' signs represent accumulated holes at the gate oxide interface, and blue '-' signs represent electrons moving toward the drain. The diagram illustrates how a heavy-ion strike can lead to a gate-oxide breakdown.

Figure 4-19. Accumulation of holes under gate oxide and the formation of image charge that drives the gate electric field to exceed the breakdown field during a catastrophic SEGR.<sup>[29]</sup>

The increase of positive-hole charge at the interface induces an equal image-electron charge at the opposite side of the gate oxide, further increasing the field across the oxide. Further hole collection from the ion event sustains the hole distribution at the interface.

The holes accumulated below the oxide expand laterally toward the P-body regions at ground potential. Because the charge injection and collection after an ion event are more rapid than the dissipative mechanisms (transport, recombination), a significant voltage transient develops across the gate oxide for a brief period.

If the magnitude of the induced oxide electric field exceeds the intrinsic breakdown strength, the oxide will break down catastrophically, short-circuiting the gate electrode to the substrate. Simulations and experiments have demonstrated that operation at higher temperatures induces a higher oxide electric field, thus increasing the probability of an SEGR.<sup>[30]</sup>

The increase in the oxide electric field is due to the decrease of carrier mobility at higher temperatures, slowing down the transport of accumulated hole charge away from the neck region. Studies of vertical devices have also shown that ion strikes at normal incidence are most likely to cause an SEGR. Lateral DMOS devices may exhibit different behavior.

Both SEBs and SEGRs are SEEs driven by the drain-to-source and gate-to-source voltages when the DMOSFET is in the off state. In both cases, the higher the bias voltages, the easier it is to induce an SEB or SEGR.

### 4.8 Prompt-dose effects

The prompt-dose environment (also referred to as the prompt-gamma environment) is a very specialized transient radiation environment created by the detonation of nuclear devices that delivers a high dose of gamma rays and X-rays over a very short time interval (microseconds to milliseconds). Both the dose and dose rate are a function of the distance from ground zero of the detonation site. Radiation intensity drops off as the distance from ground zero increases by the inverse square law ( $1/r^2$ ).

Additionally, some absorption of the emitted radiation occurs in the atmosphere, so absorption also contributes to flux reduction as a function of increased distance. Ironically, in the short period after a nuclear detonation, the sensitivity to transient effects is much more of a concern than the high dose. In stark contrast to typical single events experienced in the space or terrestrial environments, which are singular and localized events, the prompt-dose environment is global, with a transient radiation event affecting every device in an integrated circuit simultaneously.

The primary effect of prompt-dose events in microelectronics is to produce a global ionization that induces transient currents (photocurrents) in junctions. The induced transient photocurrents flow in the same direction as the junction-leakage current and produce one of three responses encountered in microelectronic devices, depending on the dose rate experienced:

- The device continues to function normally and operates through the event unscathed.
- The device suffers upsets and a partial or complete loss of functionality but survives the event, only needing to be reset.

- The device suffers catastrophic destruction when the prompt-dose event triggers an SEL, SEB or SEGR.<sup>[31, 32]</sup> Prompt-dose events generate photocurrent that is defined by the size of the circuit-junction area, the gamma-energy spectrum and flux, and the dynamic ability of the electronic circuit to sink the excess transient currents. Unlike SEEs produced by single heavy-ion events, the density of the generated charge is not the key feature, because the effective LET is very low for gamma-photon events.

For example, the photoelectric effect creates one e-h pair in silicon for each absorbed photon with 3.6 eV or greater energy. All exposed junctions produce a photocurrent transient at the same time.

Small junctions with small collection volumes generate smaller photocurrents, while larger junctions produce larger photocurrents. Operating at higher voltages increases the depletion width of reverse-biased junctions and leads to increased photocurrent magnitudes because the charge-collection volume is larger.

In addition to the direct photocurrent generated in junctions, a secondary photocurrent, usually seen at intermediate and higher dose rates, can be generated by parasitic bipolar devices that get forward-biased by the injection from the prompt photocurrent.<sup>[33]</sup> The prompt-dose response of microelectronics depends both on their construction and design and, to a large extent, on the effective dose rate to which the part is exposed.

Depending on the prompt-dose rate, a variety of different upset and failure modes have been observed. Any component has a potential upset threshold dose rate, above which functional errors start to occur (with the exception of devices that can operate through the maximum dose rate). As the dose rate further increases above the critical threshold, the ever-larger induced photocurrents affect more circuitry; eventually, at very high dose rates, destructive failures may be induced.

Such behavior is demonstrated by the SRAM bit maps shown in [Figure 4-20](#), each obtained from an SRAM device immediately after exposure to a single prompt-dose event. The SRAM was reset after each run and the magnitude of the prompt dose was increased after each event. As the prompt-dose rate increases, you'll see only localized single-bit failures similar to those encountered with conventional SEEs – except that as the dose rate increases, larger and larger regions of the device will be upset. The SBUs are not completely uncorrelated but actually linked to regions of bits that have a lower Q-value,  $Q_{crit}$ , due to manufacturing variations across the die. When the dose rate increases further, fully correlated failures start occurring, along with a drop in the power-supply voltage, affecting bits tied to the specific branch that is drooping. This effect is called rail-span collapse because the observed SEUs correlate to specific power nodes and directly relate to the droop in  $V_{DD}$  that the high transient photocurrents cause.

![Figure 4-20: Comparison of SRAM failures induced by prompt-dose exposures. Four maps showing spatial voltage distribution at dose rates of 1.15, 1.40, 1.60, and 1.70. The maps show increasing failure patterns as the dose rate increases.](a74fdbc8b78564b89bc1b262cfd995b6_img.jpg)

Figure 4-20: Comparison of SRAM failures induced by prompt-dose exposures. Four maps showing spatial voltage distribution at dose rates of 1.15, 1.40, 1.60, and 1.70. The maps show increasing failure patterns as the dose rate increases.

Figure 4-20. Comparison of SRAM failures induced by prompt-dose exposures. Note the differences in failure modes as the dose rate increases from top to bottom. The relative dose rate is shown in the upper right of each map (where 1.0 is the onset dose rate). Adapted from.<sup>[34]</sup>

Rail-span collapse is one of the dominant upset mechanisms in digital technologies. Figure 4-21 shows simulation results<sup>[35]</sup> displaying the spatial voltage distribution within a memory array under three different conditions.

On the left side of Figure 4-21, the plot shows the  $V_{DD}$  for an unirradiated device. As expected, it has a uniform voltage distribution, with all bit cells biased at the same value of  $V_{DD}$ . The middle and right-side plots show the  $V_{DD}$  distribution at two different dose rate exposures,  $1 \times 10^9$  and  $3 \times 10^9$  rad(Si)/s, respectively. Note the shape of the collapsing  $V_{DD}$ ; bits farther away from the power-distribution rails will suffer a bigger drop due to the increased interconnect resistance at larger distances from the power rails. As the dose increases, the droop increases; soon, all bits in the array will fail because of the lack of induced-voltage margin.

Because the prompt-dose effect is a transient gamma pulse, as long as no destructive effects are triggered, the microelectronic device will resume normal operation once the photocurrents and induced rail-span collapse have recovered. In digital systems, the bits that failed will need to be rewritten with valid data, but the device itself will be undamaged and will function normally after a reset. The only exception would be if the total dose exposure received was so high that it caused permanent functional failures or triggered a destructive SEE.

![Figure 4-21: Simulations of memory-array voltage distribution. Three 3D surface plots showing VDD distribution across A Position and Y Position. The left plot is for an unirradiated device (SA 3011) showing a uniform distribution. The middle plot is for a prompt-dose exposure of 1 x 10^9 rad(Si)/s (SA 3011-Bulk) showing a slight droop. The right plot is for a prompt-dose exposure of 3 x 10^9 rad(Si)/s (SA 3011-Bulk) showing a significant droop and rail-span collapse. The Y-axis represents VDD from 0.0 V to 10.0 V.](411bc48fd105531df2c427c06acd6aaa_img.jpg)

Figure 4-21: Simulations of memory-array voltage distribution. Three 3D surface plots showing VDD distribution across A Position and Y Position. The left plot is for an unirradiated device (SA 3011) showing a uniform distribution. The middle plot is for a prompt-dose exposure of 1 x 10^9 rad(Si)/s (SA 3011-Bulk) showing a slight droop. The right plot is for a prompt-dose exposure of 3 x 10^9 rad(Si)/s (SA 3011-Bulk) showing a significant droop and rail-span collapse. The Y-axis represents VDD from 0.0 V to 10.0 V.

Figure 4-21. Simulations of memory-array voltage distribution, showing the effect of rail-span collapse as a function of dose-rate exposure. The left-hand plot is unexposed, while the middle and right plots are at  $1$  and  $3 \times 10^9$  rad(Si)/s prompt-dose exposures. The effect of the photocurrents is to pull down  $V_{DD}$  during the transient.<sup>[35]</sup>

### End Notes

P. E. Dodd and L. W. Massengill, "Basic mechanisms and modeling of single-event upset in digital microelectronics," *IEEE Trans. Nucl. Sci.* 50(3), June 2003, pp. 583-602.

F. W. Sexton, "Destructive single-event effects in semiconductor devices and ICs," *IEEE Trans. Nucl. Sci.* 50(3), June 2003, pp. 603-621.

### References

- 1 R. C. Baumann, "Radiation-induced soft errors in advanced semiconductor technologies," *IEEE Trans. Device Materials and Reliability* 5(3), Sept. 2005, pp. 305-316.
- 2 C. M. Hsieh, P. C. Murley and R. O'Brien, "A field-funneling effect on the collection of alpha-particle-generated carriers in silicon devices," *IEEE Trans. Electron Device Letters* 2(4), Dec. 1981, pp. 686-693.
- 3 M. P. Baze and S. P. Buchner, "Attenuation of single event induced pulses in CMOS combinational logic," *IEEE Trans. Nucl. Sci.* 44(6), Dec. 1997, pp. 2217-2223.
- 4 B. Narasimham et al., "Characterization of digital single event transient pulse-widths in 130-nm and 90-nm CMOS technologies," *IEEE Trans. Nucl. Sci.* 54(6), Dec. 2007, pp. 2506-2511.
- 5 L. W. Massengill and P. W. Tuinenga, "Single-event transient pulse propagation in digital CMOS," *IEEE Trans. Nucl. Sci.* 55(6), Dec. 2008, pp. 2861-2871.
- 6 P. E. Dodd, M. R. Shaneyfelt, J. A. Felix and J. R. Schwank, "Production and propagation of single-event transients in high-speed digital logic ICs," *IEEE Trans. Nucl. Sci.* 51(6), Dec. 2004, pp. 3278-3284.
- 7 Y. Boulghassoul, L. W. Massengill, T. L. Turlfing and W. T. Holman, "Frequency Domain Analysis of Analog Single-Event Transients in Linear Circuits," *IEEE Trans. Nuclear Sci.* 49(6), Dec. 2002, pp. 3142-3147.
- 8 "TPS50601-SP Single-Event Effects Summary," Texas Instruments Radiation Report SLAK017A, Dec. 2017, pp. 1-30.
- 9 L. W. Massengill, "Cosmic and terrestrial single-event radiation effects in dynamic random access memories," *IEEE Trans. Nucl. Sci.* 43(2), April 1996, pp. 576-593.
- 10 P. E. Dodd and F. W. Sexton, "Critical charge concepts for CMOS SRAMs," *IEEE Trans. Nucl. Sci.* 42(6), Dec. 1996, pp. 1764-1771.
- 11 F. Wrobel, J. M. Palau, M. C. Calvet, O. Bersillon and H. Duarte, "Incidence of multi-particle events on soft error rates caused by n-Si nuclear reactions," *IEEE Trans. Nucl. Sci.* 47(6), Dec. 2000, pp. 2580-2585.
- 12 S. Satoh, Y. Tosaka and S. A. Wender, "Geometric effect of multiple-bit soft errors induced by cosmic ray neutrons on DRAMs," *IEEE Electron Device Letters* 21(6), June 2000, pp. 310-312.
- 13 J. Maiz, S. Harelend, K. Zhang and P. Armstrong, "Characterization of multi-bit soft error events in advanced SRAMs," *Digest of International Electronic Device Meeting*, Dec. 2003, pp. 21.4.1-21.4.4.
- 14 S. Buchner, M. Baze, D. Brown, D. McMorrow and J. Melinger, "Comparison of error rates in combinational and sequential logic," *IEEE Trans. Nucl. Sci.* 44(6), Dec. 1997, pp. 2209-2216.
- 15 R. Baumann, "The impact of technology scaling on soft error rate performance and limits to the efficacy of error correction," *Digest of International Electronic Device Meeting*, Dec. 2002, pp. 329-332.
- 16 N. Seifert and N. Tam, "Timing Vulnerability Factors of Sequentials," *IEEE Trans. Device Materials and Reliability* 4(3), Sept. 2004, pp. 516-522.
- 17 R. Koga, S. H. Penzin, K. B. Crawford and W. R. Crain, "Single event functional interrupt (SEFI) sensitivity in microcircuits," in *Proceedings of the Fourth European Conference on Radiation and Its Effects on Components and Systems (RADECS)*, Sept. 1998, pp. 311-318.
- 18 J. M. Benedetto, J. Black and G. Ott, "Soft error case study: Single event functional interrupts (SEFIs) in COTS SDRAMs," *IEEE NSREC Short Course*, 2008, pp. 1-20.
- 19 N. A. Dodds et al., "Selection of Well Contact Densities for Latchup-Immune Minimal-Area ICs," *IEEE Trans. Nuclear Sci.* 57(6), Dec. 2010, pp. 3575-3581.
- 20 G. Bruguier and J-M. Palau, "Single Particle-Induced Latchup," *IEEE Trans. Nucl. Sci.* 43(2), April 1996, pp. 522-532.
- 21 P. E. Dodd, M. R. Shaneyfelt, J. R. Schwank and G. L. Hash, "Neutron-induced latchup in SRAMs at ground level," *Proceedings of the International Reliability Physics Symposium*, April 2003, pp. 51-55.
- 22 H. N. Becker, T. F. Miyahira and A. H. Johnston, "Latent Damage in CMOS Devices from Single-Event Latchup," *IEEE Trans. Nucl. Sci.* 49(6), Dec. 2002, pp. 3009-3015.
- 23 G.H. Johnson, J.H. Hohl, R.D. Schrimpf and K.F. Galloway, "Simulating Single-Event Burnout of N-Channel Power MOSFETs," *IEEE Trans. Electron Devices* 40, 1993, pp. 1001-1008.
- 24 C. Dachs, F. Roubaud, J.M. Palau, G. Bruguier, J. Gasiot and P. Tastet, "Evidence of the Ion's Impact Position Effect on SEB in N-Channel Power MOSFETs," *IEEE Trans. Nucl. Sci.* 41(6), Dec. 1994, pp. 2167-2171.
- 25 W. Kaindl, G. Soelkner, H.-J. Schulze and G. Wachutka, "Cosmic Radiation-Induced Failure Mechanism of High Voltage IGBT," *Proceedings of the 17th International Symp. Power Semiconductor Devices & ICs*, May 23-26, 2005, Santa Barbara, CA, pp. 159-162.
- 26 J.R. Brews et al., "A Conceptual Model of Single-Event Gate Rupture in Power MOSFETs," *IEEE Trans. Nucl. Sci.* 40(6), Dec. 1993, pp. 1959-1966.

- 27 C.F. Wheatley et al., "Single-Event Gate Rupture in Vertical Power MOSFETs; An Original Empirical Expression," *IEEE Trans. Nucl. Sci.* 41(6), Dec. 1994, pp. 2152-2159.
- 28 M. Allenspach, J.R. Brews, I. Mouret, R.D. Schrimpf and K.F. Galloway, "Evaluation of SEGR Threshold in Power MOSFETs," *IEEE Trans. Nuclear Sci.* 41(6), Dec. 1994, pp. 2160-2166.
- 29 M. Allenspach et al., "Single-Event Gate-Rupture in Power MOSFETs: Prediction of Breakdown Biases and Evaluation of Oxide Thickness Dependence," *IEEE Trans. Nucl. Sci.* 42(6), Dec. 1995, pp. 1922-1927.
- 30 I. Mouret, M. Allenspach, R.D. Schrimpf, J.R. Brews and K.F. Galloway, "Temperature and Angular Dependence of Substrate Response in SEGR," *IEEE Trans. Nuclear Sci.* 41(6), Dec. 1994, pp. 2216-2221.
- 31 L. W. Massengill and S. E. Diehl-Nagle, "Transient Radiation Upset Simulations of CMOS Memory Circuits," *IEEE Trans. Nuclear Sci.* 31(6), Dec. 1984, pp. 1337-1343.
- 32 D. G. Mavis, D. R. Alexander and G. L. Dinger, "A Chip-Level Modeling Approach for Rail Span Collapse and Survivability Analyses," *IEEE Trans. Nuclear Sci.* 36(6), Dec. 1989, pp. 2239-2246.
- 33 G. L. Brucker, "Transient and Steady-State Radiation Response of CMOS/SOS Devices," *IEEE Trans. Nucl. Sci.* 21(6), Dec. 1974, pp. 201-207.
- 34 F. Gardic et al., "Analysis of Local and Global Transient Effects in a CMOS SRAM," *IEEE Trans. Nuclear Sci.* 43(3), June 1996, pp. 899-906.
- 35 L. W. Massengill and S. E. Diehl-Nagle, "Transient Radiation Upset Simulations of CMOS Memory Circuits," *IEEE Trans. Nuclear Sci.* 31(6), Dec. 1984, pp. 1337-1343.

# Chapter 5: Radiation sensitivity by technology

A microcircuit's radiation tolerance radiation is dependent upon many variables. This chapter will mainly focus on a product's sensitivity to radiation at a macro level, discussing general trends such as process technology and operating conditions. The next chapter will delve more deeply into the physics of radiation sensitivity and radiation mitigation techniques.

Some semiconductor technologies and process nodes (feature sizes) tend to be softer to radiation than others. But at the same time, it is important to note that two similar processes on the same technology node could have very different radiation responses.

Also, the wafer fab process is not the only determining factor for radiation hardness. Two products that share the same process can have very different radiation responses. Ultimately, semiconductor suppliers of radiation tested products have a better understanding of which processes and products are likely to be more radiation tolerant.

### 5.1 Total ionizing dose

In CMOS processes, the reduction in feature sizes over the years has generally resulted in an improvement in total ionizing dose (TID) survivability. Because ionizing radiation charges dielectrics, sensitivity to TID will depend on susceptible dielectric volume, its location and its influence on active circuits. In older CMOS processes with thick gate oxides and long channel lengths, ionizing radiation could cause threshold-voltage shifts.<sup>[1]</sup>

As gate thicknesses, voltages and feature sizes decreased and the composition of gate dielectrics changed, the impact of ionizing radiation on threshold voltage lessened. The limiting factor on TID survivability became the field oxide; charged field oxide created leakage paths underneath the oxide.<sup>[2-4]</sup>

The prevailing technology for CMOS field oxide in the 1980s and 1990s was the local oxidation of silicon (LOCOS) process (Figure 5-1). Due to many factors in the process and structure, LOCOS was very soft to ionizing radiation.<sup>[2]</sup> The grown LOCOS edge profile had a characteristic "bird's-beak" at the channel edge, which induced local electric fields that were very effective at attracting positive-hole-charge TID radiation exposure generated throughout the LOCOS volume. This hole charge attracted electrons in the n-channel MOS (NMOS) region and caused off-state leakage to result in functional failures at relatively low doses.

To accommodate scalability as process nodes dropped below 350 nm, the LOCOS process was replaced with shallow trench isolation (STI) where a trench is etched between transistors and then filled by deposited films (Figure 5-1).

STI does not give immunity to isolation leakage issues, but by managing the sidewall profile and the quality and morphology of the deposited dielectrics, TID in technologies with STI will often be much better than a similar technology with LOCOS isolation.

![Figure 5-1: Comparison of LOCOS and STI isolation technologies. The left image shows LOCOS with a 'bird's beak' structure, labeled with SiO2 and Si. The right image shows STI with a more uniform, rectangular structure, labeled with STI.](cd8f187b8a8fcf7d2fc1a64de05c9061_img.jpg)

Figure 5-1: Comparison of LOCOS and STI isolation technologies. The left image shows LOCOS with a 'bird's beak' structure, labeled with SiO2 and Si. The right image shows STI with a more uniform, rectangular structure, labeled with STI.

Figure 5-1. Thick-grown isolation oxide or LOCOS (left) and deposited STI used in more recent process technologies (right). The bird's-beak shape concentrates total ionizing dose (TID)-induced hole charge, causing leakage failures at the channel edge.<sup>[2]</sup>

The increased channel doping, thinner gate oxide and lower operating voltages all contribute to enhance robustness against TID in modern CMOS technologies. As illustrated in Figure 5-2, as feature sizes have reduced, TID performance has improved dramatically, largely due to the migration from LOCOS to STI. Use caution when assuming that an STI technology will automatically provide a high TID performance – the scatter in the data indicates that the physical properties and morphology of STI has a large effect on the final TID performance in MOSFET devices.<sup>[5, 6]</sup>

![Figure 5-2: Scatter plot of Total dose hardness (krad) vs Feature size (µm). The plot shows data points for various technology nodes, with closed symbols representing translated data (parametric values) and open symbols representing IC data (functional failures). The hardness generally increases as feature size decreases, with STI technology showing higher hardness than LOCOS at smaller nodes.](7a0777bbad359aeb869022b345b827ef_img.jpg)

| Feature size (µm) | Total dose hardness (krad) | Symbol Type    |
|-------------------|----------------------------|----------------|
| 0.8               | 0                          | Open (IC data) |
| 0.6               | 20                         | Open (IC data) |
| 0.5               | 40                         | Open (IC data) |
| 0.4               | 60                         | Open (IC data) |
| 0.35              | 70                         | Open (IC data) |
| 0.3               | 80                         | Open (IC data) |
| 0.25              | 100                        | Open (IC data) |
| 0.2               | 120                        | Open (IC data) |
| 0.18              | 150                        | Open (IC data) |
| 0.15              | 180                        | Open (IC data) |
| 0.12              | 200                        | Open (IC data) |
| 0.1               | 220                        | Open (IC data) |
| 0.08              | 250                        | Open (IC data) |
| 0.07              | 280                        | Open (IC data) |
| 0.06              | 300                        | Open (IC data) |
| 0.05              | 320                        | Open (IC data) |
| 0.04              | 350                        | Open (IC data) |
| 0.03              | 380                        | Open (IC data) |
| 0.02              | 400                        | Open (IC data) |
| 0.01              | 420                        | Open (IC data) |
| 0.005             | 450                        | Open (IC data) |
| 0.002             | 480                        | Open (IC data) |
| 0.001             | 500                        | Open (IC data) |

Figure 5-2: Scatter plot of Total dose hardness (krad) vs Feature size (µm). The plot shows data points for various technology nodes, with closed symbols representing translated data (parametric values) and open symbols representing IC data (functional failures). The hardness generally increases as feature size decreases, with STI technology showing higher hardness than LOCOS at smaller nodes.

Figure 5-2. TID hardness as a function of technology node – the use of STI became widespread at 250 nm to 180 nm. STI is generally less sensitive to TID exposure, but there is still a lot of variation.<sup>[7]</sup>

The level of TID that a CMOS product can survive depends on the dose rate the device receives. Because of self-annealing effects, CMOS products can withstand a much higher TID at low dose rates than at high dose rates. The Texas Instruments (TI) DAC121S101QML-SP space-grade precision digital-to-analog converter can fail at a dose below 30 krad(Si) when irradiated at a dose rate above 50 rad(Si)/s and survive doses greater than 100 krad(Si) when irradiated at a lower dose rate of 0.01 rad(Si)/s (Figure 5-3).<sup>[7]</sup>

When a CMOS product is irradiated at an HDR and is then biased after the radiation source is removed, the device may begin to recover. It is possible to simulate an LDR response by irradiating a device at an HDR, followed by a room-temperature anneal with the device biased.<sup>[6]</sup>

![Figure 5-3: Two line graphs showing the radiation tolerance of the DAC121S101QML-SP. The top graph plots 'INL with 5.5V supply (LSB)' against 'Radiation level [krad(Si)]'. The bottom graph plots 'Power down current (µA)' against 'Radiation level [krad(Si)]'. Both graphs compare four conditions: HDR biased (solid red line), HDR unbiased (solid blue line), LDR biased (dotted black line), and LDR unbiased (dashed green line). In both graphs, the HDR biased condition shows a sharp increase in INL and a sharp decrease in power down current starting around 30 krad(Si), while the other three conditions remain relatively flat and low.](db7d05c053733d838e1a0eb13415cbd7_img.jpg)

| Radiation level [krad(Si)] | HDR biased (LSB) | HDR unbiased (LSB) | LDR biased (LSB) | LDR unbiased (LSB) |
|----------------------------|------------------|--------------------|------------------|--------------------|
| 0                          | 2                | 2                  | 2                | 2                  |
| 20                         | 2                | 2                  | 2                | 2                  |
| 30                         | 2                | 2                  | 2                | 2                  |
| 40                         | 38               | 2                  | 2                | 2                  |
| 60                         | 40               | 2                  | 2                | 2                  |
| 80                         | 48               | 2                  | 2                | 2                  |
| 100                        | 58               | 2                  | 2                | 2                  |

| Radiation level [krad(Si)] | HDR biased (µA) | HDR unbiased (µA) | LDR biased (µA) | LDR unbiased (µA) |
|----------------------------|-----------------|-------------------|-----------------|-------------------|
| 0                          | 100             | 100               | 100             | 100               |
| 20                         | 100             | 100               | 100             | 100               |
| 30                         | 100             | 100               | 100             | 100               |
| 40                         | 400             | 100               | 100             | 100               |
| 60                         | 4200            | 100               | 100             | 100               |
| 80                         | 4800            | 100               | 100             | 100               |
| 100                        | 5800            | 100               | 100             | 100               |

Figure 5-3: Two line graphs showing the radiation tolerance of the DAC121S101QML-SP. The top graph plots 'INL with 5.5V supply (LSB)' against 'Radiation level [krad(Si)]'. The bottom graph plots 'Power down current (µA)' against 'Radiation level [krad(Si)]'. Both graphs compare four conditions: HDR biased (solid red line), HDR unbiased (solid blue line), LDR biased (dotted black line), and LDR unbiased (dashed green line). In both graphs, the HDR biased condition shows a sharp increase in INL and a sharp decrease in power down current starting around 30 krad(Si), while the other three conditions remain relatively flat and low.

**Figure 5-3.** The DAC121S101QML-SP irradiated at different dose rates, with the unit powered up during irradiation (biased) and the leads grounded during irradiation (unbiased). The HDR corresponds to 165 rad/s and LDR corresponds to 0.01 rad/s.

### CMOS impact of bias voltage

The bias voltage to which a device is subjected during irradiation also impacts CMOS sensitivity to ionizing radiation. A higher bias voltage will result in more charge buildup in the oxides. Analog CMOS products with wide operating voltage ranges will tend to survive a higher TID level when operating at lower voltages during irradiation.

The Texas Instruments DAC121S101QML-SP will fail at a TID lower than 30 krad(Si) when biased at the maximum operating voltage of 5.5 V during irradiation at an HDR. The device will pass at greater than 100 krad when biased at 3.3 V during irradiation at any dose rate. A device not biased during irradiation can survive a much higher TID level – in some cases an order of magnitude or more higher – than a device biased during irradiation. As feature sizes shrank, so did gate voltages in digital devices, which led to lower supply voltages and higher TID level survivability.<sup>[4]</sup>

### CMOS impact of process nodes/feature size

In general, CMOS process nodes above 1 µm are fairly soft to ionizing radiation, failing at TID levels below 30 krad(Si) and sometimes lower than 3 krad(Si). As process nodes dropped below 1 µm, some products began surviving levels as high as 100 krad(Si), especially at LDRs. Power processes such as high-voltage NMOS and DMOS tend to perform similarly to the larger CMOS process nodes. At the 180-nm node, it is typical for a product to pass 100 krad(Si) even at HDRs.

Deep submicron structures (90 nm and below) routinely are good to 300 krad or even into the Mrad levels. The exception is fully depleted CMOS structures on SOI substrates. Charging of the buried oxide can impact these structures.<sup>[9]</sup>

Deep submicron processes can also have higher voltage modules, with larger feature sizes and higher gate voltages. If higher voltage modules are used, they can become the limiting factor of the TID level of a product. For instance, Texas Instruments' space-grade ADC08D1520QML-SP and ADC14155QML-SP analog-to-digital converters are on the same CMOS 180-nm process. The ADC08D1520QML-SP only uses minimum-geometry 1.9-V cells and is rated to 300 krad. The ADC14155QML-SP also uses the 3.3-V modules available on this process and is rated to 100 krad.<sup>[7]</sup>

#### Classic linear bipolar products

Unlike CMOS processing, gradual evolutionary changes in bipolar process technology have had little impact on TID survivability. The classic junction-isolated bipolar integrated circuit (IC) has been around since the late 1960s. It features vertically integrated NPN transistors and may have additional elements such as junction resistors, MOS capacitors, bipolar FETs and horizontal PNP transistors. Some products also have inefficient vertical PNP transistors using the base area and substrate.

The minimum-sized feature is the metal-to-silicon contact or width of the junction resistor or metal lines, and is measured in microns. For instance, the minimum geometry of the LM139 is 10 µm. Products were generally handcrafted with unique layouts and changes to junction profiles to meet performance needs.

It has been stated that bipolar processes use low-quality oxide, which has led to poor TID performance and dose-rate issues.<sup>[10]</sup> In reality, bipolar process oxides were specifically engineered to provide the highest gain transistors with the highest breakdowns and lowest leakage possible. What is optimal for transistor performance in an analog circuit is not necessarily optimal for radiation hardness.

The TID survivability of classic bipolar analog products ranges from 1 to 100 krad(Si). TID performance can depend on the bipolar process, but also on the function of the device, the layout of the transistors and metal routing. Two products on the same process can have significantly different TID survivability levels. Texas Instruments' LM2941 and LP2953 space-grade low-dropout regulators (LDOs) have the same process, but different TID ratings (Table 1).

| Products     | Radiation tolerance |
|--------------|---------------------|
| LM2941QML-SP | 100 krad(Si)        |
| LP2953QML-SP | >30 krad(Si)        |

Table 1. TID rating of two LDOs using the same wafer fab process.

The different manufacturing improvements of bipolar products over the years might not have any impact on the TID response, or could have adverse effects. For example, in the early 1980s, a layer of silicon nitride was added to the top passivation as an excellent moisture barrier, which resulted in significant improvements to product reliability. But that additional layer of silicon nitride also resulted in the degradation of TID performance of many bipolar products.<sup>[11]</sup>

Improvements in process controls have enabled a reduction in feature sizes, and the LM139QML-SP from Texas Instruments has gone through several die shrinks since its release in 1972. The last die shrink, released in the 2000 time frame, made TID performance worse<sup>[10]</sup> because of changes in transistor sizes, shapes and metal routing. In addition to the changes detailed in reference,<sup>[12]</sup> a number of additional steps were required to return the space-grade LM139AQL-SP back to its pre-shrunk die radiation performance.

#### Enhanced low dose rate sensitivity

Many classic linear bipolar products have been shown exhibit Enhanced Low Dose Rate Sensitivity (ELDRS) where more degradation from ionizing radiation is seen when a product is irradiated at low dose rate than when at high dose rate (see Chapter 3). It is not possible to predict which products will show ELDRS, although the addition of the nitride passivation layer can enhance this phenomenon.<sup>[11]</sup>

As an example, some versions of the LM111 comparator have ELDRS, where the input bias current drifts higher when irradiated at an LDR of 0.01 mrad/s than when irradiated at 50 rad/s (Figure 5-4).<sup>[13]</sup> The space-grade LM111 from Texas Instruments does not exhibit ELDRS (Figure 5-5).<sup>[14]</sup>

![Figure 5-4: A log-log plot showing Input bias current (nA) versus Total dose [krad(SiO2)]. The y-axis ranges from 10 to 10,000 nA, and the x-axis ranges from 0 to 1,000 krad(SiO2). Two curves are shown: a red curve for 0.1 r/s 25C and a blue curve for 50 r/s 25C. Both curves show an initial increase in current with dose, peaking around 100 krad, followed by a decrease. A dashed horizontal line at 100 nA represents the Maximum Spec. A diagonal line labeled 'Transition line' separates the 'Upward trend "degradation"' region from the 'Downward trend "recovery"' region.](9107eaf139660e9cdd6a89667bc50aad_img.jpg)

Figure 5-4: A log-log plot showing Input bias current (nA) versus Total dose [krad(SiO2)]. The y-axis ranges from 10 to 10,000 nA, and the x-axis ranges from 0 to 1,000 krad(SiO2). Two curves are shown: a red curve for 0.1 r/s 25C and a blue curve for 50 r/s 25C. Both curves show an initial increase in current with dose, peaking around 100 krad, followed by a decrease. A dashed horizontal line at 100 nA represents the Maximum Spec. A diagonal line labeled 'Transition line' separates the 'Upward trend "degradation"' region from the 'Downward trend "recovery"' region.

Figure 5-4. Input bias current drift through radiation of an unidentified LM111.<sup>[13]</sup>

![Figure 5-5: A plot showing Input bias current (nA) versus Radiation (krad). The y-axis ranges from 0 to -180 nA, and the x-axis ranges from 0 to 100 krad. Four curves are shown: LDR biased (red solid), LDR unbiased (green solid), HDR biased (red dashed), and HDR unbiased (green dashed). All curves show a decrease in input bias current (becoming more negative) as radiation dose increases. The HDR curves are consistently more negative than the LDR curves.](812f92102114dc0fa8487e0bfc372472_img.jpg)

Figure 5-5: A plot showing Input bias current (nA) versus Radiation (krad). The y-axis ranges from 0 to -180 nA, and the x-axis ranges from 0 to 100 krad. Four curves are shown: LDR biased (red solid), LDR unbiased (green solid), HDR biased (red dashed), and HDR unbiased (green dashed). All curves show a decrease in input bias current (becoming more negative) as radiation dose increases. The HDR curves are consistently more negative than the LDR curves.

Figure 5-5. Input bias current for the Texas Instruments space-grade LM111QML-SP. Input current is a negative number, as the current is specified in terms of coming out of the device. HDR is at 38 rad/s and LDR is at 0.01 rad/s.

Some bipolar products behave like CMOSs and actually have less degradation at LDRs. The Texas Instruments space-grade LM111QML-SP comparator is rated to only 50 krad at an HDR, while it is rated to 100 krad at an LDR (Figure 5-6).<sup>[14]</sup> For some products, certain parameters will be worse at an LDR, while other parameters of the same device will be worse at an HDR. The only way to know if a classic bipolar product has ELDRS is to test it at an LDR.

![Figure 5-6: A plot showing Input bias current (nA) versus Radiation (krad). The y-axis ranges from 0 to 150 nA, and the x-axis ranges from 0 to 100 krad. Four curves are shown: LDR biased (red solid), LDR unbiased (green solid), HDR biased (red dashed), and HDR unbiased (green dashed). A horizontal line at approximately 25 nA represents the Spec limit. The LDR curves remain below the spec limit, while the HDR curves rise sharply above it after about 60 krad.](fcd880b51697eb8795dabe8dea711a51_img.jpg)

Figure 5-6: A plot showing Input bias current (nA) versus Radiation (krad). The y-axis ranges from 0 to 150 nA, and the x-axis ranges from 0 to 100 krad. Four curves are shown: LDR biased (red solid), LDR unbiased (green solid), HDR biased (red dashed), and HDR unbiased (green dashed). A horizontal line at approximately 25 nA represents the Spec limit. The LDR curves remain below the spec limit, while the HDR curves rise sharply above it after about 60 krad.

Figure 5-6. On the Texas Instruments LM111QML-SP space-grade comparator, output leakage current drifts out of specification after an HDR of 38 rad/s. The device is rated to 100 krad at an LDR, but only 50 krad at an HDR. HDR is 38 rad/s and LDR is 0.01 rad/s.

Unlike CMOS processes, it is difficult to predict how biasing will impact the performance of a linear bipolar product. For some products, being irradiated while unpowered is the worst case, especially at LDRs. For example, in the Texas Instruments LM117HVQML-SP space-grade adjustable high-voltage regulator, irradiating the unbiased device is the worst case for voltage reference ( $V_{REF}$ ) drift (Figures 5-6 and 5-7). On the LM2941QML-SP space-grade adjustable LDO, the output voltage drifts lower when the device is unbiased during irradiation, but drifts higher when powered up during irradiation (Figure 5-8).<sup>[15,16]</sup>

An important consideration is how the device is used when exposed to ionizing radiation. If the LM117 is powered up, it can survive a much higher TID level than when used in standby mode. That is why an ELDRS characterization includes irradiating some units in an unbiased condition.

![Figure 5-7: A line graph showing VREF (V) vs Exposure in krad(Si). The y-axis ranges from 1.15 to 1.35 V, and the x-axis ranges from 0 to 120 krad. Four curves are plotted: LDR biased (solid red), LDR unbiased (solid blue), HDR biased (dashed red), and HDR unbiased (dashed blue). The LDR unbiased curve shows the highest drift, reaching approximately 1.32 V at 100 krad. The LDR biased curve shows a slight decrease to about 1.24 V. The HDR curves remain relatively flat around 1.25 V.](dff659a422a9e5edd8ce41823a863379_img.jpg)

Figure 5-7: A line graph showing VREF (V) vs Exposure in krad(Si). The y-axis ranges from 1.15 to 1.35 V, and the x-axis ranges from 0 to 120 krad. Four curves are plotted: LDR biased (solid red), LDR unbiased (solid blue), HDR biased (dashed red), and HDR unbiased (dashed blue). The LDR unbiased curve shows the highest drift, reaching approximately 1.32 V at 100 krad. The LDR biased curve shows a slight decrease to about 1.24 V. The HDR curves remain relatively flat around 1.25 V.

**Figure 5-7. The  $V_{REF}$  drift of the Texas Instruments space-grade LM117HVHQL-SP. Irradiating the device in the unbiased condition with all leads tied together is the worst case, resulting in the highest amount of parametric drift through a 100-krad TID.**

![Figure 5-8: A line graph showing Output voltage (V) vs Exposure (krad). The y-axis ranges from 4.97 to 5.03 V, and the x-axis ranges from 0 to 110 krad. Four curves are plotted: LDR biased (solid red), LDR unbiased (solid blue), HDR biased (dashed red), and HDR unbiased (dashed blue). The LDR unbiased curve shows a significant decrease, dropping to about 4.98 V at 110 krad. The LDR biased curve shows a slight increase to about 5.01 V. The HDR curves remain relatively flat around 5.00 V.](53d8bef47c63e0897de4cd058bad2cbd_img.jpg)

Figure 5-8: A line graph showing Output voltage (V) vs Exposure (krad). The y-axis ranges from 4.97 to 5.03 V, and the x-axis ranges from 0 to 110 krad. Four curves are plotted: LDR biased (solid red), LDR unbiased (solid blue), HDR biased (dashed red), and HDR unbiased (dashed blue). The LDR unbiased curve shows a significant decrease, dropping to about 4.98 V at 110 krad. The LDR biased curve shows a slight increase to about 5.01 V. The HDR curves remain relatively flat around 5.00 V.

**Figure 5-8. Output voltage drift for TI's space grade LM2941QML-SP. When the units are biased during irradiation, the output voltage drifts high; it drifts low when the leads are connected together during irradiation.**

Many pure CMOS products have bipolar elements created by using the parasitic bipolar structures present on all bulk CMOS processes. These are commonly used to create references and ESD diodes. Could these bipolar elements exhibit ELDRS? Texas Instruments has tested several products on different CMOS processes at an LDR, specifically monitoring  $V_{REF}$  drift of the parasitic bipolar devices. ELDRS was not detected on these structures.<sup>[7]</sup>

#### Newer bipolar architectures

Revolutionary changes in bipolar architectures, such as vertically integrated PNP processes and silicon-germanium (SiGe) high-electron-mobility transistors, have drastically changed the TID performance of bipolar analog products. Many papers have been published showing SiGe transistors surviving multiple Mrads of TID exposure.<sup>[17]</sup> For bipolar CMOS processes with SiGe transistors, the CMOS portion of the die determines the TID rating for the product.<sup>[18]</sup> Texas Instruments has taken advantage of these newer bipolar technologies to develop space products such as the LM6172QML-SP, LM7171QML-SP<sup>[19]</sup> and LMH6702QML-SP<sup>[20]</sup>, which are rated to 300 krad and do not have ELDRS.

#### Post-fabrication factors

The processing that a die experiences after wafer fabrication, such as assembly and electrical stress, can have an impact on the TID performance of a product. On some products, burn-in before TID testing can impact the results (Figure 5-9).<sup>[21]</sup> Assembly in plastic packages versus a hermetic package can also change the TID performance of a device (Figure 5-9).<sup>[21]</sup> In many cases, Texas Instruments has observed better TID performance when a device is assembled in a ceramic package. This may be due to the additional stress on the die from the mold compound in a plastic package (which does not exist in a hermetic package), but there could be other factors involved. Even different types of hermetic packages have exhibited TID performance differences. In one case, a product showed ELDRS when packaged in a hermetic flat pack, but did not show ELDRS when packaged in a TO-52 metal can.<sup>[22]</sup>

![Figure 5-9: A line graph showing ICCH (A) vs Dose (krads) on a logarithmic scale. The y-axis ranges from 10^-11 to 10^-3 A, and the x-axis ranges from PreRad to 150 krad, followed by an Anneal phase. Four curves are plotted: Plastic: burned-in (solid red), Plastic: non-burned-in (solid blue), Ceramic: burned-in (dashed red), and Ceramic: non-burned-in (dashed blue). The Plastic: burned-in curve shows the highest current, peaking at about 10^-3 A at 50 krad. The Ceramic: burned-in curve shows the lowest current, peaking at about 10^-4 A at 50 krad. All curves show a sharp drop during the Anneal phase.](5347ac6c3230a27509cf53f7c30879b4_img.jpg)

Figure 5-9: A line graph showing ICCH (A) vs Dose (krads) on a logarithmic scale. The y-axis ranges from 10^-11 to 10^-3 A, and the x-axis ranges from PreRad to 150 krad, followed by an Anneal phase. Four curves are plotted: Plastic: burned-in (solid red), Plastic: non-burned-in (solid blue), Ceramic: burned-in (dashed red), and Ceramic: non-burned-in (dashed blue). The Plastic: burned-in curve shows the highest current, peaking at about 10^-3 A at 50 krad. The Ceramic: burned-in curve shows the lowest current, peaking at about 10^-4 A at 50 krad. All curves show a sharp drop during the Anneal phase.

**Figure 5-9. Supply current vs. radiation exposure of National Semiconductor's 54AC02 quad 5 NOR gate in ceramic and plastic packages, with and without burn-in before radiation. After 150 krad, the units were annealed for 168 hours at 125°C.<sup>[21]</sup>**

It has been speculated that residual hydrogen in a hermetic package after a lid seal can lead to a degradation in TID performance. In one study, exposed die irradiated in a hydrogen environment had much worse TID performance. The amount of degradation depended on the percentage of ambient hydrogen during irradiation (Figure 5-10).<sup>[23]</sup> When using radiation-hardness-assured bare die, give careful consideration to the environment of the assembly process.

![Figure 5-10: A line graph showing the change in input bias current (Delta Ib in nA) versus dose (rad(Si)/s) for a commercial-grade LM193 dual comparator. The y-axis is logarithmic, ranging from 10 to 1000 nA. The x-axis is logarithmic, ranging from 0.0001 to 1000 rad(Si)/s. Four curves are shown: 100% H2 (red), 1% H2 (dark blue), Air (light blue), and Virgin (cyan). The 100% H2 curve shows the least degradation, staying near 1000 nA. The Air curve shows moderate degradation, dropping to about 100 nA. The Virgin curve shows significant degradation, dropping to about 10 nA. The 1% H2 curve shows the most degradation, dropping to about 1 nA. A horizontal line at 1000 nA is labeled 'Bound', and a horizontal line at 10 nA is labeled 'Underestimate'.](fc4b3b76217e9b7dd5486922059bd838_img.jpg)

Figure 5-10: A line graph showing the change in input bias current (Delta Ib in nA) versus dose (rad(Si)/s) for a commercial-grade LM193 dual comparator. The y-axis is logarithmic, ranging from 10 to 1000 nA. The x-axis is logarithmic, ranging from 0.0001 to 1000 rad(Si)/s. Four curves are shown: 100% H2 (red), 1% H2 (dark blue), Air (light blue), and Virgin (cyan). The 100% H2 curve shows the least degradation, staying near 1000 nA. The Air curve shows moderate degradation, dropping to about 100 nA. The Virgin curve shows significant degradation, dropping to about 10 nA. The 1% H2 curve shows the most degradation, dropping to about 1 nA. A horizontal line at 1000 nA is labeled 'Bound', and a horizontal line at 10 nA is labeled 'Underestimate'.

Figure 5-10. Change in input bias current of a commercial-grade LM193 dual comparator when irradiated in various concentrations of hydrogen.<sup>[23]</sup>

### 5.2 Single-event effects

Most single-event effects (SEEs) are caused by an ion striking a circuit, generating electron-hole (e-h) pairs in the silicon. The electron and hole carriers can recombine (which would not cause any events) or be diffused to the active electric field of the device (which might result in some kind of electrical event). Chapter 4 details the different types of effects.

In a process with a high-resistivity substrate, the carrier lifetime is relatively long, creating a large sensitive volume that can be as deep as 60 to 100  $\mu\text{m}$  into the silicon. These processes will have a higher probability of SEEs. Classic bipolar and older CMOS processes are typically on high-resistivity substrates and have deep, sensitive volumes.

A highly doped, low-resistivity substrate will have a short carrier lifetime; typically, e-h pairs created in the low-resistivity substrate do not live long enough to create an SEE. For an SOI process, any carriers generated in the bulk silicon below the buried oxide (BOX) layer will be blocked from getting to the active areas by the BOX (Figure 5-22). Only the silicon above the BOX is the sensitive volume, resulting in a lower probability of an SEE.

### Single-event upset and single-event transients

At one time, nearly any nondestructive SEE was identified as a single-event upset (SEU). More recently, an SEU has been defined as a digital output bit flipping to the incorrect state. Single-event transients (SETs) are analog output pulses that eventually recover to the correct voltage level.

#### What is Epi?

Silicon-based ICs are built on a silicon wafer (substrate). The starting point is a wafer that is uniformly doped and has uniform resistivity throughout its bulk. "Epi" is short for epitaxial layer. It is a layer of crystalline silicon grown on top of the wafer.

Typical older CMOS processes used a P-, lightly doped, high-resistivity wafer. The wafer manufacturing process can cause defects in the surface of the wafer that can impact the performance of the transistors. Sometimes, a P-layer of epi is grown on the P-wafer because the surface of the epi has fewer defects. Some dual-well CMOS processes start out with a P+, highly doped, low-resistivity wafer with a P-epi layer grown on top of it. Classic bipolar processes start with a P-wafer.

The first step is an N+ buried layer diffusion; an N-epi layer is then grown on top of it (see Figure 5-19).

The e-h pairs generated in a P-substrate have a long lifetime, and an SEE-sensitive volume can be 60- to 100- $\mu\text{m}$  deep into the silicon. For P+ substrates, the carrier lifetime is relatively short; usually it is so short that the electrons and holes recombine before they can be swept up to the active area of the device, where they might cause an SEE.

The worst-case condition for an SEU is when a device is operating at the minimum operating voltage. As feature sizes decrease and digital elements are packed more closely together, it becomes more probable that a single ion could upset more than one bit, especially if the ion strikes the surface of the device, passing through more than one cell. This is known as multiple-bit upsets. See Chapter 6 for a more in-depth discussion on how scaling has impacted SEU probabilities.

SET probability, pulse amplitude and width are highly dependent on operating conditions, such as supply voltage, configuration and input differential (for an operational amplifier), as well as the input voltage and output load and capacitance (Figures 5-11, 5-12 and 5-13).<sup>[24-26]</sup> The proper choice of operating conditions and circuit design can reduce or even eliminate the severity of SETs (Table 2).<sup>[27, 28]</sup>

![Figure 5-11: A line graph showing the probability of output transients on the LM139 quad comparator. The y-axis is 'SEU cross-section (cm²/comparator)' on a logarithmic scale from 10⁻¹⁸ to 10⁻⁵. The x-axis is 'LET [MeV/(mg/cm²)]' on a linear scale from 0 to 80. Multiple curves are shown, each labeled with a value representing the input voltage differential (ΔV) in Volts: .05, .10, .20, .50, .78, .91, 1.04, 1.17, 1.3, 1.5. The curves show that as ΔV increases, the cross-section (probability) decreases for a given LET. A note states: 'The values of ΔV (Volts)'.](5f7e58c41b31a5f89850f013164d10a3_img.jpg)

Figure 5-11: A line graph showing the probability of output transients on the LM139 quad comparator. The y-axis is 'SEU cross-section (cm²/comparator)' on a logarithmic scale from 10⁻¹⁸ to 10⁻⁵. The x-axis is 'LET [MeV/(mg/cm²)]' on a linear scale from 0 to 80. Multiple curves are shown, each labeled with a value representing the input voltage differential (ΔV) in Volts: .05, .10, .20, .50, .78, .91, 1.04, 1.17, 1.3, 1.5. The curves show that as ΔV increases, the cross-section (probability) decreases for a given LET. A note states: 'The values of ΔV (Volts)'.

Figure 5-11. Probability of output transients on the LM139 quad comparator. Each line represents the input voltage differential ( $\Delta V$ ). The cross-section is proportional to the probability of an SET. The lower the cross-section and the higher linear energy transfer needed to create an SET, the lower the probability of an SET.<sup>[24]</sup>

![Figure 5-12: Output voltage transients on the LM139 under different supply and differential input voltages. The graph shows output voltage (V) vs. time (μs) for four conditions: Vcc=25 V, Vin=1 V (red solid); Vcc=5 V, Vin=1 V (cyan solid); Vcc=25 V, Vin=50 mV (red dashed); and Vcc=5 V, Vin=50 mV (cyan dashed). All curves show a sharp drop from 5V to 0V at t=0, followed by a recovery to 5V. The recovery time is longer for higher Vcc and higher Vin.](ce857617d1453e7e90edfaae561e2f62_img.jpg)

Figure 5-12: Output voltage transients on the LM139 under different supply and differential input voltages. The graph shows output voltage (V) vs. time (μs) for four conditions: Vcc=25 V, Vin=1 V (red solid); Vcc=5 V, Vin=1 V (cyan solid); Vcc=25 V, Vin=50 mV (red dashed); and Vcc=5 V, Vin=50 mV (cyan dashed). All curves show a sharp drop from 5V to 0V at t=0, followed by a recovery to 5V. The recovery time is longer for higher Vcc and higher Vin.

Figure 5-12. Different output transients on the LM139 under different supply voltages ( $V_{CC}$ ) and differential input voltages ( $V_{IN}$ ) with  $I_N$  at ground. Testing was done with a laser pulse so that energy injected was the same for each condition. The supply voltage does not have an impact on the pulse amplitude and width, but the  $V_{IN}$  does.<sup>[29]</sup>

![Figure 5-13: Maximum amplitude of SET pulses at the output of the LM117 linear regulator. The graph shows maximum output transient (V) vs. linear energy transfer (MeV-cm²/mg) for three load capacitor values: 0.1 μF (red), 1.1 μF (cyan), and 4.7 μF (blue). The amplitude increases with energy transfer and decreases with increasing load capacitance. A note indicates 250 to 400 events per measurement.](57e7a913a27e03b719a102d02c6bf985_img.jpg)

Figure 5-13: Maximum amplitude of SET pulses at the output of the LM117 linear regulator. The graph shows maximum output transient (V) vs. linear energy transfer (MeV-cm²/mg) for three load capacitor values: 0.1 μF (red), 1.1 μF (cyan), and 4.7 μF (blue). The amplitude increases with energy transfer and decreases with increasing load capacitance. A note indicates 250 to 400 events per measurement.

Figure 5-13. Maximum amplitude of SET pulses at the output of the LM117 linear regulator. Each line represents a different load-capacitor value. A higher load capacitance reduces the SET pulse amplitudes.<sup>[29]</sup>

| Cross-output | Maximum SET section | Amplitude positive | Maximum negative | SET duration |
|--------------|---------------------|--------------------|------------------|--------------|
| Capacitor    | (cm2)               | (V)                | (V)              | (μs)         |
| No Cap       | 1.0E-03             | 1.76               | -1.72            | 7.2+         |
| 30μF         | 1.4E-05             | 0.33               | -0.44            | 0.06         |
| 60μF         | None                | None               | None             | None         |

Table 2. LM4050-2.5 SET amplitudes and duration with different output capacitor values.<sup>[27]</sup>

Classic bipolar products with large transistors that are built on a high-resistivity substrate (resulting in deep sensitive volume) can have a higher probability of SETs with high pulse amplitudes and widths. On the LM124, under the right conditions, some transients have taken over 10  $\mu$ s to recover (Figure 5-14).<sup>[29]</sup> In contrast, on the space-grade LMH6702, which is on the Texas Instruments SOI VIP10 process, the transient widths are less than 10 ns.<sup>[30, 31]</sup> Most BiCMOS processes with SiGe transistors are on a high-resistivity substrate. Tests have shown a significant reduction in pulse widths and probability of an SET occurring when using a process with an SOI substrate (Figures 5-15 and 5-16).<sup>[32]</sup>

![Figure 5-14: Typical LM124 SET. The graph shows output voltage (V) vs. time (μs) for two conditions: Q3 ion (red) and Q3 bc-1.1pC (cyan). Both show a sharp drop from 1.2V to 0V at t=0, followed by a recovery. The Q3 ion recovery is much slower, taking over 10 μs, while the Q3 bc-1.1pC recovery is faster, taking about 5 μs.](2ff3bb4f3d116d00cea2366069aa94aa_img.jpg)

Figure 5-14: Typical LM124 SET. The graph shows output voltage (V) vs. time (μs) for two conditions: Q3 ion (red) and Q3 bc-1.1pC (cyan). Both show a sharp drop from 1.2V to 0V at t=0, followed by a recovery. The Q3 ion recovery is much slower, taking over 10 μs, while the Q3 bc-1.1pC recovery is faster, taking about 5 μs.

Figure 5-14. Typical LM124 SET.<sup>[29]</sup>

![Figure 5-15: Average transient on an NPN SiGe transistor comparing a standard p- low-resistivity substrate (bulk) to a SOI substrate. The graph shows collector current (mA) vs. time (ns) for a 36-MeV oxygen ion. The bulk nnp SiGe HBT (red) shows a large negative transient reaching -1.4 mA, while the SOI nnp SiGe HBT (cyan) shows a much smaller transient reaching about -0.2 mA. Parameters: Vcc = +3 V, SOI A_G = .25x10 μm², Bulk A_G = .5x2.5 μm².](19e9097c72fbcb33376cec8aa00d3186_img.jpg)

Figure 5-15: Average transient on an NPN SiGe transistor comparing a standard p- low-resistivity substrate (bulk) to a SOI substrate. The graph shows collector current (mA) vs. time (ns) for a 36-MeV oxygen ion. The bulk nnp SiGe HBT (red) shows a large negative transient reaching -1.4 mA, while the SOI nnp SiGe HBT (cyan) shows a much smaller transient reaching about -0.2 mA. Parameters: Vcc = +3 V, SOI A\_G = .25x10 μm², Bulk A\_G = .5x2.5 μm².

Figure 5-15. Average transient on an NPN SiGe transistor comparing a standard  $p$ - low-resistivity substrate (bulk) to a SOI substrate.<sup>[32]</sup>

![Figure 5-16: Cross-section curves for SETs on an NPN SiGe transistor. The graph plots Error cross-section/total CT area (log scale, 10^-4 to 10^0) against LET (MeV cm^2/mg, 0 to 60). Three curves are shown: Unhardened M/S (red), SiGe on SOI (blue), and SiGe on bulk (green). Annotations indicate reductions: 74% reduction, LET = 10; 84% reduction, LET = 4; 99.7% reduction, LET = 1.9. A note specifies SOI threshold = 1.8 and Bulk threshold = 0.1. The source is Texas A&M Cyclotron Institute, 500-MHz data signal.](8605b43090d582ea5046e1804178a7d8_img.jpg)

Figure 5-16: Cross-section curves for SETs on an NPN SiGe transistor. The graph plots Error cross-section/total CT area (log scale, 10^-4 to 10^0) against LET (MeV cm^2/mg, 0 to 60). Three curves are shown: Unhardened M/S (red), SiGe on SOI (blue), and SiGe on bulk (green). Annotations indicate reductions: 74% reduction, LET = 10; 84% reduction, LET = 4; 99.7% reduction, LET = 1.9. A note specifies SOI threshold = 1.8 and Bulk threshold = 0.1. The source is Texas A&M Cyclotron Institute, 500-MHz data signal.

Figure 5-16. Cross-section curves for SETs on an NPN SiGe transistor comparing a standard P- low-resistivity substrate (bulk) to an SOI substrate. The lower the cross-section, the lower the probability of an SET occurring in a space application.<sup>[25]</sup>

Changes to a product's layout can impact the SET response. When the LM139 went through a die shrink, the SET pulse widths were larger under certain operating conditions (Figure 5-17). Also, SET probability changed under different operating conditions.<sup>[25]</sup>

![Figure 5-17: Comparing the SET pulse widths of the LM139 before and after a die shrink. The graph plots Output voltage (V, -1 to 6) against Time (μs, -2.0 to 6.0). Four curves are shown: Old part, Vin=350 mV (red solid); ELDRS-free part, Vin=350 mV (blue solid); Old part, Vin=50 mV (red dashed); ELDRS-free part, Vin=50 mV (blue dashed). The ELDRS-free curves show significantly narrower pulses compared to the old part curves.](a346e19f92f1699e3f96432c0464c957_img.jpg)

Figure 5-17: Comparing the SET pulse widths of the LM139 before and after a die shrink. The graph plots Output voltage (V, -1 to 6) against Time (μs, -2.0 to 6.0). Four curves are shown: Old part, Vin=350 mV (red solid); ELDRS-free part, Vin=350 mV (blue solid); Old part, Vin=50 mV (red dashed); ELDRS-free part, Vin=50 mV (blue dashed). The ELDRS-free curves show significantly narrower pulses compared to the old part curves.

Figure 5-17. Comparing the SET pulse widths of the LM139 before a die shrink (old device) and after a die shrink of 20% (ELDRS-free device).  $V_{in}$  is the differential input voltage.

Besides causing SEEs, proton and heavy-ion strikes on an IC will also cause TID effects that impact the pulse amplitude and width of SETs (Figure 5-18).<sup>[33]</sup>

![Figure 5-18: Changes in the LM124 SET pulse shapes with TID level. The graph plots Amplitude (V, -2 to 5) against Time (s, -2x10^-6 to 8x10^-6). Multiple curves are shown for different TID levels: 0 krad (red), 5 krad (blue), 10 krad (green), 18 krad (cyan), 28 krad (magenta), 35 krad (black), and 50 krad (grey). As the TID level increases, the pulse amplitude decreases and the pulse width increases.](f22e617a7aef13de5ffd8e390bfda1c3_img.jpg)

Figure 5-18: Changes in the LM124 SET pulse shapes with TID level. The graph plots Amplitude (V, -2 to 5) against Time (s, -2x10^-6 to 8x10^-6). Multiple curves are shown for different TID levels: 0 krad (red), 5 krad (blue), 10 krad (green), 18 krad (cyan), 28 krad (magenta), 35 krad (black), and 50 krad (grey). As the TID level increases, the pulse amplitude decreases and the pulse width increases.

Figure 5-18. Changes in the LM124 SET pulse shapes with TID level.<sup>[33]</sup>

### Single-event latchup

In order for single-event latch-up (SEL) to occur, a PNPN silicon-controlled rectifier (SCR) with a gain greater than 1 must exist (see Chapter 4 for more details). These types of structures do not exist in a standard junction-isolated bipolar design and layout (Figure 5-19). SEL was reported on a nonstandard bipolar process<sup>[35]</sup> (Figure 5-20). This nonstandard process does not have a P+ isolation diffusion separating N-epi tubs and does not have an N+ buried layer. It appears to be more of a modification of LOCOS CMOS process than a classic bipolar architecture.

![Figure 5-19: Cross-section of a classic bipolar process. The diagram shows a P+ substrate (wafer) with an N+ buried layer. Above the substrate is an N-epi layer. The structure includes a Base region (P+), an Emitter region (N+), and a Collector region (N+). P+ junction isolation is used to prevent a PNPN-SCR structure from forming.](8c2b7159561b35cd2f9ef2d0b3a087da_img.jpg)

Figure 5-19: Cross-section of a classic bipolar process. The diagram shows a P+ substrate (wafer) with an N+ buried layer. Above the substrate is an N-epi layer. The structure includes a Base region (P+), an Emitter region (N+), and a Collector region (N+). P+ junction isolation is used to prevent a PNPN-SCR structure from forming.

Figure 5-19. Cross-section of a classic bipolar process. The wafer is lightly doped with high resistivity. The areas marked p+ indicates highly doped, low resistivity p area. p- indicates lightly doped, high resistivity p area. The P+ junction isolation prevents a PNPN-SCR structure from forming.<sup>[44]</sup>

![Figure 5-20: Cross-section of the bipolar device reported to have SEL in reference [35]. The diagram shows a P-substrate with two transistors, Q1 and Q2. Q1 has an N-type collector, a P+ base, and an N+ emitter. Q2 has an N-type collector, a P+ base, and an N+ emitter. Field oxide is present on the top surface. The structure is non-standard, lacking an N+ buried layer and P+ junction isolation between epi wells.](14ca186d20edaadaaf7e27710eb8a4de_img.jpg)

Figure 5-20: Cross-section of the bipolar device reported to have SEL in reference [35]. The diagram shows a P-substrate with two transistors, Q1 and Q2. Q1 has an N-type collector, a P+ base, and an N+ emitter. Q2 has an N-type collector, a P+ base, and an N+ emitter. Field oxide is present on the top surface. The structure is non-standard, lacking an N+ buried layer and P+ junction isolation between epi wells.

Figure 5-20. Cross-section of the bipolar device reported to have SEL in reference<sup>[35]</sup>. This is not a standard bipolar architecture and does not have an N+ buried layer and P+ junction isolation between epi wells.

In older supermicron CMOS processes, parasitic PNPN devices may be too large, with the base widths too big to be efficient enough to turn on or hold the latch-up voltage. Texas Instruments' LMC6484 quad operational amplifier on a 4- $\mu\text{m}$  CMOS process did not exhibit SEL under heavy-ion testing.<sup>[36]</sup> As process nodes shrink below 1  $\mu\text{m}$ , SEL becomes more prevalent.

Whether a CMOS device will have SEL depends on the layout. The space-grade DS90C031 and DS90C032 are both on the Texas Instruments CS80 800-nm process. The DS90C032 did not exhibit SEL, while the original layout of the DS90C031 did.<sup>[37,38]</sup> The PNPN structures that were responsible for SEL were identified and the layout changed to remove these structures.<sup>[39]</sup>

PNPN devices are typically created by NMOS and PMOS devices in close proximity, but there are other configurations that could create susceptible PNPN SCR structures, such as a PMOS area in close proximity to an N-resistor field (Figure 5-21).<sup>[39]</sup> Starting at around the 500-nm node and smaller, most CMOS processes are likely to experience SEL on standard CMOS structures without guard rings.

![Figure 5-21: Layout of the commercial-grade DS90C031 (top) and space-grade DS90C031 (bottom). The top image shows a standard CMOS layout with labels A, B, and C. The bottom image shows the same layout with P+ guard rings added to break up the parasitic PNPN SCR structure, with labels N+ and P+ indicating the modified regions.](9ebdcfefe6870fc994fb640732691648_img.jpg)

Figure 5-21: Layout of the commercial-grade DS90C031 (top) and space-grade DS90C031 (bottom). The top image shows a standard CMOS layout with labels A, B, and C. The bottom image shows the same layout with P+ guard rings added to break up the parasitic PNPN SCR structure, with labels N+ and P+ indicating the modified regions.

Figure 5-21. Layout of the commercial-grade DS90C031 (top). Laser probing determined that the area marked B was SEL-sensitive. The layout of the space-grade DS90C031 (bottom), with P+ guard rings added to break up the parasitic PNPN SCR.<sup>[39]</sup>

Being on a submicron CMOS process does not guarantee that a product will have SEL. There are commercial CMOS products (like some power products) that do not use standard CMOS cells or may use P+ guard rings as part of the design, similar to the space-grade version of the DS90C031.<sup>[39]</sup> Radiation-tolerant product suppliers like Texas Instruments understand which processes and what epi thicknesses are required to prevent SEL. With older products, the design archives may no longer be available, making a design review for radiation effects impossible.

There have been reports that some processes at the 90-nm node and below are inherently SEL-immune.<sup>[39,40]</sup> This is likely because as feature sizes have scaled down, so have operating voltages. A device on a 90-nm process might have an operating voltage of 1.2 V, which might be below the holding latch-up voltage for that parasitic PNPN SCR structure. However, products designed using a 65-nm device might have SEL because of the use of higher-voltage cells. Processes could also have higher-voltage modules susceptible to SEL. The 1.2-V power rails could be SEL-immune, while a 3.3-V module might latch up.

As with other SEEs, the wafer substrate could impact the SEL susceptibility of a process. It has been postulated that CMOS processes on SOI substrates do not have parasitic PNPN devices.<sup>[9]</sup> While this blanket statement is not correct for all SOI processes, it is true for some specific SOI architectures. If the process uses a very thin device layer (the active silicon on top of the BOX) and the STI is deep enough to reach down to the BOX, the N-channel and P-channel devices can be dielectrically isolated, eliminating the PNPN structures.

An alternative for SOI processes with thicker active layers is to use a deep trench isolation (DTI) that will reach down to the BOX (Figure 5-22). However, the deeper trench isolation can cause more stress on the silicon than STI. Sometimes, on processes that have DTI, DTI is only used on bipolar modules, with STI still used on the CMOS modules. SOI alone or an SOI process with DTI does not guarantee SEL immunity.

![Figure 5-22: Cross-sections of standard CMOS and SOI processes. The top diagram shows a standard CMOS process on a substrate with a buried oxide layer (BOX). It compares STI (Shallow Trench Isolation) and DTI (Deep Trench Isolation) structures. The bottom diagram shows an SOI process with a thin active layer on top of a BOX. It compares STI and DTI structures, showing that DTI can reach down to the BOX, potentially isolating the devices.](2618f4ebb25ee847035a7c3610533930_img.jpg)

Figure 5-22: Cross-sections of standard CMOS and SOI processes. The top diagram shows a standard CMOS process on a substrate with a buried oxide layer (BOX). It compares STI (Shallow Trench Isolation) and DTI (Deep Trench Isolation) structures. The bottom diagram shows an SOI process with a thin active layer on top of a BOX. It compares STI and DTI structures, showing that DTI can reach down to the BOX, potentially isolating the devices.

Figure 5-22. The cross-section of a standard CMOS process on an SOI substrate (top). The BOX is the buried oxide layer. A standard process uses STI and PNPN SCR structures that might have SEL. Whether an ion strike results in SEL depends on whether or not there is enough sensitive volume on top of the SOI to generate enough carriers to create latch-up. The bottom cross-section is of an SOI process using DTI. In this case, the PNPN structures do not exist.

Similarly, it is a myth that a CMOS product on a process that uses epi will be inherently SEL-immune. There are cases where a thin epi layer, when used in conjunction with a low-resistivity substrate, can reduce the probability of SEL, but not all CMOS processes that use epi will be SEL-immune. See the sidebar in this chapter, “What is epi?”.

In either case of an SOI or epi process, to have an SEL, there needs to be a parasitic SCR and enough active area to produce enough charge to turn the device on. The important thing to remember is that SOI or epi does not necessarily mean SEL immunity. More details about the process (and probably testing) are needed to verify SEL susceptibility. A supplier of radiation-tolerant products, such as Texas Instruments, understands which processes and what epi thicknesses are required to prevent SEL. See Chapter 6 for in-depth discussion on SEL mitigation techniques.

### Single-event functional interrupt

Originally, a single-event functional interrupt (SEFI) meant that a device went into a different operating mode as a result of an ion strike, as defined in the original JEDEC JESD57 and ASTM 1192<sup>[43]</sup> single-event test standards. Under this definition, only products programmable with registers that could be upset would be susceptible to SEFIs.

Recently, the definition in JESD57 was expanded to include any interruption in the function of the device, even if the device recovers on its own. Under this new definition, any product with a reset circuit is at risk for SEFIs.

### Single-event gate rupture, single-event burnout and single-event dielectric rupture

Single-event gate rupture (SEGR) and single-event burnout (SEB) are mainly a concern for power MOSFETs that pass relatively large amounts of current. Although they are different mechanisms, they can sometimes be difficult to discern from one another. See Chapter 4 for a discussion on mechanisms.

The threshold of failure for SEGR or SEB depends on the drain-source voltage, which is typically much lower than the rated voltage of the MOSFET. Therefore, it is usually necessary to derate the maximum operating voltage for space applications. SEGR can also depend on the gate-oxide thickness.<sup>[47]</sup>

SEB can depend upon the current passing through the FET (Figure 5-23).<sup>[47]</sup>

Single-event dielectric rupture (SEDR) has the same effect as SEGR, but for dielectrics other than gate oxides such as field and capacitor oxides. As with SEGR, SEDR depends on oxide thickness and voltage. There have been reports of SEDR on some linear amplifiers.<sup>[49]</sup> However, Texas Instruments has not seen a report of SEDR on any of its space-grade products.

### Displacement damage dose

Displacement damage is defined as crystalline defects caused by collisions with particles in space, typically protons. The types of technologies more sensitive to displacement damage dose (DDD) are those where silicon lattice damage degrades device performance. This will be of concern to processes with large structures and deep junctions and where minority carrier lifetime is important, like classic bipolar products.

Bipolar products can start to see degradation under fluences in the mid- $10^{11}$  N/cm<sup>2</sup>, or possibly lower. Surface devices like CMOS will survive a much higher fluence. Some programs with moderate dose requirements will test only bipolar devices and assume that CMOS products are not an issue.

### Dose rate, flash X-ray or prompt-dose testing

With dose-rate testing, large photocurrents are generated in the bulk of the silicon. Just as with an SEE, the sensitivity to dose rate will largely depend on the bulk material. For products on high-resistivity substrates, the photocurrents will have a much longer lifetime, and these products are more sensitive. Products on low-resistivity substrates where carrier lifetimes are shorter will be less sensitive. For a product on SOI, only the active area above the SOI will generate photocurrents.

![Figure 5-23: Safe operating area (SOA) of the Texas Instruments TPS50601-SP point-of-load switching regulator. The graph plots Input voltage, Vgs (voltage) on the y-axis (0.0 to 8.0) against Maximum load (amperes) on the x-axis (0 to 7). Three SOA regions are shown: SOA (LET ≤ 56.7) at the top, SOA (LET ≤ 65.4) in the middle, and Safe (LET ≤ 94.0) at the bottom. Data points for each LET level are plotted at 3, 4, 5, and 6 amperes. The region above the SOA (LET ≤ 56.7) is labeled 'Unsafe'.](df743a70d0295e880847c81ef47df4b5_img.jpg)

| Maximum load (amperes) | SOA (LET ≤ 56.7) V <sub>gs</sub> (V) | SOA (LET ≤ 65.4) V <sub>gs</sub> (V) | Safe (LET ≤ 94.0) V <sub>gs</sub> (V) |
|------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
| 3                      | ~7.5                                 | ~7.0                                 | ~6.5                                  |
| 4                      | ~6.5                                 | ~6.0                                 | ~5.5                                  |
| 5                      | ~6.0                                 | ~5.5                                 | ~5.0                                  |
| 6                      | ~5.5                                 | ~5.0                                 | ~4.5                                  |

Figure 5-23: Safe operating area (SOA) of the Texas Instruments TPS50601-SP point-of-load switching regulator. The graph plots Input voltage, Vgs (voltage) on the y-axis (0.0 to 8.0) against Maximum load (amperes) on the x-axis (0 to 7). Three SOA regions are shown: SOA (LET ≤ 56.7) at the top, SOA (LET ≤ 65.4) in the middle, and Safe (LET ≤ 94.0) at the bottom. Data points for each LET level are plotted at 3, 4, 5, and 6 amperes. The region above the SOA (LET ≤ 56.7) is labeled 'Unsafe'.

Figure 5-23. Safe operating area (SOA) of the Texas Instruments TPS50601-SP point-of-load switching regulator.<sup>[47]</sup>

|                                   | TID rating       | LDR performance | SEL probability |
|-----------------------------------|------------------|-----------------|-----------------|
| CMOS > 1 $\mu\text{m}$            | >30 krad         | Better than HDR | Possible        |
| CMOS 500 nm to 1 $\mu\text{m}$    | 30 to 100 krad   | Better than HDR | Possible        |
| CMOS 130 nm to 500 nm             | 100 to 300 krad  | Better than HDR | Likely          |
| CMOS < 90 nm                      | 100 krad to Mrad | Better than HDR | Possible        |
| Classic junction-isolated bipolar | 1 to 100 krad    | ELDRS possible  | Unlikely        |
| Newer high-speed bipolar          | 100 krad to Mrad | ELDRS unlikely  | Unlikely        |
| SiGe bipolar                      | Mrad             | ELDRS unlikely  | Unlikely        |
| BiCMOS with SiGe                  | 50 to 300 krad   | Better than HDR | Likely          |

*Table 3. Summary of general trends of radiation sensitivity by process. There are exceptions to the table.*

### References

- 1 M. R. Shaneyfelt, J. R. Schwank, D. M. Fleetwood, P. S. Winokur, K. L. Hughes et al., "Field dependence of interface-trap buildup in polysilicon and metal gate MOS devices," *IEEE Trans. Nucl. Sci.* 37(6), Dec. 1990, pp. 1632-1640.
- 2 H. L. Hughes and J. M. Benedetto, "Radiation Effects and Hardening of MOS Technology: Devices and Circuits," *IEEE Trans. Nucl. Sci.* 50(3), June 2003, pp. 500-521.
- 3 T. R. Oldham and F. B. McLean, "Total ionizing dose effects in MOS oxides and devices," *IEEE Trans. Nucl. Sci.* 50(3), June 2003, pp. 483-499.
- 4 H. J. Barnaby, "Total-Ionizing-Dose Effects in Modern CMOS Technologies," *IEEE Trans. Nucl. Sci.* 53(6), Dec. 2006, pp. 3003-3021.
- 5 M. R. Shaneyfelt, P. E. Dodd, B. L. Drper and R. S. Flores, "Challenges in hardening technologies using shallow-trench isolation," *IEEE Trans. Nucl. Sci.* 45(6), Dec. 1998, pp. 2584-2592.
- 6 D. M. Fleetwood, "Evolution of Total Ionizing Dose Effects in MOS Devices with Moore's Law Scaling," *IEEE Trans. Nucl. Sci.* 64(6), Dec. 2017, pp. 1-17.
- 7 K. Kruckmeyer, J. S. Prater, B. Brown and T. Thang, "Analysis of Low Dose Rate Effects on Parasitic Bipolar Structures in CMOS Processes for Mixed-Signal Integrated Circuits," *IEEE Trans. Nucl. Sci.* 58(3), June 2011, pp. 1023-103.
- 8 MIL-STD-883, Department of Defense Test Method Standard: Microcircuits, Defense Supply Center, June 2004, <https://landandmaritimeapps.dla.mil/Downloads/MilSpec/Docs/MIL-STD-883/std883.pdf>.
- 9 J. R. Schwank, V. Ferlet-Cavrois, M. R. Shaneyfelt, P. Paillet and P. E. Dodd, "Radiation effects in SOI technologies," *IEEE Trans. Nucl. Sci.* 50(3), June 2003, pp. 522-538.
- 10 R. D. Schrimpf, "Gain Degradation and Enhanced Low-Dose-Rate Sensitivity in Bipolar Transistors," *Institutional Journal of High Speed Electronics and Systems* 14(2), 2004, pp. 503-517.
- 11 M. R. Shaneyfelt, R. L. Pease, M. C. Maher, J. R. Schwank, S. Gupta et al., "Passivation Layers for Reduced Total Dose Effects and ELDRS in Linear Bipolar Devices," *IEEE Trans. Nucl. Sci.* 50(6), Dec. 2003, pp. 1785-1790.
- 12 R. L. Pease, M. C. Maher, M. R. Shaneyfelt, M. W. Savage, P. Baker et al., "Total-Dose Hardening of a Bipolar-Voltage Comparator," *IEEE Trans. Nucl. Sci.* 49(6), Dec. 2002, pp. 1785-1790.
- 13 H. J. Barnaby, R. D. Schrimpf, R. L. Pease, P. Cole, T. Turflinger et al., "Identification of Degradation Mechanisms in a Bipolar Linear Voltage Comparator Through Correlation of Transistor and Circuit Response," *IEEE Trans. Nucl. Sci.* 46(6), Dec. 1999, pp. 1666-1673.
- 14 K. Kruckmeyer, L. McGee, B. Brown and L. Miller, "Low Dose Rate Test Results of National Semiconductor's ELDRS-Free Bipolar Comparators LM111 and LM119," *2009 European Conference on Radiation and Its Effects on Components and Systems*, pp. 586-592.
- 15 K. Kruckmeyer, L. McGee, T. Trinh and J. Benedetto, "Low Dose Rate Test Results of National Semiconductor's ELDRS-Free Bipolar Low Dropout (LDO) Regulator, LM2941 at Dose Rates of 1 and 10 mrad(Si)/s," *2009 IEEE Radiation Effects Data Workshop*, July 20-24, 2009, pp. 59-64.
- 16 K. Kruckmeyer, L. McGee and T. Trinh, "Ultralow Dose Rate Test Results at 1 mrad(Si)/s to 100 krad(Si) for Texas Instruments ELDRS Free Bipolar LDO Regulator LM2941," presented at 2012 European Conference on Radiation and Its Effects on Components and Systems.
- 17 K. Kruckmeyer and T. Trinh, "ELDRS Characterization up to 300 Krad of Texas Instruments High Speed Amplifiers, LM7171 and LM6172," *2015 IEEE Radiation Effects Data Workshop*, July 13-17, 2015, pp. 1-5.
- 18 K. Kruckmeyer and T. Trinh, "ELDRS Characterization to 300 krad of Texas Instruments High Speed Amplifier LMH6702," *2016 IEEE Radiation Effects Data Workshop*, July 11-15, 2016, pp. 1-4.
- 19 F. Inanlou, N. E. Lourenco, Z. E. Fleetwood, I. Song, D. C. Howard et al., "Impact of Total Ionizing Dose on a 4th Generation, 90 nm SiGe HBT Gaussian Pulse Generator," *IEEE Trans. Nucl. Sci.* 61(6), Dec. 2014, pp. 3050-3054.
- 20 K. Kruckmeyer, T. Trinh, H. Castro, S. Dampousse and R. Butler, "TID and SEL Test Results for Texas Instruments' LMx2492 14 GHz PLL," *16th European Conference on Radiation and Its Effects on Components and Systems*, Sept. 19-23, 2016.
- 21 S. D. Clark, J. P. Bings, M. C. Maher, M. K. Williams, D. R. Alexander et al., "Plastic packaging and burn-in effects on ionizing dose response in CMOS microcircuits," *IEEE Trans. Nucl. Sci.* 42(6), Dec. 1995, pp. 1607-1614.
- 22 R. L. Pease, G. W. Dunham, J. E. Seiler, D. G. Platteter and S. S. McClure, "Total Dose and Dose Rate Response of an AD590 Temperature Transducer," *IEEE Trans. Nucl. Sci.* 54(4), Aug. 2007, pp. 1049-1054.
- 23 P. C. Adell, R. L. Pease, H. J. Barnaby, B. Rax, X. J. Chen et al., "Irradiation With Molecular Hydrogen as an Accelerated Total Dose Hardness Assurance Test Method for Bipolar Linear Circuits," *IEEE Trans. Nucl. Sci.* 56(6), Dec. 2009, pp. 3326-3333.
- 24 R. Koga, S. H. Penzin, K. B. Crawford, W. R. Crain, S. C. Moss et al., "Single Event Upset (SEU) Sensitivity Dependence of Linear Integrated Circuits (ICs) on Bias Conditions," *IEEE Trans. Nucl. Sci.* 44(6), Dec. 1997, pp. 2325-2332.
- 25 K. Kruckmeyer, S. P. Buchner and S. DasGupta, "Single-Event Transient (SET) Response of National Semiconductor's ELDRS-Free LM139 Quad Comparator," *2009 IEEE Radiation Effects Data Workshop*, pp. 65-70.
- 26 A. H. Johnston, T. F. Miyahira, F. Irom and J. S. Laird, "Single-Event Transients in Voltage Regulators," *IEEE Trans. Nucl. Sci.* 53(6), Dec. 2006, pp. 3455-3461.
- 27 K. Kruckmeyer, E. Morozumi, R. Eddy, T. Trinh, T. Santiago et al., "Single Event Transient and ELDRS Characterization Test Results for LM4050QML 2.5V Precision Reference," *2010 IEEE Radiation Effects Data Workshop*, July 20-23, 2010, pp. 164-169.

- 28 N. J.-H. Roche, S. P. Buchner, L. Dusseau, K. Kruckmeyer, J. Boch et al., "Correlation of Dynamic Parameter Modification and ASET Sensitivity in a Shunt Voltage Reference," *IEEE Trans. Nucl. Sci.* 59(6), Dec. 2012, pp. 2756-2763.
- 29 Y. Boulghassoul, L. W. Massengill, A. L. Sternberg, R. L. Pease, S. Buchner et al., "Circuit Modeling of the LM124 Operational Amplifier for Analog Single-Event Transient Analysis," *IEEE Trans. Nucl. Sci.* 49(6), Dec. 2002, pp. 3090-2096.
- 30 S. Buchner and D. McMorro, "Single Event Transients in Linear Integrated Circuits," *2005 IEEE Nuclear and Space Radiation Effects Conference Short Course*, June 11, 2005.
- 31 S. Buchner and C. Poivey, "Single Event Transient Test Report LMH6702 Operational Amplifier," NASA Goddard Space Flight Center, Oct. 20, 2006, [https://radhome.gsfc.nasa.gov/radhome/papers/L061806\\_LMH6702.pdf](https://radhome.gsfc.nasa.gov/radhome/papers/L061806_LMH6702.pdf).
- 32 E. P. Wilcox, S. D. Phillips, P. Cheng, T. Thrivikraman, A. Madan et al., "Single Event Transient Hardness of a New Complementary (npn + pnp) SiGe HBT Technology on Thick-Film SOI," *IEEE Trans. Nucl. Sci.* 57(6), Dec. 2010, pp. 3293-3297.
- 33 S. Buchner, D. McMorro, N. Roche, L. Dusseau and R. L. Pease, "The Effects of Low Dose-Rate Ionizing Radiation on the Shapes of Transients in the LM124 Operational Amplifier," *IEEE Trans. Nucl. Sci.* 55(6), Dec. 2008, pp. 3314-3320.
- 34 S. Buchner, M. Sibley, P. Eaton, D. Mavis and D. McMorro, "Total Dose Effect on the Propagation of Single Event Transients in a CMOS Inverter String," *2009 European Conference on Radiation and Its Effects on Components and Systems*, pp. 79-82.
- 35 M. Shop, J. Gorelick, R. Rau, R. Kop and A. Martinez, "Observation of Single Event Latchup in Bipolar Devices," *1993 IEEE Radiation Effects Data Workshop*, pp. 118-120.
- 36 M. V. O'Bryan, K. A. LaBel, J. W. Howard, C. Poivey, R. L. Ladbury et al., "Single Event Effects Results for Candidate Spacecraft Electronics for NASA," *2003 IEEE Radiation Effects Data Workshop*, pp. 65-76.
- 37 R. Katz, "Heavy Ion Test Summary for the National LVDS Line Drivers and Receivers," NASA Goddard Space Flight Center, April 23, 1997, <https://radhome.gsfc.nasa.gov/radhome/papers/b022497a.pdf>.
- 38 K. Kruckmeyer, T. Santiago and R. Eddy, "SEE Test Results of National Semiconductor's LVDS Driver and Receiver Pair DS90C031 and DS90C032," *11th European Conference on Radiation and Its Effects on Components and Systems*, Sept. 20-24, 2010.
- 39 D. McMorro, S. Buchner, M. Baze, B. Bartholet, R. Katz et al., "Laser-Induced Latchup Screening and Mitigation in CMOS Devices," *IEEE Trans. Nucl. Sci.* 53(4), Aug. 2006, pp. 1819-1824.
- 40 R. K. Lawrence and A. T. Kelly, "Single Event Effect Induced Multiple-Cell Upsets in a Commercial 90 nm CMOS Digital Technology," *IEEE Trans. Nucl. Sci.* 55(6), Dec. 2008, pp. 3367-3374.
- 41 T. R. Oldham, M. Suhail, M. R. Friendlich, M. A. Carls, R.L. Ladbury et al., "TID and SEE Response of Advanced 4G NAND Flash Memories," *2008 IEEE Radiation Effects Data Workshop*, pp. 31-37.
- 42 Test Procedure for the Management of Single-Event Effects in Semiconductor Devices from Heavy Ion Irradiation, JESD57, Nov. 2017.
- 43 ASTM F1192-00, "Standard Guide for the Measurement of Single Event Phenomena (SEP) Induced by Heavy Ion Irradiation of Semiconductor Devices," ASTM International, July 2006.
- 44 R. D. Skinner, "Basic Integrated Circuit Technology Reference Manual," Integrated Circuit Engineering Corp., 1993.
- 45 J.L. Titus, C.F. Wheatley, D.I. Burton, I. Mouret, M. Allenspach, J. Brews, R. Schrimpf, K. Galloway, and R.L. Pease, "Impact of oxide thickness on segr failure in vertical power mosfets; development of a semi-empirical expression", *IEEE Trans. Nucl. Sci.*, Vol. 42 No. 6, pp. 1928-1934, Dec. 1995
- 46 J. George, R. Koga, S. Crain, P. Yu, S. Nguyen, E. Normandy, D. Kachuche, and B.K. Steffan, "Single event transients in operational amplifiers", *2005 IEEE Radiation Effects Data Workshop*, pp. 8-12
- 47 Texas Instruments, Dallas TX, "TPS50601-SP Single-Event Effects Summary", Dec. 2017 [Online], Available: <http://www.ti.com/lit/slak017>.

# Chapter 6: Mitigating radiation effects in electronics

In industrial and medical applications, the primary way to mitigate or eliminate the radiation effects of microelectronics operating in radiation environments is to use appropriate levels of shielding.

Unfortunately, in many space and terrestrial applications, shielding the natural high-energy particle fluxes is not an option, because the amount of shielding required adds too much mass/size to the equipment. Thus, it is necessary to find a way to lower the intrinsic sensitivity of the microelectronics to radiation in order to ensure reliable performance in harsh environments.

This chapter covers the effects of technology scaling, demonstrating how some technologies are more robust than others based simply on their physical properties. There are various deliberate process optimizations and modifications to baseline process technologies that greatly improve robustness against radiation effects. A host of circuit layout, design and architectural optimizations used alone or in concert can make microelectronics even more robust.

The process of making a technology more robust through any method is called radiation hardening, which covers a wide variety of techniques. With few exceptions, it does not imply total immunity to radiation but rather an abatement of radiation effects such that the product will have sufficiently high reliability to fulfill its mission. Thus the concept of radiation hardening implies robustness but not immunity, unless specified as such.

Two fundamental methods harden microelectronics against radiation effects, used individually or in combination. The first method focuses on modifying the baseline semiconductor process to reduce various physical processes that affect radiation sensitivity. This method of mitigation is called radiation hardening by process (RHBP). RHBP alone will seldom result in a complete elimination of radiation effects, but can reduce them such that a component that is failing a radiation metric because of an effect in the baseline process will pass the metric with the modified process.

RHBP solutions often have an advantage in that they can make an existing product radiation-hardened (or at least tolerant) without modifying the design, thereby reducing cost and development time. Many RHBP solutions use existing mask sets (in some cases a single mask may be added or several minor modifications made) to enable better radiation performance. Because the masks are relatively unchanged, RHBP solutions generally do not affect the die area.

The second method includes design solutions ranging from layout-based changes to circuit-design alterations to redundant design at higher levels. This method of design mitigation is called radiation hardening by design (RHBD). Unlike RHBP solutions, RHBD can result in the complete elimination of specific radiation-effect sensitivities. The drawback, obviously, is that only new from-the-ground-up designs can benefit from RHBD methods. RHBD methods will add to layout area and increase design complexity.

Thus, devices designed to be robust in harsh environments are far costlier to manufacture and qualify, and require expensive radiation characterization to validate their reliability in radiation environments.

### 6.1 Radiation robustness by serendipity

A microelectronics product will only be as radiation-tolerant as the weakest component on the chip, so some of the scaling trends described in this chapter should be considered general trends only. The radiation performance of a specific product will depend on the specific properties of the process technology used to fabricate it, as well as the types and sensitivities of the integrated components used in that device.

Successive decreases in feature size along with technology scaling have resulted in higher functionality and packing densities – at the price of higher power consumption and reduced-node signal charge, the critical charge ( $Q_{crit}$ ). The impact of technology scaling on radiation effects was first observed as changes in the single-event upset (SEU) rate (or soft-error rate [SER]) of digital memories and sequential logic.

As technology scales down, each bit has a smaller area, thus actually decreasing the likelihood of a strike. On the negative side, the node capacitance and stored  $Q_{crit}$  also decrease, making circuits potentially more sensitive to smaller collected charge ( $Q_{col}$ ). Additionally, scaling from higher operating voltages to lower voltages also reduces  $Q_{crit}$ , increasing sensitivity.

The effect of voltage scaling was dominant in the 1980s and 1990s as the drain voltage ( $V_{DD}$ ) dropped from 12 V to 7.5 V, then to 5.0 V, then to 3.3 V. During this era,  $Q_{crit}$  dropped significantly at each successive technology node, and the SEU rate increased at each successive node.

In the late 1990s, as technologies approached the 180-nm node,  $V_{DD}$  scaled to ~1 V; further voltage scaling after that period was much more limited. With the saturation in  $V_{DD}$  scaling, the shrinking node capacitance had less of an impact on reducing  $Q_{crit}$ , while the shrinking junction sizes guaranteed that  $Q_{col}$  was much smaller.

From this point on, both dynamic random-access memory (DRAM) and static random-access memory (SRAM) scaling led to reduced-bit SEU rates with each successive node, with the decrease in bit SEU tracking the reduction in the collection area. Unfortunately, the whole point of technology scaling is to do more with the same area of silicon; thus the number of bits integrated continues to rise – almost canceling the bit SEU scaling trend.

To create the incredibly high functionality provided by today's consumer electronic systems and appliances, it is necessary to integrate together several distinct components known as systems-on-chip (SoC). At the core of each system is one or more processor cores with a large embedded memory (usually SRAM) interconnected with a slew of peripheral interface logic.

In larger systems, additional storage (usually DRAM and/or flash) is added to extend storage SoC capabilities. These systems have a lot of analog processing power with various input/output components (pulse-width modulators, digital-to-analog converters, analog-to-digital converters) that enable the systems to respond and interact with the outside world.

The radiation response of these components varies, based on the physical properties of the devices and as technologies scale to smaller and smaller feature sizes. Technology scaling has enabled some fairly significant improvements in radiation robustness serendipitously; in other words, the technology was optimized for power, speed, density, and other electrical or functional performance reasons not related to improving the radiation tolerance of the microcircuits.

The DRAM-bit SEU was high when manufacturers used planar capacitor cells that stored the signal charge in two-dimensional, large-area junctions, because these were very efficient at collecting radiation-induced charges.

Planar capacitor cells, with their large area junctions characterized by deep depletion regions, collect a large portion of the charge that radiation events generate. Ultimately, to address both pause/refresh challenges (DRAMs are dynamic, so the signal charge on each bit needs refreshing every so often) and to greatly decrease SEU sensitivity, the DRAM industry moved to 3D storage capacitors. The 3D storage-node design significantly increased the stored signal charge or  $Q_{crit}$  by increasing the capacitance, either by digging a deep trench in the substrate or making a plated stacking arrangement above the substrate, to increase the total capacitor area without impacting the density (building down or up instead of laterally).

While the capacitor scaled up, the area of the junctions forming the source-drain of the transfer gate was minimized, greatly reducing junction-collection efficiency. With 3D capacitor designs, collection efficiency decreases with decreasing junction volume. The cell capacitance remains relatively constant with scaling, because the value of the external capacitor cell primarily defines it.

Concurrent with DRAM scaling, the operating voltages also scaled down, but the rate of voltage scaling saturated at  $\sim 1$  V. So while the reduction in operating voltage initially reduced  $Q_{crit}$  at each successive node, its saturation – along with concurrent aggressive junction-volume scaling and a fairly constant storage capacitance enabled by the 3D cell capacitor structure – led to a significant reduction in  $Q_{coll}$  and bit SEU rate. **Figure 6-1** shows the net result to DRAM bit SEU performance, with the bit SEU of a DRAM shrinking about 5x per generation.

Most of this improvement pertains to the reduction of  $Q_{coll}$  due to the scaling down of the junction area, with voltage scaling saturated. While DRAM-bit SER has reduced more than 1,000x over five generations, the DRAM-system SEU has reduced marginally because system requirements and integration levels have increased nearly as fast ( $\sim 2$ x to 4x with each successive technology node).

In contrast, early SRAM was more robust against SEUs because of high operating voltages, and because data in an SRAM is stored in a bistable circuit made up of two cross-coupled inverters, each strongly driving the other to keep the SRAM bit in its programmed state.

![Figure 6-1: A log-linear plot showing the SEU cross-section (cm²/bit) versus the Year of DRAM marking (1985 to 2005). The y-axis is logarithmic, ranging from 1E-17 to 1E-12. The x-axis is linear, ranging from 1985 to 2005. Data points are plotted for various technology nodes: 4M, 16M, 64M, and 256M. The legend indicates: Original data (4M-16M) Kerners/Taber (blue diamonds), More recent data (64M-256M) (red circles), Ziegler et al., SC design DRAMs (16, 64) (open squares), Ziegler et al., TIC design DRAMs (16, 64) (open triangles), Fit to all original data (red line), and Fit to Baumann DRAM scaling trends (blue line). The plot shows a clear downward trend, indicating that the SEU cross-section decreases as technology nodes advance.](a4750558c0b4bdc9990f683302b5a7cf_img.jpg)

Figure 6-1: A log-linear plot showing the SEU cross-section (cm²/bit) versus the Year of DRAM marking (1985 to 2005). The y-axis is logarithmic, ranging from 1E-17 to 1E-12. The x-axis is linear, ranging from 1985 to 2005. Data points are plotted for various technology nodes: 4M, 16M, 64M, and 256M. The legend indicates: Original data (4M-16M) Kerners/Taber (blue diamonds), More recent data (64M-256M) (red circles), Ziegler et al., SC design DRAMs (16, 64) (open squares), Ziegler et al., TIC design DRAMs (16, 64) (open triangles), Fit to all original data (red line), and Fit to Baumann DRAM scaling trends (blue line). The plot shows a clear downward trend, indicating that the SEU cross-section decreases as technology nodes advance.

**Figure 6-1. DRAM technology scaling trend per bit for SEUs vs. technology node. Because each successive technology node typically uses larger bit densities, the reduction in overall failure rate from an SEU is not as good as this curve implies.<sup>[1]</sup>**

Additionally, because the SRAM has no storage capacitor, small junction collection is the only contributor of  $Q_{coll}$  from radiation events. The charge on the node capacitance largely defines the  $Q_{crit}$  for the SRAM cell (as with DRAM), but with a second term related to the drive capability of the transistor keeping the node voltage. The stronger the transistor, the higher the value of  $Q_{coll}$  that the transistor can tolerate before an SEU occurs.

This dynamic term also includes a temporal element related to the switching speed of the cell – the slower the switching speed, the longer the feedback transistors have to provide charge compensation. With technology scaling, deliberately minimizing the SRAM junction area reduces capacitance, leakage and cell area and increases the switching speed, while the SRAM operating voltage has been concurrently and aggressively scaled down to minimize power.

With each successive SRAM generation, big reductions in operating voltage and reductions in node capacitance canceled out the reductions in cell-collection efficiency due to shrinking cell-depletion volume. SRAM single-bit SEUs initially increased with each successive generation.

As illustrated in **Figure 6-2**, when SRAM feature sizes were reduced into the deep submicron regime bit, SEU peaked at 180 nm/130 nm and then decreased with each successive generation (like DRAM). This reduction from node to node is primarily due to saturation in voltage scaling, reductions in junction-collection efficiency and increased charge sharing due to short-channel effects with neighboring nodes.

Ultimately, because scaling also implies increased memory density, the saturation in SRAM-bit SEUs does not translate into a similar reduction in SRAM-system SEUs. The exponential growth in the amount of SRAM in microprocessors and digital signal processors has led to failures from SEUs staying the same or increasing with each generation.

This trend is of great concern to chip manufacturers because SRAM constitutes a large part of all advanced integrated circuits today. Ultimately, fault-tolerant system design using error detection and correction circuits can greatly reduce the failure rate in both SRAMs and DRAMs.

![Figure 6-2: A line graph showing SEU (independently normalized) vs. Technology node (nm). The y-axis is logarithmic, ranging from 0.01 to 1. The x-axis ranges from 250 nm to 22 nm. Five data series are plotted: IBM SCI 2013 (black circles), Intel 2013 (grey circles), Intel 2012 (red squares), TI 2012 (blue diamonds), and Sanda 2010 (green triangles). The curves show a peak in SEU around 180 nm/130 nm, followed by a sharp decline. A label 'Planar' is near the 28 nm node, and 'FINFET' is near the 22 nm node. A legend note states: 'Magnitudes from two different curves cannot be compared, as these curves were individually normalized!'](d7ce27646f87a7bec81474bed33145ef_img.jpg)

Figure 6-2: A line graph showing SEU (independently normalized) vs. Technology node (nm). The y-axis is logarithmic, ranging from 0.01 to 1. The x-axis ranges from 250 nm to 22 nm. Five data series are plotted: IBM SCI 2013 (black circles), Intel 2013 (grey circles), Intel 2012 (red squares), TI 2012 (blue diamonds), and Sanda 2010 (green triangles). The curves show a peak in SEU around 180 nm/130 nm, followed by a sharp decline. A label 'Planar' is near the 28 nm node, and 'FINFET' is near the 22 nm node. A legend note states: 'Magnitudes from two different curves cannot be compared, as these curves were individually normalized!'

**Figure 6-2. An SRAM-bit SEU vs. technology node.** The peak in the bit SEU occurs at 180 nm/130 nm; beyond these, voltage scaling saturates at ~1 V. Since bit densities increase with each successive node, the system failure-rate improvement is not as good as this per-bit SEU curve implies.

Feature sizes have reduced with technology scaling in order to increase well and channel doping to combat leakage effects. Additionally, transistor isolation moved away from grown field oxides (local oxidation of silicon [LOCOS]) to shallow trench isolation (STI), where a trench is etched between transistors and then filled by deposited films.

### 6.2 Radiation hardening by process

To some extent, process technology modifications alone can address the radiation sensitivity of some devices. The fundamental problem with RHBP modifications is that the optimized baseline process highly constrains the types of modifications allowed.

One of the simplest global process modifications in bulk silicon technology is to replace the baseline substrates with substrates of much higher conductivity. With this modification, the product masks are unchanged; only the substrate starting material changes. Using a highly doped substrate greatly reduces the substrate resistance and effectively reduces single-event latch-up (SEL) sensitivity. The onset linear energy transfer (LET) for SEL increases while the saturation cross-section is reduced, as shown in [Figure 6-3](#). The drop in substrate resistance means that carrier lifetime is reduced, reducing the available charge (see Chapter 5 for details).

![Figure 6-3 (top): A graph showing Device cross-section (cm²) vs. LET (MeV-cm²/mg) on a log-log scale. The y-axis ranges from 10⁻⁸ to 10⁻². The x-axis ranges from 0 to 80. Three data series are shown for different epi layer thicknesses: 12-μm epi layer (red circles), 10-μm epi layer (blue squares), and 8-μm epi layer (green triangles). All curves show an increase in cross-section with LET, with thinner epi layers resulting in lower cross-sections.](8cf12562763d72a28bb42fd6ff4905ac_img.jpg)

Figure 6-3 (top): A graph showing Device cross-section (cm²) vs. LET (MeV-cm²/mg) on a log-log scale. The y-axis ranges from 10⁻⁸ to 10⁻². The x-axis ranges from 0 to 80. Three data series are shown for different epi layer thicknesses: 12-μm epi layer (red circles), 10-μm epi layer (blue squares), and 8-μm epi layer (green triangles). All curves show an increase in cross-section with LET, with thinner epi layers resulting in lower cross-sections.

![Figure 6-3 (bottom): A cross-sectional diagram of a CMOS device. It shows an N+ well, P+ anode, N+ cathode, and P+ substrate. The diagram labels the N-well, P-epi, and P-sub layers. It also shows the parasitic bipolar junction transistors (BJTs) and the substrate resistor of NPN impacted by up-diffusion of boron from the highly doped substrate layer (bottom). Dimensions L_N+, L_Anode-cathode, and L_P+ are indicated.](dfe74512a9c9fb620f72c9dbc22874aa_img.jpg)

Figure 6-3 (bottom): A cross-sectional diagram of a CMOS device. It shows an N+ well, P+ anode, N+ cathode, and P+ substrate. The diagram labels the N-well, P-epi, and P-sub layers. It also shows the parasitic bipolar junction transistors (BJTs) and the substrate resistor of NPN impacted by up-diffusion of boron from the highly doped substrate layer (bottom). Dimensions L\_N+, L\_Anode-cathode, and L\_P+ are indicated.

**Figure 6-3. Impact of epitaxial thickness on the SEL cross-section of a CMOS process.** A highly doped substrate is required to afford a reduction in the substrate resistance (top); diagram showing parasitic bipolar junction transistors (BJTs) and substrate resistor of NPN impacted by up-diffusion of boron from the highly doped substrate layer (bottom).

For a highly doped substrate to work with an existing baseline process (whose baseline substrate doping is two to three orders of magnitude lower), it is necessary to grow an epitaxial (epi) layer of baseline doping levels over the highly doped substrates so that the circuits and wells function as close to the baseline parameters as possible. (See Chapter 5 for an explanation of epi.) As shown in [Figure 6-3](#), thinning the P-epi layer brings the highly doped substrate closer to the active devices. During thermal processing, boron out-diffuses from the substrate and further reduces the substrate resistance.

There are limits to this technique, because if the epi layer is too thin, the up-diffusing boron will counter-dope the N-wells and affect NMOS threshold voltages. The optimal epi thickness is usually determined with a split lot of various layer thicknesses – and the thickness at the onset of yield loss gives the lowest possible substrate resistance, while ensuring that the devices meet their expected electrical parameters.

This technique can be effective with relatively flat technologies (without deep implants or buried wells) such as standard digital CMOS designs, but it is not usually possible to effectively implement it on BiCMOS processes because the required epi thickness will have to be so large that the reduction of substrate resistance will be minimal.

Growing an epi layer can reduce the probability of SEL, but does not usually eliminate it completely; there are limits to the possible improvement. Also, although many modern CMOS processes are manufactured with an epi layer, usually the doping of the substrate and the epitaxy are the same, so no SEL improvement would be observed – in other words, a CMOS process stating that it is on epitaxy does not imply SEL robustness.

Although not a direct process modification per se, the use of neutron washes (the exposure of unbiased devices to a high fluence of neutrons) on a baseline process can also achieve similar effects where the neutron-induced displacement damage degrades carrier lifetimes and effectively reduces the gain of parasitic feedback that can lead to SEL. This method can work well for majority carrier devices such as MOSFETs, whose performance is relatively insensitive to displacement damage. A similar technique is to implant oxygen or other species just below the active depth of the device.

Another method of global process modifications to improve radiation robustness involves changing the composition, purity or type of existing layers to minimize a radiation effect. There are two primary examples of such modifications:

- The removal of an isotope of boron ( $^{10}\text{B}$ ) containing compounds/layers to reduce SEUs from thermal neutrons as well as  $^{10}\text{B}$ .
- The removal or minimization of alpha-emitting impurities in the process and packaging materials to reduce alpha-induced SEU rates.

An obvious way to eliminate single-event effects (SEEs) is to get rid of the radiation sources that cause them. To mitigate the SEU threat posed by the radiation produced by the inelastic neutron reaction of  $^{10}\text{B}$ , virtually all advanced technologies have deliberately removed concentrated sources of  $^{10}\text{B}$  (including boron-doped glasses and some tungsten plug-forming processes). The reduction or removal of  $^{10}\text{B}$  has led to a five- to tenfold reduction in observed SEU failure rates in SRAM.<sup>[8-9]</sup>

To reduce alpha-particle emissions, semiconductor manufacturers use extremely high-purity materials and processes, and production-screen all materials with low background alpha-emission measurements.

In the basic standard CMOS implementation, the PMOS transistors are placed in dedicated N-wells, while the NMOS transistors are in a P-well defined by the P-substrate. The disadvantage of this approach is that the NMOS channel is coupled directly to the substrate such that selective back-biasing is not an option. Charge collection is maximized for N+/P sub-ion strikes because the large volume of the substrate acts as a collection volume, increasing the magnitude, duration and probability of an SEU or SEL.

In many applications, the advantages of enclosing the NMOS in its own dedicated well leads to the dual-well CMOS configuration shown in [Figure 6-4](#) (left). A triple well is frequently implemented as a blanket deep N-well layer biased either by the primary N-wells or specific N+ sinks in a P-substrate. There is little or no area penalty of using double or triple wells, although both require extra process steps to create the dedicated P-well and deep N-well.

In general, triple-well structures offer advantages over double wells. Triple wells are widely used in memory and processor technologies specifically to improve isolation of transistors from the substrate; to reduce coupling of on-chip noise sources; and (if needed), to alter the transistor threshold voltages by back-biasing as a way to minimize power in some circuits.

The formation of a uniform well or tank in a semiconductor device has an impact on the amount of charge collected during an ion strike and on the dynamics of the charge distribution and charge sharing. The presence of a deep N-well significantly reduces the parasitic PNP base resistance and gain, while concurrently increasing the NPN base resistance and gain. Thus, the use of a triple well potentially improves or degrades latch-up/SEL robustness, depending on the process architecture.

Although triple-well structures can be more susceptible than dual-well structures to electrically induced latch-up under specific conditions, triple wells can be more robust against SEL than dual-well structures.<sup>[6]</sup> The deep N-well of the triple well truncates charge collection from ion strikes, reducing the charge collected by the P-well and reducing the charge available to turn on the parasitic NPN. Concurrently, the deep N-well removes charge more effectively than simple substrate collection, thus also reducing activation of the parasitic PNP. Whether this will have an impact on SEE robustness will depend on many factors such as junction profiles, well depths and operating voltages.

![Figure 6-4: Dual-well bulk CMOS cross-section (left) and triple-well bulk CMOS cross-section (right).](e799ee1695b238a93e6742045f01463a_img.jpg)

The figure consists of two cross-sectional diagrams of CMOS transistors. The left diagram, titled 'Dual-well bulk CMOS', shows a PMOS transistor in an N-well and an NMOS transistor in a P-well on a P-substrate. An ion strike is shown hitting the P-well. The right diagram, titled 'Triple-well bulk CMOS', shows a similar structure but with an additional 'Deep N-well' layer below the P-well. An ion strike is shown hitting the P-well, with arrows indicating that the deep N-well reduces charge collection from the P-well and the substrate.

Figure 6-4: Dual-well bulk CMOS cross-section (left) and triple-well bulk CMOS cross-section (right).

**Figure 6-4. Dual-well bulk CMOS cross-section (left) and triple-well bulk CMOS cross-section (right). Wells reduce charge collection by the substrate and the deep N-well reduced collection in the P-well, thereby reducing SEU and SEL effects.**

Another and more robust way to better isolate structures is to use substrates incorporating a very thin silicon layer on a thicker layer of oxide on a silicon or sapphire substrate (silicon on insulator [SOI] and silicon on sapphire [SOS]). This oxide, known as buried oxide (BOX), blocks charge collection from the substrate. If the device layer on the BOX is thin enough, the STI will reach down to the BOX and dielectrically isolate the PMOS and NMOS transistors from each other, thereby shutting off any parasitic path. **Figure 6-5** is a cross-section of a standard bulk design (left) and a cross-section of an SOI design (right), with a very thin device layer for comparison.

In the SOI/SOS structure, the thick oxide layer dielectrically separates the active device silicon from the substrate, limiting the active silicon volume. During an ion strike, much less charge is collected because the presence of the BOX truncates the charge distribution.

The SEU of devices made in SOI/SOS technologies is about 5-10x better than bulk, depending on whether the device is partially or fully depleted.<sup>[7-9]</sup> The SEU improvements, while reasonably good, would be drastically better if not for floating-body and parasitic bipolar effects that amplify the effect of the charge collected in the case of SOI/SOS structures.

An additional benefit of SOI/SOS structures with thin device layers is that the STI isolates the N and P wells in the CMOS, thereby precluding parasitic PNP paths, so SEL is not possible. This is only true in cases where the active layer is thin enough that the STI reaches down to the BOX. In many SOI processes, especially those used for BiCMOS, the device layer is thicker and the STI does not reach all the way down to the BOX. In this case, the wells will not be fully oxide isolated, the PNPP paths still exist and SEL may be possible.

### 6.3 Radiation hardness by design – component configuration solutions

RHBD by layout modifications is one of the primary tools a designer has to make components more robust by taking advantage of physical and spatial properties of radiation effects.

One of the easiest layout methods to increase a component's resistance to radiation-induced charge transients is to increase transistor widths. The increased transistor sizing means that there will be more current available to compensate for any spurious collected charge from a radiation event. With higher drive strength on the node (a larger transistor width, or W), the magnitude of the transient will be lessened and its duration shortened. **Figure 6-6** shows a simulation of a single-event transient (SET) on normal and 3x wider devices.

Increasing transistor widths works well, although increasing transistor junction sizes also potentially increases the Qcoll from a radiation event because the larger junction is able to better collect the spurious charge. Making the transistor wider will also increase the probability of an ion strike in proportion to the increase in overall junction area.

Although useful to reduce SEE sensitivity, the transistor sizing approach will not eliminate larger radiation-induced transients. Given the speed with which the particle strike creates excess charge, and given practical sizing limits, transistor sizing will just reduce transient magnitude and duration.

However, because low LET-radiation events are far more frequent than larger events, this technique can result in a circuit that, while not immune to SEEs, is certainly several times more robust than the baseline circuit. Mitigating the most likely fail point results in sizing solutions that are ~1.6x for the entire circuit area when fully sizing all gates in the circuit, leading to a >3x area penalty.<sup>[10]</sup>

![Figure 6-5: Cross-sections of conventional bulk CMOS and SOI CMOS during an ion strike.](fd8fdbdbfb968acf2444c93ab442a62e_img.jpg)

The figure consists of two cross-sectional diagrams comparing a conventional bulk CMOS structure (left) and an SOI CMOS structure (right) during an ion strike.

- Left: Dual-well bulk CMOS**
  - The structure shows a P-substrate with N-wells and P-wells. A gate stack with STI (Shallow Trench Isolation) is on top.
  - An ion strike (indicated by a grey arrow) enters from the top, passing through the gate stack and into the P-substrate.
  - A large blue region labeled 'N-well' is shown, indicating significant charge collection in the bulk substrate.
- Right: Triple-well bulk CMOS**
  - The structure shows a P-substrate with a Buried oxide (BOX) layer. The device layer is on top of the BOX.
  - An ion strike (indicated by a grey arrow) enters from the top, passing through the gate stack and into the BOX.
  - The charge collection is truncated by the BOX, resulting in a much smaller blue region compared to the bulk CMOS.

Figure 6-5: Cross-sections of conventional bulk CMOS and SOI CMOS during an ion strike.

**Figure 6-5.** Cross-section of conventional bulk CMOS (left) and SOI CMOS (right) during an ion strike. Note the truncation of charge collection by the BOX of the SOI/SOS structure – for a given ion strike, the SOI will collect much less charge than the bulk device. A parasitic bipolar P-channel N-channel P-channel N-channel (PNPN) structure (shown in white on the bulk CMOS) cannot form in the type of SOI shown; thus, this SOI technology does not suffer from SEL.

![Figure 6-6: Two plots showing the SET response of an inverter. The top plot shows the output of a nominal inverter (output-1x) with a sharp negative spike during a transient. The bottom plot shows the output of an inverter with 3x transistor widths (output-3x), which shows a much smaller negative spike. Both plots have a y-axis labeled 'Output (volts)' ranging from -1 to 3.5 and an x-axis labeled 'Time (ns)' ranging from 0 to 5. A dashed horizontal line at 0.5 VDD is shown in both plots.](e79b237b31616233842b1c75f51edeae_img.jpg)

Figure 6-6: Two plots showing the SET response of an inverter. The top plot shows the output of a nominal inverter (output-1x) with a sharp negative spike during a transient. The bottom plot shows the output of an inverter with 3x transistor widths (output-3x), which shows a much smaller negative spike. Both plots have a y-axis labeled 'Output (volts)' ranging from -1 to 3.5 and an x-axis labeled 'Time (ns)' ranging from 0 to 5. A dashed horizontal line at 0.5 VDD is shown in both plots.

Figure 6-6. SET response of nominal inverter (top) and one that has been drawn with 3x transistor widths (bottom).<sup>[19]</sup>

Transistor sizing approaches are suitable for analog and combinatorial logic designs (where a reduction in the rate of SETs is desired) and in sequential and memory designs (where improved SEU robustness is desired). It has also been used in six-transistor SRAM designs where upsizing the PMOS while downsizing the NMOS yields improvements of 2x on SRAM SEUs.<sup>[11]</sup>

2D barriers formed through specific layouts of active layers in wells placed around or between sensitive components can reduce interactions between devices by electrically isolating and physically separating them. RHBD mitigation using 2D guard rings and additional well contacts reduces charge-sharing effects and total dose leakage effects, and can mitigate SEL. The guard rings and additional contacts will not eliminate SETs during ion strikes but can reduce their magnitude and duration, thereby increasing the effective LET upset threshold.

PMOS transistors in weakly biased wells can collect a large amount of charge, not from direct collection but from the transient triggering of the parasitic PNP BJT by the perturbation of the N-well voltage, which temporarily forward-biases the parasitic base-emitter junction.<sup>[20]</sup> Additional well contacts or a biased 2D guard ring around each transistor in the well will greatly reduce well de-biasing during an ion strike, reducing the probability that the parasitic PNP structure will turn on.

Using properly designed guard rings (with a high density of taps/contacts) is effective at keeping the N-well potentials pinned to the appropriate potentials, thereby precluding the initiation of SEL.<sup>[12]</sup>

In some cases, particularly for higher LET events, well de-biasing will occur, but the guard ring allows much quicker restoration of the well potential, reducing the total charge collected by the event.

In addition to protecting PMOS transistors from bipolar effects and excessive charge collection, the use of N-well isolation regions between sensitive nodes appears to be one of the best ways to reduce charge-sharing effects across multiple nodes.<sup>[13]</sup> In NMOS devices, the guard rings do not work in the same way. Some degree of isolation is possible by placing the guard ring in the P-well/P-substrate, but the impact is significantly less pronounced than that of PMOS guard rings.

For NMOS in P-wells or P-substrates, full 3D N-well junction isolation (a deep N-well under the NMOS P-well/P-substrate devices contacted with deep N+ contacts – basically a localized triple well) provides performance similar to PMOS guard contact isolation.<sup>[14]</sup>

Using guard rings is an effective RHBD technique for reducing the magnitude and duration of SETs induced by ion strikes. 2D guard rings are easily implemented as a layout modification and are effective in protecting PMOS in N-wells. To protect NMOS in P-wells, 3D junction isolation enables improvements similar to the PMOS case. Adding guard rings increases the distance between circuit nodes (which is also good for reducing charge sharing) and thus incurs a circuit layout penalty in the order of 1.3x to 1.8x the area of standard cells.

Figure 6-7 compares an inverter layout without a guard ring and an inverter with guard rings (1.28x area penalty).

![Figure 6-7: Two layout diagrams comparing a conventional inverter layout (left) and an inverter with guard rings (right). The left diagram shows a standard inverter with a P-well, N-well, and active region. The right diagram shows the same inverter but with additional guard rings and contacts around the active region. A legend on the right identifies the layers: P-well (light blue), N-well (dark blue), Active (red), P-plus (light blue), N-plus (dark blue), Poly (light blue), and Cont (black).](01c9d9eb1a95d05fa6d8890e9a00eada_img.jpg)

Figure 6-7: Two layout diagrams comparing a conventional inverter layout (left) and an inverter with guard rings (right). The left diagram shows a standard inverter with a P-well, N-well, and active region. The right diagram shows the same inverter but with additional guard rings and contacts around the active region. A legend on the right identifies the layers: P-well (light blue), N-well (dark blue), Active (red), P-plus (light blue), N-plus (dark blue), Poly (light blue), and Cont (black).

Figure 6-7. Conventional inverter layout (left) and inverter with guard rings (right). The area penalty is ~1.28x.<sup>[15]</sup>

As MOSFET technologies aggressively scale, their tolerance to TID-induced threshold voltage shifts. Subthreshold slopes and transconductance degradation have improved to the point where individual transistors can generally function beyond Mrad absorbed dose levels of TID.<sup>[16]</sup>

Unfortunately, STI is still the major point of excessive post-irradiation leakage in deep submicron technologies. This off-state leakage along the isolation edge is due to the positive-hole charge accumulated at the isolation oxide edges, where it inverts the P-type silicon to form a parasitic N-channel. A well-known layout

modification called an enclosed or annular layout, shown in **Figure 6-8** (below), can effectively remove this failure mode from MOSFETs, rendering them TID-hardened.

![Figure 6-8: Regular NMOS layout (left) with edge leakage shown in red. Enclosed or annular gate layout eliminates edge (right) leakage issues by eliminating the edge.](d38282441e4548aa72ba677520ad9d77_img.jpg)

The image shows two cross-sectional diagrams of NMOS transistors. The left diagram shows a standard layout with a central channel and surrounding gate regions. Red lines indicate leakage paths along the edges of the gate. The right diagram shows an enclosed or annular gate layout, where the gate is a continuous ring around the channel, eliminating the edges and thus the leakage paths indicated by red lines.

Figure 6-8: Regular NMOS layout (left) with edge leakage shown in red. Enclosed or annular gate layout eliminates edge (right) leakage issues by eliminating the edge.

**Figure 6-8.** Regular NMOS layout (left) with edge leakage shown in red. Enclosed or annular gate layout eliminates edge (right) leakage issues by eliminating the edge.

Using an enclosed gate or annular gate layout effectively eliminates the isolation edge where TID-induced leakage failures occur (no isolation edge means no isolation-edge leakage). Because the isolation-edge leakage is removed, a normal transistor I-V with a low off-state leakage is possible, even at fairly high TID levels.

**Figure 6-9** shows the results of two transistor layouts in the same 180-nm BiCMOS process. The curve on the top corresponds to a standard layout, showing that transistor characteristics severely degrade and off-state leakage becomes problematic even at 25 krad(Si). The well-behaved I-V curves in the bottom plot of **Figure 6-9** correspond to an annular layout (in the same process), with no significant off-state leakage even at 300 krad(Si). The NMOS threshold voltage shift is still apparent in the annular layout.

Obviously, annular transistors use a lot more layout area and will have different characteristics and parasitics compared to a conventional layout. The shape of the enclosed transistors precludes aspect ratios below a certain value and imposes limits on minimum transistor sizing. To obtain higher transistor width/length values, it is sufficient to stretch the device in one dimension, without modifying the corners of the layout.

It is possible to apply RHBD principles to mitigating SEEs in power transistors. For reference, **Figure 6-10** shows a typical power MOSFET cross-section. Because the polysilicon gate in the neck region of the device is the area where single-event gate rupture (SEGR) operates to break down the gate oxide, reducing this area will reduce the occurrence of a SEGR. Reducing the area of the polysilicon gate electrode in the neck region is possible because only a fraction of the gate electrode over the channel is necessary to operate the MOSFET.

Removing the gate electrode area, as illustrated in **Figure 6-10**, over the neck region that is not over the channel has no impact on proper device operation, while areas where the polysilicon is removed will not be able to support a maximum electric-field buildup (from image charge formation); therefore, a significant SEGR cross-section reduction is likely.

![Figure 6-9 (top): I-V plot from a standard layout after different TID exposures. The plot shows Drain current (A) on a logarithmic scale from 10^-12 to 10^-4 versus Gate voltage (V) from 0 to 1.2. Three curves are shown: Pre-irradiation (red), 25 krad(Si) (green), and 50 krad(Si) (blue). The 25 krad(Si) curve shows a significant increase in off-state leakage compared to the pre-irradiation curve.](40a2aa853bedb72822c79bc143bfc69e_img.jpg)

This graph shows the drain current (A) on a logarithmic y-axis (from 10<sup>-12</sup> to 10<sup>-4</sup>) versus gate voltage (V) on a linear x-axis (from 0 to 1.2). Three curves are plotted: Pre-irradiation (red), 25 krad(Si) (green), and 50 krad(Si) (blue). The 25 krad(Si) curve shows a significant increase in off-state leakage compared to the pre-irradiation curve.

Figure 6-9 (top): I-V plot from a standard layout after different TID exposures. The plot shows Drain current (A) on a logarithmic scale from 10^-12 to 10^-4 versus Gate voltage (V) from 0 to 1.2. Three curves are shown: Pre-irradiation (red), 25 krad(Si) (green), and 50 krad(Si) (blue). The 25 krad(Si) curve shows a significant increase in off-state leakage compared to the pre-irradiation curve.

![Figure 6-9 (bottom): I-V plot from an annular layout in the same process after different TID exposures. The plot shows Drain current (A) on a logarithmic scale from 10^-12 to 10^-4 versus Gate voltage (V) from 0 to 1.2. Three curves are shown: Pre-irradiation (red), 25 krad(Si) (green), and 50 krad(Si) (blue). The curves for 25 krad(Si) and 50 krad(Si) are very close to the pre-irradiation curve, indicating no significant off-state leakage.](0859c0b136a6e9ce86426155c7bb46c1_img.jpg)

This graph shows the drain current (A) on a logarithmic y-axis (from 10<sup>-12</sup> to 10<sup>-4</sup>) versus gate voltage (V) on a linear x-axis (from 0 to 1.2). Three curves are plotted: Pre-irradiation (red), 25 krad(Si) (green), and 50 krad(Si) (blue). The curves for 25 krad(Si) and 50 krad(Si) are very close to the pre-irradiation curve, indicating no significant off-state leakage.

Figure 6-9 (bottom): I-V plot from an annular layout in the same process after different TID exposures. The plot shows Drain current (A) on a logarithmic scale from 10^-12 to 10^-4 versus Gate voltage (V) from 0 to 1.2. Three curves are shown: Pre-irradiation (red), 25 krad(Si) (green), and 50 krad(Si) (blue). The curves for 25 krad(Si) and 50 krad(Si) are very close to the pre-irradiation curve, indicating no significant off-state leakage.

**Figure 6-9.** I-V plot from a standard layout after different TID exposures. Large increases in off-state leakage are not observed until 25 krad (top). I-V plot from an annular layout in the same process after different TID exposures (bottom). There is no edge leakage and the threshold voltage shift increases with increasing dose.<sup>[17]</sup>

The onset LET at which SEGR occurs is defined largely by the oxide thickness, channel doping, operating voltages and morphological details, and will generally remain unchanged. Changing the masks associated with the gate electrode formation can greatly reduce the total oxide area where a maximum field can occur, and also significantly reduce the cross-section for SEGR.<sup>[18]</sup>

Similarly, RHBD can be used to reduce single-event burnout (SEB) by making structural and doping changes that decrease the maximum electric fields in the drain depletion region, reducing the amount of charge produced by avalanche multiplication and collecting a significant portion of the hole current away from the sensitive parasitic bipolar.<sup>[19]</sup>

By changing the P+ implant doping and coverage (layout) such that it extends below the N+ source contact, as shown in **Figure 6-10**, the magnitude of the hole flow provided by avalanche multiplication is greatly reduced. The P+ contact extension diverts the majority of the hole current into the P+ layer as opposed to allowing it to

enter the N+ source, reducing the amount of charge available to trigger and sustain the parasitic bipolar. Therefore, extending the P+ contact under the N+ source diffusion decreases SEB sensitivity – both the onset LET for SEB will increase and the cross-section will decrease. This type of modification will require changes to the layout and to the P+ and N+ doping levels.

![Figure 6-10: Cross-section diagrams of MOSFETs. The top diagram shows a standard power MOSFET with a polysilicon gate over the neck region. The bottom diagram shows a SEGR/SEB improved power transistor with a reduced polysilicon gate area in the neck region and an extended P+ source under the N+ source implant.](9165d5e7aa1eb5f163b2be33db3f9563_img.jpg)

The image contains two cross-sectional diagrams of MOSFETs. The top diagram, labeled 'Figure 6-10', shows a standard power MOSFET with layers including SiO<sub>2</sub>, Poly (polysilicon), N+ source, Aluminum, P+, pBody, Gate oxide over neck region, N-epilayer, and N+ substrate. The bottom diagram shows a SEGR/SEB improved power transistor, which is similar but features a reduced polysilicon gate area in the neck region and an extended P+ source under the N+ source implant.

Figure 6-10: Cross-section diagrams of MOSFETs. The top diagram shows a standard power MOSFET with a polysilicon gate over the neck region. The bottom diagram shows a SEGR/SEB improved power transistor with a reduced polysilicon gate area in the neck region and an extended P+ source under the N+ source implant.

**Figure 6-10.** Cross-section through a typical power MOSFET of a standard design (top). SEGR/SEB improved power transistor (bottom). Note the reduction in the polysilicon gate area in the neck region for improving SEGR and the extension of P+ source under the N+ source implant for improving SEB.

### 6.4 Radiation hardness by design – component layout solutions

Because device-level hardening typically requires fundamental modifications to the baseline manufacturing process, methods to improve SEE sensitivity at the circuit level are much more frequently employed to solve radiation-sensitivity issues. Design methods to make the component more robust generally rely on a combination of actions: increasing the drive and providing drive redundancy.

Attaching multiple drive transistors to maintain the data state of a specific node being hardened achieves drive redundancy. Because most chips have fewer latches than a high density SRAM, the design solutions can be more comprehensive because bit density is not as crucial. Typically, two transistors are assigned to drive every potential sensitive node.

A popular example of this approach has been used very successfully in the design of radiation-hardened latches and flip-flops. It is called a dual interlocked storage cell (DICE).<sup>[20]</sup> DICE cells rely on doubly redundant drive elements for each data-state node, employing 12 or more transistors versus the six for standard unhardened latches. **Figure 6-11** shows the schematic for a DICE latch.

![Figure 6-11: Schematic of a DICE latch. It shows a complex circuit with multiple transistors (P0, P1, P2, P3, N0, N1, N2, N3, N4, N5, N6, N7) and nodes (0, 1). Red circles highlight nodes 1 and 1, indicating dual feedback paths. The circuit is connected to CK (clock) and D (data) inputs.](20809e79dee38f3d6e03e1ad565a9cf5_img.jpg)

The diagram shows a schematic of a DICE latch. It consists of several PMOS (P0, P1, P2, P3) and NMOS (N0, N1, N2, N3, N4, N5, N6, N7) transistors. Nodes 0 and 1 are shown with red circles, indicating dual feedback paths. The circuit is connected to a clock input (CK) and a data input (D).

Figure 6-11: Schematic of a DICE latch. It shows a complex circuit with multiple transistors (P0, P1, P2, P3, N0, N1, N2, N3, N4, N5, N6, N7) and nodes (0, 1). Red circles highlight nodes 1 and 1, indicating dual feedback paths. The circuit is connected to CK (clock) and D (data) inputs.

**Figure 6-11.** Schematic of a DICE latch. A separate transistor drives each dual “1” node (red circles) independently. As long as ion strike-induced collected charge is limited to only one node, the other node can keep the data state valid through the strike event, greatly improving its performance through an SEU.

The fact that dual feedback paths source each sensitive node in the storage cell greatly improves SEUs. The assumption is that the two driving transistors are physically separated such that an ion strike will only inject charge into one of the two node transistors. Thus, the other transistors can provide charge compensation and keep the data state through the ion-strike event. Not surprisingly, the DICE latch utilizes ~2x the area and twice the power, but provides several orders-of-magnitude reduction in the latch SEU rate as opposed to an unhardened latch.

The actual layout of the DICE cell requires the separation of each of the feedback paths feeding a single node by a distance greater than the expected maximum event induced by a worst-case ion strike. An optimized layout of DICE latch elements can reduce their SEU rate by more than 1,000x.<sup>[21]</sup>

DICE latches are robust against SEU, but not to glitches on their inputs during the setup-and-hold time (from strikes in upstream combinatorial logic or false clock events induced by clock-tree strikes). What is required if the sequential element must be immune to both direct SEUs and SETs? Instead of focusing on hardening the individual storage nodes, latch designs that provide total immunity to both SEUs and SETs require spatial and temporal redundancy. Such circuits are analogous to error correction in memories and involve breaking the input-data signal into multiple identical logic paths, feeding into multiple latch copies whose outputs drive a majority voter circuit, as shown in **Figure 6-12**.<sup>[22]</sup>

Their area and power overhead is higher than the DICE design, but latch designs are truly immune to static upsets in any one of the latches, transients that might be injected by upstream combinatorial logic, and clock or control signal transients.

This design enables an SEU in any single latch in the logic path to be ignored, because the other two paths are the majority; thus, the correct data “wins” the vote. The triplicate clock filters SETs on the input and shifts them so that only one leg of the circuit can capture a SET; again, the majority vote clears the error.

![Figure 6-12: Schematic of a latch with spatial and temporal redundancy. The diagram shows three parallel data paths (U1, U3, U5) each receiving input 'In' and clock signals CLK A, CLK B, and CLK C. Each path has a D-type latch (U1, U3, U5) followed by a majority voter (MAJ). The outputs of the latches are connected to the majority voter. The majority voter also receives inputs from the clock signals. The output of the majority voter is 'Out'. The diagram is labeled 'Temporal sampling' and 'Synchronous voting'.](5e05915b2a93a3b404422e0966a7c924_img.jpg)

Figure 6-12: Schematic of a latch with spatial and temporal redundancy. The diagram shows three parallel data paths (U1, U3, U5) each receiving input 'In' and clock signals CLK A, CLK B, and CLK C. Each path has a D-type latch (U1, U3, U5) followed by a majority voter (MAJ). The outputs of the latches are connected to the majority voter. The majority voter also receives inputs from the clock signals. The output of the majority voter is 'Out'. The diagram is labeled 'Temporal sampling' and 'Synchronous voting'.

**Figure 6-12. Schematic of a latch with spatial and temporal redundancy, making it immune to both SEUs caused by direct node strikes and SETs injected on the inputs or clock.**

A clock glitch will only occur on one of the three driving clocks or on the system clock; again, the result will be a total filtering of the event. Clock disruptions on A, B or C will lead to the majority voter correcting the erroneous signal. A glitch on the master clock will only affect the three latches feeding the majority voter stage, which will all have the correct value; no error will be transmitted to the output. Clearly, this is a very robust design, but obviously with high area and power penalties.

### 6.5 Radiation hardness by design – circuit redundancy solutions

In general, it is difficult to make low-voltage digital memories, particularly DRAM and SRAM, immune to SEUs at the bit level. The parallel demands of low power and high density conspire to reduce the radiation robustness of these types of memories. Technology scaling has allowed some reductions in SEU bit sensitivity with each successive technology node, but products successively integrate larger and larger numbers of memory bits.

Concerning available deep-submicron CMOS processes that have been optimized for low cost, high density and low power, it is necessary to deal with a relatively high SEE sensitivity using external means (outside of bit-cell optimizations for radiation performance). In other words, circuit solutions to build in fault-tolerance are necessary. One of the most effective methods of dealing with radiation-induced bit errors in digital memory is to employ additional circuitry for the detection and correction of these bit errors.

In its simplest form, error detection consists of using an additional bit to store the parity of each data word (regardless of word length). An encoder generates the parity of the word and determines whether a word is even or odd when the word is being written to memory. When data is retrieved (read), the parity decoder runs a check comparing the parity of the stored data to its parity bit. If a single-bit upset (SBU) has occurred, the check will reveal that the parity of the data does not match the parity bit. Thus the parity system enables the detection of a single bit error for a minimal cost in terms of circuit complexity and memory width (because adding a single bit to each word increases this detection capability).

The parity approach presents two primary disadvantages. First, it is a detection scheme only, and once an error is detected, it is up to the external system to rectify the error. The external system must either retrieve valid data and rewrite the correct data (from a reliable data store) or restart the process and reload the memory.

The second problem with the standard parity approach is that for even numbers of errors, the parity bit will match the word data parity; thus multiple-bit upsets (MBUs) will potentially reside in memory, undetected. This is known as silent data corruption.

Parity is much better than no detection because it will detect all SBUs that occur, but the rate of occurrence of even-bit MBU events for that particular memory will limit the reliability. For many SRAM and DRAM memories, the overall MBU rate is ~5-15% of the SBU rate, so adding parity to the memory system reduces the average memory failure rate by ~6-20x. In high radiation environments where a lot of SBUs are expected, the memory will need to be read (the read operation invokes a data-parity check) frequently enough to clear SBUs before they can accumulate to undetectable MBUs.

In applications requiring higher reliability, particularly those where it is necessary to avoid silent data corruption and/or to minimize availability and processor overhead, it is possible to use error detection and correction (EDAC). Also referred to as an error correction circuit (ECC), ECC adds extra code bits to each data vector, encoding the data so that the "information distance" between any two possible data vectors is at least three.

Figures 6-13 shows an ECC block diagram and encoding scheme, respectively. In such systems, if a single error occurs (a change of  $\pm 1$  in information space for the word), there is no chance that the corrupted vector will be mistaken for its nearest neighbors because the information distance is three. The resulting vector uniquely identifies the original word and the location of the bit that needs correcting.

![Figure 6-13: Schematic of latch with spatial and temporal redundancy, making it immune to both SEUs caused by direct node strikes and SET events injected on the inputs or clock. The diagram shows an Encoder block, an Unprotected memory block, and a Decoder block. The Encoder outputs 'Data stable 0000' and 'Unique (correctable) error vectors' (0001, 0010, 0100, 1000, 1111, 1110, 1101, 1010). The Decoder outputs 'Data stable 0000' and 'Nonunique (but detectable) error vectors' (0001, 0010, 0100, 1000, 1111, 1110, 1101, 1010). The diagram is labeled 'Single error' and 'Double error'.](f40480872b021d2ac7c29202c199b695_img.jpg)

Figure 6-13: Schematic of latch with spatial and temporal redundancy, making it immune to both SEUs caused by direct node strikes and SET events injected on the inputs or clock. The diagram shows an Encoder block, an Unprotected memory block, and a Decoder block. The Encoder outputs 'Data stable 0000' and 'Unique (correctable) error vectors' (0001, 0010, 0100, 1000, 1111, 1110, 1101, 1010). The Decoder outputs 'Data stable 0000' and 'Nonunique (but detectable) error vectors' (0001, 0010, 0100, 1000, 1111, 1110, 1101, 1010). The diagram is labeled 'Single error' and 'Double error'.

**Figure 6-13. Schematic of latch with spatial and temporal redundancy, making it immune to both SEUs caused by direct node strikes and SET events injected on the inputs or clock.**

Double-bit errors occurring in the same “correction word” are still detectable. But with an information distance of three, a double-bit error leads to two possible source words as the original source vector; thus the error is not correctable. ECCs of this type are common and referred to as single-error correct-double-error detect (SEC-DED) systems.

The implementation shown in [Figure 6-13](#) is not efficient and only serves as an example for the concept of encoding words in information space. Hamming codes are used for encoding and are far more efficient, with efficiency improving as word width increases.

In some cases, where higher reliability is required, it is possible to implement larger information distances by encoding words with more bits, enabling the correction and detection of a larger number of bit errors. ECCs to enable double-error correct-triple-error detect (DEC-TED) are also occasionally used where necessary to maximize reliability. [Table 6-1](#) shows the bit overhead for typical SEC-DED and DEC-TED implementations.<sup>[23]</sup>

| Data word width (bits) | Single-error correction – Double-error detection (SEC-DED) |                  |                  | Double-error correction – Triple-error detection (DEC-TED) |                  |                  |
|------------------------|------------------------------------------------------------|------------------|------------------|------------------------------------------------------------|------------------|------------------|
|                        | Check bits                                                 | Total word width | Overhead for ECC | Check bits                                                 | Total word width | Overhead for ECC |
| 8                      | 5                                                          | 13               | 263%             | 9                                                          | 17               | 213%             |
| 16                     | 8                                                          | 22               | 138%             | 11                                                         | 27               | 169%             |
| 32                     | 7                                                          | 39               | 122%             | 13                                                         | 45               | 144%             |
| 64                     | 8                                                          | 72               | 113%             | 15                                                         | 79               | 123%             |
| 128                    | 9                                                          | 137              | 107%             | 17                                                         | 145              | 113%             |
| 256                    | 10                                                         | 266              | 1048%            | 19                                                         | 275              | 2108%            |

Table 6-1. Area overhead for typical SEC-DED and DEC-TED implementations.

Because most SEUs are single-bit errors, properly implemented SEC-DED ECC protection provides a significant reduction in failure rates.

Proper implementation to get the highest entitlement out of an ECC solution requires that designers maximize the physical separation between bits in a single correction word. MBU events become increasingly rare as the size of the event increases.

Physically, this makes perfect sense, because the energy of incoming particles decreases rapidly with increasing energy (or LET), as described in previous chapters on space and terrestrial radiation environments.

SRAM cell dimension and the architectural column-multiplexer (MUX) factor, or bit interleaving, define the actual physical distance between bits in the same logical word. This is critical because using a higher-column MUX factor reduces the failure rate of the same ECC solution by orders of magnitude. Because bigger MBU events that limit the efficacy of ECC systems are more rare, the larger the separation between bits, the lower the probability of an event that the ECC cannot correct. [Figure 6-14](#) shows the MBU statistics from neutron SEU studies of various Texas Instruments SRAM technologies.

The normalized failure probabilities (to the total number of SEUs observed) for single-, double- and triple-bit upsets are shown as a function of “event distance,” determined from a straight-line path connecting the affected bits (bit errors) in the row direction and calculating an effective distance using the SRAM cell dimensions (as measured from center to center).

![Figure 6-14: Normalized error probabilities (normalized to the total number of upsets) for single-, double- and triple-bit upsets as a function of event distance during neutron-induced SEUs in various SRAM technologies. The plot shows Normalized SEU rate on a logarithmic y-axis (0.0001 to 1) versus Event distance (nm) on a linear x-axis (0 to 6). Data points are shown for 28-nm HDPR, 28-nm HDBU, 28-nm HDLL, 28-nm SUHD, 45 nm, 45 nm 90°, 65 nm, 90 nm, and 180 nm. A red line represents the CFD (Cumulative Failure Distribution).](e58957e9be66d36eee4621cd225850f0_img.jpg)

Figure 6-14: Normalized error probabilities (normalized to the total number of upsets) for single-, double- and triple-bit upsets as a function of event distance during neutron-induced SEUs in various SRAM technologies. The plot shows Normalized SEU rate on a logarithmic y-axis (0.0001 to 1) versus Event distance (nm) on a linear x-axis (0 to 6). Data points are shown for 28-nm HDPR, 28-nm HDBU, 28-nm HDLL, 28-nm SUHD, 45 nm, 45 nm 90°, 65 nm, 90 nm, and 180 nm. A red line represents the CFD (Cumulative Failure Distribution).

Figure 6-14. Normalized error probabilities (normalized to the total number of upsets) for single-, double- and triple-bit upsets as a function of event distance during neutron-induced SEUs in various SRAM technologies.<sup>[24, 25]</sup>

For example, the 45-nm SRAM demonstrates that double-bit upsets (DBUs) are ~4%, triple-bit upsets are ~0.12% and quad-bit upsets are ~0.02% of the total number of SEUs observed. Thus, using a larger MUX-column factor enables larger events to be correctable and leads to much larger reductions in ECC/parity failure rates for nearly the same SEC-DED overhead.

[Figure 6-15](#) graphically demonstrates the reason that higher column MUXing or bit interleaving works at reducing the failure rate of a typical SEC-DED ECC solution. With a MUX = 1 architecture, where all bits are physically adjacent (and assuming that the MBU does not occur across a word boundary and only occurs within a single word), the event represents a 5-bit MBU in that single word. The error is uncorrectable (five red squares).

![Figure 6-15: 5-bit MBU in memory array as a function of four different column-MUX (bit-interleaving) architectures. The figure shows four diagrams for MUX = 1, 2, 4, and 8. Each diagram shows a 5-bit MBU (red squares) and its mapping to correctable SBUs (Cs) and detectable DBUs (Ds).](4ec1b27e444ce96de31776c2e76ee466_img.jpg)

Figure 6-15: 5-bit MBU in memory array as a function of four different column-MUX (bit-interleaving) architectures. The figure shows four diagrams for MUX = 1, 2, 4, and 8. Each diagram shows a 5-bit MBU (red squares) and its mapping to correctable SBUs (Cs) and detectable DBUs (Ds).

Figure 6-15. 5-bit MBU in memory array as a function of four different column-MUX (bit-interleaving) architectures. The increased MUX factor leads to improved reliability by mapping an uncorrectable MBU into multiple correctable SBUs (Cs) and detectable DBUs (Ds).

In contrast, in the MUX = 2 arrangement where the bits from two words are interleaved, the distance between bits in the same word has doubled. The 5-bit MBU is actually mapped into one triple-bit error in one word and a double-bit error in the other word – the double-bit error is detectable (the triple-bit error may be detectable or not, depending on the SEC-DED implementation).

When MUX = 4 bits, four separate words are interleaved such that the distance between bits in the same word increases by 4x. The 5-bit MBU transforms into a single detectable double-bit error in one word and one SBU in each of three words, each of which is a correctable error.

When MUX = 8 bits, all of the error bits are transformed into correctable SBUs. Therefore, using higher MUX factors, the circuit sensitivity to MBUs is reduced by mapping them into SBUs in bits of the interleaved words, changing from uncorrectable (ECC failure) events to multiple correctable (ECC success) events, thereby attaining much higher reliability for the same system overhead.

The “analog” of memory parity and ECC in systems with random logic paths involves replicating those logic paths feeding, and feeding the final output into a detection or majority-voting (two out of three) circuit.

Known as dual-modular redundant (DMR) or triple-modular redundant (TMR) circuits, these types of architectures enable either the detection of an SEU-/SET-induced error in a logic path (when the two outputs of a DMR system do not agree) or, in the case of TMR systems, overruling the other two valid inputs to the majority voter. This method uses two to three times the silicon area as an unprotected path and requires specialized simulation tools to identify the critical logic paths (because of the high cost, only

the most sensitive paths are typically protected). Also, the voter is typically drive-hardened so that single events to the voter do not give a false result.

The final and most ambitious (expensive) form of system-level redundancy (at least for monolithic solutions) is to use duplicate redundant processor cores – where multiple, identical cores run in lockstep (executing the same code at the same time). This is expensive in both area and power because the same computation and instruction flow runs on each redundant core. Like parity solutions in memory, in a dual-core lockstep system, a restart occurs when a mismatch between the cores is detected.<sup>[26]</sup>

The power and area overhead is ~2x an unprotected single core, but the reliability failure rate is reduced by many orders of magnitude. Several Texas Instruments Hercules™ microcontrollers use this type of redundancy to maximize reliability.

In systems requiring even higher reliability (or at least higher availability), using three identical cores in lockstep with a majority voter fosters the ability to correct a core that has an error, the assumption being that the error only occurs in one of three cores, so correction is based on two of the three cores having matching valid outputs. This is the most expensive redundancy scheme, but it can reduce SEE rates to near-zero levels, providing the necessary high reliability and high availability for some long-term remote or mission-critical applications.<sup>[27]</sup>

Figure 6-16 is a block diagram of double- and triple-core solutions. As with other redundancy solutions, it is important that the voter itself be hardened to avoid SEEs that would cause erroneous resets or correction operations.

![Figure 6-16: Diagram of dual- and triple-core systems. The left diagram shows a 'Dual-core lock-step system' with Core 1 and Core 2 feeding into a 'Compare' block, which then feeds into a 'Controller' block. The 'Controller' block feeds into an 'Input/output' block. The right diagram shows a 'TMR core lock-step system' with Core 1, Core 2, and Core 3 feeding into a 'Majority voter' block. The 'Majority voter' block feeds into an 'Error detection and handling' block, which then feeds into an 'Input/output' block.](7b18671bc31881a5c474883bf6a300fd_img.jpg)

```

graph LR
    subgraph Dual_core_lock_step_system [Dual-core lock-step system]
        C1[Core 1] --> Compare[Compare]
        C2[Core 2] --> Compare
        Compare --> Controller[Controller]
        Controller --> IO1[Input/output]
    end

    subgraph TMR_core_lock_step_system [TMR core lock-step system]
        C3_1[Core 1] --> MV[Majority voter]
        C3_2[Core 2] --> MV
        C3_3[Core 3] --> MV
        MV --> EDH[Error detection and handling]
        EDH --> IO2[Input/output]
    end

```

Figure 6-16: Diagram of dual- and triple-core systems. The left diagram shows a 'Dual-core lock-step system' with Core 1 and Core 2 feeding into a 'Compare' block, which then feeds into a 'Controller' block. The 'Controller' block feeds into an 'Input/output' block. The right diagram shows a 'TMR core lock-step system' with Core 1, Core 2, and Core 3 feeding into a 'Majority voter' block. The 'Majority voter' block feeds into an 'Error detection and handling' block, which then feeds into an 'Input/output' block.

Figure 6-16. Diagram of dual- and triple-core systems – the redundant cores run the same code in lockstep with error-detection logic to catch mismatch events on core outputs. In the case of the dual core, a reset is required because there is no way to tell which of the two cores is erroneous, while in the triple core, majority voting resets the failing processor in the background.

### End Notes

<http://www.chipworks.com/>.

M. R. Shaneyfelt, P. E. Dodd, B. L. Draper and R. S. Flores, "Challenges in Hardening Technologies Using Shallow-Trench Isolation," *IEEE Trans. Nucl. Sci.* 45(6), Dec. 1998, pp. 2584-2592.

D. M. Fleetwood, "Evolution of Total Ionizing Dose Effects in MOS Devices with Moore's Law Scaling," *IEEE Trans. Nucl. Sci.* 64(6), Dec. 2017, pp. 1-17.

P. E. Dodd, M. R. Shaneyfelt, J. R. Schwank and J. A. Felix, "Current and Future Challenges in Radiation Effects on CMOS Electronics," *IEEE Trans. Nucl. Sci.* 57(4), Aug. 2010, pp. 1747-1763.

J. D. Cressler et al., "The Effects of Proton Irradiation on the Lateral and Vertical Scaling of UHV/CVD SiGe HBT BiCMOS Technology," *IEEE Trans. Nucl. Sci.* 47(6), Dec. 2000, pp. 2515-2520.

R. C. Lacoe et al., "Neutron and proton irradiation for latchup suppression in a radiation-tolerant commercial submicron CMOS process," *Proceedings of the Fifth European Conference on Radiation and Its Effects on Components and Systems*, Sept. 1999, pp. 340-345.

R. L. Pease, R. D. Schrimpf and D. M. Fleetwood, "ELDRS in Bipolar Linear Circuits: A Review," *IEEE Trans Nucl. Sci.* 56(4), Aug. 2009, pp. 1894-1908.

M. R. Shaneyfelt et al., "Impact of Passivation Layers on Enhanced Low-Dose-Rate Sensitivity and Pre-Irradiation Elevated-Temperature Stress Effects in Bipolar Linear ICs," *IEEE Trans Nucl. Sci.* 49(6), Dec. 2002, pp. 3171-3179.

O. A. Amusan et al., "Charge Collection and Charge Sharing in a 130 nm CMOS Technology," *IEEE Trans. Nucl. Sci.* 53(6), Dec. 2006, pp. 3253-3258.

M. Allenspach et al., "SEGR and SEB in N-Channel Power MOSFETs," *IEEE Trans. Nucl. Sci.* 43(6), Dec. 1996, pp. 2921-2931.

### References

- 1 R. Edwards, C. Dyer and E. Normand, "Technical standard for atmospheric radiation single event effects (SEE) on avionics electronics," *Proceedings of the IEEE Radiation Effects Data Workshop*, Dec. 2004, pp. 1-5.
- 2 K. A. LaBel, D. K. Hawkins, J. A. Kinnison, W. P. Stapor and P. W. Marshall, "Single event effect characteristics of CMOS devices employing various epi-layer thicknesses," *Proceedings of the Third European Conference on Radiation and its Effects on Components and Systems*, Sept. 1995, pp. 258-262.
- 3 R. C. Baumann and E. B. Smith, "Neutron-induced boron fission as a major source of soft errors in deep submicron SRAM devices," *Proceedings of the 38th IEEE International Reliability Physics Symposium*, April 10-13, 2000, pp. 152-157.
- 4 H. Kobayashi et al., "Comparison between neutron-induced system SER and accelerated SER in SRAMs," *Proceedings of the 42nd International Reliability Physics Symposium*, April 25-29, 2004, p. 288.
- 5 J. Park et al., "Development of thermal neutron SER-resilient high-k/metal gate technology," *Proceedings of the IEEE International Reliability Physics Symposium*, June 1-5, 2014, pp. 2B.4.1-2B.4.3.
- 6 N. A. Dodds et al., "Effectiveness of SEL Hardening Strategies and the Latchup Domino Effect," *IEEE Trans. Nuclear Sci.* 59(6), Dec. 2012, pp. 2642-2650.
- 7 O. Musseau, "Single-Event Effects in SOI Technologies and Devices," *IEEE Trans. Nucl. Sci.* 43(2), April 1996, pp. 603-613.
- 8 P. Roche, G. Gasiot, K. Forbes, V. O'Sullivan and V. Ferlet, "Comparisons of Soft Error Rate for SRAMs in Commercial SOI and Bulk Below the 130-nm Technology Node," *IEEE Trans. Nucl. Sci.* 50(6), Dec. 2003, pp. 2046-54.
- 9 E. H. Cannon, D. D. Reinhardt, M. S. Gordon and P. S. Makowsensky, "SRAM SER in 90, 130 and 180nm bulk and SOI technologies," *Proceedings of the IEEE International Reliability Physics Symposium*, April 25-29, 2004, pp. 300-304.
- 10 V. Srinivasan, A. L. Sternberg, A. R. Duncan, W. H. Robinson, B. L. Bhuvu et al., "Single-Event Mitigation in Combinational Logic using Targeted Data Path Hardening," *IEEE Trans. Nucl. Sci.* 52(6), Dec. 2005, pp. 2516-2523.
- 11 G. Torrents, S. A. Bota, B. Alorda and J. Segura, "An Experimental Approach to Accurate Alpha-SER Modeling and Optimization Through Design Parameters in 6T SRAM Cells for Deep-Nanometer CMOS," *IEEE Transactions on Device and Materials Reliability* 14(4), Sept. 2014, pp. 1013-1021.
- 12 N. A. Dodds et al., "Effectiveness of SEL Hardening Strategies and the Latchup Domino Effect," *IEEE Trans. Nuclear Sci.* 59(6), Dec. 2012, pp. 2642-2650.
- 13 X. Zhu, X. Deng, R. Baumann and S. Krishnan, "Charge Collection Efficiency Ratio of N+ and P+ Diffusion Areas of 90nm CMOS Technology in the Terrestrial Neutron Environment," *IEEE Trans. Nucl. Sci.* 54(6), Dec. 2007, pp. 2156-2161.
- 14 J. D. Black et al., "HBD Layout Isolation Techniques for Multiple Node Charge Collection Mitigation," *IEEE Trans. Nucl. Sci.* 52(6), Dec. 2005, pp. 2536-2541.
- 15 R. Chen et al., "Single-Event Multiple Transients in Conventional and Guard-Ring Hardened Inverter Chains Under Pulsed Laser and Heavy-Ion Irradiation," *IEEE Trans. Nucl. Sci.* 64(9), Sept. 2017, pp. 2511-2518.
- 16 G. Anelli et al., "Radiation Tolerant VLSI Circuits in Standard Deep Submicron CMOS Technologies for the LHC Experiments: Practical Design Aspects," *IEEE Trans. Nucl. Sci.* 46(6), Dec. 1999, pp. 1690-1696.
- 17 I. Donnelly, private communication, report on Texas Instruments BiCMOS technology, TallannQuest, 2015.

- 18 T. F. Wrobel and D. E. Beutler, "Solutions to Heavy-Ion Induced Avalanche Burnout in Power Devices," *IEEE Trans. Nucl. Sci.* 39(6), Dec. 1992, pp. 1636-1641.
- 19 C. Dachs et al., "Simulation Aided Hardening of N-Channel Power MOSFETs to Prevent Single Event Burnout," *IEEE Trans. Nucl. Sci.* 42(6), Dec. 1995, pp. 1935-1939.
- 20 T. Calin, M. Nicolaidis and R. Velazco, "Upset Hardened Memory Design for Submicron CMOS Technology," *IEEE Trans. Nucl. Sci.* 43(6), Dec. 1996, pp. 2874-2878.
- 21 L. H-H. Keln et al., "LEAP: Layout Design through Error-Aware Transistor Positioning for Soft-Error Resilient Sequential Cell Design," *Proceedings of the IEEE International Reliability Physics Symposium*, May 2-6, 2010, pp. 203-212.
- 22 D.G. Mavis and P. H. Eaton, "Soft Error Rate Mitigation Techniques for Modern Microcircuits," *Proceedings of the 40th IEEE International Reliability Physics Symposium*, April 7-11, 2002, pp. 216-225.
- 23 C. Slayman, "Cache and memory error detection, correction and reduction techniques for terrestrial servers and workstations," *IEEE Transactions on Device and Materials Reliability* 5(3), May 2005, pp. 397-404.
- 24 R. Baumann, "SER Estimator Tutorial," Texas Instruments documentation for online SEU calculation tool. 2001-2009, pp. 1-69.
- 25 D. Radaelli, H. Puchner, S. Wong and S. Daniel, "Investigation of Multi-Bit Upsets in a 150 nm Technology SRAM Device," *IEEE Trans. Nucl. Sci.* 52(6), Dec. 2005, pp. 2433-2437.
- 26 T. Kottke and A. Steininger, "A Reconfigurable Generic Dual-Core Architecture," *International Conference on Dependable Systems and Networks*, June 25-28, 2006, pp. 45-54.
- 27 X. Iturbe, B. Venu, E. Ozer and S. Das, "A Triple Core Lock-Step (TCLS) ARM® Cortex®-R5 Processor for Safety-Critical and Ultra-Reliable Applications," *46th Annual IEEE/IFIP International Conference on Dependable Systems and Networks Workshop*, June 28-July 1, 2016, pp. 246-249.

# Chapter 7: Radiation testing and qualification

This chapter provides an overview of radiation testing, as well as a general understanding of the procedures and requirements needed for radiation qualification. It is not intended to be a guide or standard for testing. Consult the actual standards for details regarding testing and qualification. The focus of this chapter is on the testing and qualification of integrated circuits (ICs) for space applications, while discussing some military and terrestrial testing.

The general military specification MIL-PRF-38535 describes how to manufacture, test and qualify ICs for military and space applications.<sup>[1]</sup> The military standard MIL-STD-883 provides test methods (TMs) for meeting those requirements.<sup>[2]</sup>

The standard microcircuit drawing (SMD) is the specification for a certain device type. For example, 5962-96738 is the SMD for the LM139A. 5962R9673802VDA is the SMD identification number for the space-grade LM139A in a flat pack. The “R” after 5962 indicates that the device is radiation hardness assured (RHA) to 100 krad.

Radiation Hardened, also known as Radiation Hardness Assured (RHA) products, are those products where each lot is tested and qualified for a total ionizing dose (TID) level per MIL-PRF-38538.<sup>[1]</sup> Qualification of a lot is known as Radiation Lot Acceptance Testing (RLAT). A lot can be either a single wafer or a full wafer lot (also called a diffusion run). A letter in the SMD number and sometimes in a Texas Instruments device number indicates the TID level.

In addition to TID testing, an RHA product might meet other radiation requirements, such as single-event effect (SEE) or displacement damage dose (DDD), as defined in the SMD and/or a Texas Instruments data sheet.

Note that the SMD will call any device that is RHA “radiation hardened,” even if nothing in particular is done to radiation-harden the device.

### 7.1 TID testing

There are many different sources of ionizing radiation. In space, protons and electrons generate most of the TID radiation, while in medical applications, gamma rays or X-rays might be the source. TID testing most commonly uses gamma radiation from a cobalt-60 source. Here is the basic TID test flow:

- Assemble units from the wafer into packages.
- Electrically test the devices under test (DUTs) on automated test equipment (ATE) to verify that the DUTs meet the functional and parametric limits specified on the data sheet.
- Put the DUTs through burn-in, if the products normally receive burn-in.

Gamma rays are high-energy photons. Cobalt-60 decays into nickel-60, emitting two photons. Cobalt-60 has a half-life of 5.2 years.

- Retest the DUTs on the ATE.
- Place the DUTs in a socketed bias board and bias them under normal operating conditions.
- Expose the biased board to the radiation source and irradiate it to the rated TID level at room temperature.
- Remove the board from the radiation source and remove the DUTs from the board.
- Retest the DUTs on the ATE to verify that the units are still functional and that no critical parameters have drifted outside of the data-sheet limits.

This test procedure can vary depending on the process technology tested and the application's radiation environment (see Chapter 6 for a discussion on TID sensitivity by process technology).

Testing to 100 krad at a high dose rate (HDR) takes a few hours, including irradiation time and electrical testing. Testing to 100 krad at a low dose rate (LDR) of 10 mrad/s takes close to six months.

A number of different standards and guidelines exist for testing TID effects. TI strictly adheres to MIL-STD-883 test method (TM) 1019 for TID qualification and RLAT. Other test standards include ESA ESCC Basic Specification No. 22900 and ASTM F 1892 Standard Guide for Ionizing Radiation (Total Dose) Effects Testing of Semiconductor Devices, to be discussed in later sections.

### MIL-STD-883 TM 1019

Texas Instruments tests and qualifies products for TID using MIL-STD-883 TM 1019, which describes test and qualification options using a cobalt-60 source.<sup>[2]</sup> TM 1019 is flexible, offering test options based on a semiconductor technology's TID sensitivity at different dose rates.

TM 1019 was released in 1978. It originally offered the option of using a cobalt-60 source or an electron-beam source to irradiate DUTs. In the 1980s, the use of an electron-beam source for testing was dropped.

The original test method had just one test flow. Over time, the test method evolved and new tests were added, as it was discovered that different semiconductor technologies experienced different TID effects (see Chapter 6) and that one test flow did not cover all technologies and radiation environments. For instance, for most space applications, in a natural environment, irradiation occurs at an LDR over a span of years. A weapons application in a man-made radiation environment may be more concerned with a relatively high dose rate. TM 1019 now allows the customization of testing based on the technology and the environment for which the product is being qualified.

We will discuss the history and purpose of the different additions to put these tests in context and indicate when they are required. The current test flow is shown in [Figure 7-1](#). [Table 7-1](#) is a summary of all the tests and their purposes and [Table 7-2](#) shows the different dose rate options and when to use them.

#### Test flow and dose rate

![Flowchart of TID RLAT test flow from MIL-STD-883 TM 1019. The process starts with selecting a dose rate (50 to 300 rad/s or 0.01 rad/s), followed by irradiation to a specified dose with interim test points. Electrical tests are performed on ATE. If the test fails, an extended room-temperature anneal is required, followed by another set of electrical tests. If that fails, a MOS accelerated annealing test (MAAT) is required. If MAAT is required, an additional 0.5x dose is irradiated, followed by a 168-hour anneal at 100°C, and finally another set of electrical tests. The process ends with a Pass or Fail result.](f4fdce3ce1c0fd291f31813f83d0d0d3_img.jpg)

```

graph TD
    A[Select dose rate  
50 to 300 rad/s or 0.01 rad/s] --> B[Irradiate to specified dose  
Interim test points are sometimes taken]
    B --> C[Perform specified electrical tests  
Test data-sheet parameters on ATE]
    C -- Pass --> D[Determine if extended room  
temperature anneal test is required  
Extended room-temperature anneal test]
    C -- Fail --> D
    D --> E[Perform specified electrical tests  
Test data-sheet parameters]
    E -- Fail --> F[Determine if accelerated annealing test is required  
Metal-oxide semiconductor (MOS) accelerated  
annealing test (MAAT)]
    E -- Pass --> F
    F -- No --> G[Pass]
    F -- Yes --> H[Irradiate an additional 0.5x  
specified dose]
    H --> I[Anneal biased for 168 hours  
at 100°C]
    I --> J[Perform specified electrical tests  
Test data-sheet parameters]
    J -- Pass --> G
    J -- Fail --> K[Fail]
  
```

Flowchart of TID RLAT test flow from MIL-STD-883 TM 1019. The process starts with selecting a dose rate (50 to 300 rad/s or 0.01 rad/s), followed by irradiation to a specified dose with interim test points. Electrical tests are performed on ATE. If the test fails, an extended room-temperature anneal is required, followed by another set of electrical tests. If that fails, a MOS accelerated annealing test (MAAT) is required. If MAAT is required, an additional 0.5x dose is irradiated, followed by a 168-hour anneal at 100°C, and finally another set of electrical tests. The process ends with a Pass or Fail result.

Figure 7-1. TID RLAT flow from MIL-STD-883 TM 1019.<sup>[2]</sup>  
Image courtesy of Department of Defense.

| Test                    | Product type                 | Purpose                                                 |
|-------------------------|------------------------------|---------------------------------------------------------|
| HDR                     | Without ELDRS or TDE         | Standard test for RLAT                                  |
| MAAT                    | With MOS elements            | Determine if the technology has TDEs                    |
| Room-temperature anneal | Fails HDR                    | Determine if product could be qualified for LDR testing |
| ELDRS characterization  | With bipolar linear elements | Determine if the product has ELDRS                      |
| LDR                     | Without ELDRS                | Alternative to HDR testing for RLAT                     |
| LDR + 1.5x overtest     | With ELDRS                   | RLAT                                                    |
| Accelerated ELDRS       | With bipolar linear elements | Alternative RLAT verified through characterization      |

Table 7-1. Summary of TM019 TID tests.

| Condition | Dose rate   | Use                                                                   |
|-----------|-------------|-----------------------------------------------------------------------|
| A         | 50-300 krad | CMOS and devices that do not have ELDRS                               |
| B         | <50 rad/s   | MOS devices, as agreed to by parties to the test                      |
| C         | Any         | As agreed to by parties to the test                                   |
| D         | ≤10 mrad/s  | RLAT for devices with ELDRS and alternative for devices without ELDRS |
| E         | >10 mrad/s  | Accelerated tests verified through characterization                   |

Table 7-2. TM 1019 dose-rate conditions.

### HDR testing

Originally, TM 1019 required cobalt-60 testing at a dose rate between 1.66 rad(Si)/s and 2,500 rad(Si)/s. The test range was tightened from 50 rad/s to 300 rad/s in the early 1990s.<sup>[3]</sup>

#### MAAT or rebound test

The MOS accelerated anneal test (MAAT) is used to determine if a product has time dependent effects (TDE). It is performed at qualification on products that have MOS elements. If a device does not have TDEs, a MAAT is not performed at RLAT.

In the 1980s, it was found that some MOS structures exhibited TDEs where a product's performance continued to degrade after it was removed from the radiation source.<sup>[4,5]</sup> This was viewed as a sensitivity to LDR that did not appear at HDR testing.<sup>[2]</sup>

To test for TDE, the MOS MAAT was developed.<sup>[6]</sup> This is the basic MAAT test flow:

- After the DUTs have completed TID testing at an HDR to the rated dose and have been electrically tested, put the DUTs back in the socketed bias board.
- Irradiate DUTs an additional 0.5x the rated dose while biased under standard operating conditions.
- Move the bias board into the oven. Bake at 100°C for one week with the DUTs biased under standard operating conditions.
- Remove the DUTs from the oven and bias board.
- Electrically test the DUTs on the ATE

If the units show more degradation after going through the MAAT, then a MAAT is required for RLAT. If degradation after the MAAT is not worse, then the technology does not have TDEs and a MAAT is not required for RLAT.

The MAAT correlated well with some technologies from the 1980s.<sup>[6]</sup> To ensure that newer technologies do not have TDEs, the MAAT remains in TM 1019 and Texas Instruments still performs the MAAT. Texas Instruments has found that its technologies do not have TDEs and the MAAT anneals out the TID effects and the products return to their pre-irradiation state following the MAAT (Figure 7-2).<sup>[7]</sup> Thus, Texas Instruments products do not require a MAAT for RLAT.

![Figure 7-2: Power-down current of the ADC12D1600CCMLS at various TID levels and after a MAAT. The graph shows Power-down current (mA) on the y-axis (0 to 50) versus Test point (krad) on the x-axis. The x-axis has labels: 0.0, 3.0, 10.0, 30.0, 50.0, 100.0, 150.0, 300.0, and MAAT. Two curves are plotted: 215 (blue) and 216 (red). Both curves show a sharp increase in current starting around 150 krad, peaking at 300 krad, and then dropping significantly after the MAAT test point.](44407a1200fa896c3cdb7861f771c975_img.jpg)

| Test point (krad) | Power-down current (mA) - Unit 215 | Power-down current (mA) - Unit 216 |
|-------------------|------------------------------------|------------------------------------|
| 0.0               | ~2                                 | ~2                                 |
| 3.0               | ~2                                 | ~2                                 |
| 10.0              | ~2                                 | ~2                                 |
| 30.0              | ~2                                 | ~2                                 |
| 50.0              | ~2                                 | ~2                                 |
| 100.0             | ~2                                 | ~2                                 |
| 150.0             | ~5                                 | ~5                                 |
| 300.0             | ~42                                | ~35                                |
| MAAT              | ~2                                 | ~2                                 |

Figure 7-2: Power-down current of the ADC12D1600CCMLS at various TID levels and after a MAAT. The graph shows Power-down current (mA) on the y-axis (0 to 50) versus Test point (krad) on the x-axis. The x-axis has labels: 0.0, 3.0, 10.0, 30.0, 50.0, 100.0, 150.0, 300.0, and MAAT. Two curves are plotted: 215 (blue) and 216 (red). Both curves show a sharp increase in current starting around 150 krad, peaking at 300 krad, and then dropping significantly after the MAAT test point.

Figure 7-2. Power-down current of the ADC12D1600CCMLS at various TID levels and after a MAAT. Nos. 215 and 216 are the serial numbers of the units tested. This is a 180-nm CMOS process developed in the late 1990s.<sup>[7]</sup>

#### LDR testing for MOS products

This test is for MOS products where HDR is not a concern.

When it was originally released, TM 1019 required TID testing at a relatively high dose rate, allowing the tested TID level to be reached in a matter of minutes. For many applications, such as most space applications, the radiation environment is at an LDR, where TID accrues over a span of years.

For some process technologies, especially CMOS, HDR is the worst case; these technologies can survive a much higher TID when irradiated at an LDR (see Chapter 6). Testing at an HDR for these technologies is overly conservative for an LDR environment. A product might fail testing at an HDR, but will still be usable in an LDR environment.

In 1991, TM 1019 was updated to enable testing at dose rates lower than 50 rad/s for application environments lower than 50 rad/s.

DUTs are irradiated at dose rates lower than 50 rad/s but higher than the application dose rate. Dose rate is determined by the parties to the test.

#### Extended room-temperature anneal test

This test is performed on products that fail HDR testing to determine whether they can qualify for LDR environments. This test can be done at RLAT to qualify devices for an LDR environment using an HDR source.

In 1997, the extended room-temperature anneal test was added to simulate an LDR environment while irradiating the devices at an HDR for those products for which HDR is the worst case. If after performing standard HDR testing the units are parametrically out of specification but remain functional, the product is eligible to continue on to the extended room-temperature anneal test. Here is the basic flow of the test:

- Irradiate DUTs at an HDR to the rated TID while under bias.
- Test the DUTs on the ATE.
- If the DUTs fail on the ATE but remain functional, put back the irradiated DUTs on bias at room temperature, outside the radiation source, in a normal room environment.
- Periodically test the units electrically to determine whether they have recovered and if all parameters are back within specification.
- If the DUTs recover, qualify the products for the TID level tested at an HDR, but only for LDR environments.
- Determine the maximum dose rate for which the devices qualify by dividing the TID level tested by the length of time it took for the DUTs to recover.
- If the DUTs recover, use this test for RLAT in the future.

Figure 7-3 shows how Texas Instruments validated this test method on some more recent technologies.<sup>[8]</sup> The company uses this test for RLAT on some CMOS technologies.

![Figure 7-3: A line graph showing Zero-code error (mV) on the y-axis (0 to 25) versus Radiation or anneal level (hour) on the x-axis. The x-axis is divided into 'Irradiation' (0 to 100 krad) and 'Extended room temperature anneal' (100 krad to 1008 hours). Five data series are plotted: HDR biased (solid red line), HDR unbiased (dashed blue line), LDR biased (dashed red line), LDR unbiased (dashed blue line), and Test limit (solid blue line). The HDR biased line shows a significant peak of approximately 20 mV at 100 krad, while the other lines remain near zero. The test limit is a horizontal line at approximately 8 mV.](8f5fbabe9c2e3a7da6ad0655e54a27f7_img.jpg)

Figure 7-3: A line graph showing Zero-code error (mV) on the y-axis (0 to 25) versus Radiation or anneal level (hour) on the x-axis. The x-axis is divided into 'Irradiation' (0 to 100 krad) and 'Extended room temperature anneal' (100 krad to 1008 hours). Five data series are plotted: HDR biased (solid red line), HDR unbiased (dashed blue line), LDR biased (dashed red line), LDR unbiased (dashed blue line), and Test limit (solid blue line). The HDR biased line shows a significant peak of approximately 20 mV at 100 krad, while the other lines remain near zero. The test limit is a horizontal line at approximately 8 mV.

Figure 7-3. Zero-code error of the DAC121S101WGRQV at various TID test points at an HDR and LDR, with some units under bias during irradiation and other units with the pins tied together during irradiation. This product shows very little parametric drift under an LDR, but significant drift at an HDR with the units biased during irradiation. The biased HDR units were subjected to extended room-temperature anneal and recovered, correlating with but not underestimating the LDR drift.<sup>[9]</sup>

#### ELDRS characterization for linear bipolar and BiCMOS products for application environments lower than 50 mrad/s

This test determines whether a device has ELDRS, and how to perform RLAT. See Figure 7-4 for a flowchart on ELDRS characterization and RLAT.

In the early 1990s, it was discovered that some bipolar linear products degraded more at an LDR than at an HDR for the same TID level (Chapter 3).<sup>[9]</sup> This phenomenon was eventually called enhanced low-dose-rate sensitivity, or ELDRS.

In 2006, the ELDRS characterization was added to TM 1019. ELDRS characterization is a requirement for bipolar and BiCMOS linear and mixed-signal products for radiation environments lower than 50 rad/s. It is not required if there is no intent to qualify the product for LDR environments. It is not required for purely digital bipolar or BiCMOS products, nor for any type of pure CMOS products.

The ELDRS characterization determines whether a device has ELDRS. If the characterization determines that the product does not have ELDRS, then RLAT for that product can be performed at an HDR. If a device has ELDRS, then it is necessary to perform RLAT either through an accelerated test method or irradiation of the product to 1.5x the rated dose. For instance, if a device found to have ELDRS was rated to 100 krad, it is necessary to irradiate the device to 150 krad at 10 mrad/s, but it still must pass the 100 krad post-irradiation limits.

For ELDRS characterization, 20 units plus one control unit are electrically tested and data-logged. The following split is run:

- Five units irradiated at an HDR (50 rad/s to 300 rad/s) with units biased under operating conditions.
- Five units irradiated at an HDR (50 rad/s to 300 rad/s) with leads grounded.
- Five units irradiated at an LDR (0.01 rad/s) with units biased under operating conditions.
- Five units irradiated at an LDR (0.01 rad/s) with leads grounded.

Units are removed from the radiation source and electrically tested at both 0.5x the rated dose as well as the rated dose, comparing the median parametric drift of the samples irradiated at an HDR and an LDR. If the median LDR drift is 1.5x greater than the median HDR drift and if any of the test results are outside the pre-irradiation test limits, the device is considered to have ELDRS.

![Figure 7-4: A flowchart for ELDRS testing. It starts with a decision box 'Determine the need for ELDRS testing'. If 'Yes', it leads to 'Test at the intended application dose rate para. 3.6.3, condition C', which can result in 'Pass' or 'Fail'. If 'No', it leads to 'Perform standard test (Para. 3.6.1, condition A) See para. 3.1 through 3.10 50 to 300 rad/s', which can result in 'Pass' or 'Fail'. From 'Pass', it leads to 'Test at the intended application dose rate para. 3.6.3, condition C'. From 'Fail', it leads to 'Accelerated ELDRS test per para. 3.6.5, condition E Test conditions per characterization testing as described in 3.13.2 including overtest factors and parameter delta design margins.', which can result in 'Pass' or 'Fail'.](7c57192c514175021e4560a1a46126c1_img.jpg)

```

graph TD
    Start[Determine the need for ELDRS testing] -- Yes --> TestC[Test at the intended application dose rate  
para. 3.6.3, condition C]
    Start -- No --> TestA[Perform standard test  
(Para. 3.6.1, condition A)  
See para. 3.1 through 3.10  
50 to 300 rad/s]
    TestC -- Pass --> EndC[Pass]
    TestC -- Fail --> TestE[Accelerated ELDRS test per para. 3.6.5, condition E  
Test conditions per characterization testing as described in 3.13.2 including overtest factors and parameter delta design margins.]
    TestA -- Pass --> TestC
    TestA -- Fail --> TestE
    TestE -- Pass --> EndE[Pass]
    TestE -- Fail --> EndE[Fail]
  
```

Figure 7-4: A flowchart for ELDRS testing. It starts with a decision box 'Determine the need for ELDRS testing'. If 'Yes', it leads to 'Test at the intended application dose rate para. 3.6.3, condition C', which can result in 'Pass' or 'Fail'. If 'No', it leads to 'Perform standard test (Para. 3.6.1, condition A) See para. 3.1 through 3.10 50 to 300 rad/s', which can result in 'Pass' or 'Fail'. From 'Pass', it leads to 'Test at the intended application dose rate para. 3.6.3, condition C'. From 'Fail', it leads to 'Accelerated ELDRS test per para. 3.6.5, condition E Test conditions per characterization testing as described in 3.13.2 including overtest factors and parameter delta design margins.', which can result in 'Pass' or 'Fail'.

Figure 7-4. Linear and mixed-signal bipolar and BiCMOS TID RLAT flow from MIL-STD-883 TM 1019.<sup>[9]</sup> In the figure, "para" refers to the appropriate section in TM 1019. Image courtesy of Department of Defense.

There has been some debate about the appropriate dose rate for LDR testing. Is 0.01 rad/s low enough to detect ELDRS for applications where the dose rate was much lower? Early tests show that if a product does not have ELDRS at 0.01 rad/s, it will not exhibit ELDRS at even lower dose rates, such as 0.001 rad/s.<sup>[10]</sup>

When Texas Instruments performs an ELDRS characterization, units are irradiated at an LDR to the full TID rating. For instance, if a linear bipolar device is rated to 300 krad, then the ELDRS characterization will be done to 300 krad.<sup>[11,12]</sup> The LDR split takes over one year to reach 300 krad. Other suppliers will only provide LDR testing to 150 krad on linear bipolar products rated to 300 krad.<sup>[13]</sup>

#### RLAT for ELDRS-free products

If a product is ELDRS-free, then RLAT may be performed at HDR. Another alternative is to do RLAT at an LDR of 10 mrad/s. For most products, Texas Instruments will do RLAT at HDR. On marginal products that had a previous history of ELDRS, however, the company will continue to do RLAT at LDR on an individual wafer basis.

#### RLAT for products with ELDRS

Per TM 1019, if a product has ELDRS, RLAT should be performed at 10 mrad/s, but it should be irradiated to 1.5x the TID rating. This is a precaution in case the product exhibits even more sensitivity at dose rates lower than 10 mrad/s. If a product has ELDRS and is rated to 100 krad, it is necessary to irradiate it to 150 krad at 10 mrad/s, and the device must pass the 100-krad post-irradiation limits.

Texas Instruments strictly adheres to TM 1019 and uses this test method for RLAT on products with ELDRS.<sup>[14]</sup> Some suppliers rate products that have ELDRS at an HDR and then provide a second, lower rating for an LDR, but do not perform the 1.5x overtest that TM 1019 requires.<sup>[15]</sup>

#### Accelerated ELDRS tests

These tests simulate LDR performance on products that pass HDR testing and have linear, bipolar elements. Before using these tests for RLAT, it is first necessary to prove that the test correlates to LDR performance for a particular product.

Since testing to 100 krad at an LDR can take close to six months, there has been a quest to find an accelerated test to qualify devices for LDR environments in a reasonable length of time.

In 2003, a test was added to TM 1019 for bipolar and BiCMOS products where the units would be irradiated at 100°C at a dose rate between 0.5 rad/s and 5 rad/s. This test did not correlate to an LDR for all product types,<sup>[16]</sup> and the test option was removed in 2006. Other accelerated test methods have been proposed, such as testing at switched dose rates.<sup>[9]</sup> TM 1019 was modified so that any accelerated test method, including the elevated temperature test previously mentioned, may be used for RLAT if characterization shows that the method correlates to LDR performance.

Texas Instruments does not use any accelerated ELDRS tests, as none have been found to be consistently reliable.

#### Sample preparation before irradiation

TM 1019 does not have a requirement on how to package units for testing. As TID effects can be sensitive to assembly or packaging variations (see Chapter 6), packaging should be representative of the final product.

DUTs must go through burn-in prior to TID testing, unless it is demonstrated that burn-in does not change TID performance (see Chapter 6).

##### Sample size

In general, TM 1019 does not provide sample sizes, nor does it offer guidance on the number of DUTs to use for product qualification or RLAT. The sample-size requirements are either in MIL-STD-883 TM 5005<sup>[2]</sup> or MIL-PRF-38535, Appendix C.<sup>[1]</sup> At one time, these two documents listed different requirements, but they now agree. If there is a conflict between the two, Texas Instruments follows MIL-PRF-38535.

For qualification and RLAT of a wafer, the sample size is two units if the product has more than 4,000 transistors. For a product with less than 4,000 transistors, the sample size is four units. To qualify a whole wafer lot, the sample size is 22 units.

##### Bias during irradiation

During irradiation, the DUTs should be biased under the worst-case operating conditions that cause the most parametric drift. For CMOS products, that is the maximum operating voltage. For some bipolar products, an unbiased state could be the worst case.

Power products like regulators should have a light output-load current. A high output current will increase power consumption and self-heating of the DUT, resulting in annealing-out radiation damage.

#### Electrical test time window and dry ice

After a product is removed from the radiation source, the degradation due to the TID can change over time. For this reason, there is a time window during which the DUT must be electrically tested after its removal from the radiation source. The time window is based on the radiation rate and sometimes on the TID level. For LDR testing, the DUTs must be tested within 10% of the time it took to irradiate the units, up to a maximum of 72 hours.

For HDR testing, it is necessary to electrically test a DUT within one hour after its removal from the source. In many cases, there is no ATE conveniently located next to a radiation source to meet that one-hour time window. In such cases, the DUT can be placed in and stored on dry ice for up to 72 hours before starting the electrical test.

### MIL-STD-750 TM 1019

MIL-STD-750 covers the test methods for qualifying discrete transistors for military and space applications.<sup>[17]</sup> MIL-STD-750 TM 1019 is very similar to MIL-STD-883 TM 1019. Unlike MIL-STD-883 TM 1019, MIL-STD-750 does not require ELDRS characterization for bipolar transistors, but does require gain-degradation calculations after irradiation.

#### ESA ESCC Basic Specification No. 22900

The European Space Agency (ESA) publishes and maintains ESCC specifications. ESCC Basic Specification No. 22900 is the total dose steady-state irradiation test method.<sup>[16]</sup> The scope of this specification is for space applications only.

Testing is performed with a cobalt-60 source, but the option for using an electron source is still available. There is only one test flow for both qualification and RLAT (as shown in Figure 7-5) and it includes two options: testing dose rate and, if a previous evaluation determines that it is needed, the accelerated aging under bias test. The differences between MIL-STD-883 TM 1019 and ESA ESCC 22900 are shown in Table 7-3.

|                           | TM 1019                                                      | No. 22900                                     |
|---------------------------|--------------------------------------------------------------|-----------------------------------------------|
| Scope                     | Multiple environments                                        | Space only                                    |
| Test-flow options         | Options based on technology and radiation environment        | One test flow                                 |
| Room-temperature anneal   | Use on select products that fail an HDR for LDR environments | Done on all products as part of the test flow |
| ELDRS characterization    | On linear devices only with bipolar elements                 | On all devices with bipolar transistors       |
| ELDRS dose rate           | 10 mrad/s                                                    | 10 mrad/s to 100 mrad/s                       |
| HDR                       | 50 rad/s to 300 rad/s                                        | 0.1 rad/s to 50 rad/s                         |
| 1.5x overtest requirement | On products with ELDRS                                       | No                                            |

Table 7-3. Differences between MIL-STD-883 TM1019 and ESCC No. 22900.

#### ELDRS evaluation and dose-rate requirements

The requirement for ELDRS testing is different from MIL-STD-883 TM 1019, in that any product with a bipolar transistor must be evaluated, while TM 1019 only requires that products with linear bipolar elements be characterized for ELDRS.

For evaluation purposes, units are irradiated at two different dose levels that are at least two orders of magnitude apart. A device is considered to have ELDRS if the median LDR drift is greater than 1.5x the HDR drift. There are no other specific requirements (such as sample size) for this evaluation.

If a device has ELDRS, irradiation is done at an LDR. Otherwise, it can be done at an HDR. The ranges are:

- LDR range: 36 rad/hr to 360 rad/hr (0.01 rad/s to 0.1 rad/s).
- HDR range: 0.36 rad/hr to 180 krad/hr (0.1 rad/s to 50 rad/s).

#### Accelerated aging under bias test evaluation

The accelerated aging under bias test is the same test and is performed under the same conditions as the MAAT in TM 1019. Per the standard, an evaluation must be done on all technologies containing MOS elements to determine if they have TDEs. There are no guidelines on how to conduct this evaluation. If it is determined that a technology has TDEs, then the accelerated aging under bias test must be conducted as part of the test flow at qualification and RLAT for any products using that technology.

#### ASTM International

ASTM International provides standards over a wide range of topics. Nonmembers may have to pay a fee to access a standard.

![Flowchart of the ESA ESCC No. 22900 total dose steady-state irradiation test method, qualification and RLAT flow. The process starts with 'Serialize test samples', followed by 'Electrical test Room-temperature electrical measurements of the detail specification'. A decision diamond follows: 'Fail' leads to 'Replace part', and 'Pass' leads to 'For multiple exposures'. This is followed by 'Irradiation' (Specified dose rate to specified dose(s)), 'Electrical test', and another decision diamond. 'Fail' leads to 'Replace lot', and 'Pass' leads to 'Room-temperature anneal under bias' (24 hours), 'Electrical test', and a third decision diamond. 'Fail' leads to 'Replace lot', and 'Pass' leads to 'Accelerated aging under bias' (168 hours + 100 ±5°C), 'Electrical test', and a final decision diamond. 'Fail' leads to 'Replace lot', and 'Pass' leads to 'Accepted lot'.](e64106d52dee350a3439ff0d396d26fc_img.jpg)

```
graph TD
    A[Serialize test samples] --> B[Electrical test<br/>Room-temperature electrical measurements<br/>of the detail specification]
    B --> C{ }
    C -- Fail --> D[Replace part]
    C -- Pass --> E[For multiple exposures]
    E --> F[Irradiation<br/>Specified dose rate to specified dose(s)]
    F --> G[Electrical test]
    G --> H{ }
    H -- Fail --> I[Replace lot]
    H -- Pass --> J[Room-temperature anneal under bias<br/>24 hours]
    J --> K[Electrical test]
    K --> L{ }
    L -- Fail --> M[Replace lot]
    L -- Pass --> N[Accelerated aging under bias<br/>168 hours + 100 ±5°C]
    N --> O[Electrical test]
    O --> P{ }
    P -- Fail --> Q[Replace lot]
    P -- Pass --> R[Accepted lot]
```

Flowchart of the ESA ESCC No. 22900 total dose steady-state irradiation test method, qualification and RLAT flow. The process starts with 'Serialize test samples', followed by 'Electrical test Room-temperature electrical measurements of the detail specification'. A decision diamond follows: 'Fail' leads to 'Replace part', and 'Pass' leads to 'For multiple exposures'. This is followed by 'Irradiation' (Specified dose rate to specified dose(s)), 'Electrical test', and another decision diamond. 'Fail' leads to 'Replace lot', and 'Pass' leads to 'Room-temperature anneal under bias' (24 hours), 'Electrical test', and a third decision diamond. 'Fail' leads to 'Replace lot', and 'Pass' leads to 'Accelerated aging under bias' (168 hours + 100 ±5°C), 'Electrical test', and a final decision diamond. 'Fail' leads to 'Replace lot', and 'Pass' leads to 'Accepted lot'.

Figure 7-5. ESA ESCC No. 22900 total dose steady-state irradiation test method, qualification and RLAT flow. An earlier evaluation phase determines the dose rate and whether or not to perform the accelerated aging under bias test.<sup>[12]</sup> Image Courtesy of European Space Agency; Copyright © 2016

#### ASTM F 1892 standard guide

ASTM F 1892, Ionizing Radiation (Total Dose) Effects Testing of Semiconductor Devices, is a comprehensive guide for TID testing using any photon source (gamma rays from cobalt-60 or cesium-137, or X-rays).<sup>[19]</sup> The guide provides details about the physics of TID effects on electronics and explains why certain tests are performed. ASTM F 1892 recommends the same test flows as MIL-STD-883 TM 1019.

#### ASTM standard F 1467 standard guide

ASTM F 1467, Use of an X-ray tester ( $\approx 10$  keV Photons) in Ionizing Radiation Effects Testing of Semiconductor Devices and Microcircuits, provides specific guidelines to perform characterization and RLAT with X-ray systems.<sup>[20]</sup>

### TID test sources

#### Cobalt-60

Cobalt-60 is the most common radiation source used for total ionizing dose testing of electronic components. MIL-STD-883 TM 1019 and ESA ESCC No. 22900 specify cobalt-60, although No. 22900 still allows the use of electron beams.

There are two basic types of irradiators. [Figure 7-6](#) shows the first one, a self-contained unit where the DUT board is lowered down into a well surrounded by rods of cobalt-60. The volume of cobalt-60 and shielding inside the well determine the radiation rate, with the maximum radiation rate degrading with the half-life of cobalt-60 (5.2 years). These systems are mostly used for HDR testing.

![A photograph of a Gamma-cell 220 cobalt-60 irradiator. It is a large, white, cylindrical unit with a blue control panel on the left side. A laptop is connected to the unit, displaying a red image on its screen. The unit is situated in a laboratory setting with various equipment and cables visible in the background.](a52adf5edaaf32d82c7c2c57230599f9_img.jpg)

A photograph of a Gamma-cell 220 cobalt-60 irradiator. It is a large, white, cylindrical unit with a blue control panel on the left side. A laptop is connected to the unit, displaying a red image on its screen. The unit is situated in a laboratory setting with various equipment and cables visible in the background.

**Figure 7-6. Gamma-cell 220 cobalt-60 irradiator.**

The other type of irradiator is a room irradiator, where a cobalt-60 source in a shielded container stands in the center of a room. The DUT boards are placed around the room. When the DUTs are ready for irradiation, the source is raised up out of the container. The distance between the DUTs and the source determines the dose rate.

#### Cesium-137

Cesium-137 is another source that provides gamma rays through radioactive decay. Through decay, cesium-137 emits one photon with about half the energy of the photons emitted by cobalt-60. Because of the energy difference, there could be some correlation differences between the two sources.

#### X-rays

An X-ray source can be much more convenient for TID testing. There are no concerns for handling radioactive materials. Aracore, later known as Rapiscan, built a bench-top test system specifically designed for TID testing. The Aracore system has an advantage in that the X-ray can focus on a small area for characterizing sensitive areas. It can also test devices on a wafer without the need to package die.

These systems are no longer produced, but many still exist at universities and other research facilities. The challenge is finding a replacement when an X-ray tube burns out. MIL-PRF-38535 allows the use of X-rays for RLAT as long as the test is correlated to cobalt-60 testing.

#### Electrons and protons

Irradiation with protons or electrons is performed at a particle-accelerator facility.

#### Correlation between different radiation sources

In most cases, cobalt-60 is the standard radiation source for TID testing. Different TID sources do not necessarily correlate with each other, and correlation depends on technology.

#### Cobalt-60 vs. electron beams

Cobalt-60 testing may correlate with electron-beam testing on discrete transistors,<sup>[21]</sup> but is overly conservative for linear ICs.<sup>[22]</sup> According to reference<sup>[22]</sup>, testing with cobalt-60 results in parametric drift that is twice that of testing with an electron beam for the same TID level.

#### Cobalt-60 vs. X-rays

Because X-rays (typically 10 keV-100 keV) and cobalt-60 gamma rays (1.17 MeV or 1.33 MeV) have vastly different energies, the amount of degradation a product may experience from each source can be different for the same TID. It is necessary to account for different energy amounts deposited in the target material of interest. Procedures for calculations of dose-enhancement effects have been published in a number of papers<sup>[23-26]</sup> ASTM F 1467 also provides guidance for correlating gamma rays and X-rays.<sup>[20]</sup>

For most products, the degradation from gamma rays is worse than that from X-rays for the same TID.<sup>[23-26]</sup> However, there are some technologies, such as floating gates and subthreshold transistors, that are more sensitive to X-rays than gamma rays.<sup>[27]</sup>

### General considerations for TID testing

#### Units

See Chapter 3 for an in-depth discussion of units used for TID exposure.

For electronics in space or military applications, the absorbed dose is typically expressed in terms of rad(Si), where Si indicates silicon. The TID rating is usually expressed in terms of thousands of rad, or krad(Si).

In medical applications, TID is expressed in terms of grays (Gy). 1 Gy = 100 rad(Si).

#### Shielding and components

Packaging materials, boards or sockets generally do not shield TID sources. It is not necessary to open a package to directly expose a die to a TID source. Some sockets with thick aluminum lids provide some shielding and should be avoided.

When designing a bias board for TID testing, it is important not to use any components that are TID-sensitive, especially if the board will be reused. Passive components such as resistors and capacitors are not TID-sensitive, but active components such as power supplies can be.

#### Test time

A TID test at an HDR can be done in one day. For testing at an LDR of 10 mrad/s, it takes over five months of irradiation to reach 100 krad and over one year to reach 300 krad.

#### Worst-case test bias conditions vs. application

For TID testing, Texas Instruments irradiates products under the worst-case conditions causing the most amount of parametric drift. That way, testing covers all operating conditions of the product.

Most applications, however, do not use a product under worst-case conditions. It is possible that a product may survive a much higher TID level if operating under conditions different from the test conditions. For instance, the DAC121S101QML-SP, a CMOS product with a wide supply-voltage operating range, will survive a much higher TID level when operating at 3.3 V as opposed to the 5 V for which the device is tested.

Other considerations for the application are power-cycling of a device and dose-rate profiles. A CMOS product might survive a much higher TID if it is unpowered during irradiation. So whether or not the device is turned off for part of a mission is important. If parts of the mission include periods of HDR and LDR irradiation, the steady-state dose rate used in qualification may not predict what TID level the device will survive for products with dose-rate sensitivity.

## 7.2 Single-event effect testing

The purpose of SEE testing is to determine how a product might react when it is impacted by a single particle, such as a heavy ion or proton in space, a neutron on Earth, or an alpha particle from packaging materials. This discussion will focus on testing for space applications where high-energy protons and heavy ions are a concern, and on ICs. There are special considerations when testing other types of electronics, such as power FETs.

SEE testing is usually performed at an accelerator facility capable of producing high-energy heavy ions or protons. A DUT will be powered up and operated under normal conditions. A number of different parameters will be monitored during the testing, such as supply current and output status. The DUT will then be bombarded with heavy ions or protons, and any momentary changes in supply currents or output status will be recorded.

For space applications, how a device will perform under heavy-ion radiation is a major concern. If the device is sensitive enough to low-energy heavy ions, it might also be sensitive to high-energy protons. So qualification testing typically uses heavy ions or protons. For research purposes, there are other sources of radiation for injecting charge in a localized area, such as a pulsed laser.

SEE qualification is a one-time characterization and is usually not done as a lot acceptance test. A significant change to a product, such as a design and layout change or a process change, could impact the SEE response of a device and require a repeat of the SEE characterization. Products with an unknown manufacturing history may require a lot acceptance test.

### SEE test standards

Unlike TID testing, MIL-STD-883 does not have test methods for single-event testing. MIL-STD-750<sup>[27]</sup>, which covers discrete electronics, does include TM 1080 for single-event burnout (SEB) and gate-rupture (SEGR) testing of power MOSFETs.

For SEE testing, MIL-PRF-38535<sup>[1]</sup> refers to JESD57<sup>[28]</sup> and ASTM 1192.<sup>[29]</sup> JESD57 was updated in November 2017 and now provides comprehensive guidelines for testing.

### Heavy-ion testing

In heavy-ion testing, the DUT is placed in a beam of ions, and the functioning of the DUT is monitored in real time. The period when the ion beam starts hitting the DUT until the time when it stops is known as a beam run or ion run. An ion run usually consists of an ion of just one element and atomic mass. The number of ions that hit the DUT at one moment in time is known as the flux and is measured in terms of ions per square centimeters per second (ions/cm<sup>2</sup>-s). The total number of ions to hit the DUT during an ion run is known as the fluence and is measured in terms of total ions divided by area (ions/cm<sup>2</sup>).

#### Test facilities

Heavy-ion testing is done with a particle accelerator such as a cyclotron or Van de Graaf generator. Texas Instruments usually does testing at the cyclotrons housed at Lawrence Berkeley National Labs (LBNL)<sup>[30]</sup> or Texas A&M University (TAMU).<sup>[31]</sup> Both sites have facilities specifically set up to support SEE testing for electronics. There are other sites within the U.S.,<sup>[32]</sup> Europe<sup>[33]</sup> and worldwide. Each site has its pros and cons concerning SEE testing.

Facility rental ranges from \$600 to \$5,000 per hour, depending on the site. Part of the charge could include time for setting up the beam if it is not configured as required. Beam tuning can take up to four hours or more. A test campaign can range from four to 24 hours.

#### Ion penetration and sample preparation

In space, heavy ions can have enough energy to pass completely through a packaged IC and some level of shielding. At most test facilities, ions have only enough energy to penetrate 40  $\mu\text{m}$  to 400  $\mu\text{m}$  of silicon and cannot penetrate IC packaging. See [Figures 7-7](#) and [7-8](#) for examples of beam-penetration plots.

![Figure 7-7: Ion-penetration range in silicon at various ion energies at LBNL. This is a log-log plot showing the range in silicon (Si) in micrometers (μm) on the y-axis (ranging from 100 to 10,000) versus the linear energy transfer (LET) in MeV/cm²·mg on the x-axis (ranging from 0.1 to 100). Four data series are plotted for different ion energies: 30 MeV/U (red diamonds), 16 MeV/U (blue triangles), 10 MeV/U (green squares), and 4.5 MeV/U (cyan circles). The plot shows that as the ion energy increases, the penetration range in silicon also increases for a given LET.](d4c5f27c7e22291431b82257254ae14f_img.jpg)

Figure 7-7: Ion-penetration range in silicon at various ion energies at LBNL. This is a log-log plot showing the range in silicon (Si) in micrometers (μm) on the y-axis (ranging from 100 to 10,000) versus the linear energy transfer (LET) in MeV/cm²·mg on the x-axis (ranging from 0.1 to 100). Four data series are plotted for different ion energies: 30 MeV/U (red diamonds), 16 MeV/U (blue triangles), 10 MeV/U (green squares), and 4.5 MeV/U (cyan circles). The plot shows that as the ion energy increases, the penetration range in silicon also increases for a given LET.

**Figure 7-7. Ion-penetration range in silicon at various ion energies at LBNL.**<sup>[34]</sup>

It is necessary to open the package to expose the top of the die to the heavy-ion beam, which can be a challenge for some products such as flip-chips in which the die surface faces down. In this case, the back side of the die is exposed; the die is thinned enough for the ion beam to reach the front-side active area of the device.

Because of the limited penetration of the ions, there is usually no concern about the ions impacting the components on the test board, and extra shielding of the test board is not required.

The chosen ions should have enough penetration to reach through the sensitive depth of the product. The sensitive depth is the distance from the surface of the device to the point where charge injection will still cause an SEE. For a silicon-on-insulator product, the sensitive depth may only be 10  $\mu\text{m}$ , while a classic bipolar device might have a sensitive depth of 60  $\mu\text{m}$  to 100  $\mu\text{m}$ . See Chapter 6 for more details.

![Figure 7-8: Ion-penetration range of various ions at TAMU. This is a line graph showing the range in silicon (μm) on the x-axis (0 to 250) versus the linear energy transfer (LET) in MeV/cm²·mg on the y-axis (0 to 100). Several curves are plotted for different ions: 157Au, 181Ta, 152Ho, 111Pr, 159Gd, 116Kr, 155Cu, and 15Ar. A shaded blue region indicates the 'Bragg region'. Red diamonds on the curves represent data points 'After aramica window and 30 mm of air'. The curves show that heavier ions have a higher LET for a given range, and the Bragg peak occurs at the end of the ion's range.](39a8f00d10b50463cb1d9e79a8124a27_img.jpg)

Figure 7-8: Ion-penetration range of various ions at TAMU. This is a line graph showing the range in silicon (μm) on the x-axis (0 to 250) versus the linear energy transfer (LET) in MeV/cm²·mg on the y-axis (0 to 100). Several curves are plotted for different ions: 157Au, 181Ta, 152Ho, 111Pr, 159Gd, 116Kr, 155Cu, and 15Ar. A shaded blue region indicates the 'Bragg region'. Red diamonds on the curves represent data points 'After aramica window and 30 mm of air'. The curves show that heavier ions have a higher LET for a given range, and the Bragg peak occurs at the end of the ion's range.

**Figure 7-8. Ion-penetration range of various ions at TAMU.**<sup>[34]</sup> SEE testing most commonly uses the 15-MeV beam. Image courtesy of Cyclotron Institute, TAMU<sup>[35]</sup>

The Bragg peak is where the ion deposits the most energy and is near the end of the penetration range, as shown in [Figure 7-8](#). For most ICs, the depth of the Bragg peak into the device is not critical, as long as the penetration is past the sensitive volume. For some devices like MOSFETs, the location of the Bragg peak is critical, because the worst-case scenario occurs when the Bragg peak is at an interface or junction.<sup>[36]</sup>

Some heavy-ion facilities have energy high enough for the ion to pass through a device's packaging. This creates new challenges, such as determining how much energy is actually deposited in the sensitive area of the device<sup>[37]</sup> and board shielding.

#### LET and incident angle

Linear energy transfer (LET) is the amount of energy the ion deposits in silicon per distance. The units are megaelectron-volts multiplied by the distance divided by density ( $\text{MeV}\cdot\text{cm}^2/\text{mg}$ ). LET depends on the ion and energy of the ion beam which is measured in megaelectron-volts per nucleon or ion ( $\text{MeV}/\text{nuc}$ ). For a particular beam energy, ions of different elements will have different LETs. See Chapter 4 for more details.

LET will have an impact on the probability of an SEE. The higher the LET, the more carriers generated in the silicon, increasing the chance that the carriers will be swept up in the electric field, causing a measurable effect. See Chapter 4 for more details.

LET is measured for an ion hitting the surface of the die at a right-angle trajectory (or a zero-degree incident angle). For most ICs, the effective LET ( $\text{LET}_{\text{eff}}$ ) can be increased by increasing the incident angle of the beam. The  $\text{LET}_{\text{eff}}$  is calculated by dividing the LET by the cosine of the incident angle.

It is important to understand the architecture of the device to know whether testing at an angle will result in a valid  $\text{LET}_{\text{eff}}$ . For newer, deep-submicron devices, if the beam is at an angle, an ion might strike more than one transistor, causing multiple-bit upsets.<sup>[38]</sup> The probability of an upset could then be overstated. For devices with a deep sensitive volume, an ion at an angle might not reach the depth of the sensitive volume before passing completely through it, understating the probability of an SEE.<sup>[38, 39]</sup>

#### Single-event latch-up

Single-event latch-up (SEL) testing should be performed at the maximum operating voltage and junction temperature, as these are the worst-case conditions.<sup>[28,29]</sup>

In SEL testing, the supply current to the DUT is monitored. If the supply current jumps up and stays at this higher state until the DUT is power-cycled, this is most likely due to SEL. However, there are other effects that might cause the current to jump, such as a single-event functional interrupt (SEFI) where a setup register is upset, causing the device to go into a different state. In such cases, the current may jump high for a period of time, but then jump low as another ion strike causes it to go into another state. One way to differentiate between SEL and a SEFI is to either read back the registers to determine whether they have changed or rewrite the registers to see if the supply currents return to their pre-irradiation values.

Some experimenters will use a current limit on the voltage supplies to prevent a DUT from being destroyed in case SEL causes the DUT to draw too much current. In some cases, the power supply will automatically shut down when the current limit is reached. Exercise caution when using current limits in order to ensure that the SEE is not misdiagnosed. Just because the current hits the limit does not mean that there was SEL. As explained above, the current increase could be from the part going into a different state due to a SEFI. In the case of a regulator, the rise in current could be due to a positive-going output transient where the increase in output voltage will increase the output current, which in turn will momentarily increase the input current.

Many newer, complex ICs may experience micro latch-ups where their current only increases by a small amount. This may be because the internal power supply to the area that latches up can only provide a small amount of excess current or that the circuit that latched up is so small that it will limit the current. If the DUT is left under the beam after detection of the first SEL, more SELs will occur and the current will increase in small steps. Although this condition may not be immediately destructive, the micro SELs could impact the life of the device as the latched circuit may be drawing more current than for which it was designed.

#### Single-event functional interrupt

The worst-case condition for a SEFI is at the lowest operating voltage. No external heat is applied to the DUT during SEFI testing.

The functioning of the DUT is monitored to spot any possible changes induced by an ion strike. For products that have programmable registers with a read option, it is possible to read the registers before and after an ion run and compare them. Another option is to reload the registers without resetting or powering down the DUT to see if it returns to its expected state. For some products, a SEFI might be detected as the device going into a reset mode, such as a power-on reset.

#### Single-event transient

In some publications, single-event transients (SETs) may be referred to as single-event upsets (SEUs). Typically, transients are monitored with an oscilloscope on the output of the DUT. [Figure 7-10](#) shows examples of SETs captured by an oscilloscope.

![Figure 7-10: Two oscilloscope plots showing Reference voltage (V) vs Time (μs). The top plot shows a transient spike reaching approximately 2.8V. The bottom plot shows a transient spike reaching approximately 3.2V. Both plots show a noisy baseline around 2.5V.](609dff0a56be2ded8c960a3672afa937_img.jpg)

Figure 7-10: Two oscilloscope plots showing Reference voltage (V) vs Time (μs). The top plot shows a transient spike reaching approximately 2.8V. The bottom plot shows a transient spike reaching approximately 3.2V. Both plots show a noisy baseline around 2.5V.

Figure 7-10. Examples of SETs captured on the LM4050WG2.5-RLQV 2.5-V precision reference.<sup>[40]</sup>

Of interest is the amplitude and duration of the transients, which can be plotted out as shown in [Figure 7-11](#).

![Figure 7-11: A scatter plot showing Error amplitude (V) vs Time (μs). The plot displays data points for various ions: Xenon (58.78), Silver (48.13), Krypton (30.86), Copper (21.17), Argon (9.74), Neon (3.49), and Oxygen (2.19). The error amplitude ranges from -2.0V to 2.0V, and time ranges from 0 to 8 μs. The data points are clustered around zero, with some outliers showing larger transients.](5be24416de2bdec797676920c84b9ca0_img.jpg)

Figure 7-11: A scatter plot showing Error amplitude (V) vs Time (μs). The plot displays data points for various ions: Xenon (58.78), Silver (48.13), Krypton (30.86), Copper (21.17), Argon (9.74), Neon (3.49), and Oxygen (2.19). The error amplitude ranges from -2.0V to 2.0V, and time ranges from 0 to 8 μs. The data points are clustered around zero, with some outliers showing larger transients.

Figure 7-11. SET amplitude vs. pulse width for the LM4050 2.5-V precision reference.<sup>[40]</sup> The transient amplitude is how much the voltage varies from the nominal value. The legend shows different ions used, arranged in order of highest to lowest LET.

For an analog device with a wide operating range, SET response highly depends on operating conditions.<sup>[41,42]</sup> It may be necessary to test a device under different operating conditions – or at least in the exact conditions of operation for the application of interest. Choosing the proper operating conditions may eliminate or reduce SETs, and it may be necessary to characterize the device under different conditions to find the optimal one.<sup>[43]</sup>

The SET response can be unpredictable. In the case of the DAC121S101QML-SP, long negative-going SETs were not detected when the device operated at midrange, but were observed when the output was near the high and low supply rails, as shown in [Figure 7-12](#).

![Figure 7-12: Three scatter plots showing SETs of the DAC121S101 digital-to-analog converter at different output voltages. Each plot shows Amplitude (V) on the y-axis (from -1 to 2) versus Pulse width (ns) on the x-axis (from 0 to 5000). A red oval highlights a cluster of points near the origin. The legend indicates various materials: Si, Ta, Ti, Nb, Cu, Au, and Ni.](b8dc609f35d8251ff4e4ea111a9943bd_img.jpg)

**15% of full scale**  
Input code = 614  
Output = 0.46 V

**50% of full scale**  
Input code = 2048  
Output = 1.42 V

**85% of full scale**  
Input code = 3482  
Output = 2.37 V

Figure 7-12: Three scatter plots showing SETs of the DAC121S101 digital-to-analog converter at different output voltages. Each plot shows Amplitude (V) on the y-axis (from -1 to 2) versus Pulse width (ns) on the x-axis (from 0 to 5000). A red oval highlights a cluster of points near the origin. The legend indicates various materials: Si, Ta, Ti, Nb, Cu, Au, and Ni.

**Figure 7-12.** SETs of the DAC121S101 digital-to-analog converter at different output voltages.<sup>[42]</sup>

Although on many products the lowest operating supply voltage is the worst case, for the DAC121S101 the highest operating voltage was the worst case, resulting in a higher probability of an SET, as shown in [Figure 7-13](#).<sup>[42]</sup>

![Figure 7-13: Scatter plot showing SET cross-section (cm²) on the y-axis (from 0 to 2.0 x 10⁻⁴) versus LET (MeV·cm²/mg) on the x-axis (from 0 to 120). Two data series are shown: 5.5 V Supply voltage (red triangles) and 2.7 V Supply voltage (blue squares). The 5.5 V series shows higher cross-section values across the LET range.](78abd5ce8ac2558a660ee05672c1a016_img.jpg)

Figure 7-13: Scatter plot showing SET cross-section (cm²) on the y-axis (from 0 to 2.0 x 10⁻⁴) versus LET (MeV·cm²/mg) on the x-axis (from 0 to 120). Two data series are shown: 5.5 V Supply voltage (red triangles) and 2.7 V Supply voltage (blue squares). The 5.5 V series shows higher cross-section values across the LET range.

**Figure 7-13.** SET cross-section vs. LET of the DAC121S101 digital-to-analog converter with two different supply voltages.<sup>[42]</sup> The higher the cross-section, the higher the probability of an SET.

#### Single-event upset

For digital devices, the lowest operating supply voltage is the worst-case condition. Detecting and capturing an SEU can sometimes be a challenge. It may be necessary to use special test equipment during heavy-ion testing to monitor the digital outputs.

For capturing output code errors of ultra-high-speed analog-to-digital converters (ADCs) while running high-frequency inputs such as the ADC08D1520QML-SP or ADC12D1600QML-SP, National Semiconductor (before its acquisition by Texas Instruments) developed a special test that uses a beat frequency and code error-detection software, as shown in [Figure 7-14](#).<sup>[44-46]</sup>

![Figure 7-14: Waveform diagram showing a beat frequency. The top trace is a red sine wave labeled 'Clock'. The middle trace is a blue sine wave labeled 'Input'. The bottom trace is a green square wave labeled 'Sampled', which is a sampled version of the input signal.](b800051c57e75b44155683ea69ed4227_img.jpg)

Figure 7-14: Waveform diagram showing a beat frequency. The top trace is a red sine wave labeled 'Clock'. The middle trace is a blue sine wave labeled 'Input'. The bottom trace is a green square wave labeled 'Sampled', which is a sampled version of the input signal.

**Figure 7-14.** Beat frequency. On an ADC, with the sample rate at 1 GSPS and the input frequency slightly lower at 998.76 MHz, the sampled points on the input curve will result in an output of 1.24 MHz.<sup>[44]</sup>

#### Single-event gate rupture and SEB

MIL-STD-750 TM 1080 covers the procedures for single-event gate rupture (SEGR) and SEB testing of discrete transistors.<sup>[17]</sup>

[Figure 7-15](#) shows the circuits used for testing.

![Figure 7-15: Test circuits for SEGR and SEB. The top circuit shows a DUT with gate voltage V_GS and drain voltage V_DS, with gate current I_G and drain current I_D. The bottom circuit is similar but includes a current probe on the drain line.](3481cde1adf61b0452dd6489dada6d6a_img.jpg)

Figure 7-15: Test circuits for SEGR and SEB. The top circuit shows a DUT with gate voltage V\_GS and drain voltage V\_DS, with gate current I\_G and drain current I\_D. The bottom circuit is similar but includes a current probe on the drain line.

Figure 7-15. Test circuits for SEGR and SEB.<sup>[47]</sup>

Image courtesy of Department of Defense

In a fully integrated power circuit such as a switching regulator, it is usually not possible to isolate the power FETs. SEGR and SEB tests run with the device operating under normal conditions.

When testing for SEGR and SEB, it may be necessary to test at various input voltages and load currents to determine the failure thresholds and locate the device's safe operating area (SOA).

Figure 7-16 shows the SOA for Texas Instruments' TPS50601-SP point-of-load switching regulator.<sup>[47]</sup> With the SOA specified, it is not necessary to derate the operating voltage as would be done on a commercial grade product.

Using incident angles for  $LET_{eff}$  is not valid for SEGR and SEB testing. A standard N-type MOSFET should be tested with a zero-degree incident angle. For DMOS structures, it may be necessary to test at various angles given their complex structures.

![Figure 7-16: SOA of the TPS50601-SP point-of-load switching regulator. The graph plots Input voltage V_in (Voltage) from 0.0 to 8.0 against Maximum load (amperes) from 0 to 7. It shows three regions: SOA (LET ≤ 56.7), SOA (LET ≤ 65.4), and Safe (LET ≤ 94.0). Data points for different LET values are plotted.](a0b992c3c544896bb2567bf22e532bd1_img.jpg)

| Maximum load (amperes) | V <sub>in</sub> (V) for LET ≤ 56.7 | V <sub>in</sub> (V) for LET ≤ 65.4 | V <sub>in</sub> (V) for LET ≤ 94.0 |
|------------------------|------------------------------------|------------------------------------|------------------------------------|
| 1                      | 7.5                                | 7.5                                | 7.5                                |
| 2                      | 7.5                                | 7.5                                | 7.5                                |
| 3                      | 7.5                                | 7.5                                | 7.5                                |
| 4                      | 6.5                                | 6.5                                | 6.5                                |
| 5                      | 6.0                                | 6.0                                | 6.0                                |
| 6                      | 5.5                                | 5.5                                | 5.5                                |

Figure 7-16: SOA of the TPS50601-SP point-of-load switching regulator. The graph plots Input voltage V\_in (Voltage) from 0.0 to 8.0 against Maximum load (amperes) from 0 to 7. It shows three regions: SOA (LET ≤ 56.7), SOA (LET ≤ 65.4), and Safe (LET ≤ 94.0). Data points for different LET values are plotted.

Figure 7-16. SOA of the TPS50601-SP point-of-load switching regulator.<sup>[47]</sup>

#### SEE test setup and equipment

During an ion run, the operating DUT is monitored. For a simple device like an amplifier, it is possible to use a simple breakout board. For more complex devices, it might be possible to use (and modify if necessary) an evaluation board from the IC manufacturer. Some heavy ion test facilities, the DUT will need to be decapped to expose the die to the beam. Usually, special shielding is not required for the other components on the board.

If SEL testing is to be done, any onboard power supplies to the DUT will need to be bypassed so that the supply voltage can come from a remote source that can be monitored. It will be necessary to heat the DUT to the maximum operating temperature and confirm the junction temperature. Attaching a resistive heater to the board or using a heat gun (when not performing testing in a vacuum chamber) are common ways to heat the board. A thermistor can monitor the board temperature and an infrared gauge can measure the die temperature and correlate it to the thermistor reading. Some products have an onboard temperature diode that can be used to monitor the DUT junction temperature.

Figure 7-17 shows two examples of SEE test boards.

![Figure 7-17 (top): A board used for testing the ADC08D1520QML-SP analog-to-digital converter. It shows a Texas Instruments evaluation board with a DUT in the center, flanked by resistive heaters and a thermistor.](0de16646045ff55473ebfd2f1675da17_img.jpg)

Figure 7-17 (top): A board used for testing the ADC08D1520QML-SP analog-to-digital converter. It shows a Texas Instruments evaluation board with a DUT in the center, flanked by resistive heaters and a thermistor.

![Figure 7-17 (bottom): The setup for testing the LM98640QML-SP analog front end for charge-coupled device (CCD) and CMOS imaging applications. It shows a daughterboard connected to a WaveVision 5 data-capture board, with a thermistor and a resistive heater attached to the DUT.](f3c17bd8b02c6af70db08fba7baa84aa_img.jpg)

Figure 7-17 (bottom): The setup for testing the LM98640QML-SP analog front end for charge-coupled device (CCD) and CMOS imaging applications. It shows a daughterboard connected to a WaveVision 5 data-capture board, with a thermistor and a resistive heater attached to the DUT.

Figure 7-17. A board used for testing the ADC08D1520QML-SP analog-to-digital converter using Texas Instruments' 081000 evaluation board (top).<sup>[48]</sup> Resistive heaters are attached to the front side of the board to heat the DUT for SEL testing. The DUT is in between the heaters and has been chemically decapped to expose the surface of the die directly to the ion beam.

The setup for testing the LM98640QML-SP analog front end for charge-coupled device (CCD) and CMOS imaging applications, using a LM98640CVAL evaluation daughterboard connected to a WaveVision 5 data-capture board (bottom).<sup>[48]</sup> The thermistor is attached to the front side of the board next to the DUT. The lid is taped on for protection during handling but removed during testing. The resistive heater is attached to the underside of the board directly under the DUT.

The DUT board is irradiated with heavy ions in a “cave,” which is a remote room with shielding to protect against possible radiation exposure. At LBNL and TAMU, the control room is above the cave. A 25-foot cable is required to reach between the DUT board and the equipment in the control room. Any real-time control and monitoring of the DUT boards will need to be done remotely through 25-foot cables. There needs to be awareness of voltage drops through these long cables. The facilities are noisy environments and the long cables can act as antennas, picking up stray noise. Care must be taken to ensure the integrity of the signals, especially when working with high-speed signals.

At LBNL and many other facilities worldwide, the DUT board is inside a vacuum chamber. Getting clean signals through the vacuum chamber walls constitutes additional challenges.

#### SEE probability, cross-section and Weibull curve

A cross-section in this context is a measure of the probability of an SEE occurring and is expressed in terms of area cm<sup>2</sup>. It is calculated by dividing the total number of SEEs detected by the fluence. A lower cross-section indicates a lower probability of an SEE. A common practice is to plot the cross-section versus the LET<sub>eff</sub> of the ions used, as shown in [Figure 7-18](#).

In order to calculate error-rate predictions in orbit, the data is fitted to a Weibull curve<sup>[30]</sup>, see [Equation 7-1](#). It is then possible to use the fit parameters in different models based on the radiation environment of a mission, such as CREME96.<sup>[51]</sup>

$$F(L) = A \left( 1 - \exp \left\{ - \left[ \frac{L - L_0}{W} \right]^s \right\} \right); L > L_0$$

$$F(L) = 0; L < L_0$$

Equation 7-1.

Where:

**F(L)** is the event cross-section for a particular LET

**A** is the saturated cross section (where the cross-section curve flattens out)

**W** is the width of the distribution

**L<sub>0</sub>** is the threshold LET or onset LET, the lowest LET were SEEs are seen

**s** is the shape parameter

Parameters **A** and **L<sub>0</sub>** are known from the test results. **W** and **s** are adjusted to make the curve fit the data.

![Figure 7-18: A log-linear plot showing Cross section (cm²) on the y-axis (log scale from 1.E-07 to 1.E-03) versus LET (MeV-cm²/mg) on the x-axis (linear scale from 0 to 120). Red squares represent 'Average per channel' data points, and a blue line represents the 'Weibull fit'. The data points show a sharp increase in cross-section at low LET values, followed by a plateau around 1.E-04 cm² for LET values above 40 MeV-cm²/mg.](c46ee1a06d481330a99b781adacee939_img.jpg)

Figure 7-18: A log-linear plot showing Cross section (cm²) on the y-axis (log scale from 1.E-07 to 1.E-03) versus LET (MeV-cm²/mg) on the x-axis (linear scale from 0 to 120). Red squares represent 'Average per channel' data points, and a blue line represents the 'Weibull fit'. The data points show a sharp increase in cross-section at low LET values, followed by a plateau around 1.E-04 cm² for LET values above 40 MeV-cm²/mg.

Figure 7-18. Cross-section vs. LET<sub>eff</sub> curve of output errors for the LM98640QML-SP analog front end for CCD and CMOS imagers.<sup>[49]</sup>

The parameters used for the Weibull curve are in [Table 7-4](#).<sup>[50]</sup>

| A                       | Lo | W  | s   |
|-------------------------|----|----|-----|
| 5.88 x 10 <sup>-4</sup> | 0  | 35 | 1.8 |

Table 7-4. Weibull fit parameters for the LM98640 output SEUs exhibited in Figure 7-19.<sup>[49]</sup>

The Weibull fit parameters can also be used to describe a products relative SEE sensitivity using a figure of merit calculation.<sup>[50]</sup>

[Equation 7-2](#) shows the figure-of-merit calculation for a 30-day period:

$$FOM = 30 \times 200 \times \frac{\sigma_{\text{limit}}}{L_{0.25}^2}$$

Equation 7-2.

where  $\sigma_{\text{limit}}$  is the saturated cross-section and  $L_{0.25}^2$  is the LET at 25% of the saturated cross-section.

#### Amount of data collection and fluence limits

Typically, testing at each LET is done until 100 events are counted or the fluence reaches 10<sup>7</sup> ions/cm<sup>2</sup>, whichever comes first. At 100 events, the level of uncertainty is approximately 0.1%.<sup>[52]</sup> A fluence of 10<sup>7</sup> ions/cm<sup>2</sup> is sufficient for most environments to ensure that an event will not occur.<sup>[29]</sup>

In practicality, it may not be possible to collect 100 events. For an effect such as SEL or a SEFI, resetting the device after each event can be time-consuming, and collecting 100 events may take more time than allotted at the facility. If the effect is destructive, each event might require a new DUT.

Heavy ions are ionizing radiation, and testing will also cause TID effects. For a device that is relatively TID-soft, SEE testing to high fluences could cause the DUT to degrade, changing the SEE response. It is necessary to record the fluence of every ion run and to monitor the TID accumulation. Test method JESD57<sup>[27]</sup> and standard guide ASTM F1892<sup>[28]</sup> provide formulas for calculating TID based on LET and fluence.

### Proton single-event testing

If a device exhibits SEEs with low-LET heavy ions, it may also exhibit SEEs when irradiated by high-energy protons. What the LET threshold is and where proton testing needs to occur are up for debate. That threshold is typically between 14-37 MeV-cm<sup>2</sup>/mg.<sup>[53, 54]</sup> Just because a device does have SEEs at a low threshold LET (LET<sub>th</sub>) does not mean that the device will have SEEs with protons. Texas Instruments’ ADC08D152QML-SP had SEUs under heavy-ion testing down to a LET of 5.8 MeV-cm<sup>2</sup>/mg, but did not exhibit any LET when tested with 200-MeV protons.<sup>[55]</sup>

#### Proton test standard

JESD234<sup>[66]</sup> is the test standard for proton SEE testing with proton energies ranging from 40 MeV to 500 MeV. On newer deep-submicron processes, there have been issues with low-energy protons (<5 MeV) causing SEUs from the secondaries when protons strike high Z metals such as tungsten in the metal stack. There are currently no standards covering that type of testing.

#### Proton test facilities

Proton testing is performed at a particle accelerator such as a cyclotron, linear accelerator or synchrotron. Some of these sites are medical treatment facilities that have a setup for SEE testing, but others are pure research centers. A number of facilities in the U.S. are set up to perform SEE testing with medium-energy protons. There is an ongoing effort to find facilities to support SEE testing with higher proton energies (>100 MeV).<sup>[67]</sup>

#### Proton SEE test procedures

Proton SEE testing is very similar to heavy-ion testing, and it may be possible to use the same setups, with some modifications.

Unlike heavy ions, protons will pass through a packaged device, so there is no need to decap a DUT. Radiation of the components on the DUT board becomes an issue; therefore, it will be necessary to shield any components that are soft to protons.

Another concern is that when high-energy protons strike, secondary neutrons are created. Secondary neutrons are omnidirectional and can strike anywhere in the cave. It is necessary to shield against these as well. Because any test equipment inside the cave is at risk, it should be well-shielded or placed outside the cave.

Testing is typically done at a single proton energy to a total fluence of  $10^{10}$  to  $10^{12}$  p/cm<sup>2</sup>. Fluences this high could result in displacement damage or TID effects on some devices. For nondestructive testing, proton energies of 200 MeV may be sufficient, but higher energies may be required to detect destructive effects.<sup>[68]</sup>

#### SEE testing with lasers and other systems

It is possible to simulate heavy-ion and proton SEEs by injecting charge into the bulk of a device through other means. One method is to use a laser.<sup>[69]</sup> Single-photon laser systems tend to inject charge at the silicon surface. Two-photon absorption (TPA) systems can inject charge at various depths.<sup>[69]</sup>

Performing an SEE characterization with a laser system presents many advantages:

- There is no need to use a special facility.
- A test apparatus can be set up at almost any lab.
- There are systems on the market designed specifically for SEE testing.
- There are no radiation concerns.
- There is no need for complex systems to remotely control and monitor the DUT.

The most important advantage of laser systems is that it is possible to use a small beam size and accurately aim it at a specific section of a circuit. This feature is very useful for pinpointing the location of a circuit that is responsible for an SEE, such as SEL.<sup>[68]</sup>

The laser cannot penetrate metal layers. If a device has large metal sheets with few openings down to the silicon, it is not possible to do laser testing from the front side of the DUT. In these cases, a TPA system can be used on the back side of the die, if it is possible to expose and thin the back side of the die.

Currently, there is little correlation between a heavy-ion LET and laser energy, so it is not possible to use lasers for creating cross-section curves or establishing the probability of an SEE on a mission. Although laser testing may be able to determine whether a device is SEL-immune, it will likely be necessary to verify through heavy-ion testing.

Besides lasers, other sources are being investigated for heavy-ion characterization, such as high-energy X-rays.<sup>[69]</sup>

### 7.3 Displacement damage dose testing – neutron testing

The purpose of DDD testing is to determine whether silicon lattice damage from proton irradiation will degrade the performance of a device. Besides their ability to damage the silicon lattice, protons are also an ionizing radiation source. If performing DDD testing with protons, there could be two competing factors: displacement damage and TID irradiation. To keep the two effects separate, DDD testing is done with neutrons and TID testing is done with cobalt-60 gamma rays. Neutrons are a nonionizing energy loss (NIEL) radiation source.

#### Test standard

The test standard for displacement damage testing with neutrons is MIL-STD-883 TM 1017.<sup>[7]</sup> Here is the basic test flow:

- Assemble the DUTs in packages and electrically test with ATE.
- Irradiate the DUTs with neutrons in an unbiased state to a specified fluence (between  $10^{10}$  to  $10^{12}$  n/cm<sup>2</sup>).
- Retest the DUTs on the ATE.

#### Data analysis

Comparing pre- and post-irradiation data determines the amount of degradation. Sometimes, TID testing with gamma rays or X-rays will follow to determine the cumulative effect of displacement damage and TID.

### 7.4 Dose-rate or prompt-dose testing

Dose-rate testing determines how a device will respond to a sudden flash of ionizing radiation, such as one that occurs with nuclear detonation. It is also known as prompt-dose testing.

Irradiation is done with a flash X-ray, but it is also possible to use an electron beam from a linear accelerator. The dose rates used range from  $10^7$  to  $10^{12}$  rad/s.

Dose-rate testing is not to be confused with high dose rate (HDR) TID testing. The dose rate for “dose rate testing” is many orders of magnitude higher than for HDR TID testing.

### Dose-rate test standards

The MIL-STD-883 for dose rate test methods are:

- TM1020, Dose-rate induced latchup test procedure.
- TM1021, Dose-rate upset testing of digital microcircuits.
- TM1023, Dose-rate response of linear microcircuits.

### Dose-rate test setup and method

The setup and procedure for dose-rate testing is very similar to that for heavy-ion and proton SEE testing. Because the radiation sources used for dose-rate testing can pass through IC package materials, the DUT does not need to be decapped, but it is necessary to take the same DUT board-shielding precautions used in proton testing.

The DUT is operational and monitored while being flashed with very high-dose-rate radiation. Any anomalies in the operation of the device, such as latch-up, burnout and output transients, are recorded during each flash.

Unlike SEE testing, where a single ion impacts a small portion of the DUT at a time, in dose-rate testing the whole DUT is flashed at once. A number of different effects, like transients and upsets, might occur at the same time, depending on the product.

Typically, a program that specifies dose-rate testing requires that the testing occur under the exact operating conditions used in the program.

### 7.5 Terrestrial neutron and alpha-particle testing

Natural radiation sources on Earth such as alpha particles in IC packaging or atmospheric neutrons can impact commercial products. See Chapter 1 for more details.

### Test standards

JEDEC test standards JESD89A, JESD89-1A, JESD89-2A and JESD89-3A cover testing for soft errors from alpha rays and terrestrial cosmic radiation.<sup>[61]</sup>

MIL-STD-883 TM 1032 is the military and space standard for testing for soft errors due to packaging or die coatings.<sup>[62]</sup>

## 7.6 Texas Instruments' radiation test philosophy

Texas Instruments has provided space-grade and radiation-qualified products for more than four decades. Texas Instruments in this context includes its acquisitions of National Semiconductor and Uniretro, which have also supplied space- and radiation-qualified products for decades.

Texas Instruments provides a wide range of space products, including microcontrollers, amplifiers, comparators, data converters, interface and power management. Most of the company's space-grade products are RHA, where every lot goes through TID qualification and RLAT.

In addition to TID test results, Texas Instruments also supplies SEE test data on new products as they are released, to aid customers in quick product selection and design-in. The type of testing that Texas Instruments does depends on the technology and history of the product.

Texas Instruments does not perform radiation testing or have radiation test data on commercial-grade products. Because process, design and layout have an impact on radiation response, it is difficult to predict how each commercial device will perform under radiation without testing it.

### TID RLAT

For RHA qualification and RLAT, Texas Instruments strictly follows MIL-PRF-38535<sup>[1]</sup> and MIL-STD-883 TM 1019.<sup>[2]</sup> Because the company offers a wide variety of products using different semiconductor technologies, they do not have one simple TID test flow, instead performing different TID tests as required for silicon technology and radiation environments.

For CMOS technologies, the company performs a MAAT on the first lot tested to verify that there are no TDEs. Most CMOS products are tested and qualified at an HDR, as this is the worst case. Some CMOS products receive the room-temperature anneal test as required by the test results.

New bipolar products receive the ELDRS characterization. For bipolar devices shown to be ELDRS-free, RLAT may be done at an HDR, but the company still performs RLAT at an LDR on every wafer of classic bipolar products where ELDRS was first identified. For products that have been shown to have ELDRS, RLAT is always done at an LDR with a 1.5x overtest.

Texas Instruments owns a gamma cell for HDR testing (see [Figure 7-19](#)). For LDR testing, the company has units irradiated at facilities with a Defense Logistics Agency lab suitability certification. Most products are electrically tested at Texas Instruments on the ATE, with test coverage on all data-sheet and SMD parameters.

![A photograph of the Texas Instruments TID test facility. It features a large, cylindrical gamma cell with a 'Caesium-137 220 Ci' label, mounted on a wooden stand. To the left, a laptop sits on a desk next to a rack of electronic test equipment. The background shows a laboratory setting with various cables and equipment.](834527772ec0231b3bd34ed25da9a382_img.jpg)

A photograph of the Texas Instruments TID test facility. It features a large, cylindrical gamma cell with a 'Caesium-137 220 Ci' label, mounted on a wooden stand. To the left, a laptop sits on a desk next to a rack of electronic test equipment. The background shows a laboratory setting with various cables and equipment.

Figure 7-19. Texas Instruments TID test facility.

#### RLAT sample size

For RLAT, the sample size is either 22 units for a wafer lot or two to six units for a single wafer. Depending on the product, Texas Instruments will do either a whole wafer RLAT or a single-wafer RLAT. For small wafer-lot sizes, the company may do RLAT on each individual wafer. Also, on classic bipolar devices where there has been a history of ELDRS and lot-to-lot variation, Texas Instruments still currently tests and qualifies each individual wafer.

The RLAT procedure (wafer level or wafer lot level) is available in the TID reports that Texas Instruments provides for each lot.

#### RLAT dose rate on ELDRS-free bipolar linear products

MIL-STD-883 TM 1019 requires running a one-time ELDRS characterization on bipolar linear products. If the product does not have ELDRS, RLAT may be performed at an HDR of 50 rad/s to 300 rad/s. These products then qualify at the rated dose for both LDR and HDR.

For many bipolar products, Texas Instruments still offers the option where each wafer is tested and qualified at an LDR (10 mrad/s). On most of these products, there is the option of performing RLAT at either an LDR or an HDR. HDR- and LDR-qualified products will have different device numbers and SMD numbers.

For example, the LM124AQMLV-SP device numbers in a gull-wing package are:

|                        |                |                          |
|------------------------|----------------|--------------------------|
| HDR (50 to 300 rad/s): | LM124AWGRQMLV  | 5962R995040 <b>1</b> VZA |
| LDR (0.01 rad/s):      | LM124AWGRLQMLV | 5962R995040 <b>2</b> VZA |

In the Texas Instruments device number, “**R**” indicates that the device is rated to 100 krad, while “**RL**” indicates that the device is rated to 100 krad at LDR. In the SMD number, the device numbers are the last two numerical digits. These distinguish differences in the products. In this case, device **01** is qualified at HDR and device **02** is qualified at LDR. The SMD will indicate how each device number is qualified.

For products sold in die form, “**MDR**” indicates an HDR, while “**MDE**” indicates an LDR:

|                        |                  |                          |
|------------------------|------------------|--------------------------|
| HDR (50 to 300 rad/s): | LM124 <b>MDR</b> | 5962R995040 <b>1</b> V9A |
| LDR (0.01 rad/s):      | LM124 <b>MDE</b> | 5962R995040 <b>2</b> V9A |

Some suppliers will rate a product at 300 krad, but then state that it is only rated to 50 krad at an LDR. Texas Instruments never rates a unique device number for one TID level at an HDR and another TID level for an LDR. For instance, the company offers one version of the LM6172 rated to 300 krad at an HDR and another version rated to 100 krad at an LDR, with different product names:

|                                 |                 |                          |
|---------------------------------|-----------------|--------------------------|
| 300 krad HDR (50 to 300 rad/s): | LM6172AMGWFMQLV | 5962F956040 <b>2</b> VXA |
| 100 krad LDR (0.01 rad/s):      | LM6172AMGWRLQV  | 5962R956040 <b>3</b> VXA |

The LDR version of the LM6172 is only rated to 100 krad because the company decided not to wait the year that it takes to reach 300 krad at a dose rate of 10 mrad/s.

Another case is the LM111, where one device number is rated only to 50 krad at an HDR but to 100 krad at LDR:

|                                |               |                          |
|--------------------------------|---------------|--------------------------|
| 50 krad HDR (50 to 300 rad/s): | LM111WGLQMLV  | 5962L005240 <b>1</b> VZA |
| 100 krad LDR (0.01 rad/s):     | LM111WGRLQMLV | 5962R005240 <b>2</b> VZA |

Originally, the die used in the HDR and LDR options were different, and this is still the case for some products. Today, for many products, the LDR and HDR device numbers are now just radiation test options of products using the same die. But exercise caution, since a lot that is rated for HDR may have unknown LDR performance.

#### LDR-qualified products

Texas Instruments designates products that pass the ELDRS characterization test as ELDRS-free. These products can have RLAT done at an HDR or LDR.

The company designates products that have ELDRS as “LDR qualified.” Per TM 1019, Texas Instruments performs RLAT at LDR (10 mrad/s) with a 1.5x overtest factor in case there is additional dose-rate sensitivity at rates below 10 mrad/s. For a product rated to 100 krad, the DUT is irradiated to 150 krad at 10 mrad/s and still must pass the 100-krad limits. The SMD numbers for these products will have a 6 in the two digit device ID is the 11th character in the SMD number:

|                 |                                                                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------|
| LM4050WG2.5RLQV | 5962R092356 <b>1</b> VZA<br>Low dose-rate qualified (rated to 100 krad, but test to 150 krad at 10 mrad/s) |
|-----------------|------------------------------------------------------------------------------------------------------------|

Some suppliers will rate products with ELDRS at one level for an HDR and a different level for an LDR, and do not perform the 1.5x overtest at LDR. For instance, an operational amplifier from another supplier that failed ELDRS characterization at 50 krad is rated to 300 krad at an HDR, with a mention that it is rated to 50 krad at an LDR. RLAT is done to 300 krad at an HDR and only 50 krad at an LDR, with no 1.5x overtest as required by TM 1019.

### TID reports

Texas Instruments provides a TID RLAT report for every lot. Information in RLAT reports includes how the RLAT was performed, whether it was for a full wafer lot or an individual wafer, and the dose rate. The reports will typically show ATE test results for all data-sheet and SMD-specified parameters for each unit at each TID level tested, along with drift statistics and parametric plots vs. radiation level. Because the company offers such a wide variety of products, testing may not the same from product to product, and reports from different product families may have different formats.

The RLAT reports for each lot can be downloaded from [TI.com](#). The paperwork that ships with each lot explains how to access RLAT reports. For details, see the application note, “Texas Instruments QML Lot Documents.”

Texas Instruments also posts sample radiation test reports and published papers for many devices on [Ti.com](https://www.ti.com) under the Technical documents tab of the product, as shown in [Figure 7-20](#), and also at [ti.com/space](https://ti.com/space).

TPS50601-SP (ACTIVE)

Radiation hardened 1.6-V to 6.3-V input, 6-A synchronous step down converter

![TPS50601-SP chip](ab20479487461795fab4bd828006ec9a_img.jpg)

DATASHEET

TPS50601-SP Radiation Hardened 1.6- to 6.3-V input, 6-A Synchronous Buck Converter datasheet

View now

Download

Description & parameters

**Technical documents**

Tools & software

Order now

Quality & packaging

Support & training

Datasheet

Errata

Application notes

Technical articles

User guides

**Selection & solution guides**

White papers

Design files

Datasheet (1)

| Title                                                                                        | Type | Size (KB) | Date        |
|----------------------------------------------------------------------------------------------|------|-----------|-------------|
| TPS50601-SP Radiation Hardened 1.6- to 6.3-V input, 6-A Synchronous Buck Converter datasheet | PDF  | 1132      | 05 Dec 2015 |

Application notes (1)

| Title                                                            | Type | Size (KB) | Date        |
|------------------------------------------------------------------|------|-----------|-------------|
| Ti Space Rated Power Solution for Microsemi® RTG4™ FPGA (Rev. A) | PDF  | 796       | 27 Jul 2018 |

User guides (2)

| Title                                                         | Type | Size (KB) | Date        |
|---------------------------------------------------------------|------|-----------|-------------|
| TPS50601-SP/EVM-A1 Reference Guide (Rev. A)                   | ZIP  | 168       | 07 Jun 2013 |
| TPS50601-SP/EVM, 6-A/1.2-A, 5W/6W Regulator Evaluation Module | PDF  | 5486      | 30 Jan 2013 |

Selection & solution guides (1)

| Title                      | Type | Size (KB) | Date        |
|----------------------------|------|-----------|-------------|
| Ti Space Products (Rev. F) | PDF  | 6372      | 06 Aug 2018 |

Radiation & Reliability reports (4)

| Title                                                                             | Type | Size (KB) | Date        |
|-----------------------------------------------------------------------------------|------|-----------|-------------|
| TPS50601-SP Neutron Displacement Damage Characterization (Rev. A)                 | PDF  | 753       | 29 Mar 2019 |
| TPS50601-SP Neutron Displacement Damage Characterization                          | PDF  | 750       | 06 Feb 2019 |
| TPS50601-SP Synchronous Step-Down Converter Single-Event Effects Summary (Rev. A) | PDF  | 3400      | 11 Dec 2017 |
| TPS50601-SP Total Ionizing Dose (TID) Radiation Report                            | PDF  | 4049      | 08 Jul 2016 |

The study and response to SEEs lagged behind that of TID. ASTM F1189 was released in 1988, and the JEDEC SEE test standard, JESD57, was not released until 1996. Suppliers of space-grade ICs typically did not perform SEE testing. In the mid-2000s, Texas Instruments began performing SEE characterization on new space products to aid its customers in product selection and enable quicker design cycles.

### Texas Instruments SEE test capabilities

Texas Instruments has built significant capability and expertise to test its own products. Because the company develops these products, it has better insight into which SEEs may be critical and how best to test its devices.

Not only has the company adapted evaluation boards and bench setups for heavy-ion testing, but it has also developed special equipment and test techniques for SEE characterization. [Figure 7-21](#) shows the motherboard component of the PXI system that Texas Instruments developed for capturing SEE data. For testing ultra-high-speed ADCs under dynamic conditions, the company developed the beat frequency and code error test,<sup>[46]</sup> a method now used by others and cited in several publications.

#### SEE test frequency

SEE testing is a one-time characterization. That does not mean that a device will be tested just once and a report issued. It may take several test campaigns to fully understand how a device responds to heavy-ion radiation. For instance, the TPS50601 has made over a dozen trips to cyclotron facilities.

Any major change to a product, such as a design and layout change, may require repeating the SEE characterization. However, this is a rare case for Texas Instruments. Since the company manufactures its own space-grade die, it is able to control all manufacturing and can validate the original SEE characterization.

#### SEE testing of mature products

Most Texas Instruments mature space products have been tested by others, who published their results in journals or posted them on agency websites. For instance, the LM124 and LM139 are probably the most tested products in the space industry, with hundreds of publications produced on each.

As necessity dictates, Texas Instruments augments this legacy testing with new testing. For instance, the company has performed SET testing on the ELDRS-free versions of the LM124 and LM139 to determine whether changes to these products have an impact on SET response.

#### SEE test reports

Texas Instruments posts SEE test reports and published papers for many devices on [Ti.com](https://www.ti.com), under the Technical documents tab of the product page, as shown in [Figure 7-21](#) and also at [Ti.com/space](https://ti.com/space).

Texas Instruments will only post test results that the company has performed and can validate. If a report for a space-grade product cannot be found, it is possible to submit a request through the Texas Instruments E2E™ Community.

![Figure 7-21: Texas Instruments' SEE PXI test system motherboard at the beam at TAMU. The image shows a green printed circuit board (PCB) populated with various electronic components, including integrated circuits, capacitors, and connectors. The board is mounted on a test system, with a prominent red emergency stop button visible on the right side of the equipment. The background shows a laboratory setting with other equipment and a white wall.](cef87afaa5a63c7a04bcff33c55b2c63_img.jpg)

Figure 7-21: Texas Instruments' SEE PXI test system motherboard at the beam at TAMU. The image shows a green printed circuit board (PCB) populated with various electronic components, including integrated circuits, capacitors, and connectors. The board is mounted on a test system, with a prominent red emergency stop button visible on the right side of the equipment. The background shows a laboratory setting with other equipment and a white wall.

*Figure 7-21. Texas Instruments' SEE PXI test system motherboard at the beam at TAMU.*

### References

- 1 MIL-PRF-38535 Performance Specification, "General Specification for Integrated Circuits (Microcircuits) Manufacturing," Department of Defense, Defense Supply Center, March 16, 2007, <https://landandmaritimeapps.dla.mil/Downloads/MilSpec/Docs/MIL-PRF-38535/prf38535.pdf>.
- 2 MIL-STD-883 Test Method Standard, "Microcircuits," Department of Defense, Defense Supply Center, Feb. 22, 2017, <https://landandmaritimeapps.dla.mil/Downloads/MilSpec/Docs/MIL-STD-883/std883.pdf>.
- 3 P. S. Winokur, F. W. Sexton, J. R. Schwank, D. M. Fleetwood, P. V. Dressendorfer et al., "Total-Dose Radiation and Annealing Studies: Implications for Hardness Assurance Testing," *IEEE Trans. Nucl. Sci.* 33 (6), Dec. 1986, pp. 1343-1351.
- 4 P. S. Winokur, J. R. Schwank, P. J. McWhorter, P. V. Dressendorfer and D. C. Turpin, "Correlating the Radiation Response of MOS Capacitors and Transistors," *IEEE Trans. Nucl. Sci.* 31(6), Dec. 1984, pp. 1453-1460.
- 5 J. R. Schwank, P. S. Winokur, P. J. McWhorter, F. W. Sexton, P. V. Dressendorfer et al., "Physical Mechanisms Contributing to Device Rebound," *IEEE Trans. Nucl. Sci.* 31(6), Dec. 1984, pp. 1434-1438.
- 6 D. M. Fleetwood, P. S. Winokur, L. C. Riewe and R. L. Pease, "An Improved Standard Total-Dose Test for CMOS Space Electronics," *IEEE Trans. Nucl. Sci.* 36(6), Dec. 1989, pp. 1963-1970.
- 7 K. Kruckmeyer, L. Park and T. Trinh, "Total Ionizing Dose Characterization of the Calibration Circuit of Texas Instruments' ADC12D1600CCMLS, 12b, 3.2 GSPS Analog-to-Digital Converter," 2013 *IEEE Radiation Effects Data Workshop*, July 8-12, 2013, pp. 1-4.
- 8 K. Kruckmeyer, J. S. Prater, B. Brown and T. Thang, "Analysis of Low Dose Rate Effects on Parasitic Bipolar Structures in CMOS Processes for Mixed-Signal Integrated Circuits," *IEEE Trans. Nucl. Sci.* 58(3), June 2011, pp. 1023-1031.
- 9 R. L. Pease, R. D. Schrimpf and D. M. Fleetwood, "ELDRS in Bipolar Linear Circuits: A Review," *IEEE Trans. Nucl. Sci.* 56(4), Aug. 2009, pp. 1894-1908.
- 10 K. Kruckmeyer, L. McGee, T. Trinh and J. Benedetto, "Low Dose Rate Test Results of National Semiconductor's ELDRS-Free Bipolar Low Dropout (LDO) Regulator, LM2941 at Dose Rates of 1 and 10 mrad(Si)/s," 2009 *IEEE Radiation Effects Data Workshop*, July 20-24, 2009, pp. 59-64.
- 11 K. Kruckmeyer and T. Trinh, "ELDRS Characterization Up to 300 Krad of Texas Instruments High Speed Amplifiers, LM1717 and LM6172," 2015 *IEEE Radiation Effects Data Workshop*, July 13-17, 2015, pp. 194-198.
- 12 K. Kruckmeyer and T. Trinh, "ELDRS Characterization to 300 krad of Texas Instruments High Speed Amplifier LMH6702," 2016 *IEEE Radiation Effects Data Workshop*, July 11-15, 2016, pp. 92-94.
- 13 N. W. van Vanno, S. D. Turner, E. J. Thomson, B. Williams, S. J. Schulte et al., "Radiation Testing Results for the Intersil ISL71590SEH Temperature Sensor," 2013 *IEEE Radiation Effects Data Workshop*, July 8-12, 2013, pp. 1-4.
- 14 K. Kruckmeyer and T. Trinh, "ELDRS Characterization of Texas Instruments LM185, 1.2V Precision Reference: Retrograde Behavior Demonstrates Why Taking Interim Test Points is Important," 2014 *IEEE Radiation Effects Data Workshop*, July 14-18, 2014, pp. 1-4.
- 15 W. Abere, F. Brueggeman, R. Pease, J. Krieg and M. Simons, "Comparative Analysis of Low Dose-Rate Accelerated and Standard Cobalt-60 for a Low-Dropout Voltage Regulator and Voltage Reference," 2000 *IEEE Radiation Effects Data Workshop*, July 24-28, 2000, pp. 177-180.
- 16 Y. G. Velo, J. Boch, N. J.-H. Roche, S. Perez, J.-R. Vaile et al., "Bias Effects on Total Dose-Induced Degradation of Bipolar Linear Microcircuits for Switched Dose-Rate Irradiation," *IEEE Trans. Nucl. Sci.* 57(4), 2010, pp. 1950-1957.
- 17 MIL-STD-750 TM standard, "Test Methods for Semiconductor Devices," Department of Defense, Defense Supply Center, Nov. 30, 2016, <https://landandmaritimeapps.dla.mil/Downloads/MilSpec/Docs/MIL-STD-750/std750.pdf>.
- 18 ESA, ESCC, ESCC Basic Specification No. 22900, "Total Dose Steady-State Irradiation Test Method," <https://escies.org/download/specdraftappub?id=3413>.
- 19 ASTM F1892, "Standard Guide for Ionizing Radiation (Total Dose) Effects Testing of Semiconductor Devices," ASTM International, 2018, <https://www.astm.org/Standards/F1892.htm>.
- 20 ASTM F1467-99(2005)e1, "Standard Guide for Use of an X-ray Tester ( $\approx 10$  keV Photons) in Ionizing Radiation Effects Testing of Semiconductor Devices and Microcircuits," ASTM International, 2005, <https://www.astm.org/DATABASE.CART/HISTORICAL/F1467-99R05E1.htm>.
- 21 D.K. Nichols, W.E. Price and M.K. Gauthier, "A Comparison of Radiation Damage in Transistors from Cobalt-60 Gamma Rays and 2.2 MeV Electrons," *IEEE Trans. Nucl. Sci.* 29(6), Dec. 1982, pp. 1970-1974.
- 22 M. K. Gauthier and D. K. Nichols, "A Comparison of Radiation Damage in Linear ICs from Cobalt-60 Gamma Rays and 2.2 MeV Electrons," *IEEE Trans. Nucl. Sci.* 30(6), Dec. 1983, pp. 4192-4196.
- 23 D. B. Brown, "Photoelectron Effects on the Dose Deposited in MOS Devices by Low Energy X-Ray Sources," *IEEE Trans. Nucl. Sci.* 27(6), Dec. 1980, pp. 1465-1468.
- 24 D. B. Brown, "The Phenomenon of Electron Rollout for Energy Deposition and Defect Generation in Irradiated MOS Devices," *IEEE Trans. Nucl. Sci.* 33(6), Dec. 1986, pp. 1240-1244.
- 25 T. R. Oldham and J. M. McGarity, "Comparison of 60Co Response and 10 keV X-Ray Response in MOS Capacitors," *IEEE Trans. Nucl. Sci.* 30(6), Dec. 1983, pp. 4377-4381.
- 26 D. M. Fleetwood, D. E. Beutler, L. J. Lawrence Jr., D. B. Brown, B. L. Draper et al., "Comparison of Enhanced Device Response and Predicted X-Ray Dose Enhancement Effects on MOS Oxides," *IEEE Trans. Nucl. Sci.* 35(6), Dec. 1988, pp. 1265-1271.

- 27 G. Cellere, A. Paccagnella, A. Visconti, M. Bonanomi, A. Candelori et al., "Effect of Different Total Ionizing Dose Sources on Charge Loss from Programmed Floating Gate Cells," *IEEE Trans. Nucl. Sci.* 52(6), Dec. 2005, pp. 2372-2377.
- 28 Electronic Industries Association (EIA)/JESD57, "Test Procedures for the Measurement of Single-Event Effects in Semiconductor Devices from Heavy Ion Irradiation," <http://www.edec.org/download/search/jesd57.pdf>.
- 29 ASTM F1192, "Standard Guide for the Measurement of Single Event Phenomena (SEP) Induced by Heavy Ion Irradiation of Semiconductor Devices," ASTM International, <https://www.astm.org/Standards/F1192.htm>.
- 30 Lawrence Berkeley National Labs, Berkeley Accelerator Space Effects Facility, <http://cyclotron.lbl.gov/>.
- 31 The Cyclotron Institute, Texas A&M University Radiation Effects Facility, <https://cyclotron.tamu.edu/ref/>.
- 32 J. S. George, S. C. Moss, T. R. Haas, D. Mayer, R. McKenna et al., "Update on the U.S. Space Radiation Test Infrastructure for Single Event Effects" Aerospace Microelectronics Qualification Working Meeting, Feb. 9, 2016, [http://aerospace.wpengine.netdna-cdn.com/wp-content/uploads/conferences/MRQW2016/K1\\_George.pdf](http://aerospace.wpengine.netdna-cdn.com/wp-content/uploads/conferences/MRQW2016/K1_George.pdf).
- 33 Radiation Test Facilities, ESA European Space Components Information Exchange System, <https://escies.org/webdocument/showArticle?id=230&groupid=6>.
- 34 J. Y. Benitez, A. Donoghue, M. B. Johnson, W. Lu, B. Ninemire et al., "Recent Cocktail Beam Developments at the 88-Inch Cyclotron for SEE Testing," *2017 IEEE Radiation Data Workshop*, July 17-21, 2017, pp. 83-85.
- 35 TAMU plot.
- 36 S. Liu, J. L. Titus, M. Zafrani, H. Cao, D. Carrier et al., "Worst-Case Test Conditions of SEGR for Power DMOSFETs," *IEEE Trans. Nucl. Sci.* 57(1), Feb. 2010, pp. 279-287.
- 37 S. Buchner, N. Kanyogoro, D. McMorro, C. C. Foster, P. M. O'Neill et al., "Variable Depth Bragg Peak Method for Single-Event Effects Testing," *IEEE Trans. Nucl. Sci.* 58(6), Dec. 2011, pp. 2976-2982.
- 38 E. L. Petersen, "Single-Event Data Analysis," *IEEE Trans. Nucl. Sci.* 55(6), Dec. 2008, pp. 2819-2841.
- 39 K. Kruckmeyer, S. P. Buchner and S. DasGupta, "Single Event Transient (SET) Response of National Semiconductor's ELDRS-Free LM139 Quad Comparator," *2009 IEEE Radiation Effects Data Workshop*, July 20-24, 2009, pp. 65-70.
- 40 K. Kruckmeyer, E. Morozumi, R. Eddy, T. Trinh, T. Santiago et al., "Single-Event Transient and ELDRS Characterization Test Results for LM4050 2.5V Precision Reference," *2010 IEEE Radiation Effects Data Workshop*, July 20-23, 2010, pp. 164-169.
- 41 R. Koga, S. H. Crawford, W. R. Crain, S. C. Moss, S. D. Pinkerton et al., "Single-Event Upset (SEU) Sensitivity Dependence of Linear Integrated Circuits (ICs) on Bias Conditions," *IEEE Trans. Nucl. Sci.* 44(6), Dec. 1997, pp. 2325-2332.
- 42 K. Kruckmeyer, J. S. Prater, B. Brown and S. DasGupta, "Single-Event Transient Response Dependence on Operating Conditions for a Digital-to-Analog Converter," *IEEE Trans. Nucl. Sci.* 6(9), Dec. 2009, pp. 3567-3572.
- 43 N. J.-H. Roche, S. P. Buchner, L. Dusseau, K. Kruckmeyer, J. Boch et al., "Correlation of Dynamic Parameter Modification and ASET Sensitivity in a Shunt Voltage Reference," *IEEE Trans. Nucl. Sci.* 59(6), Dec. 2012, pp. 2756-2763.
- 44 K. Kruckmeyer, R. L. Rennie, D. H. Ostensberg, V. Ramachandran and T. Hossain, "Single-Event Upset Characterization of GHz Analog-to-Digital Converters with Dynamic Inputs Using a Beat Frequency Test Method," *2007 IEEE Radiation Effects Data Workshop*, July 23-27, 2007, pp. 113-117.
- 45 K. Kruckmeyer, R. L. Rennie and V. Ramachandran, "Use of Code Error and Beat Frequency Test Method to Identify Single-Event Upset Sensitive Circuits in a 1 GHz Analog-to-Digital Converter," *IEEE Trans. Nucl. Sci.* 55(4), Aug. 2008, pp. 2013-2018.
- 46 K. Kruckmeyer and T. Trinh, "Single-Event Effects Characterization of Texas Instruments ADC12D1600CCMLS, 12 bit, 3.2 GSPS Analog-to-Digital Converter with Static and Dynamic Inputs," *2014 IEEE Radiation Effects Data Workshop*, July 14-18, 2014, pp. 1-7.
- 47 "TPS50601-SP Single-Event Effects Summary," Texas Instruments Radiation Report SLAK017A, Dec. 2017.
- 48 "Single Event Latch-up Testing – Advanced Analog-to-Digital Converter – ADC08D1520WGFQV," Texas Instruments SNAA143, June 4, 2007.
- 49 K. Kruckmeyer, R. Eddy, A. Szczapa, B. Brown and T. Santiago, "SEE Testing of National Semiconductor's LM98640QML System on a Chip for Focal Plane Arrays and Other Imaging Systems," *2010 IEEE Radiation Effects Data Workshop*, July 20-23, 2010, pp. 63-70.
- 50 E. L. Petersen, J. C. Pickel, E. C. Smith, P. J. Rudeck and J. R. Letaw, "Geometrical Factors in SEE Rate Calculations," *IEEE Trans. Nucl. Sci.* 40(6), pp. 1888-1909.
- 51 Vanderbilt CREME website: <https://creme.isde.vanderbilt.edu/CREME-MC>.
- 52 J. R. Schwank, M. R. Shaneyfelt and P. E. Dodd, "Radiation Hardness Assurance Testing of Microelectronic Devices and Integrated Circuits: Test Guideline for Proton and Heavy Ion Single-Event Effects," *IEEE Trans. Nucl. Sci.* 60(3), June 2013, pp. 2101-2118.
- 53 S. Buchner, P. Marshall, S. Kniffin and K. LaBel, "Proton Test Guideline Development – Lessons Learned," NASA/Goddard Space Flight Center, Aug. 22, 2002, [https://radhome.gsfc.nasa.gov/radhome/papers/proton\\_testing\\_guidelines\\_2002.pdf](https://radhome.gsfc.nasa.gov/radhome/papers/proton_testing_guidelines_2002.pdf).
- 54 K. A. LaBel, "Proton Single Event Effects (SEE) Guideline," NASA/Goddard Space Flight Center, Aug. 2009, [https://radhome.gsfc.nasa.gov/radhome/papers/Proton\\_RHAGuide\\_NASAFinal.pdf](https://radhome.gsfc.nasa.gov/radhome/papers/Proton_RHAGuide_NASAFinal.pdf).
- 55 "Single-Event Upset Report – 8 b Analog-to-Digital Converter 2 Channel – ADC08D1520WGFQV," Texas Instruments SNAA144, Jan. 28, 2008.

- 56 EIA/JESD234, "Test Standard for The Measurement of Proton Radiation Single-Event Effects in Electronic Devices," [https://www.jedec.org/document\\_search?search\\_api\\_views\\_fulltext=jesd234](https://www.jedec.org/document_search?search_api_views_fulltext=jesd234).
- 57 K. A. LaBel, T. Turlinger, T. Haas, J. George, S. Moss et al., "Team Update on North American Proton Facilities for Radiation Testing," Aerospace Microelectronics Qualification Working Meeting, Feb. 9, 2016.
- 58 D. McMorrow, S. Buchner, M. Baze, B. Bartholet, R. Katz et al., "Laser-Induced Latchup Screening and Mitigation in CMOS Devices," *IEEE Trans. Nucl. Sci.* 53(4), Aug. 2006, pp. 1819-1824.
- 59 D. McMorrow, S. Buchner, W. T. Lotshaw, J. S. Melinger, M. Maher et al., "Demonstration of Single-Event Effects Induced by Through-Wafer Two-Photon Absorption," *IEEE Trans. Nucl. Sci.* 51(6), Dec. 2004, pp. 3553-3557.
- 60 D. Cardoza, S. D. LaLumondiere, N. P. Wells, M. A. Tockstein, D. L. Brewe et al., "Investigating Pulsed X-Ray Induced SEE in Analog Microelectronic Devices," *IEEE Trans. Nucl. Sci.* 62(6), Dec. 2015, pp. 2458-2467.
- 61 S. C. Moss, S. D. LaLumondiere, J. R. Scarpulla, K. P. MacWilliams, W. R. Grain et al., "Correlation of Picosecond Laser-Induced Latchup and Energetic Particle-Induced Latchup in CMOS Test Structures," *IEEE Trans. Nucl. Sci.* 42(6), Dec. 1995, pp. 1948-1956.
- 62 JEDEC website: <https://www.jedec.org/>.

# Chapter 8: Texas Instruments' space product advantage

Texas Instruments, along with its acquisitions National Semiconductor and Unitrode, has supplied space-grade products for over four decades. The company's space-grade products are manufactured, tested and qualified per military specification MIL-PRF-38535, and most are listed on the Defense Logistics Agency's Qualified Manufacturers List (QML) and are radiation hardness assured (RHA).

To aid in device selection and design-in, Texas Instruments provides upfront radiation test data with total ionizing dose (TID) and single-event effect (SEE) reports.

Texas Instruments space-grade products go through a single process flow. Because the company has its own wafer foundries, it is able to control process changes that could impact radiation performance. Its radiation reports are still applicable to materials shipped today; any changes that might impact radiation performance of a product would compel the company to repeat the tests.

This chapter will discuss what to consider when using commercial off-the-shelf (COTS) products and published radiation reports.

### 8.1 Product and process changes

To allow for manufacturing flexibility, a commercial products supplier may assemble an individual product at several different locations, using slightly different process equipment and process flows. Although these differences may not impact a device's electrical performance, they may impact its radiation performance, as radiation performance is not monitored when a product is transferred to a new wafer fab.

Texas Instruments space-grade products have one manufacturing flow. If a product goes through a fab transfer, the radiation qualification has to be repeated. [Figure 8-1](#) illustrates the differences between commercial and Texas Instruments space-grade process flows.

Mature products that are 10 years or older have likely gone through a wafer fab transfer as older wafer fabs closed down and suppliers moved products to newer fabs.

For instance, in the late 1990s, National Semiconductor closed a wafer fab that produced the space-grade 100-krad RHA LM124AQL-SP operational amplifier and LM139AQL-SP differential comparator, and moved them to newer wafer fabs with improved processing for better reliability. TID performance degraded to under 30 krad in the new fabs. National spent a significant amount of time and research to understand the cause and return the radiation performance back up to 100 krad at the new fabs.<sup>[1,2]</sup>

![Commercial flow diagram showing multiple paths from wafer fabs to delivered products.](c686c005fef31702c109f5d9dd975413_img.jpg)

The diagram titled "Commercial flow" illustrates a multi-path manufacturing process. At the top, four "Wafer fab" nodes are arranged horizontally. Below them are four "A/T site" nodes, each receiving input from one or more wafer fabs. At the bottom are four "Material set" nodes, each receiving input from one or more A/T sites. All four material sets converge into a single "Delivered product" node at the bottom. This structure represents a complex, multi-sourced commercial production flow.

Commercial products can be built in multiple fabs and assembly/test (A/T) sites and may use various material sets for each product build.

Commercial flow diagram showing multiple paths from wafer fabs to delivered products.

![Space product flow diagram showing a single path from wafer fab to delivered product.](f9873201604e723ae0bafb7e389ef619_img.jpg)

The diagram titled "Space product flow" illustrates a single-path manufacturing process. It starts with a single "Wafer fab" node at the top, which leads to a single "A/T site" node, then to a single "Material set" node, and finally to a single "Delivered product" node at the bottom. This structure represents a controlled, single-sourced space-grade production flow.

Space products are built in one fab, one A/T site and use one material set for each product build.

Space product flow diagram showing a single path from wafer fab to delivered product.

Figure 8-1. Commercial vs. Texas Instruments space-grade process flows.

### 8.2 Lot-to-lot variation

Even when a commercial product is produced at a single manufacturing site with no changes in the wafer fab process, there can still be lot-to-lot variations in radiation performance. Today's wafer fabs use many tools, such as automated equipment and statistical quality control, to reduce lot-to-lot variation and improve quality. However, the controls put in place at a commercial fab are

meant to optimize electrical performance and do not monitor for radiation hardness. Features that impact radiation performance, such as oxide stoichiometry and thicknesses, are not critical to electrical performance and do not need to be as tightly controlled. Therefore, lot-to-lot variation in radiation performance can be an issue with many processes and products.

Texas Instruments tests and qualifies each space-grade RHA wafer lot. **Table 8-1** shows TID test results for three wafer lots of the LM108 operational amplifier, processed at the same wafer fab using the same process. Lot Nos. 1 and 3 were processed just one month apart.

| Lot number | TID performance |
|------------|-----------------|
| 1          | 100 krad(Si)    |
| 2          | 30 krad(Si)     |
| 3          | 10 krad(Si)     |

**Table 8-1. LM108 TID performance. Lot Nos. 1 and 3 were processed one month apart at the same wafer fab.**

Significant lot-to-lot variation and even unit-to-unit variation within the same lot in single-event gate rupture survival voltage have both been observed in GaN FETs.<sup>[9]</sup>

### 8.3 Date codes tell you nothing

It is a common misconception that the four-digit code indicates the date when a wafer lot was processed, and that units with the same date code come from the same wafer lot or diffusion run. The four-digit date code does not refer to the wafer lot; it simply indicates when the product was encapsulated in plastic or went through the lid seal process for hermetic packaging. The wafer lot could have been processed at any time before then.

**Table 8-2** is an example of various grades and packages for the LM139, with date codes 0441 (assembled during the 41th week of 2004) and 0712 (assembled during the 12th week of 2007). Some wafer lots were fabricated three years apart.

| Date code | Lot number | Wafer fab | Part number   |
|-----------|------------|-----------|---------------|
| 0441      | EM0118BB2  | TE flow 2 | LM139AW-QMLV  |
| 0441      | HM237877   | UK 4"     | LM139AW-QMLV  |
| 0441      | EM02422T1  | TE flow 2 | LM139AWG/883  |
| 0441      | JM046X13   | UK 6"     | LM139AWGRQMLV |
| 0441      | JM046X13   | UK 6"     | LM139AWGRQMLV |
| 0441      | EM02422T3  | TE flow 2 | LM139AW-SMD   |
| 0712      | EM0118BB2  | TE flow 2 | LM139AW-QMLV  |
| 0712      | XM06023N2  | TE flow 1 | LM139AWG/883  |
| 0712      | JM046X13   | UK 6"     | LM139AWGRQMLV |
| 0712      | XM06023N2  | TE flow 1 | LM139J/883    |
| 0712      | JM051X21   | UK 6"     | LM139 MDS     |

**Table 8-2. Wafer-lot numbers and wafer fabs for various LM139 lots with their date code.**

On commercial products, the units of an assembly lot, with a unique date code, might not all come from the same wafer or diffusion lot. If there is not enough die from one wafer lot to complete an assembly lot, die will be taken from the next wafer lot in line. Also, "bonusing" used to be a common practice in the industry. If there were leftover wafers from a few wafer lots or if a wafer got separated from its mother lot, the orphaned wafers would be combined into a new wafer lot and assigned a new wafer-lot number. Whether any of these practices still exist depends on the manufacturer.

On some products, it is possible for a supplier to trace back the date code to the wafer lot if the full date code and product name are known. This is not always possible, on small chip-scale packages, however, where the date code is only one or two digits.

Texas Instruments space-grade materials have a 10-digit date code. Each unique date code comes from a single wafer. There are characters in the date code that indicate when the wafer lot finished processing and went through probe testing.

### 8.4 Radiation qualification by process

There is a risk in trying to qualify a wafer fab process based on the radiation test results from one product using that process. Process is not the only factor that determines a device's radiation performance. Other factors include device function, layout and choice of modules during the process.

Texas Instruments' DS16F95QML-SP and LM4050QML-SP are both on its L-FAST process, but the DS16F95 is rated to 300 krad while the LM4050 is only rated to 100 krad. The LM4050 is a precision reference, while the DS16F95 is an RS-485 transceiver for which the reference voltage is not critical. Even similar products using the same wafer fab and process may have different radiation performance, as in the low-dropout regulators (LDOs) described in Chapter 5, where the LM2941 is rated to 100 krad and the LP2953 is rated under 30 krad.

A BiCMOS product that does not have any CMOS structures on it might not have single-event latch-up (SEL), but another product using the same process could use CMOS structures and have SEL.

The product supplier is best positioned to understand the differences between products using the same process and to know whether any radiation data from one product could be applied to another product. Even so, Texas Instruments tests and qualifies each individual product, even for slight variations such as voltage options.

### 8.5 Using published radiation test data

There is a wealth of radiation test reports and publications about Texas Instruments and other suppliers' products in technical journals and on agency websites. Some of these documents report specific research studies and may not contain enough information to be applicable to a specific need, requirement or application. It is important to carefully evaluate test reports for a number of aspects such as product tested; test conditions; and in extreme cases, the validity of the test method and test results.

### Device tested: not every LM124 is the same

It is crucial to verify the actual product to determine if a report is even applicable to the product of interest. Is the product tested in the report exactly the same as the product of interest? Will variations in the product result in different radiation performance?

National Semiconductor developed the LM124 in 1972. Many other companies cloned the device and some still sell their own versions of the LM124.

Texas Instruments had its own LM124, but also obtained the National Semiconductor version of the LM124 when it purchased National in 2011. Texas Instruments has commercial, military and space-grade versions of the LM124, both of Texas Instruments and National originals, which can have different designs, layouts, fab processes, wafer fabs and radiation performance.

The company has two different space-grade versions of the LM124 with different radiation performances: the Texas Instruments LM124-SP is rated to 50 krad, while the National LM124AQM-L-SP is rated to 100 krad.

The National Semiconductor version of the LM124 went through a die shrink in 2001. Most papers, even those published after 2001, contain radiation test data on the older National die before the die shrink and not on the new die supplied by Texas Instruments today. There have been hundreds of papers and reports written on radiation testing of the LM124, but many do not include the grade tested, the manufacturing date or even the manufacturer's name.

Attempting to use a commercial product in place of the space-grade version of a device can be risky or even disastrous. For instance, the space-grade versions of the ADC128S102 and DAC121S101 are radiation-hardened by design, while the commercial versions are not and will experience both SEL and single-event functional interrupt (SEFI) at low ion energies.<sup>[4]</sup> Another example is the DS90C031, where the space-grade version was modified to prevent SEL, but the military-grade version was not.<sup>[6]</sup> A risk to a number of space programs using the military-grade device had to be assessed; ultimately some boards had to be reworked, jeopardizing mission schedules.

#### Test conditions

The operating conditions used during radiation testing can have an impact on a device's radiation performance. On many products, the supply voltage during irradiation can have a significant impact on features such as TID survivability or SEE probability (see Chapter 5 for more details). Was the testing performed under worst-case conditions? Do the test conditions match a specific application?

A number of papers describe TID tests on the LP2953, with wildly different results ranging from 2.5 krad to 30 krad.<sup>[6-9]</sup> None of the papers indicate the specific operating conditions used during irradiation. Was the variation in radiation performance caused by the test conditions or some other factor? Although these papers present enough information for the targeted research purpose, they do not provide enough information to determine whether the LP2953 could work in most applications.

SEE testing is not always done under the worst-case conditions. In testing the commercial versions of the ADC128S102 and

DAC121S101, the supply voltage was at 3.6 V and the die temperature was 50°C.<sup>[4]</sup> The test results show SEL at a linear energy transfer (LET) of 32 MeV-cm<sup>2</sup>/mg on the DAC121S101 and 40-65 MeV-cm<sup>2</sup>/mg for the Va supply on the ADC128S102 with no SEL on the Vd supply. Testing by Texas Instruments and others has shown that when tested at maximum operating conditions (5 V to 5.25 V), these commercial products have SEL at LET thresholds as low as 10 MeV-cm<sup>2</sup>/mg on all supplies.

For a power product, a capacitor on the output can attenuate or eliminate output transients (see Chapter 5). Using the recommended capacitors or application-specific capacitors will provide a more accurate test result.<sup>[10]</sup>

In extreme cases, the test setup might not be valid. Many LDOs require output capacitors with a specified electron spin resonance range to keep the output stable. If the capacitors are not present, the device will be unstable. SEE test results could be misdiagnosed, and lead to putting the blame of the product's instability on the heavy ions instead of the test setup, as shown in the example

Figure 8-2.

![Circuit diagram of a typical application for the LM2991 LDO. It shows an unregulated input connected to the IN pin, with a bypass capacitor C_IN* to ground. The ON/OFF pin is connected to ground. The output is taken from the OUT pin, which has a feedback network consisting of a resistor R1 to the input and a resistor R2 to ground. An output capacitor C_OUT** is connected between the OUT pin and ground. The output is labeled as a regulated input.](ca3fe82a47b87503fc317d0dbd188ef9_img.jpg)

Typical application

Circuit diagram of a typical application for the LM2991 LDO. It shows an unregulated input connected to the IN pin, with a bypass capacitor C\_IN\* to ground. The ON/OFF pin is connected to ground. The output is taken from the OUT pin, which has a feedback network consisting of a resistor R1 to the input and a resistor R2 to ground. An output capacitor C\_OUT\*\* is connected between the OUT pin and ground. The output is labeled as a regulated input.

$$V_{OUT} = V_{REF} (1 + R2/R1)$$

\* Required if the regulator is located further than 6 inches from the power-supply filter capacitors. A 1- $\mu$ F solid tantalum or a 10- $\mu$ F aluminum electrolytic capacitor is recommended.

\*\*Required for stability. Must be at least a 10- $\mu$ F aluminum electrolytic or a 1- $\mu$ F solid tantalum capacitor to maintain stability. May be increased without bound to maintain regulation during transients. Locate the capacitor as close as possible to the regulator. The equivalent series resistance is critical, and should be less than 10  $\Omega$  over the same operating temperature range as the regulator.

![Circuit diagram for an SEE test setup. It shows a D.U.T. (Device Under Test) labeled LM2991J. The input is connected to a 15V supply (V_IN = 15 V). The output is connected to a load consisting of a 1k2 resistor in series with a 180 resistor to ground.](58ec6f2b0981a93bab24cbffeb0bfcf4_img.jpg)

Circuit diagram for an SEE test setup. It shows a D.U.T. (Device Under Test) labeled LM2991J. The input is connected to a 15V supply (V\_IN = 15 V). The output is connected to a load consisting of a 1k2 resistor in series with a 180 resistor to ground.

Figure 8-2. The top diagram and application instructions are from the LM2991 data sheet<sup>[11]</sup> and indicate the need to use output capacitors for output stability. The bottom diagram is an SEE test setup with no capacitors.<sup>[12]</sup> Image courtesy of International Science and Technology Center

#### Failure criteria

What criteria determine the failure threshold of a device, and does this threshold match the critical parameters of a particular application? How big do the output transients need to be before they cause a problem? As shown in [Figure 8-3](#), the LM139 output SETs can have different amplitudes, ranging from a few millivolts to full scale. At which transient level will a particular system detect an error? As [Figure 8-3](#) shows, the probability of having a full-scale transient is orders of magnitude less than having a small transient that might not impact the application.

![Figure 8-3: Examples of LM139 output transients (top) and cross-section of transients (bottom).](ca97ce18a835aa5a37ddd7043b51a9bf_img.jpg)

The figure consists of two plots. The top plot shows Output (V) on the y-axis (0 to 6) versus Time (μs) on the x-axis (-2 to 8). It displays several transient pulses of varying amplitudes and widths, with a red line indicating a specific transient level. The bottom plot shows Cross-section (cm<sup>2</sup>) on a logarithmic y-axis (1.0E-07 to 1.0E-03) versus Effective LET (MeV-cm<sup>2</sup>/mg) on the x-axis (0 to 50). It shows two curves: a red line for a -2.5-V trigger and a teal line for a -15-mV trigger. The red curve has peaks at 0° and 45° angles, while the teal curve has a peak at 45° and a higher value at 60°.

Figure 8-3: Examples of LM139 output transients (top) and cross-section of transients (bottom).

**Figure 8-3.** Examples of LM139 output transients (top). A cross-section of the transients with amplitudes greater than 2.5 V (red line) and all transients (teal line) (bottom). Most of the transients have an amplitude less than 2.5 V and might not impact the application.<sup>[13]</sup>

Which parameter in TID testing is considered critical and needs monitoring, and how far does a parameter have to drift before it is considered a failure? Do the results match a specific application's needs? Due to the extreme difficulty of testing all parameters, many researchers report the impact of radiation using only a few parameters. For TID testing, Texas Instruments tests all data-sheet parameters and provides drift statistics.

### Improper definitions and misdiagnosis

In some reports, SEEs have been improperly defined or misdiagnosed.

A minor confusion in the use of terms is that the SEU will sometimes be used for any event that is not destructive. This is common in older papers before the all SEE definitions were established.

In extreme cases, improper definitions and invalid test setups can result in critical misdiagnoses. One report incorrectly stated that the LM117 and LM2991 had SEL, causing some space programs to shy away from using them.<sup>[11]</sup> Other papers have shown that the LM117 does not have SEL,<sup>[14]</sup> and the LM2991 uses the same junction isolated bipolar process (see Chapter 5).

The report gives the following definition for SEL: "SEL is defined as the heavy-ion induced firing of a parasitic structure inherent to some monolithic integrated circuit technologies, which exhibits negative differential resistance. Firing of the structure results in an uncontrolled increase of component supply current, which might subsequently lead to component destruction (burnout)."<sup>[11]</sup> That definition more closely matches the definition of SET instead of SEL in Joint Electron Device Engineering Council JESD57: "A momentary voltage excursion (voltage spike) at a node in an integrated circuit caused by the passage of a single energetic particle."<sup>[15]</sup> The SEL definition in JESD57 is "an abnormal high-current state in a device due to the turn-on of a real or parasitic thyristor by the passage of a single energetic particle through sensitive regions of the device structure, resulting in the loss of device functionality."<sup>[15]</sup>

During this testing<sup>[11]</sup>, a current limit was put on the supply to the input voltage of the regulator. If the input current hit the current limit, the voltage supply was immediately shut off and the event was labeled an SEL.

In fact, this was a voltage transient on the output that caused an increase in load current, momentarily producing an increase in current on the voltage input pin. Because the supply voltage was immediately shut off when the current transient was detected, it was impossible to determine whether the device would return to its normal operating condition after the transient subsided. In addition, the required stabilization capacitors were not used on the outputs, which resulted in output instability and much larger transients.

Another common misdiagnosis occurs when a SEFI causes a product to go into a different operating mode that draws more current and is labeled incorrectly as SEL. Conversely, micro-SEL events, where the supply current increases in small increments, have sometimes been misinterpreted as SEFIs.

Texas Instruments posts radiation test reports and papers on [TI.com](https://www.ti.com). No reports are posted unless the company was involved in the testing and able to verify the results.

### References

- 1 M. R. Shaneyfelt, R. L. Pease, M. C. Maher, J. R. Schwank, S. Gupta et al., "Passivation Layers for Reduced Total Dose Effects and ELDRS in Linear Bipolar Devices," *IEEE Trans. Nucl. Sci.* 50(6), Dec. 2003, pp. 1785-1790.
- 2 R. L. Pease, M. C. Maher, M. R. Shaneyfelt, M. W. Savage, P. Baker et al., "Total-Dose Hardening of a Bipolar-Voltage Comparator," *IEEE Trans. Nucl. Sci.* 49(6), Dec. 2002, pp. 1785-1790.
- 3 L. Z. Scheick, "Recent Gallium Nitride Power HEMT Single-Event Testing Results," *2016 IEEE Radiation Effects Data Workshop*, July 11-15, 2016, pp. 36-41.
- 4 D. Hu, "COTS Components Radiation Test Activity and Results at MSSL," *2016 IEEE Radiation Effects Data Workshop*, July 11-15, 2016, pp. 268-274.
- 5 D. McMorow, S. Buchner, M. Baze, B. Bartholet, R. Katz et al., "Laser-Induced Latchup Screening and Mitigation in CMOS Devices," *IEEE Trans. Nucl. Sci.* 53(4), Aug. 2006, pp. 1819-1824.
- 6 T. F. Miyahira, B. G. Rax and A. H. Johnston, "Total Dose Degradation of Low-Dropout Voltage Regulators," *2005 IEEE Radiation Effects Data Workshop*, July 11-15, 2005, pp. 127-131.
- 7 S. S. McClure, J. L. Gorelick, R. Pease and A. H. Johnston, "Dose Rate and Bias Dependency of Total Dose Sensitivity of Low Dropout Voltage Regulators," *2000 IEEE Radiation Effects Data Workshop*, July 24-28, 2000, pp. 100-105.
- 8 D. J. Cochran, S. D. Kniffin, K. A. LaBel, M. V. O'Bryan, R. A. Reed et al., "Total Ionizing Dose Results and Displacement Damage Results for Candidate Spacecraft Electronics for NASA," *2003 IEEE Radiation Effects Data Workshop*, pp. 57-64.
- 9 T. R. Oldham and J. H. Lee, "Compendium of Ball Aerospace TID and SEE Test Results," *2016 IEEE Radiation Effects Data Workshop*, July 11-15, 2016, pp. 10-18.
- 10 N. J.-H. Roche, S. P. Buchner, L. Dusseau, K. Kruckmeyer, J. Boch et al., "Correlation of Dynamic Parameter Modification and ASET Sensitivity in a Shunt Voltage Reference," *IEEE Trans. Nucl. Sci.* 59(6), Dec. 2012, pp. 2756-2763.
- 11 Texas Instruments LM2991QML Negative Low Dropout Adjustable Regulator data sheet, Oct. 2011, <http://www.Ti.com/lit/ds/symlink/lm2991qml.pdf>.
- 12 Astrium GmbH, Munich, Germany, "Irradiation Test Report for Selected Electronic Components Used in Equipment for ISS/ COF Designed by Chevalier Photonics," July 19, 2001, <https://escies.org/download/webDocumentFile?id=342>.
- 13 K. Kruckmeyer, S. P. Buchner and S. DasGupta, "Single Event Transient (SET) Response of National Semiconductor's ELDRS-Free LM139 Quad Comparator," *2009 IEEE Radiation Effects Data Workshop*, July 20-24, 2009, pp. 65-70.
- 14 K. LaBel, A. Moran, D. Hawk, A. Sanders, C. Seidleck et al., "Single Event Effect Proton and Heavy Ion Test Results in Support of Candidate NASA Programs," *1995 IEEE Radiation Effects Data Workshop*, July 17-24, 1995, pp. 16-32.
- 15 EIA/JESD57, Test Procedures for the Measurement of Single-Event Effects in Semiconductor Devices from Heavy Ion Irradiation, <http://www.jedec.org/download/search/jesd57.pdf>.

## Glossary

### Alpha particle

The nucleus of a helium atom, consisting of two protons and two electrons. Type of radioactive decay.

### Bias voltage

Voltage applied to a node of an electronic device.

### Bragg peak

Depth in silicon where most of an ion's energy is deposited.

### Bremsstrahlung

An X-ray emitted due to an electron losing speed during a collision with a nucleus.

### Carrier recombination

When holes and electrons combine, resulting in no charge.

### Corona

Outer layer of the sun.

### Coronal mass ejection (CME)

When significant amounts of plasma and magnetic field are released from the solar corona.

### Coulombic interactions

Interactions between charged particles, either attraction or repulsion.

### Cross-section

In single-event effect testing, the number of errors per area of a device.

### Deep trench isolation

A deep trench etched in silicon and then filled with oxide to separate transistors.

### Die

An individual integrated circuit, not including packaging.

### Diffusion lot

A group of wafers that went through the wafer fab diffusion process at the same time, in the same diffusion tube; may also be called a wafer lot.

### Displacement damage dose (DDD)

Radiation with particles of enough energy and mass to cause damage to the lattice of a semiconductor.

### Dose-rate effects

Impact on a device from a very high radiation dose rate. Also known as prompt dose.

### Effective linear energy transfer

A calculation of the total energy deposited in a volume for particles that impact the volume at an angle. This calculation is not valid for all microcircuit devices.

### Electromagnetic waves

Waves of energy, including radio waves, microwaves, infrared waves, visible light, ultraviolet light, X-rays and gamma rays. The physical counterpart is photons.

### Enhanced low-dose-rate sensitivity (ELDRS)

Indicates that a device can tolerate a higher total ionizing dose at a high dose rate than at a low dose rate.

### Fluence

Total number of particles to hit an area.

### Flux

Movement or rate of movement. In heavy-ion testing, the flux is the number of ions hitting a unit area in a unit amount of time.

### Free path

How far a particle can travel before colliding into another particle.

### Galactic cosmic ray

Energetic atom fragments, which can be nuclei, protons or electrons.

### Geostationary orbit

Around 20,000 miles from the Earth's surface. The orbit is the same as the Earth's rotation; therefore, a satellite is always in the same place relative to a point on the Earth's surface.

### Heavy ion

A charged atom heavier than helium. For radiation testing, they are positively charged due to the loss of one or more electrons. A helium ion is known as an alpha particle.

### Ion

A negatively or positively charged particle.

### Ion run

Time from when the ion beam is turned on to when it is turned off; also known as a beam run.

### Integrated circuit (IC)

Also known as a computer chip.

### Linear energy transfer

The amount of energy a particle deposits in a substance.

### Local oxidation of silicon (LOCOS)

The growth of field oxide to separate N-channel and P-channel devices in a complementary metal-oxide semiconductor process.

### Lot

A group of units that were processed together. A lot could be the die from a single wafer, a group of wafers or a group of units that were assembled at the same time.

### Low Earth orbit (LEO)

About 60 to 1,200 miles from the Earth's surface.

### Medium Earth orbit

About 1,200 to 22,000 miles from the Earth's surface.

### Multiple-bit upset (MBU)

When more than one cell is upset from an ion strike.

### Nonionizing energy loss (NIEL)

Radiation from a nonionizing particle, such as a neutron.

### Prompt dose

A very high radiation dose rate, typically from a nuclear detonation. Also known as dose rate effects.

### Rad

Unit of ionizing radiation absorbed.

### Radiation

Transport of energy from one location to another, where the carriers are photons, ions, electrons, muons and/or nucleons (neutrons or protons).

### Radiation hardened

Changes to a product that make it more tolerant to radiation, but sometimes just referring to a product that is radiation tested.

### **Radiation hardness by design**

Designing a part for improved tolerance to radiation.

### **Radiation hardness by process**

Creating a wafer fab process to improve tolerance to radiation.

### **Radiation lot acceptance test (RLAT)**

Radiation test performed on a lot of material to verify that it meets the specified radiation level.

### **Radioactive decay**

When an unstable atom loses energy through its core, emitting particles.

### **Sensitive volume**

The region of a microcircuit where a particle strike can cause a single-event effect.

### **Shallow trench isolation**

A shallow trench etched into silicon and then filled with oxide to separate N-channel and P-channel devices in a CMOS process.

### **Single-event burnout (SEB)**

Damage to a circuit from excess current flow due to an ion strike, typically in a metal-oxide semiconductor transistor.

### **Single-event effect (SEE)**

What happens when a particle hits a microelectronic circuit or component.

### **Single-event functional interrupt (SEFI)**

Change in the operating mode of an integrated circuit due to a particle strike. Originally meaning a change in a setup register, it now commonly refers to any change, such as an integrated circuit going into reset.

### **Single-event gate rupture (SEGR)**

Damage to the gate oxide of a metal-oxide semiconductor device from a particle strike.

### **Single-event latch-up (SEL)**

When a parasitic thyristor turns on due to a particle strike. The thyristor will remain on until supply voltage is removed.

### **Single-event phenomena**

Same as a single-event effect.

### **Single-event transient (SET)**

A voltage pulse caused by a particle strike.

### **Single-event upset (SEU)**

A change in the state of a digital circuit caused by a particle strike. Sometimes used to cover many different types of nondestructive single-event effects.

### **Solar flares**

Sudden burst in the sun's brightness; sometimes accompanied by a coronal mass ejection, which increases the number of charged particles in the solar wind.

### **Solar wind**

Stream of charged particles emitted into space from the sun.

### **Standard microcircuit drawing (SMD)**

Device information and specifications maintained by the Defense Logistics Agency.

### **System-on-chip (SoC)**

An integrated circuit with many functions; all components are implemented within the chip silicon.

### **Total ionizing dose (TID)**

Amount of a radiation that a device has received.

### **Van Allen radiation belt**

Area around the Earth where energetic particles, mostly from solar winds, are captured by the Earth's magnetic field.

## Acronyms

|         |                                                                   |         |                                                   |         |                                          |
|---------|-------------------------------------------------------------------|---------|---------------------------------------------------|---------|------------------------------------------|
| ADC     | analog-to-digital converter                                       | GCR     | galactic cosmic ray                               | RHBD    | radiation hardening by design            |
| AMU     | atomic mass unit                                                  | GEO     | geostationary orbit                               | RHBP    | radiation hardening by process           |
| ASET    | analog single-event transient                                     | GSO     | geosynchronous orbit                              | RLAT    | radiation lot acceptance testing         |
| ASTM    | American Society for Testing and Materials                        | Gy      | gray                                              | SAA     | South Atlantic Anomaly                   |
| ATE     | automated test equipment                                          | HDR     | high dose rate                                    | SBU     | single-bit upset                         |
| BiCMOS  | bipolar complementary metal-oxide semiconductor                   | HEO     | high Earth orbit                                  | SEB     | single-event burnout                     |
| BJT     | bipolar junction transistor                                       | hFE     | bipolar transistor gain                           | SEC-DED | single-error correct-double-error detect |
| BL      | bitline                                                           | IC      | integrated circuit                                | SEDR    | single-event dielectric rupture          |
| BOX     | buried oxide                                                      | IGBT    | insulated gate bipolar transistor                 | SEE     | single-event effect                      |
| BPSG    | boron-doped phosphosilicate glass                                 | LBL     | Lawrence Berkeley National Labs                   | SEFI    | single-event functional interrupt        |
| CAT     | computerized axial tomography                                     | LDO     | low-dropout regulator                             | SEGR    | single-event gate rupture                |
| CCD     | charge-coupled device                                             | LDR     | low dose rate                                     | SEL     | single-event latch-up                    |
| CMEs    | coronal mass ejections                                            | LEO     | low Earth orbit                                   | SEM     | scanning electron microscope             |
| CMOS    | complementary metal-oxide semiconductor                           | LET     | linear energy transfer                            | SEP     | solar energetic particles                |
| COTS    | commercial off-the-shelf                                          | LOCOS   | local oxidation of silicon                        | SER     | soft-error rate                          |
| CT      | computer tomography                                               | MAAT    | metal-oxide semiconductor accelerated anneal test | SET     | single-event transient                   |
| DBU     | double-bit upset                                                  | MBU     | multiple-bit upset                                | SEU     | single-event upset                       |
| DD      | displacement damage                                               | MCU     | multicell upset                                   | Si      | silicon                                  |
| DDD     | displacement damage dose                                          | MEO     | medium Earth orbit                                | SiGe    | silicon germanium                        |
| DEC-TED | double-error correct-triple-error detect                          | MIL-STD | military standard                                 | SMD     | standard microcircuit drawing            |
| DICE    | dual interlocked storage cell                                     | MOS     | metal-oxide semiconductor                         | SOA     | safe operating area                      |
| DMOSFET | double-diffused metal-oxide semiconductor field-effect transistor | MOSFET  | metal-oxide semiconductor field-effect transistor | SoC     | system-on-chip                           |
| DMR     | dual-modular redundant                                            | MUX     | multiplexer                                       | SOI     | silicon-on-insulator                     |
| DRAM    | dynamic random access memory                                      | ND/PD   | neutron dose/proton dose                          | SOS     | silicon-on-sapphire                      |
| DSET    | digital single-event transient                                    | NIEL    | nonionizing energy loss                           | SRAM    | static random access memory              |
| DTI     | deep trench isolation                                             | NMOS    | N-channel metal-oxide semiconductor               | SRIM    | Stopping and Range of Ions in Matter     |
| DUT     | device under test                                                 | NPN     | NPN transistor                                    | STI     | shallow trench isolation                 |
| e-h     | electron hole                                                     | NYC     | New York City                                     | TAMU    | Texas A&M University                     |
| ECC     | error correction circuit                                          | OM      | optical microscope                                | TDE     | time-dependent effect                    |
| ELDRS   | enhanced low-dose-rate sensitivity                                | PMOS    | P-channel metal-oxide semiconductor               | TEM     | transmission electron microscope         |
| EMP     | electromagnetic pulse                                             | PNP     | PNP transistor                                    | TID     | total ionizing dose                      |
| ESA     | European Space Agency                                             | PNPN    | PNPN silicon controlled rectifier                 | TM      | test method                              |
| ESCC    | European Space Components Coordination                            | QML     | Qualified Manufacturers List                      | TMR     | triple-modular redundant                 |
| FET     | field-effect transistor                                           | R       | read                                              | TPA     | two-photon absorption                    |
| FIT     | failures in time                                                  | RFID    | radio-frequency identification                    | ULA     | ultra-low alpha                          |
| FPGA    | field-programmable gate array                                     | RHA     | radiation hardness assurance                      | W       | write                                    |
|         |                                                                   |         |                                                   | WL      | wordline                                 |

Providing leading-edge radiation hardened and assured products, solutions from TI meet long operating-life and harsh environment standards. You can rely on our system-level knowledge, continuity of supply, world-class support and design resources to support even the most stringent design requirements.

[www.ti.com/space](http://www.ti.com/space)

**Important Notice:** The products and services of Texas Instruments Incorporated and its subsidiaries described herein are sold subject to TI's standard terms and conditions of sale. Customers are advised to obtain the most current and complete information about TI products and services before placing orders. TI assumes no liability for applications assistance, customer's applications or product designs, software performance, or infringement of patents. The publication of information regarding any other company's products or services does not constitute TI's approval, warranty or endorsement thereof.

The platform bar, Hercules and E2E are trademarks of Texas Instruments. All other trademarks are the property of their respective owners.

© 2019 Texas Instruments Incorporated. All rights reserved.

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, or other requirements. These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale ([www.ti.com/legal/termsofsale.html](http://www.ti.com/legal/termsofsale.html)) or other applicable terms available either on [ti.com](http://ti.com) or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products.

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265  
Copyright © 2020, Texas Instruments Incorporated