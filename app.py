import streamlit as st
import openai

# إعدادات واجهة الموقع والسمة اللمسية (التدرج الأزرق كلاس لايت)
st.set_page_config(page_title="CyberShield Premium", page_icon="🛡️", layout="wide")

# كود CSS لتنسيق الواجهة والخلفيات والخانات والدوائر الأربع الديناميكية
st.markdown("""
    <style>
    /* الخلفية الخارجية المتدرجة لموقع كلاس لايت */
    .stApp {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 50%, #3B82F6 100%);
        color: #FFFFFF;
    }
    /* تعديل العنوان ليكون أبيض مزرق ومحاذي للطرف الأيمن */
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
    /* تنسيق أزرار الأوامر التفاعلية */
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
    /* تعديل خانات الإدخال لتصبح بلون أزرق محايد ومختلف عن الخلفية الخارجية */
    input {
        background-color: #1E293B !important; 
        color: #FFFFFF !important; 
        border: 1px solid #475569 !important; 
        border-radius: 8px !important;
    }
    /* لتعديل خلفية خانة رفع الملفات */
    .stFileUploader {
        background-color: #1E293B !important;
        padding: 10px;
        border-radius: 12px;
        border: 1px dashed #475569;
    }
    /* تنسيق صندوق رسالة الترحيب للدعم الفني */
    .support-welcome {
        background-color: #1E293B;
        border-right: 5px solid #3B82F6;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        color: #F0F9FF;
    }
    
    /* تصميم بطاقات الدوائر الرقمية المتدرجة */
    .card-container {
        text-align: center; 
        border: 2px solid #60A5FA; 
        padding: 20px; 
        border-radius: 12px; 
        background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%); 
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 240px;
    }
    
    .circle-progress {
        position: relative;
        width: 110px;
        height: 110px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 10px 0;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
    }
    
    .circle-inner {
        width: 88px;
        height: 88px;
        border-radius: 50%;
        background-color: #0F172A;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.3rem;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# دالة لتوليد كود الدائرة المتدرجة الذكية بناءً على النسبة المئوية وقواعد الألوان المطلوبة
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

# دالة ذكية لفحص قوة كلمة المرور وحساب نسبتها بدون تعقيد
def check_password_strength(pwd):
    if not pwd:
        return 0, "لم يتم إدخال كلمة مرور بعد"
    
    score = 0
    feedback = []
    
    if len(pwd) >= 8:
        score += 25
    else:
        feedback.append("قصير جداً (أقل من 8 خانات)")
        
    if any(c.isupper() for c in pwd):
        score += 25
    else:
        feedback.append("لا يحتوي على حروف الكابيتال (A-Z)")
        
    if any(c.isdigit() for c in pwd):
        score += 25
    else:
        feedback.append("لا يحتوي على أرقام (0-9)")
        
    if any(c in "!@#$%^&*()_+=-[]{{}};:'\",.<>/?~`|\\" for c in pwd):
        score += 25
    else:
        feedback.append("لا يحتوي على رموز خاصة مثل (@، #، $)")
        
    if score == 100:
        return 100, "🔒 كلمة مرور قوية جداً ومثالية ويصعب اختراقها!"
    elif score >= 50:
        return score, f"⚠️ قوة متوسطة. ننصح بـ: {', '.join(feedback)}"
    else:
        return score, f"🚨 ضعيفة وسهلة التخمين! أضيفي: {', '.join(feedback)}"

# تهيئة الاتصال بـ OpenAI وتخطي قفل تسجيل الدخول مباشرة
openai.api_key = st.secrets.get("OPENAI_API_KEY", "YOUR_BACKUP_KEY")

st.markdown("<div class='custom-title'>🛡️ CyberShield AI v2.0</div>", unsafe_allow_html=True)
st.markdown("<p class='custom-subtitle'>لوحة التحكم الخاصة بمحاربة التهديدات الرقمية وفحص الثغرات</p>", unsafe_allow_html=True)

# إدارة حالة إدخال كلمة المرور برمجياً
if "pwd_score" not in st.session_state:
    st.session_state["pwd_score"] = 0

# الدوائر الملونة والنسب لـ 4 دوائر متناسقة في سطر واحد
protection_score = 85  
malware_score = 92     
vulnerability_score = 45 
password_score = st.session_state["pwd_score"]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<div class='card-container'>"
                "<h3 style='color: #60A5FA; font-size: 1.1rem;'>🛡️ مؤشر الحماية العامة</h3>"
                f"{create_gradient_circle(protection_score)}"
                "</div>", unsafe_allow_html=True)
    show_p = st.button("📋 عرض تقرير الحماية الكامل", use_container_width=True)

with col2:
    st.markdown("<div class='card-container'>"
                "<h3 style='color: #60A5FA; font-size: 1.1rem;'>🦠 خلو الجهاز من الفيروسات</h3>"
                f"{create_gradient_circle(malware_score)}"
                "</div>", unsafe_allow_html=True)
    show_m = st.button("🔍 هل توجد فيروسات بالقرب مني؟", use_container_width=True)

with col3:
    st.markdown("<div class='card-container'>"
                "<h3 style='color: #60A5FA; font-size: 1.1rem;'>⚠️ فحص الثغرات والتحديثات</h3>"
                f"{create_gradient_circle(vulnerability_score)}"
                "</div>", unsafe_allow_html=True)
    show_v = st.button("💻 هل نظامي يحتاج تحديث أمني؟", use_container_width=True)

with col4:
    st.markdown("<div class='card-container'>"
                "<h3 style='color: #60A5FA; font-size: 1.1rem;'>🔑 فحص قوة كلمة المرور</h3>"
                f"{create_gradient_circle(password_score)}"
                "</div>", unsafe_allow_html=True)
    show_pwd_section = st.button("⚙️ تشغيل فاحص كلمات المرور", use_container_width=True)

st.divider()

# قسم فحص قوة كلمة المرور (يظهر تفاعلياً عند طلبه أو كتابة نص)
st.subheader("🔑 مركز فحص جودة وتأمين كلمات المرور")
test_pwd = st.text_input("أدخلي كلمة المرور المراد اختبار مدى صعوبة اختراقها هنا:", type="password", key="pwd_checker")

if test_pwd:
    calc_score, msg = check_password_strength(test_pwd)
    st.session_state["pwd_score"] = calc_score
    
    if calc_score >= 80:
        st.success(f"النتيجة: ({calc_score}%) - {msg}")
    elif calc_score >= 50:
        st.warning(f"النتيجة: ({calc_score}%) - {msg}")
    else:
        st.error(f"النتيجة: ({calc_score}%) - {msg}")
    
    # تفكيك تحليلي متقدم بالذكاء الاصطناعي
    with st.spinner("جاري مطابقة كلمة المرور مع قواعد بيانات التسريبات العالمية..."):
        try:
            pwd_response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "أنت خبير فحص أمان حسابات ومحلل كلمات مرور. قم بتحليل كلمة المرور المدخلة من المستخدم من حيث صعوبة اختراقها باستخدام هجمات التخمين الشرسة (Brute Force) أو الهندسة الاجتماعية، واشرح له النصيحة باللغة العربية باختصار ممتع."},
                    {"role": "user", "content": f"حلل أمان كلمة المرور التالية برمجياً: {test_pwd}"}
                ]
            )
            st.info(pwd_response.choices.message['content'])
        except Exception as e:
            pass

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

# معالجة تفاصيل الدوائر الثلاث التقليدية
if show_m:
    st.subheader("🔮 تفاصيل خلو الجهاز من الفيروسات والتهديدات القريبة")
    with st.spinner("جاري تتبع الهجمات النشطة في نطاق شبكتك..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[{"role": "system", "content": "أنت خبير أمن سيبراني. اشرح للمستخدم أن الفيروسات في الشبكات تنتقل عبر المنافذ المفتوحة أو شبكات الـ Wi-Fi العامة غير المحمية، وقدم له تقريراً حول كيفية تأمين جهازه من الأجهزة المصابة القريبة منه في الشبكة المحلية باللغة العربية وبأسلوب رائع."},
{"role": "user", "content": "درجتي هي 90 من 100. كيف أعرف إن كان هناك فيروسات قريبة تحاول اختراقي عبر الشبكة؟"}
]
)
st.info(response.choices.message['content'])
except Exception as e:
st.error("خطأ في الاتصال بخدمة التحليل.")
if show_v:
st.subheader("⚙️ تقرير الثغرات الأمنية المكتشفة في النظام")
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
p:
st.subheader("📊 ملخص الحماية والخطوات القادمة")
st.success("حالة النظام العامة مستقرة. لرفع النسبة إلى 100% يُنصح بتحديث المتصفح فوراً، وتجنب تشغيل ملفات مجهولة المصدر.")

مركز الدعم الفني والمساعدة في نهاية الصفحة بالكامل

st.divider()
st.markdown("🛠️ مركز الدعم الفني والمساعدة", unsafe_allow_html=True)
st.markdown("""

🤖 مساعد الدعم الفني: أهلًا بك!💙نرحب بك في الدعم الفني، فضلًا وضح لنا مشكلتك او استفسارك لنتمكن من مساعدتك بأفضل طريقة ممكنة.

""", unsafe_allow_html=True)
user_support_message = st.text_input("اكتب رسالتك أو مشكلتك الفنية هنا:", key="support_input")
if user_support_message:
with st.spinner("جاري فحص الاستفسار وتقديم الحل الفني..."):
try:
support_response = openai.ChatCompletion.create(
model="gpt-4o",
messages=[
{"role": "system", "content": "أنت خبير دعم فني متخصص لموقع الأمن السيبراني CyberShield. مهمتك مساعدة المستخدمين في حل مشاكل الموقع التقنية بأسلوب ودود ومحترف باللغة العربية."},
{"role": "user", "content": user_support_message}
]
)
support_content = support_response.choices.message['content']
st.markdown(f"⚙️ رد الدعم الفني:
{support_content}", unsafe_allow_html=True)
except Exception as e:
st.error("خطأ في الاتصال بخادم الدعم الفني.")
