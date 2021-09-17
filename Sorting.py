  text = [resume, job_description]
    
    cv = CountVectorizer(lowercase=True, stop_words = 'english')
    
    count_matrix = cv.fit_transform(text)
    
    matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
    
    matchPercentage = round(matchPercentage)

    if matchPercentage>1:
        path,file_name = os.path.split(onlyfiles[i])
        if file_name != file_names:
        ls.append(( matchPercentage,file_name))           
ls = sorted(ls, reverse = True)


print("\033[1m ORDER OF PERSON MATCHES FOR THE JOB\033[0m") 
for m in ls:
    print(m[1]," this person matches about ",m[0],"% for the job")
    
    
