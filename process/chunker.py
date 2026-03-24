import sys

def chunk_text(filename, chunk_size=2000, overlap=500):
    with open(filename, 'r') as f:
        words = f.read().split()
    
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))
        if i + chunk_size >= len(words):
            break
    return chunks

if __name__ == "__main__":
    chunks = chunk_text('full_transcript.txt')
    for i, chunk in enumerate(chunks):
        with open(f'chunk_{i+1}.txt', 'w') as f:
            f.write(chunk)
    print(f"Created {len(chunks)} chunks.")
