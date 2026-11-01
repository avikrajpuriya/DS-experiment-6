# Experiment 6 -- Statistical Distribution Analysis

## Title

Analyzing and Interpreting Statistical Distributions

## Aim

To analyze and interpret the probability distributions of numerical
variables in the urban climate dataset using graphical and statistical
techniques.

## Dataset

This experiment uses `urban_climate.csv`.

The dataset contains urban climate measurements such as: - Temperature -
Humidity - Precipitation - Wind speed - Urban heat island intensity

> Note: The experiment handout refers to robotic sensor measurements.
> For this practical, the same statistical distribution analysis is
> applied to the urban climate dataset.

## Software and Libraries Required

-   Python 3.x
-   Jupyter Notebook
-   NumPy
-   Pandas
-   Matplotlib
-   SciPy
-   Seaborn (if used in the notebook)

## Files

-   `urban_climate.csv` -- Dataset used for analysis.
-   `Data_Science_Experiment_6.ipynb` -- Jupyter Notebook containing the
    practical code and analysis.
-   `README.md` -- Instructions and experiment information.

## Activities Performed

1.  Load the urban climate dataset.
2.  Select suitable numerical attributes.
3.  Calculate mean, median and standard deviation.
4.  Plot histograms for selected variables.
5.  Generate density plots.
6.  Calculate skewness and kurtosis.
7.  Identify potential outliers.
8.  Compare observed data with a suitable theoretical distribution, such
    as the normal distribution.
9.  Interpret the distribution of selected variables.
10. Discuss how distribution characteristics can affect data analysis.

## Installation

Open a terminal or command prompt and install the required libraries:

``` bash
python -m pip install numpy pandas matplotlib scipy seaborn jupyter
```

## How to Run

1.  Extract the experiment ZIP file.
2.  Keep `urban_climate.csv` and `Data_Science_Experiment_6.ipynb` in
    the same folder.
3.  Open a terminal in that folder.
4.  Start Jupyter Notebook:

``` bash
jupyter notebook
```

5.  Open `Data_Science_Experiment_6.ipynb`.
6.  Run the notebook cells from top to bottom using **Run All** or
    `Shift + Enter`.

If the notebook uses a different filename, use the exact notebook
filename included in your folder. Make sure the CSV filename in the
loading cell is `urban_climate.csv`.

## Expected Outputs

The notebook generates statistical summaries and visualizations,
including: - Mean, median and standard deviation table - Histograms -
Density plots - Skewness and kurtosis values - Potential outlier
results - Normal distribution comparison - Interpretation of the
selected variables

## Conclusion

The statistical distributions of selected urban climate variables are
analyzed using numerical and graphical methods. The analysis helps
understand their spread, shape, skewness, kurtosis and possible
outliers.

## References

-   Douglas C. Montgomery and George C. Runger, *Applied Statistics and
    Probability for Engineers*.
-   Jake VanderPlas, *Python Data Science Handbook*.
-   SciPy Documentation: https://docs.scipy.org/doc/scipy/
-   Matplotlib Documentation: https://matplotlib.org/stable/
-   Pandas Documentation: https://pandas.pydata.org/docs/
