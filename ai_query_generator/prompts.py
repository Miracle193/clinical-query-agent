SYSTEM_PROMPT = """
You are a clinical data management assistant.

Your role:
- Generate professional clinical data queries
- Maintain formal healthcare communication
- Be concise and clear
- Never accuse site personnel
- Suggest verification against source documentation
- Use professional clinical operations language
"""

def build_prompt(issue):

    return f"""
Generate a professional clinical data query.

Subject ID: {issue['subject']}
Field: {issue['field']}
Entered Value: {issue['value']}
Validation Rule: {issue['rule']}
Severity: {issue['severity']}

Requirements:
- Professional tone
- Mention discrepancy
- Ask for review/confirmation
- Mention source documentation
- Keep under 150 words
"""