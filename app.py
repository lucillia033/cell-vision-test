{"name": "세포골격", "image": "cytoskeleton.png", "page": "pages/9_세포골격.py"},
]

# 소기관 이동 요청을 처리합니다.
# 허용된 페이지로만 이동하도록 페이지 경로를 확인합니다.
# 쿼리 매개변수로 전달된 페이지 이동 요청 처리
page_lookup = {item["page"]: item["page"] for item in ORGANELLES}
requested_page = st.query_params.get("go")

if requested_page in page_lookup:
    st.query_params.clear()
st.switch_page(page_lookup[requested_page])


# 이미지 파일을 HTML에서 사용할 수 있도록 변환
def image_to_data_uri(image_path):
    if not image_path.is_file():
        return None

    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }

    mime_type = mime_types.get(image_path.suffix.lower())
    if mime_type is None:
        return None

    try:
        encoded = base64.b64encode(
            image_path.read_bytes()
        ).decode("utf-8")
        return f"data:{mime_type};base64,{encoded}"
    except OSError:
        return None


# 어두운 테마
st.markdown(
"""
@@ -54,74 +80,83 @@
       background: #17232E;
   }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 1rem;
    }

   h1, p {
       color: #F1F5F9;
   }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 1rem;
    .intro-text {
        color: #B8C5D1;
        text-align: center;
        margin-bottom: 4px;
   }
   </style>
   """,
unsafe_allow_html=True,
)

st.title("Cell Explorer")
st.write("중앙의 세포를 둘러싼 소기관을 선택해 구조와 기능을 탐색해 보세요.")

st.markdown(
"""
    <style>
    .orbit-description {
        text-align: center;
        color: #B8C5D1;
        font-size: 14px;
        margin-bottom: 8px;
    }
    </style>
    <div class="orbit-description">
        소기관 사진을 누르면 상세 페이지로 이동합니다.
    </div>
    <p class="intro-text">
        세포를 둘러싼 소기관을 선택해 구조와 기능을 탐색해 보세요.
    </p>
   """,
unsafe_allow_html=True,
)

st.markdown(
    """
    <p style="
        text-align:center;
        color:#8FA8BA;
        font-size:13px;
        margin-top:0;
        margin-bottom:8px;
    ">
        소기관 이미지를 클릭하면 해당 상세 페이지로 이동합니다.
    </p>
    """,
    unsafe_allow_html=True,
)

