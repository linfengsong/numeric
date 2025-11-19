import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
from peft import PeftModel
#from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv
import os
import json

def run_question(question):
    #systemPrompt = "First, provide the Lean4 code for the proof and then resolve by both lean4 and normal language."
    systemPrompt = "You are mathematricians. Translate input Math question statement to Lean4 question statement. Remove duplicate import and open line"
    messages=[
        {
            "role": "system",
            "content": systemPrompt
        },
        {
            "role": "user",
            "content": question
        }
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        max_tokens=50000,
        enable_thinking=True # Switches between thinking and non-thinking modes. Default is True.
    )
    model_inputs = tokenizer([text], return_tensors="pt").to("cuda:0")

    # conduct text completion
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=32768
    )
    output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

    # parsing thinking content
    try:
        # rindex finding 151668 (</think>)
        index = len(output_ids) - output_ids[::-1].index(151668)
    except ValueError:
        index = 0

    thinking_content = tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
    content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")

    return f"thinking content: \n{thinking_content}\n\ncontent: \n{content}"
                
def create_module():
    #model_name = "Qwen/Qwen3-4B-Instruct-2507"
    #model_name = "/home/linfe/ai_dev/py311-LLaMA-Factory/LLaMA-Factory/models/qwen3_math_statement_small"
    model_name = "/home/linfe/ai_dev/py311-LLaMA-Factory/LLaMA-Factory/models/qwen3_math_statement"
    adapter_model_name = "/home/linfe/ai_dev/py311-LLaMA-Factory/LLaMA-Factory/saves/Qwen3-4B-Instruct-2507/lora/train_2025-11-15-21-00-25"


    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", device_map="cuda:0")

    #model = PeftModel.from_pretrained(base_model, adapter_model_name)

    return model, tokenizer

load_dotenv()

model, tokenizer = create_module()

#response =run_question("Who are you")
#print(f"response: \n{response}")

statment="for any cosimplicial objects $X'$ and $X$ in a category $C$, and any morphism $f : X \\to X'$, show that for any natural number $n$ and any element $i$ in the finite set of size $n + 1$, the following diagram commutes:\n\\[\n\\begin{tikzcd}\nX_n \\arrow[r, \"f_n\"] \\arrow[d, \"\\sigma_i\"] & X'_n \\arrow[d, \"\\sigma_i\"] \\\\\nX_{n+1} \\arrow[r, \"f_{n+1}\"] & X'_{n+1}\n\\end{tikzcd}\n\\]\nwhere $\\sigma_i$ represents the $i$-th face map for $X$ and $X'$."

#import Mathlib
#open Opposite
#open CategoryTheory
#open CategoryTheory.Limits
#open Simplicial
#open Simplicial
#open Simplicial
#theorem \u03c3_naturality_extracted [Category.{v : u} C] {X' X : CosimplicialObject C} (f : X \u27f6 X') {n : \u2115} (i : Fin (n + 1)),
#  X.\u03c3 i \u226b f.app (SimplexCategory.mk n) = f.app (SimplexCategory.mk (n + 1)) \u226b X'.\u03c3 i := sorry

#response =run_question(statment)
#print(f"response: \n{response}")

count = 10
jsonl_file_path = "/home/linfe/math/frenzymath_4_16/data/Herald_statements.jsonl"
index = 0
with open(jsonl_file_path, 'r', encoding='utf-8') as rf:
    for line in rf:
        index += 1
        if index > 10:
            break
        print(f"index: \n{index}\n")
        stripped_line = line.strip()
        if stripped_line:
            record = json.loads(stripped_line)
            informal_statement = record["informal_statement"]
            response =run_question(informal_statement)
            print(f"response: \n{response}\n")

print("done")