
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Cell Vision - 리소좀",
    layout="wide"
)

# 프로젝트 경로 설정
ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_DIR = ROOT_DIR / "images"
IMAGE_PATH = IMAGE_DIR / "lysosome.png"

st.markdown("""
<style>
.stApp {
    background: #101820;
    color: #F1F5F9;
}
[data-testid="stSidebar"] {
    background: #17232E;
}
[data-testid="stHeader"] {
    background: #101820;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1150px;
}
h1, h2, h3 {
    color: #F1F5F9 !important;
}
p, li, span, label {
    color: #D9E2EC;
}
.overview {
    background: #17232E;
    border-left: 4px solid #63B3ED;
    border-radius: 8px;
    padding: 18px 22px;
    line-height: 1.8;
    color: #E2E8F0;
}
.article-section {
    margin-top: 30px;
    line-height: 1.9;
}
.article-section h2 {
    border-bottom: 1px solid #344454;
    padding-bottom: 9px;
    margin-bottom: 15px;
}
.article-section h3 {
    color: #90CDF4 !important;
    margin-top: 22px;
    margin-bottom: 8px;
}
div.stButton > button {
    background: #233647;
    color: #F1F5F9;
    border: 1px solid #52677A;
    border-radius: 8px;
}
div.stButton > button:hover {
    background: #304B61;
    color: #FFFFFF;
    border-color: #90CDF4;
}
hr {
    border-color: #344454;
}
</style>
""", unsafe_allow_html=True)

# 메인 화면으로 돌아가기
if st.button("← 메인 화면으로 돌아가기"):
    st.switch_page("app.py")

st.title("리소좀")
st.caption("Lysosome · 세포 내 물질을 분해하고 재활용하는 소기관")

st.divider()

image_col, overview_col = st.columns(
    [1, 1.25],
    gap="large"
)

with image_col:
    st.subheader("리소좀 이미지")

    # 임시 진단: 실제 실행 경로와 파일 존재 여부 확인
    st.markdown("#### 이미지 경로 진단")

    st.code(
        f"현재 페이지: {Path(__file__).resolve()}\n"
        f"프로젝트 경로: {ROOT_DIR}\n"
        f"이미지 폴더: {IMAGE_DIR}\n"
        f"이미지 파일: {IMAGE_PATH}",
        language="text"
    )

    st.write("이미지 폴더 존재 여부:", IMAGE_DIR.is_dir())
    st.write("이미지 파일 존재 여부:", IMAGE_PATH.is_file())

    if IMAGE_DIR.is_dir():
        st.write(
            "실제로 확인되는 이미지 폴더의 파일 목록:"
        )
        st.write(
            sorted(
                file.name
                for file in IMAGE_DIR.iterdir()
                if file.is_file()
            )
        )
    else:
        st.warning(
            "현재 계산된 위치에 images 폴더가 없습니다."
        )

    if IMAGE_PATH.is_file():
        try:
            st.image(
                str(IMAGE_PATH),
                width="stretch"
            )
            st.success("리소좀 이미지를 정상적으로 읽었습니다.")
        except Exception as error:
            st.error("이미지 파일을 읽는 중 오류가 발생했습니다.")
            st.exception(error)
    else:
        st.error(
            "이미지를 찾을 수 없습니다: "
            f"{IMAGE_PATH}"
        )

with overview_col:
    st.subheader("개요")
    st.markdown("""
    <div class="overview">
    리소좀은 막으로 둘러싸인 소기관으로, 내부에 여러 가수분해 효소를
    가지고 있다. 내부는 세포질보다 산성인 환경으로 유지되어 효소가
    물질을 분해하기에 적합하다. 리소좀은 세포 안으로 들어온 물질과
    오래되거나 손상된 세포 구성 요소를 분해하고, 그 결과물을
    세포가 다시 이용할 수 있도록 돕는다.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div class="article-section">

## 구조

### 리소좀 막

리소좀은 단일 막으로 둘러싸여 있다. 막은 분해 효소와 분해 중인
물질을 세포질과 구분하여 세포의 다른 구성 요소가 불필요하게
분해되는 것을 방지한다. 막에는 수소 이온을 내부로 이동시키는
단백질과 분해 산물을 세포질로 운반하는 단백질이 존재한다.

### 가수분해 효소

리소좀에는 단백질, 핵산, 지질, 탄수화물 등을 분해하는 여러
가수분해 효소가 존재한다. 이 효소들은 물을 이용해 큰 분자의
화학 결합을 끊고 작은 분자로 분해한다.

### 산성 내부 환경

리소좀 내부는 세포질보다 낮은 pH를 유지한다. 막 단백질이
수소 이온을 내부로 운반하여 산성 환경을 만든다. 많은 리소좀
효소는 이러한 환경에서 높은 활성을 보인다.

## 주요 기능

### 세포 내 소화

세포가 세포내섭취로 받아들인 물질은 소낭에 담겨 세포 안으로
들어온다. 이 소낭이 리소좀과 융합하면 효소가 물질을 분해한다.
분해 결과로 생성된 작은 분자 중 일부는 세포질로 이동해 다시 사용된다.

### 손상된 세포 구성 요소의 제거

세포 내부의 단백질과 소기관은 시간이 지나면서 손상되거나 기능이
저하될 수 있다. 리소좀은 이러한 구성 요소의 분해와 재활용에
관여하여 세포 내부 환경을 유지한다.

### 물질 재활용

분해된 아미노산, 당, 지방산 등의 일부는 세포의 대사 과정에
다시 이용될 수 있다. 따라서 리소좀은 불필요한 물질을 제거하는
동시에 세포가 필요한 물질을 회수하도록 돕는다.

## 작동 원리

### 물질을 소낭에 담기

세포는 세포막을 안쪽으로 함입하여 세포 밖의 물질을 소낭 안에
받아들일 수 있다. 이러한 세포내섭취를 통해 들어온 물질은
세포 내부의 소낭 이동 경로를 거친다.

### 소낭과 리소좀의 융합

물질을 담은 소낭이 리소좀 또는 리소좀으로 이어지는 구획과
융합하면 분해 효소가 작용할 수 있는 환경이 형성된다. 효소는
물질을 더 작은 분자로 분해하며, 분해된 산물은 운반 단백질을
통해 세포질로 이동할 수 있다.

### 자가포식

자가포식은 세포 내부의 일부 구성 요소를 막으로 둘러싸
분해 경로로 보내는 과정이다. 이 과정에서 손상된 소기관이나
오래된 세포 구성 요소가 분해되고, 그 성분이 재활용될 수 있다.
자가포식은 세포의 상태와 영양 조건 등에 따라 조절된다.

## 다른 세포소기관과의 관계

### 소포체

리소좀의 분해 효소를 구성하는 단백질은 리보솜에서 합성되어
소포체로 들어간다. 소포체에서 접힘과 초기 가공을 거친 뒤
골지체로 전달된다.

### 골지체

골지체는 리소좀으로 보내질 효소를 가공하고 분류한다.
이후 운반 소낭과 세포 내 막 수송 경로를 통해 효소가 적절한
구획에 전달되어 리소좀의 기능이 유지된다.

### 세포막

세포막은 세포내섭취를 통해 물질을 세포 안으로 받아들인다.
그 물질이 리소좀의 분해 경로로 전달되면 세포는 외부에서
들어온 물질을 분해하고 필요한 성분을 회수할 수 있다.

</div>
""", unsafe_allow_html=True)
