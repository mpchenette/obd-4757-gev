# obd-4757-gev

## Demo
---
1. Unit Test Generation
   - /tests
      - calculator.py
      - @workspace /tests (Sonnet)
      - pytest tests/
   - General Chat info - context, / commands, etc
   - Agent Mode
      - now with no files (or even no directory!)
      - "can you write unit tests for all of my python files? (except for calculator!)"
      - pytest tests/
2. Commenting / Documentation
   - Copilot Edits
      - "add comments and docstrings to all my python files"
   - Create README
        - tell copilot to also add a desciption section, section on how to run and potential future improvements section
3. Other Copilot Features
   - Code Review(s)
   - Vision? arch diagram to terraform?
4. Custom Instructions
   - show using to specify unit test framework
5. Agent mode?
   - run this for me? self-healing? python envs?
   - takes more tokens, hits rate limits more frequently
   - but can run commands (with permission) and can see your whole codebase. No need to provide context!

   <!--    - PYTHONPATH=$PYTHONPATH:. pytest tests/ -->