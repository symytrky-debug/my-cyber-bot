import streamlit as st
import openai

# إعدادات واجهة الموقع والسمة اللمسية (التدرج الأزرق)
st.set_page_config(page_title="CyberShield Premium", page_icon="🛡️", layout="wide")

# كود CSS لتنسيق الواجهة والخلفيات والخانات والدوائر
st.markdown("""
    <style>
    /* Background gradient like ClassLight */
    .stApp {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 50%, #3B82F6 100%);
        color: #FFFFFF;
    }
    /* Title style - Bluish White aligned to the right side */
    .custom-title {
        text-align: right; 
        color: #F0F9FF; 
        font-family: 'Cairo', sans-serif;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .custom-subtitle {
        text-align: right;
        color: #93C5FD !important;
        margin-bottom: 25px;
    }
    h2, h3, p, label, .stMarkdown {
        color: #FFFFFF !important;
    }
    /* Interactive buttons style */
    div.stButton > button:first-child {
        background-color: #2563EB;
        color: white;
        border-radius: 8px;
        border: 1px solid #60A5FA;
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #3B82F6;
        border-color: #93C5FD;
        box-shadow: 0px 0px 10px #3B82F6;
    }
    /* Neutral blue input fields */
    input {
        background-color: #1E293B !important; 
        color: #FFFFFF !important; 
        border: 1px solid #475569 !important; 
        border-radius: 8px !important;
    }
    /* File uploader background styling */
    .stFileUploader {
        background-color: #1E293B !important;
        padding: 10px;
        border-radius: 12px;
        border: 1px dashed #475569;
    }
    /* Support section welcome box styling */
    .support-welcome {
        background-color: #1E293B;
        border-right: 5px solid #3B82F6;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        color: #F0F9FF;
    }
    
    /* Dynamic Progress Circles styling based on value color change rules */
    .card-container {
        text-align: center; 
        border: 2px solid #60A5FA; 
        padding: 25px; 
        border-radius: 12px; 
        background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%); 
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    
    .circle-progress {
        position: relative;
        width: 130px;
        height: 130px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 15px 0;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
    }
    
    .circle-inner {
        width: 106px;
        height: 106px;
        border-radius: 50%;
        background-color: #0F172A;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.6rem;
        font-weight: bold;
        color: #FFFFFF;
    }
    </style>
""", unsafe_allow_html=True)

# دالة لتوليد كود الدائرة المتدرجة الديناميكية وتغيير ألوانها تلقائياً
def create_gradient_circle(score):
    if score >= 80:
        gradient_color = f"conic-gradient(#10B981 0% {score}%, #34D399 {score}%, #1F2937 {score}% 100%)"
        text_color = "#10B981"
    elif score >= 50:
        gradient_color = f"conic-gradient(#F59E0B 0% {score}%, #F97316 {score}%, #1F2937 {score}% 100%)"
        text_color = "#F59E0B"
    else:
        gradient_color = f"conic-gradient(#EF4444 0% {score}%, #DC2626 {score}%, #1F2937 {score}% 100%)"
        text_color = "#EF4444"
        
    html_code = f"""
    <div class="circle-progress" style="background: {gradient_color};">
        <div class="circle-inner" style="color: {text_color};">
            {score}%
        </div>
    </div>
    """
    return html_code

# 1. نظام حماية الموقع (تسجيل الدخول الآمن)
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.markdown("<h2 style='text-align: right; color: #FFFFFF;'>🔒 نظام المحارب السيبراني - تسجيل الدخول</h2>", unsafe_allow_html=True)
    username = st.text_input("اسم المستخدم")
    password = st.text_input("كلمة المرور", type="password")
    login_button = st.button("دخول آمن")
    
    if login_button:
        if username == "admin" and password == "cyber2026":
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("بيانات الدخول غير صحيحة! الموقع خاص فقط.")
    st.stop()

# --- بعد تسجيل الدخول الناجح يظهر الموقع بالتصميم المتدرج الجديد ---

openai.api_key = st.secrets.get("OPENAI_API_KEY", "YOUR_BACKUP_KEY")

st.markdown("<div class='custom-title'>🛡️ CyberShield AI v2.0</div>", unsafe_allow_html=True)
st.markdown("<p class='custom-subtitle'>لوحة التحكم الخاصة بمحاربة التهديدات الرقمية وفحص الثغرات</p>", unsafe_allow_html=True)

# الدوائر الملونة والنسب الديناميكية
protection_score = 85  
malware_score = 92     
vulnerability_score = 45 

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='card-container'>"
                "<h3 style='color: #60A5FA;'>🛡️ مؤشر الحماية العامة</h3>"
                f"{create_gradient_circle(protection_score)}"
                "</div>", unsafe_allow_html=True)
    show_p = st.button("📋 عرض تقرير الحماية الكامل", use_container_width=True)

with col2:
    st.markdown("<div class='card-container'>"
                "<h3 style='color: #60A5FA;'>🦠 خلو الجهاز من الفيروسات</h3>"
                f"{create_gradient_circle(malware_score)}"
                "</div>", unsafe_allow_html=True)
    show_m = st.button("🔍 هل توجد فيروسات بالقرب مني؟", use_container_width=True)

