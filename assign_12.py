import pandas as pd
schoolmet=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_12\schoolmets_names.xlsx")
#print(schoolmet)
collegemet=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_12\collegemets_names.xls.xlsx")
#print(collegemet)

inn_merge_sch_coll=schoolmet.merge(collegemet,how="inner",on="FriendName")
print(inn_merge_sch_coll)
#print(inn_merge_sch_coll.shape)
left_merge_sch_col=schoolmet.merge(collegemet,how="left",on="FriendName")
print(left_merge_sch_col)
right_merge_sch_col=schoolmet.merge(collegemet,how="right",on="FriendName")
print(right_merge_sch_col)
oute_merge_sch_col=schoolmet.merge(collegemet,how="outer",on="FriendName")
print(oute_merge_sch_col)

import pandas as pd
soup=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_12\soups_items.xlsx")
#print(soup)
fry=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_12\fry_items.xlsx")
#print(fry)

#inn_merge_soup_fry=soup.merge(fry,how="inner",on="Taste")
#print(inn_merge_soup_fry)
#print(inn_merge_sch_coll.shape)
#left_merge_soup_fry=soup.merge(fry,how="left",on="Taste")
#print(left_merge_soup_fry)
#right_merge_soup_fry=soup.merge(fry,how="right",on="Taste")
#print(right_merge_soup_fry)
oute_merge_soup_fry=soup.merge(fry,how="outer",on="Taste")
print(oute_merge_soup_fry)

import pandas as pd
chicken=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_12\chicken_items.xlsx")
#print(chicken)
mutton=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_12\mutton_items.xlsx")
#print(mutton)
#inn_mer_chi_mut=chicken.merge(mutton,how="inner",on="Taste")
#print(inn_mer_chi_mut)
#left_mer_chi_mut=chicken.merge(mutton,how="left",on="Taste")
#print(left_mer_chi_mut)
#right_mer_chi_mut=chicken.merge(mutton,how="right",on="Taste")
#print(right_mer_chi_mut)
outer_mer_chi_mut=chicken.merge(mutton,how="outer",on="Taste")
print(outer_mer_chi_mut)


import pandas as pd
winter=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_12\winterseason_names.xlsx")
#print(winter)
summer=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_12\summerseason_names.xlsx")
#print(summer)
rainy=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_12\rainyseason_names.xlsx")
#print(rainy)

inn_mer_win_sum_rai=winter.merge(summer,how="inner",on="Season").merge(rainy,how="inner",on="Season")
print(inn_mer_win_sum_rai)
left_mer_win_sum_rai=winter.merge(summer,how="left",on="Season").merge(rainy,how="left",on="Season")
print(left_mer_win_sum_rai)
right_mer_win_sum_rai=winter.merge(summer,how="right",on="Season").merge(rainy,how="right",on="Season")
#print(right_mer_win_sum_rai)
outer_mer_win_sum_rai=winter.merge(summer,how="outer",on="Season").merge(rainy,how="outer",on="Season")
print(outer_mer_win_sum_rai)

import pandas as pd
red=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_12\redflowers_names.xlsx")
#print(red)
white=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_12\whiteflowers_names.xlsx")
#print(white)
pink=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_12\pinkflower_names.xlsx")
#print(pink)
yellow=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_12\yellowflower_names.xlsx")
#print(yellow)


re_wh=red.merge(white,how="left",on="colour")

pi_ye=pink.merge(yellow,how="left",on="colour")


left=re_wh.merge(pi_ye,how="left",on="colour")
print(left)

#re_wh=red.merge(white,how="inner",on="colour")

#pi_ye=pink.merge(yellow,how="inner",on="colour")
#inner=re_wh.merge(pi_ye,how="inner",on="colour")
#print(inner)


re_wh=red.merge(white,how="right",on="colour")

pi_ye=pink.merge(yellow,how="right",on="colour")
right=re_wh.merge(pi_ye,how="right",on="colour")
print(right)

re_wh=red.merge(white,how="outer",on="colour")

pi_ye=pink.merge(yellow,how="outer",on="colour")
outer=re_wh.merge(pi_ye,how="outer",on="colour")
print(outer)






import pandas as pd
red=pd.read_excel(r"C:\Users\HP\Documents\Book1.xlsx")
#print(red)
white=pd.read_excel(r"C:\Users\HP\Documents\Trainee\Salam_assignments\salam_assignments\assign_12\whiteflowers_names.xlsx")
#print(white)
re_wh=red.join(white,how="right")
print(re_wh)







