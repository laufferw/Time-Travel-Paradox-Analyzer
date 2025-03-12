import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_paradox(scenario_text):
    """
    Analyze a time travel scenario to identify potential paradoxes
    
    Args:
        scenario_text (str): The time travel scenario to analyze
        
    Returns:
        str: Analysis of potential paradoxes in the scenario
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": """You are a Time Travel Paradox Analyzer specializing in temporal mechanics, 
                causal relationships, and logical consistency within time travel narratives.
                Analyze the scenario carefully and identify any potential paradoxes or logical inconsistencies."""},
                {"role": "user", "content": f"Analyze this time travel scenario for paradoxes:\n\n{scenario_text}"}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error analyzing paradox: {str(e)}"

def identify_paradox_type(scenario_text, user_suggested_type=None):
    """
    Identify the specific type of time travel paradox
    
    Args:
        scenario_text (str): The time travel scenario text
        user_suggested_type (str, optional): User's suggestion of paradox type
        
    Returns:
        str: Identified paradox type with explanation
    """
    prompt_addition = ""
    if user_suggested_type and user_suggested_type != "Other/Unknown":
        prompt_addition = f"\n\nThe user suspects this might be a {user_suggested_type}. Evaluate if this is correct."
    
    try:
        response = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": """You are a Time Travel Paradox Classifier specializing in identifying 
                specific types of temporal paradoxes. Common types include:
                - Grandfather Paradox (actions preventing one's existence)
                - Bootstrap Paradox (information/objects with no origin)
                - Predestination Paradox (attempts to change the past cause it)
                - Butterfly Effect (small changes causing massive alterations)
                - Novikov Self-Consistency Principle (paradoxes are impossible)
                - Multiple Timelines/Parallel Universes
                
                Identify the most likely type of paradox in the scenario."""},
                {"role": "user", "content": f"Identify the type of time travel paradox in this scenario:{prompt_addition}\n\n{scenario_text}"}
            ],
            temperature=0.7,
            max_tokens=800
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error identifying paradox type: {str(e)}"

def check_timeline_consistency(scenario_text, timeline_details=None):
    """
    Analyze the consistency of the timeline in the scenario
    
    Args:
        scenario_text (str): The time travel scenario text
        timeline_details (str, optional): Additional timeline details provided by user
        
    Returns:
        str: Timeline consistency analysis
    """
    additional_context = ""
    if timeline_details:
        additional_context = f"\n\nAdditional timeline details provided by the user:\n{timeline_details}"
    
    try:
        response = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": """You are a Timeline Consistency Analyzer specializing in evaluating 
                the logical consistency of time travel narratives. Focus on:
                - Cause and effect relationships
                - Timeline branches and alterations
                - Internal consistency of the narrative
                - Logical contradictions
                
                Provide a detailed analysis of the timeline's consistency."""},
                {"role": "user", "content": f"Analyze the timeline consistency in this scenario:{additional_context}\n\n{scenario_text}"}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error checking timeline consistency: {str(e)}"

def get_paradox_resolution(scenario_text, paradox_type, causality_model=None):
    """
    Generate potential resolutions for the identified paradox
    
    Args:
        scenario_text (str): The time travel scenario text
        paradox_type (str): The identified type of paradox
        causality_model (str, optional): The causality model preference (Fixed Timeline, Multiple Timelines, etc.)
        
    Returns:
        str: Potential resolutions for the paradox
    """
    causality_context = ""
    if causality_model:
        causality_context = f"\n\nPreferred causality model: {causality_model}"
    
    try:
        response = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": """You are a Time Travel Paradox Resolution Specialist who finds logical 
                and narrative solutions to temporal paradoxes. Consider:
                - Multiple timeline/universe theories
                - Fixed timeline approaches (Novikov Self-Consistency)
                - Dynamic timeline mechanics
                - Narrative devices to maintain coherence
                - Scientific theories that might apply
                
                Provide 3-5 potential resolutions that maintain logical consistency."""},
                {"role": "user", "content": f"Suggest possible resolutions for the following time travel scenario:{causality_context}\n\n{scenario_text}"}
            ],
            temperature=0.8,
            max_tokens=1200
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating paradox resolutions: {str(e)}"

