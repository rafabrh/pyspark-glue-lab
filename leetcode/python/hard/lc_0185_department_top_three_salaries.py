"""
LeetCode: 185 - department_top_three_salaries
Difficulty: hard
Pattern: SQL

Idea:   
- <fill>    
    
Complexity:
- Time: O(?)
- Space: O(?)

Pitfalls:
- <fill>
"""

import pandas as pd

def solve(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge with Department to get the department's name
    df = employee.merge(
        department, 
        left_on='departmentId', 
        right_on='id', 
        suffixes=('_emp', '_dept')
    )
    
    # Calculate the dense rank of salary for each department
    df['rank'] = df.groupby('departmentId')['salary'].rank(method='dense', ascending=False)
    
    # Filter only the top 3 highest unique salaries
    top_3_df = df[df['rank'] <= 3]
    
    # Select the required columns and rename them to match the expected output
    result = top_3_df[['name_dept', 'name_emp', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']
    
    return result
