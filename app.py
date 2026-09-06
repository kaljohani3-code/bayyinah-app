import os
import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(
    page_title=" منصة بَيِّنَة الذكية علي شاطر",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. التنسيقات والخطوط
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap');

    body, p, h1, h2, h3, h4, h5, h6, div, span, input {
        font-family: 'Tajawal', sans-serif !important;
    }

    [data-testid="stSidebarCollapseButton"] span,
    .stInstructions {
        display: none !important;
    }

    .main-card {
        background: linear-gradient(135deg, #1e3a8a, #0f172a);
        padding: 2.5rem 1.5rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        direction: rtl;
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        margin-bottom: 2rem;
    }

    .main-card h1 {
        color: #ffffff !important;
        font-size: 2rem !important;
        font-weight: 800 !important;
        margin-bottom: 0.6rem !important;
    }

    .main-card p {
        color: #cbd5e1 !important;
        font-size: 1.05rem !important;
        margin: 0 !important;
    }

    .stTextInput > div > div > input {
        direction: rtl !important;
        text-align: right !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        font-size: 1.05rem !important;
        border: 2px solid #cbd5e1 !important;
    }

    .stTextInput label {
        direction: rtl !important;
        text-align: right !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        color: #1e293b !important;
    }

    .result-title {
        direction: rtl;
        text-align: right;
        font-size: 1.3rem;
        font-weight: 800;
        color: #1e3a8a;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
    }

    .result-box {
        background-color: #f8fafc;
        border-right: 5px solid #1e3a8a;
        padding: 1.5rem;
        border-radius: 12px;
        direction: rtl;
        text-align: right;
        line-height: 1.8;
        font-size: 1.05rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
</style>
""", unsafe_allow_html=True)

# 3. دالة البحث في كتاب المرجع
def search_reference(query):
    filename = "sample_reference.txt"
    if not os.path.exists(filename):
        return None, "ملف المرجع (sample_reference.txt) غير موجود في مجلد المشروع."
    
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    
    paragraphs = [p.strip() for p in content.split("\n\n") if p.strip()]
    matched = []
    
    keywords = [k for k in query.split() if len(k) > 2]
    
    for p in paragraphs:
        if any(keyword in p for keyword in keywords):
            matched.append(p)
            
    if matched:
        return "\n\n---\n\n".join(matched), None
    else:
        return None, "لم يتم العثور على نص مباشر مطالع لهذه المسألة في المرجع النشط."

# 4. القائمة الجانبية (Sidebar)
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

# 5. الواجهة الرئيسية
st.markdown("""
<div class="main-card">
    <h1>منصة بَيِّنَة للبحث والاستدلال الفقهي</h1>
    <p>مساعدك الذكي لإستخراج الأحكام الشرعية المدعومة بالنصوص المباشرة</p>
</div>
""", unsafe_allow_html=True)

# 6. منطقة التفاعل واستخراج النتائج
user_query = st.text_input("أدخل مسألتك الفقهية هنا:", placeholder="مثال: ما هي اركان الصلاة؟")

if user_query:
    results, error = search_reference(user_query)
    if results:
        st.markdown('<div class="result-title">📌 النص الفقهي والاستدلال المباشر:</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-box">{results}</div>', unsafe_allow_html=True)
    else:
        st.warning(error)
