res_output = [] 
des_output = [] 
ls = []
resu=[]




for i in range(0,len_dir):
    mypath=r'C:\Users\Administrator\Desktop\Resumes'
    
    onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

    
    
    
    resume = open(onlyfiles[i],'rb')
    
    pdfReader = PyPDF2.PdfFileReader(resume)

    pageObject = pdfReader.getPage(0)
    
    resume=pageObject.extractText()
    
    resume=clean_text(resume)
    
    
    
    
    
    stop_words = set(stopwords.words('english'))
    
    word_tokens = word_tokenize(resume) 
    
    for w in word_tokens: 
        
        if w not in stop_words:  
            
            res_output.append(w)
            
    resume= ' '.join([str(elem) for elem in res_output])
    
    res_output.clear()

    
    
    
    k='C:/Users/Administrator/Desktop/Resumes/job.pdf'
    
    job_description=open('C:/Users/Administrator/Desktop/Resumes/job.pdf','rb')
    
    paths,file_names = os.path.split(k)
    
    
    pdfReader = PyPDF2.PdfFileReader(job_description)

    
    
    pageObject = pdfReader.getPage(0)
    
    job_description=pageObject.extractText()
    
    job_description=clean_text(job_description)
    
    
    
