import os
import gradio as gr
from dotenv import load_dotenv
from progress_spinner import ProgressSpinner
from paradox_analyzer import (
    analyze_paradox,
    get_paradox_resolution,
    identify_paradox_type,
    check_timeline_consistency
)

# Load environment variables
load_dotenv()

# Check if the API key is set
if not os.getenv("OPENAI_API_KEY"):
    print("Warning: OPENAI_API_KEY not found in environment variables.")
    print("Please create a .env file with your OpenAI API key.")

# CSS for styling
css = """
.title {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 1rem;
}
.subtitle {
    text-align: center;
    font-size: 1.2rem;
    margin-bottom: 2rem;
    color: rgba(0, 0, 0, 0.7);
}
.section-header {
    font-size: 1.5rem;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
}
.footer {
    text-align: center;
    margin-top: 2rem;
    font-size: 0.9rem;
}
"""

# Function to handle paradox analysis
def analyze_time_paradox(
    scenario_text, 
    selected_paradox_type=None, 
    timeline_details=None, 
    causality_settings=None
):
    # Create spinner for visual feedback during analysis
    spinner = ProgressSpinner("Analyzing temporal paradox...")
    
    try:
        # Start the spinner
        spinner.start()
        
        # Analyze the paradox from the scenario
        analysis_result = analyze_paradox(scenario_text)
        
        # Identify the type of paradox
        spinner.update_message("Identifying paradox type...")
        paradox_type = identify_paradox_type(scenario_text, selected_paradox_type)
        
        # Check timeline consistency
        spinner.update_message("Checking timeline consistency...")
        timeline_analysis = check_timeline_consistency(scenario_text, timeline_details)
        
        # Get potential resolutions
        spinner.update_message("Calculating potential resolutions...")
        resolutions = get_paradox_resolution(scenario_text, paradox_type, causality_settings)
    finally:
        # Ensure the spinner is stopped even if an exception occurs
        spinner.stop()
    
    # Combine all results
    full_analysis = f"""
## Paradox Analysis

{analysis_result}

## Paradox Type

{paradox_type}

## Timeline Consistency

{timeline_analysis}

## Potential Resolutions

{resolutions}
"""
    
    return full_analysis

# Build the Gradio interface
with gr.Blocks(css=css) as demo:
    gr.HTML("<h1 class='title'>Time Travel Paradox Analyzer</h1>")
    gr.HTML("<p class='subtitle'>Analyze temporal paradoxes, check timeline consistency, and find potential resolutions.</p>")
    
    with gr.Tab("Paradox Analysis"):
        gr.HTML("<div class='section-header'>Enter your time travel scenario:</div>")
        scenario_input = gr.Textbox(
            placeholder="Describe your time travel scenario in detail...",
            lines=10
        )
        
        with gr.Accordion("Advanced Options", open=False):
            paradox_type = gr.Dropdown(
                choices=[
                    "Grandfather Paradox",
                    "Bootstrap Paradox",
                    "Predestination Paradox",
                    "Butterfly Effect",
                    "Novikov Self-Consistency Principle",
                    "Multiple Timelines",
                    "Other/Unknown"
                ],
                label="Suspected Paradox Type (Optional)",
                value="Other/Unknown"
            )
            
            timeline_details = gr.Textbox(
                placeholder="Additional timeline details...",
                label="Timeline Details (Optional)",
                lines=3
            )
            
            causality_settings = gr.Radio(
                choices=["Fixed Timeline", "Multiple Timelines", "Dynamic Timeline"],
                label="Causality Model (Optional)",
                value="Fixed Timeline"
            )
        
        analyze_button = gr.Button("Analyze Paradox")
        
        gr.HTML("<div class='section-header'>Analysis Results:</div>")
        output = gr.Markdown()
        
        analyze_button.click(
            fn=analyze_time_paradox,
            inputs=[scenario_input, paradox_type, timeline_details, causality_settings],
            outputs=output
        )
    
    with gr.Tab("About"):
        gr.HTML("""
        <div style="padding: 20px;">
            <h2>About Time Travel Paradox Analyzer</h2>
            <p>
                This tool helps writers, game designers, and science fiction enthusiasts analyze time travel scenarios
                for logical consistency and identify potential paradoxes. It uses AI to examine narrative
                time travel mechanics and suggest possible resolutions.
            </p>
            
            <h3>Features:</h3>
            <ul>
                <li>Identifies common time travel paradoxes</li>
                <li>Checks timeline consistency</li>
                <li>Suggests narrative solutions to resolve paradoxes</li>
                <li>Analyzes causality within your scenario</li>
                <li>Helps develop more coherent time travel stories</li>
            </ul>
            
            <h3>Common Paradox Types:</h3>
            <ol>
                <li><strong>Grandfather Paradox</strong>: When a time traveler prevents their own existence</li>
                <li><strong>Bootstrap Paradox</strong>: Information or objects with no origin</li>
                <li><strong>Predestination Paradox</strong>: Attempts to change the past actually cause it</li>
                <li><strong>Butterfly Effect</strong>: Small changes creating massive timeline alterations</li>
                <li><strong>Novikov Self-Consistency Principle</strong>: Time travel is possible but paradoxes are not</li>
            </ol>
        </div>
        """)
    
    gr.HTML("<div class='footer'>Created with OpenAI and Gradio</div>")

# Launch the app
if __name__ == "__main__":
    demo.launch()

