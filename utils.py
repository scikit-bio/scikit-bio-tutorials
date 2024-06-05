# Utilities for tutorial files

def load_protein_t5_embedding(sequence, model_name, tokenizer_name):
    import torch
    from transformers import T5Tokenizer, T5EncoderModel
    # (In case we want to use ONNX model)
    # from optimum.onnxruntime import ORTModel
    tokenizer = T5Tokenizer.from_pretrained(tokenizer_name)
    model = T5EncoderModel.from_pretrained(model_name)

    # tokenize sequences and pad up to the longest sequence in the batch
    ids = tokenizer.batch_encode_plus(sequence, add_special_tokens=True, padding="longest")
    input_ids = torch.tensor(ids['input_ids'])
    attention_mask = torch.tensor(ids['attention_mask'])

    # generate embeddings
    with torch.no_grad():
        embedding_repr = model(input_ids=input_ids,attention_mask=attention_mask)
        
    return embedding_repr.last_hidden_state

# Function to read a fasta file and return a list of sequences
def read_fasta_file(filename, n_sequences):
  fileObj = open(filename, 'r')
  sequences = []
  seqFragments = []
  for line in fileObj:
    if line.startswith('>'):
      if(len(sequences) == n_sequences-1):
        break
      if seqFragments:
        sequence = ''.join(seqFragments)
        sequences.append(sequence)
      seqFragments = []
    else:
      seq = line.rstrip()
      seqFragments.append(seq)
  if seqFragments:
    sequence = ''.join(seqFragments)
    sequences.append(sequence)
  fileObj.close()
  return sequences