import streamlit as st

# セッション初期化
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.answers = []
    st.session_state.score = 0
    st.session_state.result = ""

st.title("Health Check")
st.caption("人事アプリ｜ストレスチェック")

# 質問リスト（質問文、説明、スコア条件）
questions = [
    ("最近、疲れていますか？", "Are you tired recently?", "yes"),
    ("睡眠時間は足りていますか？", "Do you get enough sleep?", "no"),
    ("最近、イライラしやすいですか？", "Do you feel irritated recently?", "yes"),
]

# 質問のステップ表示（1～3）
if st.session_state.step <= len(questions):
    q_index = st.session_state.step - 1
    jp_q, en_q, score_on = questions[q_index]

    st.subheader(f"{st.session_state.step:02d}. {jp_q}")
    st.caption(en_q)
    st.markdown("あなたの回答を選んでください：")

    answer = st.radio(
        label="",
        options=["yes", "no"],
        horizontal=True,
        key=f"q{st.session_state.step}"
    )

    if st.button("次へ"):
        st.session_state.answers.append(answer)

        # スコア加算判定
        if answer == score_on:
            st.session_state.score += 1

        st.session_state.step += 1
        st.rerun()

# 結果表示（ステップ4）
elif st.session_state.step == 4:
    st.subheader("あなたのストレス診断結果")
    score = st.session_state.score

    # 診断メッセージ分岐
    if score == 0:
        result = (
            "■ とても健康な状態です！\n"
            "Great! You seem very well-balanced and healthy."
        )
    elif score == 1:
        result = (
            "■ やや疲れ気味かも？少し意識して休みましょう。\n"
            "Mild stress. Take short breaks to refresh yourself."
        )
    else:
        result = (
            "■ 注意！ストレスが蓄積している可能性があります。\n"
            "Caution! You may be under stress. Consider taking proper rest or seeking support."
        )

    st.text(result)

    # 回答とスコアも表示（オプション）
    with st.expander("回答の内訳を見る"):
        for i, (q, _, _) in enumerate(questions):
            st.write(f"Q{i+1}. {q} → あなたの回答：{st.session_state.answers[i]}")
        st.write(f"スコア合計：{score}")

    if st.button("最初に戻る"):
        st.session_state.clear()
        st.rerun()
