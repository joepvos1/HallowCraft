FileName = input("EnterFileName: ")
Collors = ["dark_gray", "white", "green", "blue", "dark_purple", "gold"]
k = '"'
bo = '{'
bs = '}'
RgbValue = r"{rgb:1545156}"
x = r"\'"

with open(FileName, "w", encoding="utf-8") as File:
    for index in Collors:
        if index != "dark_gray":
            Collor = "aqua"
        else:
            Collor = "dark_gray"
        File.write(f"give @a leather_chestplate[dyed_color={RgbValue},custom_name='[{k}{k},{bo}{k}text{k}:{k}Storm{x}s Chestplate{k},{k}italic{k}:false,{k}color{k}:{k}gold{k}{bs}]',lore=['[{k}{k},{bo}{k}text{k}:{k} [{k},{k}italic{k}:false,{k}color{k}:{k}{index}{k}{bs},{bo}{k}text{k}:{k}✎{k},{k}italic{k}:false,{k}color{k}:{k}{Collor}{k},{k}bold{k}:true{bs},{bo}{k}text{k}:{k}] [{k},{k}italic{k}:false,{k}color{k}:{k}{index}{k}{bs},{bo}{k}text{k}:{k}✎{k},{k}italic{k}:false,{k}color{k}:{k}{Collor}{k},{k}bold{k}:true{bs},{bo}{k}text{k}:{k}]{k},{k}italic{k}:false,{k}color{k}:{k}{index}{k}{bs}]']]\n")

