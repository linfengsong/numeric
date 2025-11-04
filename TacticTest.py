import asyncio
import logging
from typing import Any
from vllm import LLM, SamplingParams
from vllm.lora.request import LoRARequest

def chat_template_to_prompt(messages, template):
        result = ""
        if template=='qwen':
            result += "<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n"
        # elif template=='deepseek':
        #     result += "<｜begin▁of▁sentence｜>"
        total_step = len(messages)
        for i, message in enumerate(messages):
            if template == 'internlm':
                result += ('<|im_start|>' + message['role'] + 
                        '\n' + message['content'])
                if i+1 != total_step:
                    result += '<|im_end|>\n'
                elif message['role'] == 'user':
                    result += '<|im_end|>\n<|im_start|>assistant\n'
            elif template=='deepseek':
                if message['role']=='user':
                    result += 'User: ' + message['content'] + '\n\n'
                elif message['role']=='assistant':
                    result += 'Assistant:' + message['content'] + '<｜end▁of▁sentence｜>'
                elif message['role'] == 'system':
                    result += message['content'] + '\n\n'
                if i+1 == total_step and message['role'] == 'user':
                    result += 'Assistant:'
            elif template=='qwen': 
                if message['role'] == 'user':
                    result += f"<|im_start|>user\n{message['content']}<|im_end|>\n"
                elif message['role'] == 'assistant':
                    result += f"<|im_start|>assistant\n{message['content']}<|im_end|>\n"
                if i+1 == total_step and message['role'] == 'user':
                    result += "<|im_start|>assistant\n"
            elif template=='deepseek3':
                if message['role'] == 'user':
                    result += f"<｜User｜>{message['content']}"
                elif message['role'] == 'assistant':
                    result += f"<｜Assistant｜>{message['content']}<｜end▁of▁sentence｜>"
                if i+1 == total_step and message['role'] == 'user':
                    result += "<｜Assistant｜>"
            else:
                raise NotImplementedError
        return result

def build_theorems_str(related_theorems):
        return "\n\n".join([
            f"ID:{index}\nFormal name: {i['Formal name']}\nInformal name: {i['Informal name']}\nFormal statement: {i['Formal statement']}"
            for index, i in enumerate(related_theorems[:6])
        ])

def build_local_prompt_str(state: str, related_theorems: list[dict['str', 'str']]) -> str:
        theorems_str = build_theorems_str(related_theorems)
        prompt = f"Please generate a tactic in lean4 to solve the state.\nHere're some theorems that may be helpful:\n{theorems_str}\nSTATE:\n{state}\nTACTIC:\n"
        prompt = chat_template_to_prompt(
            [{'role': 'user', 'content': prompt}], 'deepseek'
        )
        return prompt


llm = LLM(model="Qwen/Qwen2.5-Math-7B")

sampling_params = {
    "temperature": 1.5,
    "max_tokens": 256,
    "top_p": 0.9,
    "logprobs": 1
}

related_theorems = None
state = "{α : Sort u} → (p : α → Prop) → (∃ x, p x) → { x // p x }:=\n  choice <| let ⟨x, px⟩ := h; ⟨⟨x, px⟩⟩"

prompt = build_local_prompt_str(state, related_theorems)
sampling_params = SamplingParams(n=1, **sampling_params)
outputs = llm.generate([prompt], sampling_params, use_tqdm=False)