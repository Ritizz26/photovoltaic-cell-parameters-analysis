# PV Cell Parameter Analysis

A small Python project for studying how important parameters of a
photovoltaic (PV) cell affect its I-V and power characteristics.

The project uses the single-diode model and numerical methods to
simulate the cell under different parameter values.

## Project Structure

### 1. ideal_parameter_analysis.py

Studies the effect of photogenerated current (Iph) using the
ideal single-diode model.

Iph is varied while the other parameters are kept constant.

### 2. series_resistance_analysis.py

Uses the single-diode model with series and shunt resistance.

The series resistance (Rs) is varied while the other parameters
are kept constant.

### 3. shunt_resistance_analysis.py

Uses the same model but varies the shunt resistance (Rsh).

The other parameters are kept constant.

## Parameters Studied

- Photogenerated current (Iph)
- Series resistance (Rs)
- Shunt resistance (Rsh)

## What is analyzed

For each case, the project compares the simulated I-V curves
and important PV performance parameters such as:

- Short-circuit current (Isc)
- Open-circuit voltage (Voc)
- Maximum power (Pmax)
- Voltage at maximum power (Vmp)
- Current at maximum power (Imp)
- Fill factor (FF)

## Tools

- Python
- NumPy
- Matplotlib
- SciPy

## Purpose

This project was built to understand how changes in the
single-diode model parameters influence PV-cell behavior
through numerical simulation.