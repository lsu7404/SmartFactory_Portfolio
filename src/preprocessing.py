import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)

    df.columns = [
        "데이터번호",
        "제품ID",
        "제품유형",
        "외기온도(K)",
        "공정온도(K)",
        "회전속도(RPM)",
        "토크(Nm)",
        "공구마모시간(분)",
        "설비고장",
        "공구마모고장(TWF)",
        "발열고장(HDF)",
        "동력고장(PWF)",
        "과부하고장(OSF)",
        "무작위고장(RNF)"
    ]

    return df