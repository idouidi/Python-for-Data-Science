# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: idouidi <idouidi@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/09 15:27:02 by idouidi           #+#    #+#              #
#    Updated: 2026/05/09 20:46:52 by idouidi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

try:
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    if len(sys.argv) == 2:
        arg = sys.argv[1]

        if not arg.lstrip("+-").isdigit():
            raise AssertionError("argument is not an integer")

        print("I'm Even." if int(arg) % 2 == 0 else "I'm Odd.")

except AssertionError as error:
    print(f"AssertionError: {error}")