---
type: Test Operations / Testing Facilities / Facility Capabilities
title: HIAF-SIBL Radiation-Testing Capabilities
description: Provider-stated beam, chamber, positioning, feedthrough, monitoring,
  mounting, access, and fee capabilities relevant to electronics radiation tests.
tags:
- facility
- capability
- beam
- let
- dosimetry
- electronics
timestamp: '2026-08-09T05:55:24Z'
---
The following values are transcribed from the HIAF-SIBL brochure and should be confirmed with the facility when planning a campaign. They describe available infrastructure, not test acceptance criteria.

# Beam species, energy, LET, and range
The brochure states particle beams from protons up to 28 MeV through gold ions up to 350 MeV, with intermediate species and energies used to obtain desired linear energy transfer (LET). Its selected maximum-energy table is reproduced below; surface LET and range in silicon were calculated with SRIM by the brochure authors.

| Species | Max E (MeV) | Max E/A (MeV/amu) | Surface LET in Si (MeV/(mg/cm²)) | Range in Si (µm) |
| --- | ---: | ---: | ---: | ---: |
| ¹H | 28.15 | 28.15 | 0.02 | 4372.00 |
| ¹²C | 98.15 | 8.18 | 1.48 | 175.58 |
| ¹⁶O | 126.15 | 7.88 | 2.64 | 134.32 |
| ²⁴Mg | 172.63 | 7.19 | 5.76 | 92.62 |
| ⁴⁰Ca | 228.35 | 5.71 | 15.59 | 53.87 |
| ⁵⁸Ni | 279.60 | 4.82 | 27.67 | 46.03 |
| ⁶³Cu | 279.60 | 4.44 | 30.08 | 42.42 |
| ⁹³Nb | 311.80 | 3.35 | 26.74 | 51.13 |
| ¹⁹⁷Au | 349.89 | 1.78 | 85.49 | 29.85 |

# Flux, area, chamber, and positioning
- Stated flux range: 10 to 10¹² ions/cm²/s; achievable values can vary with beam energy and facility radiation-safety limits.
- The brochure states no facility-imposed total-fluence limit, while noting that higher fluence increases irradiation time.
- Raster magnet beam spot: 1 × 1 mm to 70 × 70 mm; downstream 40 × 40 mm slits constrain the uniform user-defined beam area to 1 × 1 mm through 40 × 40 mm.
- Maximum component or multi-board envelope: 250 × 200 mm.
- Total possible irradiation area using stage motion: 220 × 200 mm.
- All testing is under vacuum.
- The remotely controlled stage translates in x and y and rotates to tilt the board and vary beam incidence angle.

# Electrical access and mounts
Interchangeable vacuum feedthrough plates let users operate and communicate with a device under test. The brochure lists 12 SMA female/female connectors rated to 18 GHz, 6 reversible DSUB-25 male/male connectors, 2 Ethernet interfaces, 2 USB 3.0 Type-A female/female connectors, and 10 BNC connectors; custom plates may be possible.

Available mounts are described as:
- A material/solar-cell plate for fifteen 20 × 20 mm samples, with clearance for the silicon detector.
- An electronics pinboard with a 25 mm grid of M4 threaded holes; the brochure says this mount is incompatible with use of the energy detectors.

# Dosimetry and monitoring
- Low-flux monitoring: scintillators with silicon photomultipliers (SiPMs).
- High-flux monitoring: beam profile monitor.
- Available detector: silicon ΔE–E telescope comprising two stacked silicon surface-barrier detectors, compatible with the material-sample mount.

These are facility equipment statements; the brochure does not itself define a standards-compliant dosimetry method, uncertainty budget, calibration traceability, or device-specific test protocol.

# Access, support, and fees
- Enquiries, tours, requirement discussions, and booking guidance are offered through `userengagement.hiaf@anu.edu.au`.
- Daily fees stated in the brochure: $3,000–$12,000 depending on user category; the brochure text does not identify the currency.
- One beam-time day represents 16 hours of operation with dedicated physicist and technical support.
- Industry users are stated to incur a one-time $2,500 setup/consultation fee, irrespective of test-day count; the brochure text does not identify the currency and directs users to request the detailed pricing guide.
- Current availability, beam schedules, technical configuration, fee currency, and final quotation require direct confirmation.

# Related concepts
- [HIAF-SIBL](../hiaf-sibl.md)
- [Service and certification boundary](hiaf-sibl-service-boundary.md)
- [Single Event Effects Test](../../testing-methods-procedures/single-event-effects-test.md)
- [Radiation Effects Test Program](../../../test-plans/radiation-effects-test-program.md)

# SRIM citation
Ziegler, J. F., Ziegler, M., & Biersack, J. (2010). “SRIM – The stopping and range of ions in matter (2010).” *Nuclear Instruments and Methods in Physics Research Section B*, 268(11–12), 1818–1823. [https://doi.org/10.1016/j.nimb.2010.02.091](https://doi.org/10.1016/j.nimb.2010.02.091)

# Citations
- [HIAF-SIBL Radiation Testing Capabilities Brochure](hiaf-sibl-brochure.md)
