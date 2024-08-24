# Microprocessor Heat Dissipation Simulation

Link to report: https://github.com/arantruslove/Microprocessor-Heat-Dissipation/blob/pictorial/Report.pdf

## Project Overview

This project investigates the heat dissipation of a 2D microprocessor model using computational methods. By solving Poisson’s equation for heat conduction, the simulation aims to estimate the average operating temperature of a microprocessor under various cooling scenarios, including attachment to a ceramic case, heat sink, and exposure to natural or forced convection.

## Key Features

- **Finite Difference Method:**
  - Utilized to solve Poisson’s equation for heat conduction in a microprocessor system.
  
- **Cooling Scenarios:**
  - Evaluated different setups including natural convection, forced convection, and variations in heat sink dimensions.

- **Optimization:**
  - Determined the minimal heat sink footprint required to keep the microprocessor operating below 80°C under forced convection.

## Results

- **Natural Convection:**
  - No configurations could keep the microprocessor below 100°C, emphasizing the need for active cooling methods.

- **Forced Convection:**
  - A configuration with a heat sink width of 49 mm and a fin height of 53 mm (including the base) successfully reduced the mean operating temperature to 72 ± 7°C. This system footprint of 1495 mm² suggests potential integration with desktop computers.

## Conclusion

The project demonstrated the importance of heat sink design and active cooling in managing microprocessor temperatures. Despite limitations such as the use of a 2D model, the simulation provided valuable insights into optimizing microprocessor cooling systems.
