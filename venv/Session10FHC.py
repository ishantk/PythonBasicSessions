#file = open("/Users/ishantkumar/Downloads/ai.txt","w")

javaCode = """
class Test{
    public static void main(String[] args){
        System.out.println("This is Awesome");
    }
}
"""

#with open("/Users/ishantkumar/Downloads/ai.txt","w") as file:
with open("/Users/ishantkumar/Downloads/Test.java","a") as file:
    #data = "This is Awesome\n"
    #file.write(data)
    file.write(javaCode)
    print("--File Written--")
    file.close()