import pandas as pd
import numpy as np

def anagram(df):
	df['word1sorted'] = df['Word 1'].apply(lambda x: sorted(x.lower()))
	df['word2sorted'] = df['Word 2'].apply(lambda x: sorted(x.lower()))
	df['Anagram?'] = np.where(df["word1sorted"] == df["word2sorted"], 'Yes', 'No')

	return(df)

def get_output_schema():
	return pd.DataFrame({
  	 'Word 1' : prep_string()
 	,'Word 2' : prep_string()
 	,'Anagram?' : prep_string()
 	})