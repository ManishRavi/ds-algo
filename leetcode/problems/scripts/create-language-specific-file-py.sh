set -e
PARENT_PATH="leetcode/problems"
LANGUAGE_SPECIFIC_DIRECTORY_NAME="language-specific"
PROBLEM_SPECIFIC_DIRECTORY_NAME="problem-specific"
SESSIONS_DIRECTORY_NAME="sessions"
CURRENT_SESSION_DIRECTORY_NAME="2023-04-22_2023-??-??"
LANGUAGE="python"
COUNT=0


cd ../$SESSIONS_DIRECTORY_NAME/$CURRENT_SESSION_DIRECTORY_NAME

for file in `git status --porcelain | cut -c 4-`
do
    if  [[ $file == $PARENT_PATH/$SESSIONS_DIRECTORY_NAME* ]] ;
    then
        # echo $file
        # * Setting IFS (input field separator) value as "/"
        IFS='/'
        # * Reading the split string into array
        read -ra fileSplit <<< "$file"
        fileName=${fileSplit[${#fileSplit[@]} - 1]}
        # problemName=${fileName:0:${#fileName} - 3}
        # echo $fileName $problemName
        # pwd
        languageSpecificPath=../../$LANGUAGE_SPECIFIC_DIRECTORY_NAME/$LANGUAGE
        echo "COPY | $fileName | ${languageSpecificPath:6:${#languageSpecificPath}}"
        
        # mkdir -p "$languageSpecificPath"
        cp "$fileName" "$languageSpecificPath"

        COUNT=$((COUNT+1))
    fi
done

echo "$COUNT files copied successfully!"
