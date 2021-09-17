 
    stop_words = set(stopwords.words('english'))
    
    word_tokens = word_tokenize(job_description) 
    
    for y in word_tokens: 
        
        if y not in stop_words:  
            
            des_output.append(y)
            
    job_description= ' '.join([str(eleme) for eleme in des_output])
    
    des_output.clear()
    
    
    
    resume= word_tokenize(resume) 
    for wrd in resume :
        if wrd in job_description:
            resu.append(wrd)
            
            
    resume= ' '.join([str(eleme) for eleme in resu])
    
    
    resu.clear()        
    
    
