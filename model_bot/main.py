#!/usr/bin/env python
import sys
import warnings
import traceback
from src.model_bot.crew import ModelBot

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information.

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs'
    }
    try:
        print("\n=== Running the Crew ===\n")
        result = ModelBot().crew().kickoff(inputs=inputs)
        print("\n=== Final Crew Output ===\n")
        print(result.raw)  # Display raw output
    except Exception as e:
        print(f"Error while running the crew: {e}")
        traceback.print_exc()

def train():
    """
    Train the crew for a given number of iterations.
    Usage: python main.py train <n_iterations> <output_filename>
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        n_iterations = int(sys.argv[2])
        filename = sys.argv[3]
        print("\n=== Training the Crew ===\n")
        ModelBot().crew().train(n_iterations=n_iterations, filename=filename, inputs=inputs)
        print(f"\n=== Training Complete: Results saved to {filename} ===\n")
    except IndexError:
        print("Usage: python main.py train <n_iterations> <output_filename>")
    except Exception as e:
        print(f"Error while training the crew: {e}")
        traceback.print_exc()

def replay():
    """
    Replay the crew execution from a specific task.
    Usage: python main.py replay <task_id>
    """
    try:
        task_id = sys.argv[2]
        print("\n=== Replaying the Crew Execution ===\n")
        result = ModelBot().crew().replay(task_id=task_id)
        print("\n=== Replay Output ===\n")
        print(result.raw)
    except IndexError:
        print("Usage: python main.py replay <task_id>")
    except Exception as e:
        print(f"Error while replaying the crew: {e}")
        traceback.print_exc()

def test():
    """
    Test the crew execution for a number of iterations.
    Usage: python main.py test <n_iterations> <openai_model_name>
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        n_iterations = int(sys.argv[2])
        model_name = sys.argv[3]
        print("\n=== Testing the Crew Execution ===\n")
        ModelBot().crew().test(n_iterations=n_iterations, openai_model_name=model_name, inputs=inputs)
        print("\n=== Testing Complete ===\n")
    except IndexError:
        print("Usage: python main.py test <n_iterations> <openai_model_name>")
    except Exception as e:
        print(f"Error while testing the crew: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage: python main.py <command> [options]\n"
            "Commands:\n"
            "  run                       Run the crew\n"
            "  train <n> <file>          Train the crew for n iterations, saving to file\n"
            "  replay <task_id>          Replay the crew from a specific task ID\n"
            "  test <n> <model>          Test the crew with n iterations and OpenAI model\n"
        )
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print("Invalid command. Use 'run', 'train', 'replay', or 'test'.")
        sys.exit(1)
