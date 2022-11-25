import os 
def main():
  print("<<<< Github Action >>>>")
  token = os.enviorn.get("AK_SECRET_TOKEN")
  if not token:
    raise RuntimeError("Token Not Found !!")
  print(token)
                      

if __name__ == "__main__":
  main()
  
 
