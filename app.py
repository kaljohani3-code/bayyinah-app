import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="منصة بَيِّنَة الذكية",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. تنسيق أنيق مع إخفاء أخطاء نصوص الأيقونات العلوية
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap');

    body, p, h1, h2, h3, h4, h5, h6, div, span, input {
        font-family: 'Tajawal', sans-serif !important;
    }

    /* إخفاء النص المشوه في الشريط العلوي */
    [data-testid="stSidebarCollapseButton"] span {
        display: none !important;
    }

    .main-card {
        background: linear-gradient(135deg, #1e3a8a, #0f172a);
        padding: 2rem 1rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        direction: rtl;
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        margin-bottom: 1.5rem;
    }

    .main-card h1 {
        color: #ffffff !important;
        font-size: 1.6rem !important;
        font-weight: 800 !important;
        margin-bottom: 0.5rem !important;
    }

    .main-card p {
        color: #cbd5e1 !important;
        font-size: 0.95rem !important;
        margin: 0 !important;
    }

    .stTextInput label, .stTextInput input {
        direction: rtl !important;
        text-align: right !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.title("💡 عن المنصة")
    st.info("""
    **منصة بَيِّنَة الذكية** (نسخة تجريبية)
    
    منظومة استدلال فقهي تعتمد النص المباشر والمشروط من المراجع المعتمدة لضمان أعلى درجات الموثوقية.
    
    > *"فَاسْأَلُوا أَهْلَ الذِّكْرِ إِن كُنتُمْ لَا تَعْلَمُونَ"*
    """)
    st.markdown("---")
    st.caption("تطوير وبرمجة:")
    st.markdown("**م. خالد علي الجهني**")
    st.divider()
    st.markdown("📖 **المرجع النشط:** كتاب فقه العبادات")

# 4. الواجهة الرئيسية
st.markdown("""
<div class="main-card">
    <h1>منصة بَيِّنَة للبحث والاستدلال الفقهي</h1>
    <p>مساعدك الذكي لإستخراج الأحكام الشرعية المدعومة بالنصوص المباشرة</p>
</div>
""", unsafe_allow_html=True)

# 5. منطقة التفاعل والاستعلام
user_query = st.text_input("أدخل مسألتك الفقهية هنا:", placeholder="مثال: ما حكم صلاة المسافر في الطائرة؟")

if user_query:
    st.success(f"جاري البحث والاستدلال عن: **{user_query}**")
