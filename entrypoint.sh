#!/bin/bash

set -e

function print_help {
    echo "Available options:"
    echo " start commands (differential_evolution_GA cmd line arguments) - Start Differential Evolution server"
    echo " start -h                                      - Print  help"
    echo " help                                          - Print this help"
    echo " run                                           - Run an arbitrary command inside the container"
}


case ${1} in
    start)
        exec python -m .server "${@:2}"
        ;;
    run)
        exec "${@:2}"
        ;;
    *)
        print_help
        ;;
esac


