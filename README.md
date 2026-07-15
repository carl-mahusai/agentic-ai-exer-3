# agentic-ai-exer-3

pip install -r requirements.txt

python main.py

## Core Specifications

* The policy brief generator takes a **topic** as its input.
* The policy brief generator must have the following agents:
  * Debater Agents (**at least 2**)
    * Proponent Agent
      * Generates arguments **for the topic** (e.g. “Remote work increases productivity and employee satisfaction.”).
    * Opponent Agent
      * Generates arguments **against the topic** (e.g. “Remote work reduces collaboration and innovation.”).
    * Optional: Agents that offer alternative viewpoints.
  * Aggregator / Compromise Agent
    * Takes the arguments from the debater agents.
    * Synthesizes into a **balanced resolution** (e.g. “Hybrid work policy with 3 days in-office”). The agent should add context, conditions, and rationale like in typical policy documents.
    * The final writeup (**in markdown format**) must specify the title, policy, as well as justifications on how it ensures compromise between arguments shown by the debaters.
  * Evaluator Agent
    * Scores the resolution against the following metrics:
      * Clarity (is the writeup understandable?)
      * Fairness (did it represent both sides?)
      * Actionability (is it implementable?)
      * Compliance (does it align with legal standards?)
    * Provides a qualitative explanation of the scoring decisions, identifies strengths, and outlines opportunities for refinement.
    * The output must be structured, for example:

      ```json
      {
        "evaluation": {
            "clarity": 8.0,
            "fairness": 9.0,
            "actionability": 7.0,
            "feedback": {
                "justification": "The policy is clear but ...",
                "strengths": "Strong compliance, ...",
                "improvements": "Add measurable ..."
            }
        }
      }
      ```
  * Publisher Agent
    * Takes the writeup from the compromise agent and the evaluation scores from the evaluator agent.
    * Must have the following tools:
      * A function that determines:
        * the overall evaluation score by taking the average of the metrics.
        * if the policy **FAILS** when:
          * At least one metric is less than 6, or
          * Overall score is less than 6.5.
      * A function that converts the markdown output to PDF and saves it to a `data/policies` directory with the appropriate name (i.e. `<title>.pdf`).
    * Generates the PDF version of the final writeup if it receives passing feedback.
    * Generates a short report on the overall evaluation (overall score, PASS / FAIL remark) and on the status of the PDF generation (e.g. where the file is saved). A text output from the agent is enough. No need to save generated reports.
* Create **at least three policy** documents to be used in later exercises.

possbible structure

project/
│
├── agents/
│   ├── proponent.py
│   ├── opponent.py
│   ├── aggregator.py
│   ├── evaluator.py
│   └── publisher.py
│
├── tools/
│   ├── pdf.py
│   └── scoring.py
│
├── workflows/
│   └── policy_workflow.py
│
├── schemas/
│   ├── evaluation.py
│   └── policy.py
│
├── data/
│   └── policies/
│
└── main.py