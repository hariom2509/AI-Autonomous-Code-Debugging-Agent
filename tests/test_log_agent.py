from agents.log_analyzer_agent import analyze_log

log = """
Traceback (most recent call last):
File "views.py", line 22, in login_user
user = request.data['user_id']
KeyError: 'user_id'
"""

result = analyze_log(log)

print(result)