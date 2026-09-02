import os
import re
import streamlit as st

# ضبط إعدادات الصفحة
st.set_page_config(page_title="منصة بَيِّنَة الذكية", page_icon="⚖️", layout="wide")
# 2. تحسين تصميم الواجهة والخطوط (CSS Morden UI)
st.markdown("""
<style>
    /* استدعاء خط Cairo الحديث من Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

    /* تطبيق الخط على كافة عناصر التطبيق */
    html, body, [class*="css"], font, span, div, p, h1, h2, h3, input, button {
        font-family: 'Cairo', sans-serif !important;
    }

    /* تحسين الهيدر الرئيسي (Hero Banner) */
    .title-header {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        padding: 2.5rem 1.5rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
        margin-bottom: 2rem;
    }

    .title-header h1 {
        font-weight: 800;
        font-size: 2.2rem;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }

    .title-header p {
        font-weight: 600;
        color: #e0e6ed;
        font-size: 1.1rem;
    }

    /* تحسين القائمة الجانبية Sidebar */
    [data-testid="stSidebar"] {
        background-color: #f8fafc;
        border-left: 1px solid #e2e8f0;
    }

    /* تحسين حقل المدخلات (مربع البحث) */
    .stTextInput input {
        border-radius: 12px !important;
        border: 2px solid #cbd5e1 !important;
        padding: 12px 16px !important;
        font-size: 1rem !important;
        transition: all 0.3s ease;
    }

    .stTextInput input:focus {
        border-color: #2c5364 !important;
        box-shadow: 0 0 10px rgba(44, 83, 100, 0.2) !important;
    }

    /* تحسين صندوق النتيجة المباشرة */
    .stSuccess {
        border-radius: 12px !important;
        padding: 1.2rem !important;
        font-size: 1.1rem !important;
        line-height: 1.8 !important;
        border-right: 6px solid #10b981 !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important;
    }
</style>
""", unsafe_allow_html=True)
# تطبيق التنسيقات العصرية CSS
st.markdown("""
    <style>
    /* استيراد خط تجريدي عصري من Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif;
    }
    
    /* خلفية هادئة للمنصة */
    .stApp {
        background-color: #f8fafc;
    }
    
    /* تصميم الهيدر الرئيسي بألوان متدرجة عصري */
    .main-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 10px 25px -5px rgba(30, 58, 138, 0.25);
        margin-bottom: 2rem;
    }
    
    /* تصميم بطاقات النتائج والمراجع */
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border-right: 5px solid #3b82f6;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 1rem;
    }
    
    /* تحسين شكل زر البحث */
    .stButton>button {
        background: linear-gradient(90deg, #2563eb, #1d4ed8);
        color: white;
        border-radius: 8px;
        font-weight: bold;
        padding: 0.6rem 2rem;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# 1. إعداد الصفحة وتفعيل التصميم التجاوبي
st.set_page_config(
    page_title="منصة بَيِّنَة - الاستدلال الموثوق",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. إضافة لمسات وتصميم CSS مخصص للواجهة
st.markdown("""
  # 3. القائمة الجانبية (Sidebar)
# 3. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.title("💡 عن المنصة")
    
    sidebar_html = """
    <div style="background-color: #f1f5f9; padding: 1.2rem; border-radius: 12px; border-right: 4px solid #1e3a8a; margin-bottom: 1rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: #1e3a8a; margin: 0; font-weight: 700;">منصة بَيِّنَة الذكية</h4>
            <span style="background-color: #fef3c7; color: #d97706; font-size: 0.75rem; font-weight: 700; padding: 2px 8px; border-radius: 6px; border: 1px solid #fde68a;">نسخة تجريبية</span>
        </div>
        <p style="color: #475569; font-size: 0.95rem; line-height: 1.6; margin-bottom: 0.8rem;">
            منظومة استدلال فقهي تعتمد النص المباشر والمشروط من المراجع المعتمدة لضمان أعلى درجات الموثوقية والحد من الاجتهاد الخارجي
        </p>
        <p style="color: #0f172a; font-size: 0.9rem; font-weight: 700; text-align: center; background: #e2e8f0; padding: 6px; border-radius: 8px; margin: 0;">
            ﴾فَاسْأَلُوا أَهْلَ الذِّكْرِ إِن كُنتُمْ لَا تَعْلَمُونَ﴿
        </p>
    </div>
    
    <div style="background-color: #ffffff; padding: 1rem; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 2px 6px rgba(0,0,0,0.04);">
        <p style="margin: 0; font-size: 0.85rem; color: #64748b;">تطوير وبرمجة:</p>
        <p style="margin: 4px 0 0 0; font-size: 1rem; font-weight: 700; color: #0f172a;">م. خالد علي الجهني</p>
    </div>
    """
    st.markdown(sidebar_html, unsafe_allow_html=True)
    
    st.divider()
    st.markdown("<b>📖 المرجع النشط:</b> كتاب فقه العبادات", unsafe_allow_html=True)
    
    <div style="background-color: #ffffff; padding: 1rem; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 2px 6px rgba(0,0,0,0.04);">
        <p style="margin: 0; font-size: 0.85rem; color: #64748b;">تطوير وبرمجة:</p>
        <p style="margin: 4px 0 0 0; font-size: 1rem; font-weight: 700; color: #0f172a;">م. خالد علي الجهني</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.markdown("<b>📖 المرجع النشط:</b> كتاب فقه العبادات", unsafe_allow_html=True)
        margin-bottom: 2rem;
    }
    .title-header h1 {
        color: #ffffff !important;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .title-header p {
        color: #e0e0e0;
        font-size: 1.1rem;
    }

    /* بطاقة النتيجة المقتبسة */
    .result-card {
        background-color: #ffffff;
        border-right: 5px solid #2a5298;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
        transition: transform 0.2s ease;
    }
    .result-card:hover {
        transform: translateY(-2px);
    }
    .result-meta {
        display: inline-block;
        background-color: #eef2f7;
        color: #1e3c72;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: bold;
        margin-bottom: 0.8rem;
    }
    .result-body {
        color: #333333;
        font-size: 1.05rem;
        line-height: 1.8;
        white-space: pre-line;
    }

    /* القائمة الجانبية */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-left: 1px solid #e9ecef;
    }
    </style>
