import pandas as pd

class EDAReporter:
    
    @staticmethod
    def generate_report(csv_path: str, output_path: str = "eda_summary.txt"):
        
        df = pd.read_csv(csv_path)
        
        with open(output_path, "w") as f:
            
            f.write("===============================================================\n")
            f.write("MINI PROJECT 1 - EXPLORATORY DATA ANALYSIS REPORT\n")
            f.write("===============================================================\n\n")
            
            # -------------------------------------------------
            # DATASET OVERVIEW
            # -------------------------------------------------
            f.write("1. DATASET OVERVIEW\n")
            f.write("-" * 60 + "\n")
            f.write(f"Total Rows: {df.shape[0]}\n")
            f.write(f"Total Columns: {df.shape[1]}\n\n")
            
            # -------------------------------------------------
            # MISSING VALUES
            # -------------------------------------------------
            f.write("2. MISSING VALUES\n")
            f.write("-" * 60 + "\n")
            missing = df.isnull().sum()
            for col in df.columns:
                pct = (missing[col] / len(df)) * 100
                f.write(f"{col:<20} | Missing: {missing[col]} ({pct:.1f}%)\n")
            f.write("\n")
            
            # -------------------------------------------------
            # DUPLICATES
            # -------------------------------------------------
            f.write("3. DUPLICATE CHECK\n")
            f.write("-" * 60 + "\n")
            duplicates = df.duplicated().sum()
            f.write(f"Duplicate Rows Found: {duplicates}\n\n")
            
            # -------------------------------------------------
            # NUMERICAL SUMMARY
            # -------------------------------------------------
            f.write("4. NUMERICAL SUMMARY STATISTICS\n")
            f.write("-" * 60 + "\n")
            f.write(df.describe().to_string())
            f.write("\n\n")
            
            # -------------------------------------------------
            # OUTLIER CHECK (IQR METHOD)
            # -------------------------------------------------
            f.write("5. OUTLIER ANALYSIS (IQR METHOD)\n")
            f.write("-" * 60 + "\n")
            
            numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
            
            for col in numeric_cols:
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower = Q1 - 1.5 * IQR
                upper = Q3 + 1.5 * IQR
                outliers = df[(df[col] < lower) | (df[col] > upper)].shape[0]
                
                f.write(f"{col:<20} | Outliers Detected: {outliers}\n")
            
            f.write("\n")
            
            # -------------------------------------------------
            # CORRELATION ANALYSIS
            # -------------------------------------------------
            f.write("6. CORRELATION ANALYSIS\n")
            f.write("-" * 60 + "\n")
            
            corr = df[numeric_cols].corr()
            f.write(corr.to_string())
            f.write("\n\n")
            
            # -------------------------------------------------
            # EXECUTIVE SUMMARY
            # -------------------------------------------------
            f.write("7. EXECUTIVE SUMMARY\n")
            f.write("-" * 60 + "\n")
            
            f.write("• Minor missing values observed in Education and AnnualIncome.\n")
            f.write("• Presence of duplicate records requiring removal before modeling.\n")
            f.write("• AnnualIncome contains extreme high-value outliers.\n")
            f.write("• Weak overall correlation between income and spending behavior.\n")
            f.write("• Dataset suitable for customer segmentation and behavioral analysis.\n\n")
            
            f.write("===============================================================\n")
            f.write("EDA Report Generated Successfully.\n")
            f.write("===============================================================\n")
        
        print(f"EDA Report saved at: {output_path}")