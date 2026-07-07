import matplotlib.pyplot as plt
import seaborn as sns

# ====================================
# 공통 그래프 설정
# ====================================
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

PRODUCT_COLORS = ["#4E79A7", "#F28E2B", "#59A14F"]
STATUS_COLORS = ["#4E79A7", "#D9534F"]


def plot_bar(
    series,
    title,
    xlabel,
    ylabel,
    labels,
    colors,
    save_path,
    value_format="{:.2f}"
):
    plt.figure(figsize=(8, 5))

    bars = plt.bar(
        labels,
        series.values,
        color=colors,
        width=0.30
    )

    plt.title(title, fontsize=15)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # 막대가 너무 두꺼워 보이지 않도록 x축 여백 직접 설정
    plt.xlim(-0.6, len(labels) - 0.4)

    plt.grid(
        axis="y",
        linestyle="--",
        alpha=0.4
    )

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    offset = max(series.values) * 0.02

    for bar in bars:
        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + offset,
            value_format.format(height),
            ha="center",
            fontsize=9
        )

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()


def plot_boxplot(
    df,
    column,
    by,
    title,
    xlabel,
    ylabel,
    xticklabels,
    save_path
):
    fig, ax = plt.subplots(figsize=(8, 5))

    df.boxplot(
        column=column,
        by=by,
        grid=False,
        ax=ax
    )

    ax.set_title(title)
    fig.suptitle("")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    if xticklabels:
        ax.set_xticklabels(xticklabels)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()


def plot_heatmap(corr_df, save_path):
    plt.figure(figsize=(9, 7))

    sns.heatmap(
        corr_df,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        linewidths=0.5
    )

    plt.title("주요 변수 상관관계 Heatmap", fontsize=15)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()


def plot_scatter(df, save_path):
    normal = df[df["설비고장"] == 0]
    failure = df[df["설비고장"] == 1]

    plt.figure(figsize=(8, 6))

    plt.scatter(
        normal["회전속도(RPM)"],
        normal["토크(Nm)"],
        alpha=0.25,
        label="정상"
    )

    plt.scatter(
        failure["회전속도(RPM)"],
        failure["토크(Nm)"],
        alpha=0.8,
        label="고장"
    )

    plt.title("회전속도와 토크에 따른 설비고장 분포", fontsize=15)
    plt.xlabel("회전속도(RPM)")
    plt.ylabel("토크(Nm)")
    plt.legend()

    plt.grid(
        linestyle="--",
        alpha=0.3
    )

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()