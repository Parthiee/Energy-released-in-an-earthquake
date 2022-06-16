with open("SAMPLEDATA.txt") as file:
  content=file.readlines()
  for i in content:
    a=i.split(":")
    rscale=float(a[1])
    print(a[0],":",rscale)
    joules="10**(1.5*rscale+4.8)"
    tonnage="10**(1.5*rscale-3)"
    energy=eval(joules)
    explodedtnt=eval(tonnage)
    print("Equivalent amount of energy (Joules):",energy)
    print("Equivalent amount of energy (Exploded TNT):",explodedtnt)
    print()
    import contextlib 
    file_path = 'DATA.txt'
    with open(file_path, "a") as o:
        with contextlib.redirect_stdout(o):
            print(a[0],":",rscale)
            print("Equivalent amount of energy (Joules):",energy)
            print("Equivalent amount of energy (Exploded TNT):",explodedtnt)
            print()


