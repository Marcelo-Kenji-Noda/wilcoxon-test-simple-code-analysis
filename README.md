## Simple Wilcoxon Signed-Rank Test Script

### Problem Description

The Wilcoxon test compares the difference between two paired samples. In this scenario, the paired samples represent measurements taken on the same samples. The first set of measurements is conducted by observer A, while the second set is conducted by observer B.

The null hypothesis (H0) tested by the Wilcoxon test is:

- H0: The measurements conducted by observer A are equal to the measurements conducted by observer B.
- H1: The measurements conducted by observer A are not equal to the measurements conducted by observer B.

Let's consider a significance level of 0.05. If the p-value is smaller than 0.05, we reject the null hypothesis; otherwise, we fail to reject the null hypothesis.

### Results

**Values:**
- Median value for counts by observer A = MD_A
- Median value for counts by observer B = MD_B

**Tests Results:**
- p-value = p
- Effect size (r) = r which is considered small according to Cohen (1988)

Since the p-value is greater than 0.05, we fail to reject the null hypothesis. Therefore, there is no significant difference between the paired samples. ( Or Since the p-value is smaller than 0.05 we reject the null hypothesis. Therefore, there is a significant difference between the paired samples )

### Source Code

#### Configurations

```
[files]
data_filepath: str (File path)
columns: list[str] (Columns to be tested)

[statistical_test]
significance: float (Significance level of test)
```

#### Executing the Script

Execute the following command in the command line: ```python src/main.py```

#### Output

Output values:

```
Sample size = {dataframe.shape[0]}
P-value = {p_value}
```

If p < significance value:

```
Reject the null hypothesis. There is a significant difference between those two columns.
```

Else:

```
Fail to reject the null hypothesis. There is no significant difference between those two columns.
```

### Sources

- [Tutorial: Wilcoxon Test](https://datatab.net/tutorial/wilcoxon-test)
- [SciPy Documentation: scipy.stats.wilcoxon](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html)