import streamlit as st

# Sidebar with your image and contact details
st.sidebar.image("images/mamun_circle_pic.png", use_column_width=True)
st.sidebar.title("Khondoker Md Mamunur Rashid")
st.sidebar.write("Sr. Software Engineer (Remote)")
st.sidebar.write("Savvie International Corp, Canada")
st.sidebar.write("+8801872993476")
st.sidebar.write("[GitHub](https://github.com/rashid2050)")
st.sidebar.write("charlicoder@gmail.com")


# Define sections
sections = {
    "Career Summary": """
    I have more than 10 years of experience working as a "Software Developer (Python/JavaScript Stack)".
    
    With over a decade of experience, I specialize in building scalable, high-performance applications and data pipelines. 
    My expertise includes developing ETL processes with AWS (S3, Glue, ECS, Batch, Fargate, SAM-CLI, CloudFormation), 
    Snowflake, and Snowpark; full-stack development using Python, Django, Django Rest Framework, Node.js and React; 
    and developing & deploying machine learning models using scikit-learn, TensorFlow, matplotlib etc. 
    I have a strong background in cloud services and DevOps practices, including Docker, Kubernetes, SAM cli, and AWS CloudFormation. 
    I’m adept at using PostgreSQL, Elasticsearch, PySpark, and NumPy/Pandas for data management and analysis. 
    My work enhances business efficiency and customer satisfaction in both collaborative and remote environments.
    """,

    "Skills Developed": """
    - Web application design, development, and deployment
    - Design, develop and deploy RESTful APIs that operated as microservices
    - ETL pipeline design and automation
    - Vector search, RAG, Chatbot implementation
    - Machine learning model development and deployment
    - Cross-functional collaboration and problem-solving
    
    Additional Tools & Technologies:
    - Blockchain development (Solidity, Truffle, Ganache, HardHat, Hyperledger, Fabrik)
    - Web Pentesting Tools (NMAP, SQLMap, Burp Suite, Metasploit, Skipfish etc)
    """,

    "Experience": """
    **Savvie International Corp, Canada** - Senior Software Engineer (Part time)  
    May 2024 - continue  
    - ETL Data Pipeline Development: Designed and implemented ETL data pipelines utilizing Snowpark (Snowflake), AWS Batch, S3, SQS, ECR, ECS, Fargate, SAM cli, and CloudFormation.
    - Vector (Semantic) Search Implementation: Developed and integrated vector (semantic) search capabilities for e-commerce products utilizing tools like Pinecone, FastAPI, Pandas, Numpy, Sentence_transformers, etc.
    - Machine Learning Model Development: Created and deployed machine learning models for product categorization based on image and title data.
    
    **W3Engineers Ltd, Dhaka** - Senior Software Engineer  
    Apr 2023 - Apr 2024  
    - Architected and executed data pipelines to streamline data extraction, transformation, and loading (ETL) processes.
    - Led end-to-end development of Django-based projects.
    - Promoted experience with Kubernetes, Docker, and Amazon Web Services.
    
    ... (additional experience here)
    """,

    "Education": """
    **Shahjalal University of Science and Technology, Bangladesh**  
    Post Graduate Diploma In Software Engineering  
    July 2006 - June 2007
    
    **Shahjalal University of Science and Technology, Bangladesh**  
    Training on CCNA  
    Dec 2004 - Dec 2005
    
    **National University, Bangladesh**  
    Bachelor of Science (BSc)  
    Jan 1999 - Dec 2004  
    BSc honors in Physics.
    """,

    "Recommendations": """
    **Ron Dyck** - CTO, Entrepreneur, Savvie International Corp  
    _"Mamunur Rashid was a great asset to our team. When thrown some very challenging problems, I found him to be very resourceful and hard working. I would highly recommend him."_
    
    **Iraj Islam** - Co-founder and CTO of NewsCred.com  
    _"Mamunur Rashid is an intelligent, hard working, and driven software engineer. During his time at NewsCred he was both a Software Engineer and an SQA Engineer. He contributed to feature development of various products and also made sure quality was maintained. We are grateful for his time at NewsCred and wish him a bright future as a successful Software Engineer."_
    """
}

# Sidebar navigation
selection = st.sidebar.radio("Go to", list(sections.keys()))

# Main content
st.title(selection)
st.write(sections[selection])
