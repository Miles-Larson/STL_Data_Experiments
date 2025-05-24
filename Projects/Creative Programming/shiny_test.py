from pathlib import Path

import pandas as pd
import seaborn as sns
import io
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui

#file from https://raw.githubusercontent.com/jcheng5/simplepenguins.R/main/penguins.csv
#With Shiny App installed in VSCODE run with CTRL+SHIFT+P select Shiny:Run Shiny App

sns.set_theme()


df = pd.read_csv("C:\Projects\GitHub\Creative_Programming\Creative Programming\penguins.csv", na_values="NA")
numeric_cols = df.select_dtypes(include=["float64"]).columns.tolist()
species = df["Species"].unique().tolist()
species.sort()

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_selectize(
            "xvar", "X variable", numeric_cols, selected="Bill Length (mm)"
        ),
        ui.input_selectize(
            "yvar", "Y variable", numeric_cols, selected="Bill Depth (mm)"
        ),
        ui.input_checkbox_group(
            "species", "Filter by species", species, selected=species
        ),
        ui.hr(),
        ui.input_switch("by_species", "Show species", value=True),
        ui.input_switch("show_margins", "Show marginal plots", value=True),
        ui.download_button('download_data' , 'Download'),
        # I'm trying to make this fucking download button work
    
    ),
    ui.card(
        ui.output_plot("scatter"),
        
    )
)

def server(input: Inputs, output: Outputs, session: Session):
    @reactive.Calc
    def filtered_df() -> pd.DataFrame:
        """Returns a Pandas data frame that includes only the desired rows"""

        # This calculation "req"uires that at least one species is selected
        req(len(input.species()) > 0)

        # Filter the rows so we only include the desired species
        return df[df["Species"].isin(input.species())]
    
    def download_data():
        csv_buffer = io.StringIO()
        filtered_df.to_csv(csv_buffer, index=False)
        yield csv_buffer.getvalue().encode("utf-8")
        # I'm trying to make this fucking download button work

    @output
    @render.plot
    def scatter():
        """Generates a plot for Shiny to display to the user"""

        # The plotting function to use depends on whether margins are desired
        plotfunc = sns.jointplot if input.show_margins() else sns.scatterplot

        plotfunc(
            data=filtered_df(),
            x=input.xvar(),
            y=input.yvar(),
            hue="Species" if input.by_species() else None,
            hue_order=species,
            legend=False,
        )
        
app = App(app_ui, server)
