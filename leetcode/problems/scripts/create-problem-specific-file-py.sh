set -e
PARENT_PATH="leetcode/problems"
LANGUAGE_SPECIFIC_DIRECTORY_NAME="language-specific"
PROBLEM_SPECIFIC_DIRECTORY_NAME="problem-specific"
LANGUAGE="python"
COUNT=0


cd ../$LANGUAGE_SPECIFIC_DIRECTORY_NAME/$LANGUAGE

for file in `git status --porcelain | cut -c 4-`
do
    if  [[ $file == $PARENT_PATH/$LANGUAGE_SPECIFIC_DIRECTORY_NAME* ]] ;
    then
        # echo $file
        # * Setting IFS (input field separator) value as "/"
        IFS='/'
        # * Reading the split string into array
        read -ra fileSplit <<< "$file"
        fileName=${fileSplit[${#fileSplit[@]} - 1]}
        problemName=${fileName:0:${#fileName} - 3}
        # echo $fileName $problemName
        # pwd
        problemSpecificPath=../../$PROBLEM_SPECIFIC_DIRECTORY_NAME/$problemName
        if [[ -f "$problemSpecificPath/$fileName" ]]
        then
            echo "PROBLEM SPECIFIC FILE EXISTS | $fileName | ${problemSpecificPath:6:${#problemSpecificPath}}"
        else
            echo "PROBLEM SPECIFIC FILE COPY | $fileName | ${problemSpecificPath:6:${#problemSpecificPath}}"
        
            mkdir -p "$problemSpecificPath"
            cp "$fileName" "$problemSpecificPath"

            COUNT=$((COUNT+1))
        fi
    fi
done

echo "$COUNT files copied successfully!"
