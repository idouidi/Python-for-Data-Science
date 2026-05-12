# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: idouidi <idouidi@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/09 14:34:32 by idouidi           #+#    #+#              #
#    Updated: 2026/05/09 15:21:59 by idouidi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def NULL_not_found(object: any) -> int:

    if object is None:
        print(f"Nothing: None {type(object)}")

    elif type(object) is float:
        print(f"Cheese: nan {type(object)}")

    elif type(object) is int:
        print(f"Zero: {object} {type(object)}")

    elif type(object) is str and object == "":
        print(f"Empty: {type(object)}")

    elif type(object) is bool:
        print(f"Fake: {object} {type(object)}")

    else:
        print("Type not Found")
        return 1

    return 0
