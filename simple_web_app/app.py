from flask import Flask, render_template, request
import markdown
import custom_parsing
import llm_utils

app = Flask(__name__)

dropdown_opts = {
"A" : "summarize",
"B" : "list key topics", 
"C" : "critique" 
}

@app.route("/", methods=["GET", "POST"])
def home():
    selected_option = None
    if request.method == "POST":
        text_input = request.form.get("text_input")
        md_txt = custom_parsing.download_pdf_to_markdown(text_input)
        
        dropdown_option = request.form.get("dropdown")
        selected_option = f"You entered: '{text_input}', and selected: '{dropdown_opts[dropdown_option]}'."

        if dropdown_option == "A": # Summarize
            response = llm_utils.summarize(md_txt)
        elif dropdown_option == "B": # List key features
            response = llm_utils.key_features(md_txt)
        elif dropdown_option == "C": # critique
            response = llm_utils.critique(md_txt)
        selected_option += f"\n\n{response}"
        #selected_option = selected_option.replace("\n", "<br>")
        selected_option = markdown.markdown(selected_option)

    return render_template("index.html", selected_option=selected_option)

if __name__ == "__main__":
    app.run(debug=True)

