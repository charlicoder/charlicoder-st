import streamlit as st
from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./images/mamun_circle_pic.png", width=230)

with col2:
    st.title("K Md Mamunur Rashid", anchor=False)
    st.write(
        "Sr. Software Engineer | Full Stack Developer | Data Engineer"
    )
    st.markdown("""
        ### My Profiles
        - [LinkedIn](https://www.linkedin.com/in/charlicoder)
        - [GitHub](https://github.com/charlicoder)
        """)
    if st.button("Contact Me"):
        show_contact_form()


st.write("---")

st.write("\n")
st.subheader("Experience & Qualificatoins", anchor=False)
st.write(
    """
    - I have more than 10 years of experience working as a "Software Developer (Python/JavaScript Stack)".
    - Web application design, development, and deployment
    - Design, develop and deploy RESTful APIs that operated as microservices
    - ETL pipeline design and automation
    - Vector search, RAG, Chatbot  implementation
    - Machine learning model development and deployment
    - Cross-functional collaboration and problem-solving
    """
)

st.write("\n")
st.subheader("Hard skills", anchor=False)
st.write(
    """
    - Python, Django, Django Rest Framework, FastAPI, Celery, BeautifulSoup
    - JavaScript, NodeJS, ExpressJS, React
    - PostgreSQL, MongoDB, GraphQL, Redis, ElasticSearch, RabbitMQ, Snowflake
    - Git, Docker, Docker Compose, Kubernetes, Jira, Bash Script, Terraform
    - AWS Cloud Services (EC2, Lambda, SQS, S3, Glue, API Gateway, RDS, DynamoDB, 
        Elastic Beanstalk, OpenSearch, CloudFront, ElastiCache, SNS etc)
    - NumPy, Pandas, Matplotlib, Scikit-Learn, Tensorflow etc
    """
)
