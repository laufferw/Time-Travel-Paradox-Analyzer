# Time Travel Paradox Analyzer

An interactive application that uses AI to analyze time travel scenarios for logical consistency, identify paradoxes, and suggest potential resolutions.

## Overview

The Time Travel Paradox Analyzer is designed for writers, game designers, and science fiction enthusiasts who want to ensure their time travel narratives maintain logical consistency. The tool leverages OpenAI's GPT models to:

- Analyze time travel scenarios for logical contradictions
- Identify specific types of temporal paradoxes
- Check timeline consistency across multiple events
- Generate potential resolutions that maintain narrative coherence

## Features

- **Paradox Identification**: Detects common time travel paradoxes like Grandfather Paradox, Bootstrap Paradox, and more
- **Timeline Analysis**: Evaluates the logical consistency of events across a timeline
- **Resolution Suggestions**: Provides multiple approaches to resolve identified paradoxes
- **Interactive Interface**: User-friendly Gradio web interface for easy interaction
- **Customization Options**: Set preferences for causality models and timeline mechanics

## Common Paradox Types

1. **Grandfather Paradox**: When a time traveler prevents their own existence
2. **Bootstrap Paradox**: Information or objects with no origin (causal loop)
3. **Predestination Paradox**: Attempts to change the past actually cause it
4. **Butterfly Effect**: Small changes creating massive timeline alterations
5. **Novikov Self-Consistency**: The principle that paradoxes cannot occur

## Installation

### Prerequisites

- Python 3.8+
- OpenAI API key

### Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/time-paradox-analyzer.git
   cd time-paradox-analyzer
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your OpenAI API key:
   ```
   cp .env.example .env
   # Edit .env file and add your API key
   ```

## Usage

1. Run the application:
   ```
   python main.py
   ```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:7860)

3. Enter your time travel scenario in the text box and click "Analyze Paradox"

4. For more detailed analysis, use the Advanced Options to specify:
   - Suspected paradox type
   - Additional timeline details
   - Preferred causality model

## Example Scenarios

### Basic Grandfather Paradox
```
A man travels back in time and accidentally prevents his grandparents from meeting, 
potentially erasing his own existence.
```

### Bootstrap Paradox
```
A composer travels back in time and shares his famous symphony with his younger self, 
who then becomes famous for "creating" it. The music has no original creator.
```

### Predestination Paradox
```
A detective travels back in time to prevent a crime, only to accidentally cause 
the very incident they were trying to prevent.
```

## Technical Details

- Built with Python, Gradio, and OpenA