""", unsafe_allow_html=True)
# 3. القائمة الجانبية (Sidebar)
# 3. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.title("💡 عن المنصة")
    
    st.markdown("""
    <div style="background-color: #f1f5f9; padding: 1.2rem; border-radius: 12px; border-right: 4px solid #1e3a8a; margin-bottom: 1rem;">
        <h4 style="color: #1e3a8a; margin-top: 0; font-weight: 700;">منصة بَيِّنَة الذكية</h4>
        <p style="color: #475569; font-size: 0.95rem; line-height: 1.6; margin-bottom: 0.8rem;">
            منظومة استدلال فقهي تعتمد النص المباشر والمشروط من المراجع المعتمدة، لضمان أعلى درجات الموثوقية والحد من الاجتهاد الخارجي.
        </p>
        <p style="color: #0f172a; font-size: 0.9rem; font-weight: 700; text-align: center; background: #e2e8f0; padding: 6px; border-radius: 8px; margin: 0;">
            ﴿فَاسْأَلُوا أَهْلَ الذِّكْرِ إِن كُنتُمْ لَا تَعْلَمُونَ﴾
        </p>
    </div>
    
    <div style="background-color: #ffffff; padding: 1rem; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 2px 6px rgba(0,0,0,0.04);">
        <p style="margin: 0; font-size: 0.85rem; color: #64748b;">تطوير وبرمجة:</p>
        <p style="margin: 4px 0 0 0; font-size: 1rem; font-weight: 700; color: #0f172a;">م. خالد علي الجهني</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.markdown("<b>📖 المرجع النشط:</b> كتاب فقه العبادات", unsafe_allow_html=True)
st.markdown("""
    <div class="title-header">
        <h1> منصة بَيِّنَة الذكية</h1>
         <h2>﴾فَاسْأَلُوا أَهْلَ الذِّكْرِ إِن كُنتُمْ لَا تَعْلَمُونَ﴿</h2>
        <p>للاستدلال الفقهي والفتوى الموثوقة من المصادر الرسمية مباشرة</p>
    </div>
""", unsafe_allow_html=True)

text_path = "sample_reference.txt"

def clean_arabic(text):
    if not text:
        return ""
    text = re.sub(r'[\u064B-\u0652]', '', text)
    text = re.sub(r'[إأآا]', 'ا', text)
    text = re.sub(r'ى', 'ي', text)
    text = re.sub(r'ة', 'ه', text)
    return text

def load_reference_data():
    if not os.path.exists(text_path):
        return []
    
    with open(text_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    raw_pages = content.split("[صفحة ")
    pages_data = []
    
    for p in raw_pages:
        if not p.strip():
            continue
        parts = p.split("]\n", 1)
        page_num = parts[0]
        text_body = parts[1] if len(parts) > 1 else parts[0]
        
        pages_data.append({
            "page": page_num,
            "raw_text": text_body.strip(),
            "cleaned_text": clean_arabic(text_body)
        })
        
    return pages_data

pages_data = load_reference_data()

if not pages_data:
    st.error("لم يتم العثور على الملف النصي المرجعي `sample_reference.txt`!")
    st.stop()

# 5. منطقة صندوق البحث
st.markdown("### 🔍 بحث في المرجع الفقهي المعتمد")
user_query = st.text_input("", placeholder="اكتب سؤالك هنا (مثال: ما هي أركان الوضوء، حكم الصلاة...)")

if user_query:
    with st.spinner("جاري استرجاع الحكم والاستدلال المباشر..."):
        cleaned_query = clean_arabic(user_query)
        search_words = [w.strip() for w in cleaned_query.split() if len(w.strip()) > 1]
        
        matches = []
        for p in pages_data:
            cleaned_text = p["cleaned_text"]
            
            matched_words_count = sum(1 for w in search_words if w in cleaned_text)
            
            lines = cleaned_text.split('\n')
            first_line = lines[0] if lines else cleaned_text
            title_bonus = sum(5 for w in search_words if w in first_line)
            
            total_score = matched_words_count + title_bonus
            
            if matched_words_count >= 1:
                matches.append((total_score, p))
        
        matches.sort(key=lambda x: x[0], reverse=True)
        
        if matches:
            top_match = matches[0][1]
            
            st.markdown("### 💡 الحكم والاستدلال المباشر:")
            st.success(top_match["raw_text"])
            st.caption(f"📌 {top_match['page']}")
        else:
            st.warning("لم يتم العثور على نص مرتبط بهذا البحث في المرجع المعتمد.")
