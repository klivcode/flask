from app import create_app
app= create_app()



# run.py=> app launcher
if __name__=="__main__":
    app.run(debug=True)
    
    