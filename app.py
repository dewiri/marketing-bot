# Streamlit Setup
st.set_page_config(page_title="Marketing Quiz", layout="centered")
st.title("📱 Marketing Quiz")
st.write("Kapitel 1.1 – 1.19 | Entscheide, ob Aussagen richtig oder falsch sind.")

# Session State Initialisierung
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = random.sample(questions, len(questions))
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.show_result = False
    st.session_state.quiz_done = False
    st.session_state.user_answer = None

# Quiz Logik
if not st.session_state.quiz_done and st.session_state.current < len(st.session_state.shuffled_questions):
    q = st.session_state.shuffled_questions[st.session_state.current]

    if not st.session_state.show_result:
        st.subheader(q["question"])
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Richtig", key="richtig"):
                st.session_state.show_result = True
                st.session_state.user_answer = "richtig"
                if q["answer"] == "richtig":
                    st.session_state.score += 1
        with col2:
            if st.button("❌ Falsch", key="falsch"):
                st.session_state.show_result = True
                st.session_state.user_answer = "falsch"
                if q["answer"] == "falsch":
                    st.session_state.score += 1

    if st.session_state.show_result:
        if st.session_state.user_answer == q["answer"]:
            st.markdown("<div style='background-color:#d4edda;padding:10px;border-radius:8px;'>✅ Deine Antwort war richtig!</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='background-color:#f8d7da;padding:10px;border-radius:8px;'>❌ Deine Antwort war falsch!</div>", unsafe_allow_html=True)

        st.info(f"**Begründung:** {q['explanation']}")

        if st.button("➡️ Nächste Frage", key=f"next_{st.session_state.current}"):
            st.session_state.current += 1
            st.session_state.show_result = False
            st.session_state.user_answer = None
            st.experimental_rerun()

# Quiz abgeschlossen
elif not st.session_state.quiz_done:
    st.session_state.quiz_done = True
    st.success(f"✅ Quiz abgeschlossen! Ergebnis: {st.session_state.score}/{len(st.session_state.shuffled_questions)}")
    if st.button("🔁 Quiz neu starten", use_container_width=True):
        for key in ["shuffled_questions", "current", "score", "show_result", "quiz_done", "user_answer"]:
            del st.session_state[key]
