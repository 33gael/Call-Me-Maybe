# Call Me Maybe

Call Me Maybe is an educational function-calling project built around the
`Qwen/Qwen3-0.6B` language model. Its goal is to translate a natural-language
request into a structured function call while guaranteeing that the generated
output is valid JSON and conforms to the available function definitions.

> **Project status:** work in progress. The development environment and SDK
> exploration are functional, but the final function-calling pipeline has not
> been implemented yet.

## Final Goal

The completed application will receive:

- a JSON file describing the available functions and their parameter schemas;
- one or more natural-language prompts;
- optional input and output paths supplied through command-line arguments.

For each prompt, it must produce an object with exactly three fields:
`prompt`, `name`, and `parameters`. For example, a request asking for the sum of
two numbers should become a structured call to the appropriate addition
function with correctly typed arguments.

The main technical objective is to implement **constrained decoding**. At every
generation step, invalid tokens will be masked by setting their logits to
negative infinity. This prevents the model from producing malformed JSON or an
output that violates the selected function schema. The function itself must be
selected by the language model rather than by hard-coded heuristics or pattern
matching.

## What Currently Works

- The project is managed with `uv` and targets Python 3.10 or newer.
- The provided local `llm_sdk` package is integrated as a workspace dependency.
- Runtime and development dependencies are separated in `pyproject.toml`.
- The project can be launched through the required module entry point with
  `uv run python -m src`.
- Makefile targets are available for dependency synchronization, execution,
  debugging, cleanup, and static analysis.
- The Qwen model can be instantiated through the public SDK.
- Text can be encoded into token IDs and decoded back into text.
- Individual tokens and their boundaries can be inspected.
- The model vocabulary can be loaded and explored as JSON.
- Important JSON punctuation tokens and tokenizer behavior have been examined.
- Input fixtures containing function definitions and test prompts are present.

The exploratory work is currently located in `explore.py`. It is intentionally
separate from the deliverable application under `src/`.

## What Does Not Work Yet

The command-line application is currently only an empty shell. Running it
without an error does **not** mean that function calling is operational.

The following parts remain to be designed or implemented:

- a naive token-by-token generation loop for comparison and experimentation;
- logit retrieval and next-token selection in the final decoding loop;
- constrained decoding and invalid-token masking;
- LLM-based selection of a function from the supplied definitions;
- schema-aware generation of correctly typed parameter values;
- command-line argument parsing;
- loading and validating arbitrary input files;
- Pydantic models for application data;
- graceful handling of missing files, invalid JSON, and invalid schemas;
- generation of the final JSON output file;
- automated tests for valid and invalid inputs;
- final Flake8 and strict mypy compliance for the complete implementation;
- validation of the complete workload against the required time limit.

## Current Architecture

```text
.
|-- data/input/       Sample function definitions and prompts
|-- llm_sdk/          SDK supplied with the project
|-- src/              Final application package (not implemented yet)
|-- explore.py        Temporary SDK and tokenizer experiments
|-- Makefile          Common development commands
`-- pyproject.toml    Project metadata and dependencies
```

The intended final flow is:

```text
Natural-language prompt
        |
        v
Qwen3-0.6B logits
        |
        v
Schema-aware token mask
        |
        v
Constrained token selection
        |
        v
Validated function-call JSON
```

## Technical Constraints

- Python 3.10 or newer;
- `uv` for environment and dependency management;
- `Qwen/Qwen3-0.6B` accessed only through the public `llm_sdk` interface;
- Pydantic for data classes and validation;
- type hints, PEP 257 docstrings, Flake8, and mypy;
- no function-selection heuristics;
- no use of private SDK methods or attributes;
- no hard-coded behavior based on the provided examples;
- graceful error handling instead of uncaught crashes.

## Planned Usage

The final interface required by the project is:

```bash
uv sync
uv run python -m src \
  --functions_definition <functions-file> \
  --input <input-file-or-directory> \
  --output <output-file-or-directory>
```

The arguments will be optional and will use the project input and output
directories by default. This interface is documented here as the target API;
the argument-processing pipeline is not implemented at the current stage.

## Development Roadmap

1. Finish exploring logits and vocabulary behavior.
2. Build a naive argmax generation loop and observe its failure modes.
3. Define the constrained-decoding state machine.
4. Implement schema-aware token masking.
5. Build the complete command-line and file-processing pipeline.
6. Add validation, error handling, tests, documentation, and quality checks.

## What This Project Demonstrates

Even in its current exploratory stage, this project demonstrates work with
tokenization, vocabulary inspection, model logits, Python packaging, local SDK
integration, reproducible environments, static analysis, and the design of a
decoding algorithm governed by a formal output schema.

The final result is intended to show that reliable structured output does not
have to depend on prompting alone: generation can be controlled token by token
so that invalid outputs are impossible by construction.
