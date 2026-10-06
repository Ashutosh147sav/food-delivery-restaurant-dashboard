import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output


# ==========================================================
# 1. LOAD DATASET
# ==========================================================

df = pd.read_csv("archive.zip")


# ==========================================================
# 2. DATA CLEANING
# ==========================================================

# Clean rating column
df["rate"] = df["rate"].str.replace("/5", "", regex=False)

# Convert rating to numeric
df["rate"] = pd.to_numeric(
    df["rate"],
    errors="coerce"
)

# Convert cost to numeric
df["approx_cost(for two people)"] = pd.to_numeric(
    df["approx_cost(for two people)"],
    errors="coerce"
)

# Convert votes to numeric
df["votes"] = pd.to_numeric(
    df["votes"],
    errors="coerce"
)

# Remove missing values
df = df.dropna(
    subset=[
        "rate",
        "votes",
        "approx_cost(for two people)",
        "listed_in(type)"
    ]
)


# ==========================================================
# 3. VALUE FOR MONEY SCORE
# ==========================================================

# Higher score means better rating at relatively lower cost
df["value_score"] = (
    df["rate"]
    / df["approx_cost(for two people)"]
) * 1000


# ==========================================================
# 4. CREATE DASH APPLICATION
# ==========================================================

app = Dash(__name__)

app.title = "Food Delivery Restaurant Analytics"


# ==========================================================
# 5. COLOR THEME
# ==========================================================

NAVY = "#111827"
DARK_NAVY = "#0F172A"

ORANGE = "#F97316"
LIGHT_ORANGE = "#FFF7ED"

BLUE = "#2563EB"
GREEN = "#059669"
PURPLE = "#7C3AED"

WHITE = "#FFFFFF"
LIGHT_BG = "#F3F4F6"

TEXT = "#1F2937"
MUTED = "#6B7280"
BORDER = "#E5E7EB"


# ==========================================================
# 6. KPI CARD FUNCTION
# ==========================================================

def create_kpi_card(title, value, icon):

    return html.Div(

        [

            html.Div(
                icon,
                style={
                    "fontSize": "28px",
                    "marginBottom": "8px"
                }
            ),

            html.Div(
                title,
                style={
                    "fontSize": "14px",
                    "fontWeight": "600",
                    "color": MUTED,
                    "marginBottom": "6px"
                }
            ),

            html.Div(
                value,
                style={
                    "fontSize": "28px",
                    "fontWeight": "700",
                    "color": TEXT
                }
            )

        ],

        style={
            "flex": "1",
            "minWidth": "180px",
            "backgroundColor": WHITE,
            "padding": "22px",
            "borderRadius": "16px",
            "border": f"1px solid {BORDER}",
            "boxShadow": "0 4px 12px rgba(0,0,0,0.06)"
        }
    )


# ==========================================================
# 7. CHART CARD FUNCTION
# ==========================================================

def create_chart_card(title, description, graph_id):

    return html.Div(

        [

            html.H3(
                title,
                style={
                    "margin": "0 0 4px 0",
                    "fontSize": "19px"
                }
            ),

            html.P(
                description,
                style={
                    "color": MUTED,
                    "fontSize": "13px",
                    "margin": "0 0 10px 0"
                }
            ),

            dcc.Graph(
                id=graph_id,
                config={
                    "displayModeBar": False
                }
            )

        ],

        style={
            "backgroundColor": WHITE,
            "padding": "20px",
            "borderRadius": "16px",
            "border": f"1px solid {BORDER}",
            "boxShadow": "0 4px 12px rgba(0,0,0,0.05)",
            "flex": "1",
            "minWidth": "450px"
        }
    )


# ==========================================================
# 8. DASHBOARD LAYOUT
# ==========================================================

