
import streamlit as st
from pathlib import Path
from io import BytesIO
from PIL import Image, ImageDraw

st.set_page_config(
    page_title="Cell Vision",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT_DIR = Path(__file__).resolve().parent
IMAGE_DIR = ROOT_DIR / "images"

ORGANELLES = {
    "핵": ("nucleus.png", "pages/1_핵.py"),
    "리보솜": ("ribosome.png", "pages/2_리보솜.py"),
    "미토콘드리아": ("mitochondria.png", "pages/3_미토콘드리아.py"),
    "소포체": ("er.png", "pages/4_소포체.py"),
    "골지체": ("golgi.png", "pages/5_골지체.py"),
    "리소좀": ("lysosome.png", "pages/6_리소좀.py"),
    "세포막": ("membrane.png", "pages/7_세포막.py"),
    "세포질": ("cytosol.png", "pages/8_세포질.py"),
    "세포골격": ("cytoskeleton.png", "pages/9_세포골격.py"),
}

CELL_IMAGE = IMAGE_DIR / "cell.png"

# 화면 디자인
st.markdown(
    """
    <style>
    .stApp {
        background-color: #101820;
        color: #F1F5F9;
    }

    [data-testid="stSidebar"] {
        background-color: #17232E;
    }

    [data-testid="stSidebar"] * {
        color: #F1F5F9;
    }

    .block-container {
        max-width: 1500px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3, p {
        color: #F1F5F9;
    }

    /* 소기관 이름을 흰색으로 표시 */
    [data-testid="stPageLink"] a,
    [data-testid="stPageLink"] a p {
        color: #FFFFFF !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        text-decoration: none !important;
        justify-content: center !important;
        text-align: center !important;
        padding: 0.1rem 0 !important;
        min-height: 0 !important;
        font-size: 0.95rem !important;
        font-weight: 500 !important;
    }

    [data-testid="stPageLink"] a:hover,
    [data-testid="stPageLink"] a:hover p {
        color: #7DD3FC !important;
        text-decoration: underline !important;
    }

    .cell-caption {
        color: #FFFFFF;
        text-align: center;
        font-size: 1.05rem;
        margin-top: 0.4rem;
    }

    @media (max-width: 768px) {
        .block-container {
            padding-left: 0.4rem;
            padding-right: 0.4rem;
        }

        [data-testid="stPageLink"] a,
        [data-testid="stPageLink"] a p {
            font-size: 0.75rem !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def make_circle_image(image_path, size=400):
    """
    이미지를 정사각형 캔버스에 맞춘 후 원형으로 표시합니다.
    원본 비율을 유지하므로 이미지가 가로세로로 늘어나지 않습니다.
    """
    with Image.open(image_path) as source:
        image = source.convert("RGBA")

    # 원본 비율을 유지하면서 캔버스 안에 맞춤
    image.thumbnail((size, size), Image.Resampling.LANCZOS)

    # 투명한 정사각형 캔버스 생성
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))

    # 이미지 중앙 배치
    x = (size - image.width) // 2
    y = (size - image.height) // 2
    canvas.alpha_composite(image, (x, y))

    # 원형 마스크 생성
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size - 1, size - 1), fill=255)

    # 원형 바깥쪽을 투명하게 처리
    alpha = canvas.getchannel("A")
    from PIL import ImageChops
    canvas.putalpha(ImageChops.multiply(alpha, mask))

    return canvas


def show_circle_image(image_path, width):
    """원형 이미지를 변환해 표시합니다."""
    if not image_path.is_file():
        st.warning(
            f"이미지를 찾을 수 없습니다: images/{image_path.name}"
        )
        return

    try:
        circular_image = make_circle_image(image_path)

        buffer = BytesIO()
        circular_image.save(buffer, format="PNG")
        buffer.seek(0)

        st.image(buffer, width=width)

    except Exception as error:
        st.error(f"{image_path.name} 이미지를 표시하지 못했습니다.")
        st.caption(str(error))


def show_organelle(name):
    """작은 원형 소기관 이미지와 이름을 표시합니다."""
    image_name, page_path = ORGANELLES[name]
    image_path = IMAGE_DIR / image_name

    show_circle_image(image_path, width=85)

    # 소기관 이름을 누르면 해당 페이지로 이동
    st.page_link(
        page_path,
        label=name,
        icon=None,
        use_container_width=True,
    )


# 제목
st.title("Cell Vision")
st.write("세포를 구성하는 소기관을 선택해 구조와 기능을 알아보세요.")
st.divider()

# 위쪽 소기관
top = st.columns(5, gap="small")

with top[0]:
    st.empty()
with top[1]:
    show_organelle("핵")
with top[2]:
    show_organelle("리보솜")
with top[3]:
    show_organelle("미토콘드리아")
with top[4]:
    st.empty()

st.write("")

# 위쪽 양옆 소기관
upper_sides = st.columns(5, gap="small")

with upper_sides[0]:
    show_organelle("소포체")
with upper_sides[1]:
    st.empty()
with upper_sides[2]:
    st.empty()
with upper_sides[3]:
    st.empty()
with upper_sides[4]:
    show_organelle("골지체")

st.write("")

# 중앙 세포 이미지와 양옆 소기관
middle = st.columns(
    [1.1, 0.2, 3.8, 0.2, 1.1],
    gap="small",
)

with middle[0]:
    show_organelle("리소좀")

with middle[1]:
    st.empty()

with middle[2]:
    if CELL_IMAGE.is_file():
        # 전체 세포 이미지는 크게, 원형으로 표시
        show_circle_image(CELL_IMAGE, width=440)

        st.markdown(
            '<div class="cell-caption">동물세포</div>',
            unsafe_allow_html=True,
        )
    else:
        st.warning(
            "전체 세포 이미지를 찾을 수 없습니다. "
            "images/cell.png 파일이 있는지 확인해 주세요."
        )

with middle[3]:
    st.empty()

with middle[4]:
    show_organelle("세포막")

st.write("")

# 아래쪽 소기관
bottom = st.columns(5, gap="small")

with bottom[0]:
    st.empty()
with bottom[1]:
    show_organelle("세포질")
with bottom[2]:
    st.empty()
with bottom[3]:
    show_organelle("세포골격")
with bottom[4]:
    st.empty()
