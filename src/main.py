from preprocessing import load_data
from analysis import (
    basic_summary,
    failure_summary,
    product_type_analysis,
    failure_based_analysis,
    correlation_analysis
)
from visualization import (
    plot_bar,
    plot_boxplot,
    plot_heatmap,
    plot_scatter,
    PRODUCT_COLORS,
    STATUS_COLORS
)

# ====================================
# 1. 데이터 불러오기
# ====================================
df = load_data("../data/ai4i2020.csv")

# ====================================
# 2. 분석 결과 생성
# ====================================
basic = basic_summary(df)
failure = failure_summary(df)
product = product_type_analysis(df)
failure_based = failure_based_analysis(df)
corr_df = correlation_analysis(df)

# ====================================
# 3. 기본 결과 출력
# ====================================
print("=" * 60)
print("데이터 크기")
print(basic["data_shape"])

print("=" * 60)
print("결측치 확인")
print(basic["missing_values"])

print("=" * 60)
print("기초 통계량")
print(basic["describe_df"])

print("=" * 60)
print(f"설비 고장률 : {failure['failure_rate']:.2f}%")

print("=" * 60)
print("설비 고장 여부")
print(failure["machine_failure_count"])

print("=" * 60)
print("고장 유형별 발생 건수")
print(failure["failure_type_count"])

print("=" * 60)
print("제품 유형별 고장률")
print(product["type_failure_rate"].round(2))

print("=" * 60)
print("설비고장 여부별 평균 토크")
print(failure_based["failure_torque"].round(2))

print("=" * 60)
print("설비고장 여부별 평균 회전속도")
print(failure_based["failure_rpm"].round(2))

print("=" * 60)
print("주요 변수 상관관계")
print(corr_df.round(3))

# ====================================
# 4. 핵심 시각화 저장
# ====================================

# 1) 제품 유형별 고장률
plot_bar(
    product["type_failure_rate"],
    "제품 유형별 설비 고장률",
    "제품 유형",
    "고장률 (%)",
    ["L", "M", "H"],
    PRODUCT_COLORS,
    "../images/01_제품유형별_고장률.png",
    "{:.2f}%"
)

# 2) 설비고장 여부별 평균 토크
plot_bar(
    failure_based["failure_torque"],
    "설비고장 여부별 평균 토크",
    "설비 상태",
    "평균 토크(Nm)",
    ["정상", "고장"],
    STATUS_COLORS,
    "../images/02_설비고장여부별_평균토크.png",
    "{:.2f}Nm"
)

# 3) 설비고장 여부별 평균 회전속도
plot_bar(
    failure_based["failure_rpm"],
    "설비고장 여부별 평균 회전속도",
    "설비 상태",
    "평균 회전속도(RPM)",
    ["정상", "고장"],
    STATUS_COLORS,
    "../images/03_설비고장여부별_평균회전속도.png",
    "{:.1f}RPM"
)

# 4) 주요 변수 상관관계 Heatmap
plot_heatmap(
    corr_df,
    "../images/04_주요변수_상관관계_Heatmap.png"
)

# 5) 설비고장 여부별 토크 분포 Box Plot
plot_boxplot(
    df,
    "토크(Nm)",
    "설비고장",
    "설비고장 여부별 토크 분포",
    "설비 상태",
    "토크(Nm)",
    ["정상", "고장"],
    "../images/05_설비고장여부별_토크_BoxPlot.png"
)

# 6) 회전속도와 토크 산점도
plot_scatter(
    df,
    "../images/06_회전속도_토크_설비고장_산점도.png"
)