app.layout = html.Div(

    style={
        "backgroundColor": LIGHT_BG,
        "minHeight": "100vh",
        "fontFamily": "Arial, sans-serif",
        "color": TEXT
    },

    children=[

        # ==================================================
        # HEADER
        # ==================================================

        html.Div(

            [

                html.Div(

                    [

                        html.Div(
                            "🍽️",
                            style={
                                "fontSize": "42px",
                                "marginRight": "15px"
                            }
                        ),

                        html.Div(

                            [

                                html.H1(
                                    "Food Delivery Analytics",
                                    style={
                                        "margin": "0",
                                        "fontSize": "32px",
                                        "fontWeight": "700"
                                    }
                                ),

                                html.P(
                                    "Restaurant insights powered by Zomato data",
                                    style={
                                        "margin": "6px 0 0 0",
                                        "fontSize": "15px",
                                        "opacity": "0.85"
                                    }
                                )

                            ]
                        )

                    ],

                    style={
                        "display": "flex",
                        "alignItems": "center"
                    }
                )

            ],

            style={
                "backgroundColor": NAVY,
                "color": WHITE,
                "padding": "28px 5%",
                "boxShadow": "0 4px 15px rgba(0,0,0,0.15)"
            }
        ),


        # ==================================================
        # MAIN CONTENT
        # ==================================================

        html.Div(

            [

                # ==================================================
                # FILTER
                # ==================================================

                html.Div(

                    [

                        html.H3(
                            "Restaurant Analysis",
                            style={
                                "margin": "0 0 5px 0",
                                "fontSize": "20px"
                            }
                        ),

                        html.P(
                            "Select a restaurant type to explore its performance.",
                            style={
                                "margin": "0 0 15px 0",
                                "color": MUTED,
                                "fontSize": "14px"
                            }
                        ),

                        dcc.Dropdown(

                            id="type-dropdown",

                            options=[

                                {
                                    "label": "🍽️ All Restaurant Types",
                                    "value": "all"
                                }

                            ] + [

                                {
                                    "label": restaurant_type,
                                    "value": restaurant_type
                                }

                                for restaurant_type in sorted(
                                    df["listed_in(type)"]
                                    .dropna()
                                    .unique()
                                )
                            ],

                            value="all",

                            clearable=False,

                            style={
                                "fontSize": "15px"
                            }
                        )

                    ],

                    style={
                        "backgroundColor": WHITE,
                        "padding": "24px",
                        "borderRadius": "16px",
                        "border": f"1px solid {BORDER}",
                        "boxShadow": "0 4px 12px rgba(0,0,0,0.05)",
                        "marginBottom": "25px"
                    }
                ),


                # ==================================================
                # KPI CARDS
                # ==================================================

                html.Div(
                    id="kpi-container",

                    style={
                        "display": "flex",
                        "gap": "18px",
                        "flexWrap": "wrap",
                        "marginBottom": "30px"
                    }
                ),


                # ==================================================
                # ROW 1 - RATING + POPULARITY
                # ==================================================

                html.Div(

                    [

                        create_chart_card(
                            "⭐ Top Restaurants by Rating",
                            "Highest-rated restaurants in the selected category.",
                            "rating-chart"
                        ),

                        create_chart_card(
                            "🔥 Most Popular Restaurants",
                            "Restaurants receiving the highest number of votes.",
                            "votes-chart"
                        )

                    ],

                    style={
                        "display": "flex",
                        "gap": "20px",
                        "flexWrap": "wrap",
                        "marginBottom": "25px"
                    }
                ),


                # ==================================================
                # ROW 2 - SCATTER + RESTAURANT TYPE
                # ==================================================

                html.Div(

                    [

                        create_chart_card(
                            "💰 Rating vs Cost",
                            "Relationship between restaurant rating and approximate cost.",
                            "cost-rating-chart"
                        ),

                        create_chart_card(
                            "🍕 Restaurant Type Distribution",
                            "Number of restaurants in each restaurant category.",
                            "type-chart"
                        )

                    ],

                    style={
                        "display": "flex",
                        "gap": "20px",
                        "flexWrap": "wrap",
                        "marginBottom": "25px"
                    }
                ),


                # ==================================================
                # ROW 3 - ONLINE ORDER + TABLE BOOKING
                # ==================================================

                html.Div(

                    [

                        create_chart_card(
                            "📦 Online Order Analysis",
                            "Comparison of restaurants offering online ordering.",
                            "online-order-chart"
                        ),

                        create_chart_card(
                            "🪑 Table Booking Analysis",
                            "Comparison of restaurants offering table booking.",
                            "table-booking-chart"
                        )

                    ],

                    style={
                        "display": "flex",
                        "gap": "20px",
                        "flexWrap": "wrap",
                        "marginBottom": "25px"
                    }
                ),


                # ==================================================
                # ROW 4 - VALUE FOR MONEY
                # ==================================================

                html.Div(

                    [

                        html.H3(
                            "💎 Best Value-for-Money Restaurants",
                            style={
                                "margin": "0 0 4px 0",
                                "fontSize": "19px"
                            }
                        ),

                        html.P(
                            "Restaurants with relatively strong ratings compared with their approximate cost.",
                            style={
                                "color": MUTED,
                                "fontSize": "13px",
                                "margin": "0 0 10px 0"
                            }
                        ),

                        dcc.Graph(
                            id="value-chart",
                            config={
                                "displayModeBar": False
                            }
                        )

                    ],

                    style={
                        "backgroundColor": WHITE,
                        "padding": "20px",
                        "borderRadius": "16px",
                        "border": f"1px solid {BORDER}",
                        "boxShadow": "0 4px 12px rgba(0,0,0,0.05)",
                        "marginBottom": "30px"
                    }
                ),


                # ==================================================
                # FOOTER
                # ==================================================

                html.Div(

                    [

                        html.P(
                            "Food Delivery Restaurant Analytics Dashboard",
                            style={
                                "margin": "0",
                                "fontWeight": "600"
                            }
                        ),

                        html.P(
                            "Built using Python • Pandas • Plotly • Dash",
                            style={
                                "margin": "5px 0 0 0",
                                "fontSize": "13px",
                                "color": MUTED
                            }
                        )

                    ],

                    style={
                        "textAlign": "center",
                        "padding": "20px 0 10px 0"
                    }
                )

            ],

            style={
                "width": "90%",
                "maxWidth": "1400px",
                "margin": "30px auto"
            }
        )
    ]
)


