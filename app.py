
# =========================================================
# 8. 소기관 정보 파일
# DATA FILE 표시와 ACCESS FILE 버튼을 같은 줄에 배치
# =========================================================

st.markdown(
    '<div class="section-bar">INTELLIGENCE FILES // ORGANELLE DATABASE</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="subtitle">
        SELECT AN INTELLIGENCE FILE TO ACCESS DETAILED BIOLOGICAL INFORMATION.
    </div>
    """,
    unsafe_allow_html=True,
)

for start in range(0, len(ORGANELLES), 3):
    row_items = ORGANELLES[start:start + 3]
    columns = st.columns(3, gap="medium")

    for column, organelle in zip(columns, row_items):
        with column:
            # 소기관 코드, 이름, 설명
            st.markdown(
                f"""
                <div class="intel-card">
                    <div class="intel-code">
                        {organelle["code"]} // INTELLIGENCE FILE
                    </div>
                    <div class="intel-name">{organelle["name"]}</div>
                    <div class="intel-description">
                        {organelle["description"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # DATA FILE 문구와 버튼을 같은 행에 배치
            status_col, button_col = st.columns(
                [1.35, 1],
                vertical_alignment="center",
                gap="small",
            )

            with status_col:
                st.markdown(
                    """
                    <div style="
                        color: #86c9d5;
                        font-family: monospace;
                        font-size: 9px;
                        letter-spacing: 0.5px;
                        padding: 8px 0;
                        white-space: nowrap;
                    ">
                        ● DATA FILE / BIOLOGICAL
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with button_col:
                page_path = ROOT_DIR / organelle["page"]

                if page_path.exists():
                    st.page_link(
                        organelle["page"],
                        label="ACCESS FILE",
                        use_container_width=True,
                    )
                else:
                    st.caption("PAGE UNAVAILABLE")

            # 소기관 이미지
            image_path = IMAGE_DIR / organelle["image"]

            if image_path.exists():
                st.image(
                    str(image_path),
                    use_container_width=True,
                )
            else:
                st.warning(
                    f'이미지 파일을 찾을 수 없습니다: images/{organelle["image"]}'
                )

