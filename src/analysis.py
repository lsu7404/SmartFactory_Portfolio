def basic_summary(df):
    describe_df = df.describe()

    describe_df.rename(index={
        "count": "개수",
        "mean": "평균",
        "std": "표준편차",
        "min": "최소값",
        "25%": "1사분위수",
        "50%": "중앙값",
        "75%": "3사분위수",
        "max": "최대값"
    }, inplace=True)

    return {
        "head_data": df.head(),
        "data_shape": df.shape,
        "missing_values": df.isnull().sum(),
        "describe_df": describe_df
    }


def failure_summary(df):
    failure_columns = [
        "공구마모고장(TWF)",
        "발열고장(HDF)",
        "동력고장(PWF)",
        "과부하고장(OSF)",
        "무작위고장(RNF)"
    ]

    return {
        "failure_rate": df["설비고장"].mean() * 100,
        "machine_failure_count": df["설비고장"].value_counts(),
        "failure_type_count": df[failure_columns].sum()
    }


def product_type_analysis(df):
    return {
        "type_failure_rate": (
            df.groupby("제품유형")["설비고장"]
            .mean()
            .reindex(["L", "M", "H"]) * 100
        )
    }


def failure_based_analysis(df):
    return {
        "failure_torque": df.groupby("설비고장")["토크(Nm)"].mean(),
        "failure_rpm": df.groupby("설비고장")["회전속도(RPM)"].mean()
    }


def correlation_analysis(df):
    corr_columns = [
        "외기온도(K)",
        "공정온도(K)",
        "회전속도(RPM)",
        "토크(Nm)",
        "공구마모시간(분)",
        "설비고장"
    ]

    return df[corr_columns].corr()