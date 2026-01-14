import re

summa = 0
interval = []
ids = []

def generate_interval(data):
      interval_part = []
        for i in range(int(data[0]), int(data[1])+1):
                interval_part.append(i)
                  return interval_part


              with open('test.txt', 'r') as f:
                    for line in f:
                            if "-" in line:
                                      data = re.findall(r"\d+", line)
                                            interval.extend(generate_interval(data))
                                                elif line == '\n':
                                                          pass
                                                          else:
                                                                    id = re.findall(r"\d+", line)
                                                                          ids.append(int(id[0]))

                                                                            print(interval)
                                                                              print(ids)
                                                                                metszet = list(filter(lambda x: x in interval, ids))
                                                                                  print(len(metszet))


                                                                                  print("summ", summa)
