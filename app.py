
CELL_IMAGE = IMAGE_DIR / "cell.png"

# 화면 디자인
st.markdown(
"""
   <style>
@@ -53,7 +54,7 @@
       color: #F1F5F9;
   }

    /* 모든 소기관 이름은 흰색 */
    /* 소기관 이름을 흰색으로 표시 */
   [data-testid="stPageLink"] a,
   [data-testid="stPageLink"] a p {
       color: #FFFFFF !important;
@@ -100,32 +101,43 @@


def make_circle_image(image_path, size=400):
    """원본 이미지의 중앙을 기준으로 원형 이미지를 만듭니다."""
    """
    이미지를 정사각형 캔버스에 맞춘 후 원형으로 표시합니다.
    원본 비율을 유지하므로 이미지가 가로세로로 늘어나지 않습니다.
    """
with Image.open(image_path) as source:
image = source.convert("RGBA")

    # 정사각형으로 맞춘 후 원형 마스크 적용
    width, height = image.size
    side = min(width, height)
    # 원본 비율을 유지하면서 캔버스 안에 맞춤
    image.thumbnail((size, size), Image.Resampling.LANCZOS)

    left = (width - side) // 2
    top = (height - side) // 2
    # 투명한 정사각형 캔버스 생성
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))

    image = image.crop((left, top, left + side, top + side))
    image = image.resize((size, size), Image.Resampling.LANCZOS)
    # 이미지 중앙 배치
    x = (size - image.width) // 2
    y = (size - image.height) // 2
    canvas.alpha_composite(image, (x, y))

    # 원형 마스크 생성
mask = Image.new("L", (size, size), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, size - 1, size - 1), fill=255)

    image.putalpha(mask)
    return image
    # 원형 바깥쪽을 투명하게 처리
    alpha = canvas.getchannel("A")
    from PIL import ImageChops
    canvas.putalpha(ImageChops.multiply(alpha, mask))

    return canvas


def show_circle_image(image_path, width):
    """원형으로 변환한 이미지를 Streamlit에 표시합니다."""
    """원형 이미지를 변환해 표시합니다."""
if not image_path.is_file():
        st.warning(f"이미지를 찾을 수 없습니다: {image_path.name}")
        st.warning(
            f"이미지를 찾을 수 없습니다: images/{image_path.name}"
        )
return

try:
@@ -147,10 +159,9 @@ def show_organelle(name):
image_name, page_path = ORGANELLES[name]
image_path = IMAGE_DIR / image_name

    # 주변 소기관은 작은 원형 이미지
show_circle_image(image_path, width=85)

    # 이름을 누르면 상세 페이지로 이동
    # 소기관 이름을 누르면 해당 페이지로 이동
st.page_link(
page_path,
label=name,
@@ -159,6 +170,7 @@ def show_organelle(name):
)


# 제목
st.title("Cell Vision")
st.write("세포를 구성하는 소기관을 선택해 구조와 기능을 알아보세요.")
st.divider()
@@ -179,7 +191,7 @@ def show_organelle(name):

st.write("")

# 중앙 위쪽 양옆 소기관
# 위쪽 양옆 소기관
upper_sides = st.columns(5, gap="small")

with upper_sides[0]:
@@ -195,8 +207,11 @@ def show_organelle(name):

st.write("")

# 중앙 세포 이미지와 양쪽 소기관
middle = st.columns([1.1, 0.2, 3.8, 0.2, 1.1], gap="small")
# 중앙 세포 이미지와 양옆 소기관
middle = st.columns(
    [1.1, 0.2, 3.8, 0.2, 1.1],
    gap="small",
)

with middle[0]:
show_organelle("리소좀")
@@ -206,7 +221,7 @@ def show_organelle(name):

with middle[2]:
if CELL_IMAGE.is_file():
        # 전체 세포 이미지도 원형으로 변환
        # 전체 세포 이미지는 크게, 원형으로 표시
show_circle_image(CELL_IMAGE, width=440)

st.markdown(
@@ -216,7 +231,7 @@ def show_organelle(name):
else:
st.warning(
"전체 세포 이미지를 찾을 수 없습니다. "
            "images 폴더에 cell.png 파일이 있는지 확인해 주세요."
            "images/cell.png 파일이 있는지 확인해 주세요."
)

with middle[3]:
