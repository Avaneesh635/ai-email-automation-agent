import streamlit as st

from agents import (
    classify_email,
    analyze_priority,
    summarize_email,
    extract_actions,
    generate_reply
)

st.set_page_config(
    page_title="Multi-Agent Email Automation System",
    page_icon="📧",
    layout="wide"
)

st.title(
    "📧 Multi-Agent Email Automation System"
)

email_text = st.text_area(
    "Paste Email",
    height=300
)

if st.button(
    "Analyze Email"
):

    if email_text:

        with st.spinner(
            "Running Agents..."
        ):

            category = classify_email(
                email_text
            )

            priority = analyze_priority(
                email_text
            )

            summary = summarize_email(
                email_text
            )

            actions = extract_actions(
                email_text
            )

            reply = generate_reply(
                email_text
            )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Category",
                category
            )

        with col2:

            st.metric(
                "Priority",
                priority
            )

        st.divider()

        st.subheader(
            "📄 Summary"
        )

        st.info(
            summary
        )

        st.subheader(
            "✅ Action Items"
        )

        st.success(
            actions
        )

        st.subheader(
            "✉️ Suggested Reply"
        )

        st.write(
            reply
        )

        report = f"""
CATEGORY
{category}

PRIORITY
{priority}

SUMMARY
{summary}

ACTION ITEMS
{actions}

SUGGESTED REPLY
{reply}
"""

        st.download_button(
            label="📥 Download Report",
            data=report,
            file_name="email_analysis.txt",
            mime="text/plain"
        )

    else:

        st.warning(
            "Please paste an email."
        )