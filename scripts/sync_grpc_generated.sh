#!/bin/bash
# Sync generated grpc python code in the bscp project to the current SDK project, steps:
# - Go to bcs-services project and generate latest code
# - Adjust `INCLUDE_PATTERNS` is needed

if [ -z "$1" ]; then
  echo "Usage: $0 <bscp_proj_root>"
  echo "Error: argument <bscp_proj_root> is required."
  exit 1
fi

BSCP_PROJ_ROOT="$1"

SOURCE_DIR=$BSCP_PROJ_ROOT
DEST_DIR=../bk_bscp

# Patterns for subdirectories to include
INCLUDE_PATTERNS=(
    "*/pkg/protocol/core"
    "*/pkg/protocol/feed_server"
)

# Sync a subdirectory pattern, include only python source files
sync_subdir_pattern() {
    local pattern=$1
    # Create an array to hold the rsync include patterns
    local include_from=( "--include=*/" "--include=*.py" "--include=*.pyi" "--exclude=*" )

    # Find subdirectories that match the pattern and sync them
    find "$SOURCE_DIR" -type d -path "$pattern" -print0 | while IFS= read -r -d '' subdir; do
        # Compute the relative path from SOURCE_DIR
        local rel_path="${subdir#$SOURCE_DIR/}"
        
        # Run rsync for each subdirectory
        mkdir -p "$DEST_DIR/$rel_path"
        rsync -avm --delete --delete-excluded "${include_from[@]}" "$subdir/" "$DEST_DIR/$rel_path"
    done
}

# Update the directory structure and import path
update_directory() {
    cd $DEST_DIR
    rm -rf grpc_lib && mkdir -p grpc_lib
    mv pkg/protocol/* grpc_lib 
    rm -r pkg/

    # Update the import path in the generated files
    find . -type f -exec sed -i 's/ pkg\.protocol/ bk_bscp.grpc_lib/g' {} +
}

# Main execution
for pattern in "${INCLUDE_PATTERNS[@]}"; do
    sync_subdir_pattern "$pattern"
done

update_directory