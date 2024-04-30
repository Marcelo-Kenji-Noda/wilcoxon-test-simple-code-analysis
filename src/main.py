import pytoml as toml
import pandas as pd
import numpy as np
from scipy.stats import wilcoxon

def wilcoxon_signed_rank_test(df: pd.DataFrame, columns: list[str]):
    """
    Perform Wilcoxon signed-rank test to compare paired samples.
    
    Parameters:
    df (pd.DataFrame): Dataframe containing the columns to be tested
    columns (list): List of columns to be tested
    
    Returns:
    (float, float): Tuple containing the test statistic and p-value.
    """
    # Perform Wilcoxon signed-rank test
    if len(columns) != 2:
        AssertionError(f"The number of columns given is {len(columns)}, expected 2")
    return wilcoxon(df[columns[0]], df[columns[1]])
    
def print_summary_informations(dataframe:pd.DataFrame,statistic:float, pvalue:float, zstatistic: float, columns: list) -> None:
    """
    Print some informations about the data and the test
    Args:
        dataframe (pd.DataFrame): Dataframe
        z_value (float): Z-value for the Wilcoxon test
        columns (list): Columns included in the test
    """
    
    print(f"Sample size: {dataframe.shape[0]}")
    for col in columns:
        print(f"Median '{col}': {dataframe[col].median()}")
    print(f"Statistic: {statistic}")
    print(f"P-value: {pvalue}")
    print(f"Effect Size: {abs(zstatistic/np.sqrt(dataframe.shape[0]))}")
    print("==="*10)
    return

def main() -> None:
    # Reading config files
    with open("config.toml","rb") as cfg:
        config = toml.load(cfg)
        
    # Reading dataframe
    dataframe = pd.read_excel(config['files']['data_filpath'], usecols=config['files']['columns'])
    
    # Wilcoxon test
    results = wilcoxon_signed_rank_test(dataframe, config['files']['columns'])
    
    statistic = results.statistic
    p_value = results.pvalue
    zstatistic = results.zstatistic
    ## The Wilcoxon signed-rank test tests the null hypothesis that two related paired samples come from the same distribution. In particular
    ## So if p_value is lower than the significance we reject the null hypothesis
    ## Results:

    print_summary_informations(dataframe=dataframe,statistic=statistic, pvalue=p_value, zstatistic=zstatistic, columns=config['files']['columns'])
    
    if p_value < config['statistical_test']['significance']:
        print("Reject the null hypothesis. There is a significant difference between those two columns.")
    else:
        print("Fail to reject the null hypothesis. There is no significant difference between those two columns")
    return

if __name__ == '__main__':
    main()

    