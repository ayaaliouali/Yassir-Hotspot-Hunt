# Yassir Hotspot Hunt

This repository contains the Python script used to solve the **Yassir Taxi Hotspot Challenge**.

## Overview

The challenge involves analyzing a taxi dataset to detect **hidden clusters of trips** and uncover the **real hotspot**. The dataset contains decoys and shifted coordinates, and the real hotspot is derived from the **earliest valid cluster of fares**.

## Files

- `yassir.py` – Python script that:
  - Detects all valid clusters following the challenge rules.
  - Identifies the earliest valid cluster.
  - Decodes fares to compute the real hotspot coordinates in Batna.
  - Outputs a Google Maps link to verify the hotspot location.

- `taxi_hotspot_dataset.csv` –  dataset used in the challenge.

## How to Run
1. Install dependencies:

```bash
pip install pandas
Run the script:

bash
python yassir.py
