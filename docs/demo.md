# obd-4757-gev

## Demo
---
1. Unit Test Generation
   - /tests
      - calculator.py
      - @workspace /tests (Sonnet)
      - pytest tests/ <!-- (remove add max float if it appears) -->
   - General Chat info - context, / commands, etc
   - Agent Mode
      - now with no files (or even no directory!)
      - "can you write unit tests for all of my python files? (except for calculator!)"
      - pytest tests/ <!-- let Agent mode iterate if needed -->
      - Hope for some failures (no, seriously! so we can see agent mode in action)
2. Commenting / Documentation
   - Copilot Edits
      - "add comments and docstrings to #file:services.py #file:app.py and #file:models.py"
   - Copilot Chat (or Agent Mode)
      - Create README
        - "@workspace can you create a readme based on my project (we can ignore calculator.py)"
        - tell copilot to also add a desciption section, section on how to run and potential future improvements section
3. Explanation / Translation
3. Other Copilot Features
   - Code Review(s)
   - Vision
      - drag + drop
      - "can you generate a terraform file based on this infra diagram"
4. Custom Instructions
   - show using to specify unit test framework

Unused
---
- Agent mode?
   - run this for me? self-healing? python envs?
   - takes more tokens, hits rate limits more frequently
   - but can run commands (with permission) and can see your whole codebase. No need to provide context!

   <!-- PYTHONPATH=$PYTHONPATH:. pytest tests/ -->