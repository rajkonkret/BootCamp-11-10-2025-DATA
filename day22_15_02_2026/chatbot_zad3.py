from transformers import pipeline

# pip install tf-keras
# pip install torch torchvision torchaudio
# pip install accelerate

# chatbot = pipeline(
#     "text-generation",
#     model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     # device_map="auto"
#     device="mps" # gpu, cpu
# )
#
# print("start")
# response = chatbot("Cześć, jak mogę Ci pomóc?", max_new_tokens=80)
# print(response)
# # start
# # Passing `generation_config` together with generation-related arguments=({'max_new_tokens'}) is deprecated and will be removed in future versions. Please pass either a `generation_config` object OR all generation parameters explicitly, but not both.
# # Both `max_new_tokens` (=50) and `max_length`(=2048) seem to have been set. `max_new_tokens` will take precedence. Please refer to the documentation for more information. (https://huggingface.co/docs/transformers/main/en/main_classes/text_generation)
# # [{'generated_text': 'Cześć, jak mogę Ci pomóc?\nCzy można zainteresować się naszą firmą?\n\n2. Wprowadzenie: Na początku naszej wizyty mamy dwie pierwsze pytania, które będą bard'}]
# print(response[0]["generated_text"])

chatbot = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    device_map="auto"
    # device="mps"  # gpu, cpu
)

prompt = "<|User|>Cześć, jak mogę Ci pomóc?<|assistant|>"
response = chatbot(prompt,
                   max_new_tokens=160,
                   temperature=0.7,
                   top_p=0.9)

print(response[0]["generated_text"])
