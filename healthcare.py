import streamlit as st
from PIL import Image
def next_page():
    st.session_state.page += 1
def prev_page():
    if st.session_state.page > 0:
        st.session_state.page -= 1

def main():
    if 'page' not in st.session_state:
        st.session_state.page = 0
    if st.session_state.page == 0:
        st.title("HEALTHCARE ASSISTANT")
        st.header("HEALTH")
        name = st.text_input("Name")
        email = st.text_input("Email")
        age = st.text_input("Age")
        mobile_no = st.text_input("Mobile Number")
        if st.button('Let\'s go...'):
            next_page()
    elif st.session_state.page == 1:
        st.title("Select Your Symptom")
        st.session_state.symptoms = st.selectbox(
            'Select your symptoms',
            options=['Fever', 'Cough', 'Headache', 'Backpain', 'Stomachache','Shoulder pain','Knee pain','Hip pain','Neck pain','Sinus','Eyes twitching','Tooth ache','Chest pain','Ear pain']
        )
        if st.button('Next'):
            next_page()
        if st.button('Previous'):
          prev_page()
    elif st.session_state.page == 2:
        st.title("Symptom Analysis")
        if st.session_state.symptoms == 'Backpain':
            st.header("BACKPAIN")
            image_path = r"C:\Users\Aa\OneDrive\Desktop\healthcare\1726422095450.jpg"
            image = Image.open(image_path)
            st.image(image, caption="Backpain", use_column_width=True)
            st.header('REASON FOR BACKPAIN')
            st.write('1. Improper lifting, poor posture')
            st.write('2. Being overweight may increase the risk of back strain')
            st.write('3. Back pain becomes more common with age, especially after 45')
            st.header('REMEDIES')
            st.write('1. Walking strengthens the muscles around your spine, adding stability and helping minimize back pain')

        elif st.session_state.symptoms == 'Headache':
            st.header("HEADACHE")
            image_path=r"C:\Users\Aa\OneDrive\Desktop\healthcare\1726424329407.jpg"
            image=Image.open(image_path)
            st.image(image, caption="Headache", use_column_width=True)
            st.header('REASON FOR HEADACHE')
            st.write('1. Extreme heat and cold may also cause headaches')
            st.write('2. Continuous usage of mobile devices and laptops')
            st.write('3. Dehydration affects blood pressure and vision')
            st.header('REMEDIES')
            st.write('1. Hot or cold showers may provide relief for some people')
            st.write('2. Resting in a quiet room with a cool cloth on your forehead may help')
            st.write('3. Gently massaging your head and neck muscles may provide relief')

        elif st.session_state.symptoms == 'Cough':
            st.header("COUGH")
            image_path=r"C:\Users\Aa\OneDrive\Desktop\healthcare\1726424329383.jpeg"
            image=Image.open(image_path)
            st.image(image, caption="Cough", use_column_width=True)
            st.header('REASON FOR COUGH')
            st.write('1. Allergies that involve the nose and sinuses')
            st.write('2. The common cold, flu, and other viral infections')
            st.header('REMEDIES')
            st.write('1. A teaspoon or two of honey may cut mucus production and kill germs. Note: Do not give honey to children under 1 year old.')

        elif st.session_state.symptoms == 'Stomachache':
            st.header("STOMACHACHE")
            image_path=r"C:\Users\Aa\OneDrive\Desktop\healthcare\1726424329399.jpg"
            image=Image.open(image_path)
            st.image(image, caption="Stomachache", use_column_width=True)
            st.header('REASON FOR STOMACHACHE')
            st.write('1. Digestive issues, menstruation, passing virus, food poisoning')
            st.write('2. If you have appendicitis, you may experience stomach pain for a long time. (PLEASE VISIT A DOCTOR)')
            st.header('REMEDIES')
            st.write('1. Drink plenty of clear fluids to stay hydrated')
            st.write('2. Eat easy-to-digest foods like crackers and bananas')
            st.write('3. Avoid spicy, fried, and sugary foods, as well as caffeine')

        elif st.session_state.symptoms == 'Fever':
            st.header("FEVER")
            image_path=r"C:\Users\Aa\OneDrive\Desktop\healthcare\1726424329390.jpg"
            image=Image.open(image_path)
            st.image(image, caption="Fever", use_column_width=True)
            st.header('REASON FOR FEVER')
            st.write('1. Viral infection')
            st.write('2. Bacterial infection')
            st.write('3. Heat exhaustion')
            st.header('REMEDIES')
            st.write('1. Take paracetamol or ibuprofen in appropriate doses to help bring your temperature down')
            st.write('2. Drink plenty of fluids, particularly water')
            st.write('3. Avoid alcohol, tea, and coffee, as these drinks can cause slight dehydration')
        elif st.session_state.symptoms=='Neck pain':
            st.header('NECK PAIN')
            image_path = r"C:\Users\Aa\OneDrive\Desktop\healthcare\1726855606193.jpg"
            image = Image.open(image_path)
            st.image(image, caption="Neck pain", use_column_width=True)
            st.header('REASON FOR NECK PAIN')
            st.write('1.Neck pain that lasts longer than three months is considered chronic') 
            st.write('2.Sitting at a desk for a long time or watching TV with poor posture can cause neck pain') 
            st.write('3.Working on a computer for a long time, sleeping in an awkward position, or being exposed to a cold draft')
            st.header('REMEDIES')
            st.write('1.Gentle stretching and massage may help to relieve neck pain')
            st.write('2.Pain relievers such as paracetamol and ibuprofen may also be useful')
            st.write('3.Using ice packs or heating pads can help relieve neck pain fast. ')
        elif st.session_state.symptoms=='Shoulder pain':
            st.header('SHOULDER PAIN')
            image_path = r"C:\Users\Aa\OneDrive\Desktop\healthcare\1726855606205.jpg"
            image = Image.open(image_path)
            st.image(image, caption="Shoulder pain", use_column_width=True)
            st.header('RESON FOR SHOULDER PAIN')
            st.write('1.A broken shoulder bone can cause pain') 
            st.write('2.Job stress and other psychological factors like depression and anxiety can increase muscle tension and activity, which can lead to shoulder pain')
            st.header('REMEDIES')
            st.write('1.Put an ice pack to your painful shoulder for 15 to 20 minutes a few times each day')
            st.write('2.Use essential oils derived from therapeutic plants to reduce pain, tension, and swelling')
        elif st.session_state.symptoms=='Hip pain':
            st.header('HIP PAIN')
            image_path = r"C:\Users\Aa\OneDrive\Desktop\healthcare\1726855606188.jpg"
            image = Image.open(image_path)
            st.image(image, caption="Hip pain", use_column_width=True)
            st.header('REASON FOR HIP PAIN')
            st.write('1.Straining the muscles or ligaments around the hip joint through overuse or injury can cause hip discomfort')
            st.write('2.Nerve pain that originates in the lower back and radiates down through the hip can cause hip pain')
            st.header('REMEDIES')
            st.write('1.Walking is one of the best ways to relieve hip pain')
            st.write('2.While lying on your back, use your arms to raise your hips towards the ceiling, hold, and then slowly lower them back down')
            st.write('3.Sleeping on your back can help relieve hip pain, especially if you’re a side sleeper. ')
        elif st.session_state.symptoms=='Knee pain':
            st.header('KNEE PAIN')
            image_path = r"C:\Users\Aa\OneDrive\Desktop\healthcare\1726855606199.webp"
            image = Image.open(image_path)
            st.image(image, caption="Knee pain", use_column_width=True)
            st.header('REASON FOR KNEE PAIN')
            st.write('1.The most common causes of knee pain are related to aging, injury or repeated stress on the knee.')
            st.write('2.Knee pain can be related to aging')
            st.write('3.Continuous standing and walking without rest can leads to knee pain')
            st.header('REMEDIES')
            st.write('1.Losing weight may help relieve long-term knee pain')
            st.write('2.Apply ice to reduce inflammation, consider wearing a compression bandage')
            st.write('3.While sitting on the floor, bend one knee up towards your chest, then straighten your leg as much as possible. Repeat 10 times for each leg')
        elif st.session_state.symptoms=='Sinus':
            st.header('SINUS')
            image_path = r"C:\Users\Aa\OneDrive\Desktop\healthcare\1727028431766.jpg"
            image = Image.open(image_path)
            st.image(image, caption="Sinus", use_column_width=True)
            st.header('REASON FOR SINUS')
            st.write('1.Most often caused by the common cold')
            st.write('2.It is often caused by bacterial (germ) infection. Sometimes, viruses and fungi (molds) cause it.')
            st.write('3.An infected tooth or fungal infection can also occasionally cause the sinuses to become inflamed.')
            st.header('REMEDIES')
            st.write('1.Rest helps the body fight infection and speed recovery')
            st.write('2.Keep drinking plenty of fluids.')
            st.write('3.Take long showers or breathe in steam from a pot of warm (but not too hot) water')
        elif st.session_state.symptoms=='Ear pain':
            st.header('EAR PAIN')
            image_path = r"C:\Users\Aa\OneDrive\Desktop\healthcare\1727028431741.jpg"
            image = Image.open(image_path)
            st.image(image, caption="Ear pain", use_column_width=True)
            st.header('REASON FOR EAR PAIN')
            st.write('1.If your ear hurts when you touch it, you may have an upper respiratory infection caused by a virus or bacteria')
            st.write('2.Swimming, wearing hearing aids or headphones that damage the skin inside the ear canal, or putting cotton swabs or fingers in the ear canal.')
            st.write('3.Pain in the jaw or teeth may be felt in the ear.')
            st.header('REMEDIES')
            st.write('1.Place a cold pack or cold wet washcloth on the outer ear for 20 minutes to reduce pain.')
            st.write('2.If you’re dealing with an ear infection caused by bacteria, you’ll likely need antibiotics')
            st.markdown('<p style="color:yellow;">Make an appointment to see a doctor if you:</p>',unsafe_allow_html=True)
            st.write('1.Develop a fever')
            st.write('2.Feel pain that lasts more than one day')
            st.write('3.Notice your hearing getting worse over time')
            st.write('4.If your child becomes irritable and restless')
        elif st.session_state.symptoms=='Tooth ache':
            st.header('TOOTH PAIN')
            image_path = r"C:\Users\Aa\OneDrive\Desktop\healthcare\1727028431749.jpeg"
            image = Image.open(image_path)
            st.image(image, caption="Tooth pain", use_column_width=True)
            st.header('REASON FOR TOOTH PAIN')
            st.write('1.Eating cold, hot, acidic, or high-sugar foods at night may make your teeth sore or extra sensitive, especially if your teeth are already damaged by early')
            st.write('2.If you have temporary gum irritation, it should go away on its own in a day or two. ')
            st.write('3.If you have temporary gum irritation, it should go away on its own in a day or two. ')
            st.header('REMEDIES')
            st.write('1.Saltwater rinse')
            st.write('2.Apply an ice pack to the painful area.')
            st.markdown('<p style="color:yellow;">4.See a doctor immediately if you gad fever:</p>',unsafe_allow_html=True)
            st.write('4.Have red, swollen gums or foul-smelling discharge')
            st.write('5.Experience difficulty swallowing or breathing')
        elif st.session_state.symptoms=='Chest pain':
            st.header('Chest pain')
            image_path = r"C:\Users\Aa\OneDrive\Desktop\healthcare\1727028431734.jpg"
            image = Image.open(image_path)
            st.image(image, caption="Chest pain", use_column_width=True)
            st.header('REASON FOR Chest pain')
            st.write('1.Other serious symptoms include pain that spreads to the arms, back, neck, or jaw, shortness of breath, tightness in the chest, or pain that starts with nausea, vomiting, and sweating. Any person experiencing chest pain should consult a doctor.')
            st.write('2.Chest pain can come from heart, lung, digestive or other issues')
            st.header('REMEDIES')
            st.write('1.If you have new or unexplained chest pain or think you’re having a heart attack, call 911 or emergency medical help immediately. ')
            st.write('2.Don’t ignore the symptoms of a heart attack')
        elif st.session_state.symptoms=='Eyes twitching':
            st.header('Eyes twitching')
            image_path = r"C:\Users\Aa\OneDrive\Desktop\healthcare\1727028431758.gif"
            image = Image.open(image_path)
            st.image(image, caption="Twiching", use_column_width=True)
            st.header('REASON FOR EYES TWITCHING')
            st.write('1.Eye strain can cause throbbing pain in the eyes, especially after prolonged screen time, exposure to bright lights, or too much near work')
            st.write('2.Dry eyes, stress, fatigue, eye strain, and certain medications can contribute to an episode.')
            st.write('3.Eye twitching is temporary in most cases and goes away on its own.')
            st.header('REMEDIES')
            st.write('1.Resting, reducing stress and decreasing caffeine may help resolve eye twitching within a few days or weeks')
            st.write('2.Get more sleep.')
        
        if st.button('Previous'):
            prev_page()


if __name__ == "__main__":
    main()
