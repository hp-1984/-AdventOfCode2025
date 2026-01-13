a
import re

devices = dict()

def serch_exit(start):
      verem = []
        verem.append(start)
          counter = 0

            while verem:
                    poz = verem.pop()
                        if poz == "out":
                                  counter +=1
                                      else:
                                                for next_poz in devices[poz]:
                                                            verem.append(next_poz)
                                                              return counter



                                                          with open('input.txt', 'r') as f:
                                                                for line in f:
                                                                        pattern = r'\b[a-zA-Z]{3}\b'
                                                                            matches = re.findall(pattern, line)
                                                                                devices[matches[0]] = matches[1:]

                                                                                print(serch_exit("you"))

