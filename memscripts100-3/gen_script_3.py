infos=[('agnews-mxbai-1024-euclidean', 769382, 1024, 100), ('arxiv-nomic-768-normalized', 1000000, 768, 100), ('ccnews-nomic-768-normalized', 495328, 768, 100), ('celeba-resnet-2048-cosine', 201599, 2048, 100), ('coco-nomic-768-normalized', 282360, 768, 100), ('codesearchnet-jina-768-cosine', 1000000, 768, 100), ('gooaq-distilroberta-768-normalized', 1000000, 768, 100), ('laion-clip-512-normalized', 1000000, 512, 100), ('landmark-nomic-768-normalized', 760757, 768, 100), ('llama-128-ip', 256921, 128, 100), ('yahoo-minilm-384-normalized', 677305, 384, 100), ('yandex-200-cosine', 1000000, 200, 100)]



import sys
final_run=''
content=open("template.sh", "r").read()
for info in infos:
    ds=info[0]
    n=str(info[1])
    d=str(info[2])
    qn=str(info[3])
    log_file_name = ds+".sh"
    final_run=final_run+'bash '+log_file_name+' & '
    sys.stdout = open(log_file_name, "w")
    new_content=content+''
    new_content=new_content.replace('[n]',n)
    new_content=new_content.replace('[d]',d)
    new_content=new_content.replace('[qn]',qn)
    new_content=new_content.replace('[folderPath]',ds)
    print(new_content)
final_run=final_run+'echo 1'
sys.stdout = open('run_all.sh', "w")          
print(final_run)           
    
    
