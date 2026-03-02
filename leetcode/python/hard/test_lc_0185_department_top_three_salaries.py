from lc_0185_department_top_three_salaries import solve

import pandas as pd

def test_basic():
    # Input Employee table
    employee_data = {
        'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        'name': ['Joe', 'Henry', 'Sam', 'Max', 'Janet', 'Randy', 'Will', 'Alice', 'Bob', 'Charlie', 'David'],
        'salary': [85000, 80000, 60000, 90000, 69000, 85000, 70000, 100000, 110000, 120000, 130000],
        'departmentId': [1, 2, 2, 1, 1, 1, 1, 3, 3, 3, 3]
    }
    employee_df = pd.DataFrame(employee_data)

    # Input Department table
    department_data = {
        'id': [1, 2, 3],
        'name': ['IT', 'Sales', 'Marketing']
    }
    department_df = pd.DataFrame(department_data)

    # Expected Result table
    expected_data = {
        'Department': ['IT', 'IT', 'IT', 'IT', 'Sales', 'Sales', 'Marketing', 'Marketing', 'Marketing'],
        'Employee': ['Max', 'Joe', 'Randy', 'Will', 'Henry', 'Sam', 'David', 'Charlie', 'Bob'],
        'Salary': [90000, 85000, 85000, 70000, 80000, 60000, 130000, 120000, 110000]
    }
    expected_df = pd.DataFrame(expected_data)

    # Call the solution
    result_df = solve(employee_df, department_df)

    # Sort both to compare them properly regardless of order
    result_df = result_df.sort_values(by=['Department', 'Salary', 'Employee'], ascending=[True, False, True]).reset_index(drop=True)
    expected_df = expected_df.sort_values(by=['Department', 'Salary', 'Employee'], ascending=[True, False, True]).reset_index(drop=True)

    # Print friendly messages
    for dept in result_df['Department'].unique():
        dept_df = result_df[result_df['Department'] == dept]
        
        # Sort salaries in descending order here to guarantee Highest -> Lowest output order
        salaries = sorted(dept_df['Salary'].unique(), reverse=True)
        print(f"\n--- Departamento: {dept} ---")
        
        # Helper variables to print ranks based on unique salaries
        rank = 1
        for salary in salaries:
            employees_with_salary = dept_df[dept_df['Salary'] == salary]['Employee'].tolist()
            employees_str = ", ".join(employees_with_salary)
            
            if rank == 1:
                print(f"Maior salário: {salary} ({employees_str})")
            elif rank == 2:
                print(f"Segundo maior salário: {salary} ({employees_str})")
            elif rank == 3:
                print(f"Terceiro maior salário: {salary} ({employees_str})")
            
            rank += 1

    pd.testing.assert_frame_equal(result_df, expected_df)
        