def image_to_data_uri(image_path):
    """이미지를 HTML에서 표시할 수 있는 데이터 URI로 변환합니다."""
    if not image_path.exists():
        return None

    suffix = image_path.suffix.lower()
    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }
    mime_type = mime_types.get(suffix, "image/png")

    encoded = base64.b64encode(image_path.read_bytes()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"
# 중앙 세포 이미지
cell_image = image_to_data_uri(IMAGE_DIR / "cell.png")

if cell_image:
    center_html = f"""
        <div class="cell-center">
            <img src="{cell_image}" alt="세포 전체 구조">
        </div>
    """
else:
    center_html = """
        <div class="cell-center cell-placeholder">
            <span>세포 이미지 없음</span>
            <small>images/cell.png 파일을 확인해 주세요.</small>
        </div>
    """

# HTML 안에 모든 이미지를 넣어 원형 배치와 클릭 이동을 구현합니다.
cell_image = image_to_data_uri(IMAGE_DIR / "cell.png")

# 9개 아이콘을 원주 위에 같은 간격으로 배치합니다.
# 원형 궤도에 소기관 9개를 균등하게 배치
orbit_items = []

for index, item in enumerate(ORGANELLES):
angle = -90 + index * (360 / len(ORGANELLES))
radians = math.radians(angle)

    # 원의 중심을 50%, 50%로 하고 반지름을 36%로 설정합니다.
x = 50 + 36 * math.cos(radians)
y = 50 + 36 * math.sin(radians)

image_uri = image_to_data_uri(IMAGE_DIR / item["image"])
name = html.escape(item["name"])
    page = quote(item["page"], safe="")

if image_uri:
image_html = (
@@ -130,19 +165,19 @@ def image_to_data_uri(image_path):
)
else:
image_html = (
            f'<div class="missing-image">{name}</div>'
            f'<span class="missing-image">'
            f'{name}<br>이미지 없음</span>'
)

    # 쿼리 문자열을 이용해 Streamlit에서 상세 페이지로 전환합니다.
    destination = "?" + "go=" + quote(item["page"], safe="")

    # 부모 페이지의 주소를 기준으로 이동 URL을 생성합니다.
    # iframe 내부의 상대 주소로 이동하던 기존 방식을 수정했습니다.
orbit_items.append(
f"""
       <a class="organelle"
           href="{destination}"
           target="_top"
           href="?go={page}"
           data-page="{page}"
          aria-label="{name} 상세 페이지로 이동"
           style="left:{x:.4f}%; top:{y:.4f}%;">
           style="left:{x:.4f}%;top:{y:.4f}%;">
           <span class="image-circle">
               {image_html}
           </span>
@@ -151,195 +186,214 @@ def image_to_data_uri(image_path):
       """
)

if cell_image:
    center_html = f"""
        <div class="cell-center">
            <img src="{cell_image}" alt="세포 전체 구조">
        </div>
    """
else:
    center_html = """
        <div class="cell-center cell-placeholder">
            <span>세포 전체 이미지</span>
            <small>images/cell.png 파일을 확인해 주세요.</small>
        </div>
    """

orbit_html = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    * {{
        box-sizing: border-box;
    }}

    html, body {{
        margin: 0;
        padding: 0;
        width: 100%;
        background: #101820;
        color: #F1F5F9;
        font-family: Arial, "Malgun Gothic", sans-serif;
    }}

<style>
* {{
    box-sizing: border-box;
}}

html, body {{
    margin: 0;
    padding: 0;
    width: 100%;
    background: #101820;
    color: #F1F5F9;
    font-family: Arial, "Malgun Gothic", sans-serif;
}}

.orbit {{
    position: relative;
    width: min(100%, 760px);
    aspect-ratio: 1 / 1;
    margin: 0 auto;
    overflow: visible;
    background: radial-gradient(
        circle,
        rgba(48, 75, 95, 0.18) 0%,
        rgba(16, 24, 32, 0) 67%
    );
}}

.orbit-ring {{
    position: absolute;
    width: 72%;
    height: 72%;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    border: 1px solid rgba(142, 174, 198, 0.25);
    border-radius: 50%;
    pointer-events: none;
}}

.cell-center {{
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 34%;
    height: 34%;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    overflow: hidden;
    background: #17232E;
    border: 1px solid #405568;
    box-shadow: 0 0 28px rgba(103, 155, 190, 0.15);
    z-index: 1;
}}

.cell-center img {{
    display: block;
    width: 100%;
    height: 100%;
    object-fit: contain;
}}

.cell-placeholder {{
    flex-direction: column;
    gap: 8px;
    text-align: center;
    padding: 12px;
}}

.cell-placeholder small {{
    color: #B8C5D1;
    font-size: 10px;
}}

.organelle {{
    position: absolute;
    width: 15%;
    transform: translate(-50%, -50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 5px;
    color: #F1F5F9;
    text-decoration: none;
    z-index: 2;
    cursor: pointer;
    -webkit-tap-highlight-color: transparent;
}}

.image-circle {{
    display: flex;
    width: 100%;
    aspect-ratio: 1 / 1;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    border-radius: 50%;
    background: #1B2A36;
    border: 2px solid #607D92;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3);
    transition: transform 0.18s ease, border-color 0.18s ease;
}}

.organelle:hover .image-circle,
.organelle:focus-visible .image-circle {{
    transform: scale(1.08);
    border-color: #C2E3FA;
}}

.organelle-image {{
    display: block;
    width: 100%;
    height: 100%;
    object-fit: contain;
    padding: 5px;
}}

.organelle-name {{
    display: block;
    width: max-content;
    max-width: 145%;
    color: #F1F5F9;
    font-size: clamp(10px, 1.8vw, 14px);
    font-weight: 600;
    text-align: center;
    white-space: nowrap;
    text-shadow: 0 1px 4px #101820;
}}

.missing-image {{
    color: #B8C5D1;
    font-size: 10px;
    text-align: center;
    padding: 4px;
}}

@media (max-width: 480px) {{
   .orbit {{
        position: relative;
        width: min(100%, 760px);
        aspect-ratio: 1 / 1;
        margin: 0 auto;
        overflow: visible;
        background: radial-gradient(
            circle,
            rgba(48, 75, 95, 0.18) 0%,
            rgba(16, 24, 32, 0) 67%
        );
    }}

    .orbit-ring {{
        position: absolute;
        width: 72%;
        height: 72%;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        border: 1px solid rgba(142, 174, 198, 0.25);
        border-radius: 50%;
        pointer-events: none;
    }}

    .cell-center {{
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        width: 36%;
        height: 36%;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        overflow: hidden;
        background: #17232E;
        border: 1px solid #405568;
        box-shadow: 0 0 28px rgba(103, 155, 190, 0.15);
    }}

    .cell-center img {{
       width: 100%;
        height: 100%;
        object-fit: contain;
    }}

    .cell-placeholder {{
        flex-direction: column;
        gap: 8px;
        text-align: center;
        padding: 12px;
    }}

    .cell-placeholder small {{
        color: #B8C5D1;
        font-size: 10px;
   }}

   .organelle {{
        position: absolute;
        width: 15%;
        transform: translate(-50%, -50%);
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 5px;
        color: #F1F5F9;
        text-decoration: none;
        z-index: 2;
        -webkit-tap-highlight-color: transparent;
        width: 16%;
   }}

    .image-circle {{
        display: flex;
        width: 100%;
        aspect-ratio: 1 / 1;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        border-radius: 50%;
        background: #1B2A36;
        border: 2px solid #607D92;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3);
        transition: transform 0.18s ease, border-color 0.18s ease;
    }}

    .organelle:hover .image-circle,
    .organelle:focus-visible .image-circle {{
        transform: scale(1.1);
        border-color: #C2E3FA;
    }}

    .organelle-image {{
        display: block;
        width: 100%;
        height: 100%;
        object-fit: contain;
        padding: 5px;
    .cell-center {{
        width: 32%;
        height: 32%;
   }}

   .organelle-name {{
        display: block;
        width: max-content;
        max-width: 145%;
        color: #F1F5F9;
        font-size: clamp(10px, 1.8vw, 14px);
        font-weight: 600;
        text-align: center;
        white-space: nowrap;
        text-shadow: 0 1px 4px #101820;
    }}

    .missing-image {{
        font-size: 11px;
        text-align: center;
        padding: 4px;
        color: #B8C5D1;
    }}

    @media (max-width: 480px) {{
        .orbit {{
            width: 100%;
        }}

        .organelle {{
            width: 16%;
        }}

        .cell-center {{
            width: 34%;
            height: 34%;
        }}

        .organelle-name {{
            font-size: 10px;
        }}
        font-size: 10px;
   }}
}}
</style>
</head>

<body>
   <main class="orbit">
       <div class="orbit-ring"></div>
       {center_html}
       {''.join(orbit_items)}
   </main>

    <script>
    document.querySelectorAll(".organelle").forEach(function(link) {{
        link.addEventListener("click", function(event) {{
            event.preventDefault();

            const page = link.dataset.page;
            if (!page) return;

            try {{
                const destination = new URL(
                    window.parent.location.href
                );

                destination.searchParams.set(
                    "go",
                    decodeURIComponent(page)
                );

                window.parent.location.href =
                    destination.toString();
            }} catch (error) {{
                window.top.location.href = link.href;
            }}
        }});
    }});
    </script>
</body>
</html>
"""

components.html(
orbit_html,
    height=780,
    height=760,
scrolling=False,
)

st.caption("사진을 선택해 각 소기관의 상세 정보를 확인하세요.")
st.caption("각 소기관 이미지를 선택해 상세 정보를 확인하세요.")