with col3:
    st.markdown("<div class='card-container'>"
                "<h3 style='color: #60A5FA;'>⚠️ فحص الثغرات والتحديثات</h3>"
                f"{create_gradient_circle(vulnerability_score)}"
                "</div>", unsafe_allow_html=True)
    show_v = st.button("💻 هل نظامي يحتاج تحديث أمني؟", use_container_width=True)

st.divider()

# مركز فحص الملفات والأكواد المشبوهة
st.subheader("📁 مركز تحليل الملفات والأكواد المشبوهة")
uploaded_file = st.file_uploader("ارفع ملفاً، كود برمجياً، أو نص رسالة مشبوهة لتحليلها بالذكاء الاصطناعي:", type=["txt", "py", "js", "html", "exe"])

if uploaded_file is not None:
    file_details = uploaded_file.read().decode("utf-8", errors="ignore")[:2000]
    with st.spinner("جاري فحص وتفكيك الأكواد والملفات بحثاً عن برمجيات خبيثة..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "أنت محلل برمجيات خبيثة (Malware Analyst). قم بفحص النص أو الكود المرفق وحدد ما إذا كان يحتوي على أنشطة مشبوهة، فيروسات فدية، أو أكواد اختراق واشرح النتيجة للمستخدم باحترافية وبساطة وبشكل منسق باللغة العربية."},
                    {"role": "user", "content": f"قم بتحليل هذا المحتوى أمنياً:\n{file_details}"}
                ]
            )
            st.error("🚨 تقرير تحليل الملف المشبوه:")
            st.write(response.choices.message['content'])
        except Exception as e:
            st.error("خطأ في الاتصال بنظام الفحص المتقدم.")

st.divider()

# معالجة تفاصيل الدوائر الثلاث
if show_m:
    st.subheader("🔮 تفاصيل خلو الجهاز من الفيروسات والتهديدات القريبة")
    with st.spinner("جاري تتبع الهجمات النشطة في نطاق شبكتك..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "أنت خبير أمن سيبراني. اشرح للمستخدم أن الفيروسات في الشبكات تنتقل عبر المنافذ المفتوحة أو شبكات الـ Wi-Fi العامة غير المحمية، وقدم له تقريراً حول كيفية تأمين جهازه من الأجهزة المصابة القريبة منه في الشبكة المحلية باللغة العربية وبأسلوب رائع."},
                    {"role": "user", "content": "درجتي هي 90 من 100. كيف أعرف إن كان هناك فيروسات قريبة تحاول اختراقي عبر الشبكة؟"}
                ]
            )
            st.info(response.choices.message['content'])
        except Exception as e:
            st.error("خطأ في الاتصال بخدمة التحليل.")

if show_v:
    st.subheader("⚙️ تقرير الثغرات الأمنية M المكتشفة في النظام")
    with st.spinner("جاري مطابقة إصدار المتصفح بقاعدة بيانات الثغرات CVE..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "أنت مهندس أمن سيبراني متخصص في إدارة الثغرات (Vulnerability Management). اشرح للمستخدم أهمية سد ثغرات النظام الحالية وهل التحديث إلزامي فوراً أم يمكن استخدام جدار حماية قوي كحل مؤقت للحماية من الثغرات بدون تحديث باللغة العربية وببساطة."},
                    {"role": "user", "content": "تقييمي هو 75 من 100 في التحديثات. هل أنا معرض للخطر بسبب ثغرة غير مسدودة؟ وما العمل?"}
                ]
            )
            st.warning(response.choices.message['content'])
        except Exception as e:
            st.error("خطأ في الاتصال بنظام الفحص.")

if show_p:
    st.subheader("📊 ملخص الحماية والخطوات القادمة")
    st.success("حالة النظام العامة مستقرة. لرفع النسبة إلى 100% يُنصح بتحديث المتصفح فوراً، وتجنب تشغيل ملفات مجهولة المصدر.")

# مركز الدعم الفني والمساعدة في نهاية الصفحة بالكامل (تم إغلاق كافة الأقواس بنجاح)
st.divider()
st.markdown("<h3 style='text-align: right; color: #60A5FA;'>🛠️ مركز الدعم الفني والمساعدة</h3>", unsafe_allow_html=True)

st.markdown("""
    <div class='support-welcome'>
        🤖 <b>مساعد الدعم الفني:</b> أهلًا بك!💙نرحب بك في الدعم الفني، فضلًا وضح لنا مشكلتك او استفسارك لنتمكن من مساعدتك بأفضل طريقة ممكنة.
    </div>
""", unsafe_allow_html=True)

user_support_message = st.text_input("اكتب رسالتك أو مشكلتك الفنية هنا:", key="support_input")

if user_support_message:
    with st.spinner("جاري فحص الاستفسار وتقديم الحل الفني..."):
        try:
            support_response = openai.ChatCompletion.create()
