# D&D 5e Monster Challenge Rating Predictor

## Overview
Challenge Rating (CR) in fifth edition Dungeons and Dragons is designed to tell 
Dungeon Masters how dangerous a monster is. In practice the system is widely regarded 
as inconsistent. Two monsters of identical CR can produce encounters of dramatically 
different difficulty, and the underlying reasons for this discrepancy have not been 
formally examined through data analysis. This project applies machine learning to 
investigate whether a monster's raw stat block can predict its CR and to identify 
which stats actually drive the official rating system.

## Goals
This project aims to investigate whether raw stat blocks can reliably predict official 
Challenge Ratings, identify which stats drive the rating system, and deliver a practical 
homebrew validator that Dungeon Masters can use to evaluate custom monster designs 
against a model trained on official fifth edition monsters.

## Key Findings
The model achieves an $R^2$ of $0.97$ and a Mean Absolute Error ($MAE$) of $0.75$ CR levels, 
confirming that raw stat blocks largely determine CR. Hit Points alone accounts for 
$88.4%$ of predictive power, revealing the CR system as fundamentally an HP scaling 
system. Dexterity contributes only $0.5%$ to model predictions despite its direct 
relevance to combat difficulty, suggesting the official system ignores this stat. Together these 
findings inform a practical validator that flags when a homebrew monster's stats suggest a CR 
meaningfully different from the designer's intent.

## Tools and Libraries
| Library      | Version | Source             |
|--------------|---------|--------------------|
| pandas       | 3.0.2   | pandas.pydata.org  |
| numpy        | 2.4.4   | numpy.org          |
| matplotlib   | 3.10.9  | matplotlib.org     |
| seaborn      | 0.13.2  | seaborn.pydata.org |
| scikit-learn | 1.8.0   | scikit-learn.org   |
| Python       | 3.12    | python.org         |

## Data Source
Dataset: D&D 5e Monster Stats
Owner: Jairo Hernandez
Source: https://www.kaggle.com/datasets/jairohernandez/d-and-d-5e-monster-stats?select=DnD5e_Monsters_Stats.csv

## Project Status
Core analysis complete. Streamlit application in development.

## Development Log
| Date         | Milestone                                                                                           |
|--------------|-----------------------------------------------------------------------------------------------------|
| May 4, 2026  | Project created: environment setup, repository initialized                                          |
| May 4, 2026  | Dataset identified: D&D 5e Monster Stats sourced from Kaggle                                        |
| May 4, 2026  | Dataset downloaded: DnD_5e_Monsters_Stats.csv added to project                                      |
| May 4, 2026  | Exploratory data analysis begun: CR distribution and feature correlations                           |
| May 4, 2026  | Scatter plots complete: DEX finding confirmed visually, model trained successfully                  |
| May 7, 2026  | Model Evaluated: MAE 0.75, R2 0.97, feature importance analysis complete                            |
| May 8, 2026  | Notebook restructured into lab report format with: abstract, discussion, conclusion, and references |
| May 18, 2026 | Notebook formatting and text edits: LaTeX notation, italics, and structural cleanup                 |
| May 19, 2026 | Model exported to .pkl file, Streamlit app development begun, README.md updated                     |
| June 9, 2026 | Added requirements.txt for reproducibility                                                          |

## Author
Jory Pitts | BS Computational Data Science | Graduating Fall 2027
GitHub: jpitts-dev