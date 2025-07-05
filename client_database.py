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
    industry = st.text_input("Industry Focus")
    geo = st.text_input("Geographic Focus")
    revenue_range = st.text_input("Preferred Revenue Range")
    match_status = st.selectbox("Match Status", ["Not Contacted", "Matched", "Not a Fit", "Archived"])
    
    # New fields
    # st.subheader("🎯 Pipeline & Communication")
    # st.markdown("---")
    
    pipeline_status = st.selectbox(
        "Pipeline Status",
        ["Active prospect", "Warm lead", "Cold", "Do not contact"],
        key="pipeline_status"
    )
    
    # Communication Preference as individual checkboxes
    comm_options = ["Email", "Phone", "In-person", "Video calls"]
    communication_preference = []
    st.markdown("**Communication Preference**")
    for opt in comm_options:
        if st.checkbox(opt, key=f"comm_{opt}"):
            communication_preference.append(opt)

    # Sector Exclusions as individual checkboxes
    sector_options = ["Gambling", "Tobacco", "Adult content", "Cryptocurrency", "Weapons", "Alcohol", "Other"]
    sector_exclusions = []
    st.markdown("**Sector Exclusions**")
    for opt in sector_options:
        if st.checkbox(opt, key=f"sector_{opt}"):
            sector_exclusions.append(opt)
    
    deal_pipeline_velocity = st.number_input(
        "Deal Pipeline Velocity (deals/month)",
        min_value=1,
        max_value=50,
        value=5,
        help="How many deals per month they want to see",
        key="deal_pipeline_velocity"
    )
    
    how_they_found_us = st.selectbox(
        "How They Found Us",
        ["Referral", "LinkedIn", "Website", "Event", "Cold Outreach", "Other"],
        help="Track marketing effectiveness",
        key="how_they_found_us"
    )
    
    revenue_range = st.text_input(
        "Revenue Range",
        placeholder="e.g., $100k - $1M, $500k - $5M",
        help="Essential for micro PE deal matching",
        key="revenue_range"
    )
    
    next_action_required = st.text_area(
        "Next Action Required",
        placeholder="Describe the next action needed to keep team aligned...",
        help="Keeps team aligned on next steps",
        key="next_action_required"
    )

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
            "Industry Focus": industry,
            "Geographic Focus": geo,
            "Preferred Revenue Range": revenue_range,
            "Match Status": match_status,
            "Pipeline Status": pipeline_status,
            "Communication Preference": communication_preference,
            "Sector Exclusions": sector_exclusions,
            "Deal Pipeline Velocity": deal_pipeline_velocity,
            "How They Found Us": how_they_found_us,
            "Revenue Range": revenue_range,
            "Next Action Required": next_action_required
        }).execute()

        st.success("✅ Client successfully added to Supabase!")