# ==========================================================
# 9. CALLBACK
# ==========================================================

@app.callback(

    [

        Output(
            "rating-chart",
            "figure"
        ),

        Output(
            "votes-chart",
            "figure"
        ),

        Output(
            "cost-rating-chart",
            "figure"
        ),

        Output(
            "type-chart",
            "figure"
        ),

        Output(
            "online-order-chart",
            "figure"
        ),

        Output(
            "table-booking-chart",
            "figure"
        ),

        Output(
            "value-chart",
            "figure"
        ),

        Output(
            "kpi-container",
            "children"
        )

    ],

    Input(
        "type-dropdown",
        "value"
    )
)


def update_dashboard(selected_type):


    # ======================================================
    # FILTER DATA
    # ======================================================

    if selected_type == "all":

        filtered_df = df.copy()

    else:

        filtered_df = df[
            df["listed_in(type)"] == selected_type
        ].copy()


    # ======================================================
    # KPI CALCULATIONS
    # ======================================================

    total_restaurants = filtered_df[
        "name"
    ].nunique()

    average_rating = filtered_df[
        "rate"
    ].mean()

    average_cost = filtered_df[
        "approx_cost(for two people)"
    ].mean()

    total_votes = filtered_df[
        "votes"
    ].sum()


    # ======================================================
    # KPI CARDS
    # ======================================================

    kpi_cards = [

        create_kpi_card(
            "Total Restaurants",
            f"{total_restaurants}",
            "🍽️"
        ),

        create_kpi_card(
            "Average Rating",
            f"{average_rating:.2f} / 5",
            "⭐"
        ),

        create_kpi_card(
            "Average Cost for Two",
            f"₹{average_cost:.0f}",
            "💰"
        ),

        create_kpi_card(
            "Total Votes",
            f"{total_votes:,}",
            "👍"
        )

    ]


    # ======================================================
    # CHART 1
    # TOP 10 RESTAURANTS BY RATING
    # ======================================================

    rating_data = (

        filtered_df

        .groupby(
            "name",
            as_index=False
        )["rate"]

        .mean()

        .sort_values(
            "rate",
            ascending=False
        )

        .head(10)
    )


    rating_fig = px.bar(

        rating_data,

        x="rate",

        y="name",

        orientation="h",

        color="rate",

        color_continuous_scale=[
            "#FED7AA",
            "#FB923C",
            "#EA580C"
        ],

        labels={
            "rate": "Rating",
            "name": "Restaurant"
        }
    )


    rating_fig.update_layout(

        height=430,

        margin={
            "l": 10,
            "r": 10,
            "t": 20,
            "b": 50
        },

        plot_bgcolor="white",

        paper_bgcolor="white",

        coloraxis_showscale=False,

        xaxis={
            "range": [0, 5],
            "gridcolor": "#E5E7EB"
        },

        yaxis={
            "categoryorder": "total ascending"
        }
    )


    # ======================================================
    # CHART 2
    # TOP 10 RESTAURANTS BY VOTES
    # ======================================================

    votes_data = (

        filtered_df

        .groupby(
            "name",
            as_index=False
        )["votes"]

        .sum()

        .sort_values(
            "votes",
            ascending=False
        )

        .head(10)
    )


    votes_fig = px.bar(

        votes_data,

        x="name",

        y="votes",

        color="votes",

        color_continuous_scale=[
            "#BFDBFE",
            "#60A5FA",
            "#2563EB"
        ],

        labels={
            "name": "Restaurant",
            "votes": "Votes"
        }
    )


    votes_fig.update_layout(

        height=430,

        margin={
            "l": 10,
            "r": 10,
            "t": 20,
            "b": 90
        },

        plot_bgcolor="white",

        paper_bgcolor="white",

        coloraxis_showscale=False,

        xaxis={
            "tickangle": -45
        },

        yaxis={
            "gridcolor": "#E5E7EB"
        }
    )


    # ======================================================
    # CHART 3
    # RATING VS COST
    # ======================================================

    scatter_fig = px.scatter(

        filtered_df,

        x="approx_cost(for two people)",

        y="rate",

        hover_name="name",

        size="votes",

        color="rate",

        color_continuous_scale=[
            "#FED7AA",
            "#FB923C",
            "#EA580C"
        ],

        labels={

            "approx_cost(for two people)":
                "Approximate Cost for Two (₹)",

            "rate":
                "Restaurant Rating",

            "votes":
                "Votes"
        }
    )


    scatter_fig.update_layout(

        height=430,

        margin={
            "l": 10,
            "r": 10,
            "t": 20,
            "b": 60
        },

        plot_bgcolor="white",

        paper_bgcolor="white",

        xaxis={
            "gridcolor": "#E5E7EB"
        },

        yaxis={
            "range": [0, 5],
            "gridcolor": "#E5E7EB"
        }
    )


    # ======================================================
    # CHART 4
    # RESTAURANT TYPE DISTRIBUTION
    # ======================================================

    type_data = (

        filtered_df

        ["listed_in(type)"]

        .value_counts()

        .reset_index()
    )


    type_data.columns = [
        "Restaurant Type",
        "Count"
    ]


    type_fig = px.pie(

        type_data,

        names="Restaurant Type",

        values="Count",

        hole=0.55,

        labels={
            "Restaurant Type": "Restaurant Type",
            "Count": "Restaurants"
        }
    )


    type_fig.update_layout(

        height=430,

        margin={
            "l": 10,
            "r": 10,
            "t": 20,
            "b": 20
        },

        paper_bgcolor="white",

        legend={
            "orientation": "h",
            "y": -0.1
        }
    )


    # ======================================================
    # CHART 5
    # ONLINE ORDER ANALYSIS
    # ======================================================

    online_data = (

        filtered_df

        .groupby(
            "online_order",
            as_index=False
        )

        .agg(

            Restaurants=(
                "name",
                "nunique"
            ),

            Average_Rating=(
                "rate",
                "mean"
            )

        )
    )


    online_data["Order Status"] = online_data[
        "online_order"
    ].map({

        "Yes": "Online Order Available",

        "No": "Online Order Not Available"

    })


    online_fig = px.bar(

        online_data,

        x="Order Status",

        y="Restaurants",

        color="Order Status",

        color_discrete_sequence=[
            ORANGE,
            BLUE
        ],

        text="Restaurants",

        labels={
            "Restaurants": "Number of Restaurants",
            "Order Status": "Online Order"
        }
    )


    online_fig.update_traces(
        textposition="outside"
    )


    online_fig.update_layout(

        height=430,

        showlegend=False,

        margin={
            "l": 10,
            "r": 10,
            "t": 20,
            "b": 60
        },

        plot_bgcolor="white",

        paper_bgcolor="white",

        yaxis={
            "gridcolor": "#E5E7EB"
        }
    )


    # ======================================================
    # CHART 6
    # TABLE BOOKING ANALYSIS
    # ======================================================

    booking_data = (

        filtered_df

        .groupby(
            "book_table",
            as_index=False
        )

        .agg(

            Restaurants=(
                "name",
                "nunique"
            ),

            Average_Rating=(
                "rate",
                "mean"
            )

        )
    )


    booking_data["Booking Status"] = booking_data[
        "book_table"
    ].map({

        "Yes": "Table Booking Available",

        "No": "Table Booking Not Available"

    })


    booking_fig = px.bar(

        booking_data,

        x="Booking Status",

        y="Restaurants",

        color="Booking Status",

        color_discrete_sequence=[
            GREEN,
            PURPLE
        ],

        text="Restaurants",

        labels={
            "Restaurants": "Number of Restaurants",
            "Booking Status": "Table Booking"
        }
    )


    booking_fig.update_traces(
        textposition="outside"
    )


    booking_fig.update_layout(

        height=430,

        showlegend=False,

        margin={
            "l": 10,
            "r": 10,
            "t": 20,
            "b": 60
        },

        plot_bgcolor="white",

        paper_bgcolor="white",

        yaxis={
            "gridcolor": "#E5E7EB"
        }
    )


    # ======================================================
    # CHART 7
    # VALUE FOR MONEY
    # ======================================================

    value_data = (

        filtered_df

        .groupby(
            "name",
            as_index=False
        )

        .agg(

            Rating=(
                "rate",
                "mean"
            ),

            Cost=(
                "approx_cost(for two people)",
                "mean"
            ),

            Value_Score=(
                "value_score",
                "mean"
            )

        )

        .sort_values(
            "Value_Score",
            ascending=False
        )

        .head(10)
    )


    value_fig = px.bar(

        value_data,

        x="Value_Score",

        y="name",

        orientation="h",

        color="Value_Score",

        color_continuous_scale=[
            "#D1FAE5",
            "#34D399",
            "#059669"
        ],

        hover_data=[
            "Rating",
            "Cost"
        ],

        labels={
            "Value_Score": "Value Score",
            "name": "Restaurant",
            "Rating": "Rating",
            "Cost": "Cost for Two"
        }
    )


    value_fig.update_layout(

        height=450,

        margin={
            "l": 10,
            "r": 10,
            "t": 20,
            "b": 50
        },

        plot_bgcolor="white",

        paper_bgcolor="white",

        coloraxis_showscale=False,

        xaxis={
            "gridcolor": "#E5E7EB"
        },

        yaxis={
            "categoryorder": "total ascending"
        }
    )


    # ======================================================
    # RETURN ALL CHARTS AND KPIs
    # ======================================================

    return (

        rating_fig,

        votes_fig,

        scatter_fig,

        type_fig,

        online_fig,

        booking_fig,

        value_fig,

        kpi_cards

    )


# ==========================================================
# 10. RUN DASHBOARD
# ==========================================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8050,
        debug=True
    )