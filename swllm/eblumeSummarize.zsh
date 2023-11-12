# https://gist.github.com/eblume/0243472ad6619bccf5aa3537d48ec0d7
my_summarize () {
	if [ $# -eq 0 ]
	then
		echo "Usage: my_summarize FILE_OR_URL"
		return 1
	fi
	local content
	if [[ $1 =~ ^https?:// ]]
	then
		content=$(curl -s "$1" | lynx -dump -stdin) 
	else
		file_type=$(file -b --mime-type "$1") 
		case $file_type in
			(application/pdf) content=$(pdftotext "$1" -)  ;;
			(text/* | */xml) content=$(<"$1")  ;;
			(*) echo "Unsupported file type: $file_type"
				return 2 ;;
		esac
	fi
	content=$(echo "$content" | iconv -f "$(iconv --list | grep -m 1 -o 'UTF-8//')" -t 'UTF-8//IGNORE') 
	llm -m 4 -s "Summarize this content. Break down any viewpoints with direct quotes and author attributions. For technical content, give an overall summary and provide relevant links (if any) to further reading. Output markdown. Go long." <<< "$content"
}
my_summarize $1
