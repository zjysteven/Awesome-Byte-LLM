import json

def generate_markdown(json_file, output_file):
    with open(json_file, 'r') as f:
        papers = json.load(f)
    
    with open(output_file, 'w') as f:
        # Write title and description
        f.write("# Awesome Byte-Based Large Language Models\n")
        f.write("A curated list of papers on byte-based large language models.\n\n")
        
        # Table header
        f.write("| Title | Authors | Year | Link | Summary |\n")
        f.write("|-------|---------|------|------|---------|\n")
        
        # Populate the table
        for paper in papers:
            f.write(f"| [{paper['title']}]({paper['link']}) | {paper['authors']} | {paper['year']} | [Link]({paper['link']}) | {paper['summary']} |\n")

if __name__ == "__main__":
    generate_markdown('papers.json', 'README.md')
