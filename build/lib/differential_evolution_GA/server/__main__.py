# coding:utf-8
from de_GA.server.routes import main, create_argument_parse

if __name__ == "__main__":
    CMDLINE_ARGS = create_argument_parse().parse_args()
    main(CMDLINE_ARGS)
