import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configure page layout and title
st.set_page_config(layout='wide', page_title='Startup Funding Analysis', page_icon='💡')

# Load data
df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# Custom styles with stunning background and cursor effects
st.markdown("""
    <style>
        /* Global background styling */
        body {
            background: url('https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80');
            background-size: cover;
            background-attachment: fixed;
            font-family: 'Arial', sans-serif;
            color: #333;
        }

        /* Sidebar styling */
        .sidebar .sidebar-content {
            background-color: rgba(248, 249, 250, 0.8);
            padding: 20px;
            border-radius: 10px;
        }

        /* Metric styling */
        .metric {
            background-color: rgba(227, 242, 253, 0.8);
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-weight: bold;
            color: #0d6efd;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* Header and title styling */
        h1, h2, h3 {
            color: #0d6efd;
            font-weight: bold;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
        }

        /* Cursor sparkle effect */
        * {
            cursor: url('https://cur.cursors-4u.net/cursors/cur-2/cur170.cur'), auto;
        }

        .sparkle-trail {
            position: fixed;
            pointer-events: none;
            z-index: 10000;
        }

    </style>
    <script>
        document.addEventListener('mousemove', (e) => {
            const sparkle = document.createElement('div');
            sparkle.className = 'sparkle-trail';
            sparkle.style.left = `${e.pageX}px`;
            sparkle.style.top = `${e.pageY}px`;
            sparkle.style.width = '10px';
            sparkle.style.height = '10px';
            sparkle.style.background = 'radial-gradient(circle, #ffd700, rgba(255, 215, 0, 0))';
            sparkle.style.borderRadius = '50%';
            sparkle.style.animation = 'sparkle-fade 0.5s linear';

            document.body.appendChild(sparkle);
            setTimeout(() => sparkle.remove(), 500);
        });

        const style = document.createElement('style');
        style.innerHTML = `
            @keyframes sparkle-fade {
                from { opacity: 1; transform: scale(1); }
                to { opacity: 0; transform: scale(2); }
            }
        `;
        document.head.appendChild(style);
    </script>
""", unsafe_allow_html=True)

# Overall Analysis
def load_overall_analysis():
    st.title('📊 Overall Analysis')

    # Total invested amount
    total = round(df['amount'].sum())
    # Max amount infused in a startup
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    # Avg ticket size
    avg_funding = df.groupby('startup')['amount'].sum().mean()
    # Total funded startups
    num_startups = df['startup'].nunique()

    # Metrics section
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric('💵 Total Investment', str(total) + ' Cr')
    with col2:
        st.metric('🏆 Max Investment', str(max_funding) + ' Cr')
    with col3:
        st.metric('📈 Avg Ticket Size', str(round(avg_funding)) + ' Cr')
    with col4:
        st.metric('🚀 Funded Startups', num_startups)

    # MoM graph
    st.header('📅 Month-on-Month Analysis')
    selected_option = st.selectbox('Select Type', ['Total', 'Count'], key='mom_analysis')
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')

    fig3, ax3 = plt.subplots(figsize=(10, 5))
    ax3.plot(temp_df['x_axis'], temp_df['amount'], marker='o', color='#0d6efd')
    ax3.set_title('Month-on-Month Investment Analysis', fontsize=16)
    ax3.set_xlabel('Month-Year', fontsize=12)
    ax3.set_ylabel('Amount (Cr)', fontsize=12)
    ax3.grid(True, linestyle='--', alpha=0.5)
    plt.xticks(rotation=45, ha='right', fontsize=8)

    st.pyplot(fig3)

# Investor Details Analysis
def load_investor_details(investor):
    st.title(f'Investor Analysis: {investor}')

    # Recent 5 investments
    last5_df = df[df['investors'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('🕒 Most Recent Investments')
    st.dataframe(last5_df)

    col1, col2 = st.columns(2)
    with col1:
        # Biggest investments
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('💼 Biggest Investments')
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(big_series.index, big_series.values, color='#0d6efd')
        ax.set_title('Biggest Investments', fontsize=16)
        ax.set_ylabel('Amount (Cr)', fontsize=12)
        st.pyplot(fig)

    with col2:
        # Sector-wise investments
        vertical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('📊 Sectors Invested In')
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        ax1.pie(vertical_series, labels=vertical_series.index, autopct='%0.01f%%', startangle=90, colors=plt.cm.tab10.colors)
        ax1.set_title('Sectors Invested In', fontsize=16)
        st.pyplot(fig1)

    # Year-over-Year investment
    df['year'] = df['date'].dt.year
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()

    st.subheader('📈 Year-over-Year Investment')
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    ax2.plot(year_series.index, year_series.values, marker='o', color='#0d6efd')
    ax2.set_title('Year-over-Year Investment', fontsize=16)
    ax2.set_xlabel('Year', fontsize=12)
    ax2.set_ylabel('Amount (Cr)', fontsize=12)
    ax2.grid(True, linestyle='--', alpha=0.5)

    st.pyplot(fig2)

# Sidebar navigation
st.sidebar.title('🔍 Startup Funding Analysis')
st.sidebar.markdown('Navigate through the options below to explore the funding details!')
option = st.sidebar.radio('Select an Option', ['Overall Analysis', 'StartUp', 'Investor'], index=0)

if option == 'Overall Analysis':
    load_overall_analysis()

elif option == 'StartUp':
    selected_startup = st.sidebar.selectbox('Select StartUp', sorted(df['startup'].unique().tolist()), key='startup_select')
    btn1 = st.sidebar.button('Find StartUp Details')
    st.title('🚀 StartUp Analysis')
    # Placeholder for startup-specific analysis (extend as needed)
else:
    selected_investor = st.sidebar.selectbox('Select Investor', sorted(set(df['investors'].str.split(',').sum())), key='investor_select')
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)
