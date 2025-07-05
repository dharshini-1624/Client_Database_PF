import streamlit as st
import os
from supabase import create_client

# Load environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Check if environment variables are set
if not SUPABASE_URL or not SUPABASE_KEY:
    st.error("❌ SUPABASE_URL and SUPABASE_KEY must be set in Streamlit secrets.")
    st.error("Please configure your secrets in Streamlit Cloud dashboard.")
    st.stop()

# Connect to Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("🤝 Add New Client to Client DB")

with st.form("client_form"):
    client_name = st.text_input("Client Name")
    company_name = st.text_input("Company Name")
    company_linkedin = st.text_input("Company LinkedIn")
    client_linkedin = st.text_input("Client LinkedIn")
    contact_email = st.text_input("Contact Email")
    location = st.text_input("Location/Time Zone")
    business_model = st.text_area("Preferred Business Model(s)")
    deal_criteria = st.text_area("Deal Criteria(s)")
    deal_size = st.text_input("Deal Size")
    deal_source = st.text_input("Deal Source")
    urgency = st.selectbox("Client Urgency", ["High", "Medium", "Low", "Unknown"])
    deals_presented = st.number_input("Deals Presented", min_value=0, step=1)
    deals_discussion = st.text_area("Deals in Discussion")
    deals_closed = st.number_input("Deals Closed", min_value=0, step=1)
    related_docs = st.text_input("Related Document(s)")
    client_source = st.text_input("Client Source")
    last_contacted = st.date_input("Last Contacted On")
    followup_date = st.date_input("Follow-Up Date")
    stage = st.text_input("Client- Relationship Stage")
    team_member = st.text_input("Primary Analyst Assigned")
    notes = st.text_area("Notes/Comments")
    nda_status = st.selectbox("NDA Status", ["Executed", "Not Executed", "Unknown"])
    ai_summary = st.text_area("AI summary")
    emp_pref = st.text_input("Employee Count Preference")
    industry = st.text_input("Industry Focus")
    geo = st.text_input("Geographic Focus")
    revenue_range = st.text_input("Preferred Revenue Range")
    match_status = st.selectbox("Match Status", ["Not Contacted", "Matched", "Not a Fit", "Archived"])

    submitted = st.form_submit_button("Submit")

    if submitted:
        result = supabase.table("Client_Matchmaking").insert({
            "Client Name": client_name,
            "Company Name": company_name,
            "Company LinkedIn": company_linkedin,
            "Client LinkedIn": client_linkedin,
            "Contact Email": contact_email,
            "Location/Time Zone": location,
            "Preferred Business Model(s)": business_model,
            "Deal Criteria(s)": deal_criteria,
            "Deal Size": deal_size,
            "Deal Source": deal_source,
            "Client Urgency": urgency,
            "Deals Presented": deals_presented,
            "Deals in Discussion": deals_discussion,
            "Deals Closed": deals_closed,
            "Related Document(s)": related_docs,
            "Client Source": client_source,
            "Last Contacted On": str(last_contacted),
            "Follow-Up Date": str(followup_date),
            "Client- Relationship Stage": stage,
            "Primary Analyst Assigned": team_member,
            "Notes/Comments": notes,
            "NDA Status": nda_status,
            "AI summary": ai_summary,
            "Employee Count Preference": emp_pref,
            "Industry Focus": industry,
            "Geographic Focus": geo,
            "Preferred Revenue Range": revenue_range,
            "Match Status": match_status
        }).execute()

        st.success("✅ Client successfully added to Supabase!")
