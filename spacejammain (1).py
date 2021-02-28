information=[]
def GetFit():
    print("\t\tHello there!! Hope you are having a lovely day!\n \t\t Welcome to GetFit")
    information=info()
    d={1:"Diet Tracker",2:"Work Out",3:"Diet Plan",4:"Fitness Tracker"}
    print(d)
    cond=True
    while(cond==True):
        print("Enter choice number")
        choice=int(input())
        if choice==1:
            diet_tracker(information[4])
            cond=False
        elif choice==2:
            workout()
            cond=False
        elif choice==3:
            diet_plan(information[3])
            cond=False
        elif choice==4:
            fitness_tracker(information)
            cond=False
        else:
            print("Please enter a valid choice number")

    close()


def info():

    ca=True
    chw=True
    cg=True
    print("Enter your name.")
    name = input()
    print("Hey ", name, ",Enter your age.")
    while ca==True:
        age = input()
        if age.isdigit()==False:
            print("Enter numbers only")
        else:
            age=int(age)
            if age<0 or age>100:
                print("You do not need a fitness app... you are a medical marvel")
                print("enter your real age")
            else:
                ca=False
    print("Okay, we need a few more details.")
    print("Enter  height (in cm), weight (in kg), gender(f/m/o)")
    while chw==True:
        H = input()
        W = input()
        if H.isdigit()!=True or W.isdigit()!=True:
            print("enter reasonable values")
        else:
            h=float(H)
            w=float(W)
            chw=False
    while cg==True:   
        g = input()
        G=g.upper()
        if G.startswith('M')==True or G.startswith('F')==True or G.startswith('O')==True:
            cg=False
        else:
            print("enter correct input please")
    return [name,age,h,w,g]
    

def diet_tracker(gender):
    
    dm={'carbohydrates':325,'proteins':56,'fats':60,'vitamins and minerals':2,'fluids':2.7}
    df={'carbohydrates':325,'proteins':46,'fats':55,'vitamins and minerals':2,'fluids':3.5}
    print("Okay so tell me how much")
    c=float(input("carbohydrates did you take in today? (in grams)"))
    p=float(input("proteins did you take in today? (in grams)"))
    f=float(input("fat did you take in today? (in grams)"))
    vm=float(input("vitamins and minerals did you take in today? (in grams)"))
    fl=float(input("fluids did you take in today? (in litre)"))
    
    inputd={'carbohydrates':c,'proteins':p,'fats':f,'vitamins and minerals':vm,'fluids':fl}

    
    
    if gender.startswith('m' or 'M' or 'o' or 'O'):
        count=0
        for i in dm:
            if dm[i]==inputd[i]:
                print("you are taking the right amount of ",i)
                count+=1
            elif dm[i]<inputd[i]:
                print("you are taking ",i," in excess by ",inputd[i]-dm[i]," grams")
            else:
                print("you are taking ",i," in deficiet by ",dm[i]-inputd[i]," grams")

        if count==len(dm):
                print("your diet is perfectly balanced. Good job!!")


    if gender.startswith('f' or 'F'):
        count=0
        for i in df:
            if df[i]==inputd[i]:
                print("you are taking the right amount of ",i)
                count+=1
            elif df[i]<inputd[i]:
                print("you are taking ",i," in excess by ",inputd[i]-df[i])
            else:
                print("you are taking ",i," in deficiet by ",df[i]-inputd[i])

        if count==len(df):
                print("your diet is perfectly balanced. Good job!!")




def workout():
    print("WHAT DO YOU WANT TO TONE TODAY?")
    dw={1:'Leg',2:'Core',3:'Arms',4:'Full Body',5:'Flexibility',6:'Endurance/Cardio',7:'Glutes'}
    print(dw)
    print("enter the choice number")
    

    leg=['clams','crab_walk','glute_bridge','foam_rolling','hamstring_curl','squat,walking_lunge','box_jump','single_leg_romanian_deadlift','barbell_deadlift','goblet_squat','calf_raises','hip_flexor_and_quad_strech','hamstring_strech','hamstring_and_calves_strech']
    
    arms=['lateral_raise','push_ups','overhead_extension','biceps_curl','dumbbell_row','single_arm_push_press','plank_to_push_up','dumbbell_curl_and_press','dumbbell_kickback','triceps_dips','tricep_dips_with_single_leg_extension','back_fly']
    
    core=['hip_lifts','flutter_kicks','scissor_kicks','v_sits','v_ups','leg_lifts','hollow_body_hold','hip_dips','toe_touches','plank','deadbug','vertical_leg_crunch','plank_rolls','reverse_crunch','side_plank','inchworm','bird_dog','bear_crawl']
    
    full_body=['burpees','squats','step_ups','pull_ups','push_ups','dips','jump_lunges']
    
    flexibility=['Standing_Hamstring_Stretch','Lunge_With_Spinal_Twist','Triceps_Stretch','Figure_Four_Stretch','90/90_Stretch','Frog_Stretch','Butterfly_Stretch','Seated_Shoulder_Squeeze','Side_Bend_Stretch','Lunging_Hip_Flexor_Stretch','Lying_Pectoral_Stretch','Knee_to_Chest_Stretch']
    
    endurance=['Jump_Squat','Walk-Out_to_Push-Up','High-Low_Plank','Superman','Side_Plank_to_Thread_the_Needle','Push-Up_to_Knee_Touch','Bicycle_Crunch','Hollow_Hold_to_V-Sit','Plyo_Lunge','Uphill_Running','Running_sprints']
    
    glutes=['Glute_bridges','reverse_lunges','squat','step_up','bulgarian_split_squat','sumo_squat','donkey_kicks']

    dworkout={'leg':leg,'arms':arms,'core':core,'full_body':full_body,'flexibility':flexibility,'endurance':endurance,'glutes':glutes}

   

    def Choice(list1):
        c=[]
        cond='choice'
        while(cond!='exit'):
            n=input()
            if n=='exit':
                cond='exit'
            elif n.isdigit()==True and int(n)<len(list1):
                c.append(int(n))
            else:
                print("invalid choice... enter again")
        return c

    import time
    def timer():
        i=40
        while i:
            print(i)
            i=i-1
            time.sleep(1)
            print("\n"*45)


    print("customise your routine... enter the index of exercises you intend to add. When you are done, enter 'exit'")


    condition=True

    while(condition==True):
        choice=int(input())
        if choice==1:
            for i in range(0,len(leg)):
                print(i,".",leg[i])
            ch=Choice(leg)
            for j in ch:
                print(leg[j],"... here we go...")
                timer()
                print("great job!!")
                time.sleep(5)
                print("\n"*45)
            condition=False

        elif choice==2:
            for i in range(0,len(arms)):
                print(i,".",arms[i])
            ch=Choice(arms)
            for j in ch:
                print(arms[j],"... here we go...")
                timer()
                print("great job... now the next one")
                time.sleep(5)
                print("\n"*45)
            condition=False


        elif choice==3:
            for i in range(0,len(core)):
                print(i,".",core[i])
            ch=Choice(core)
            for j in ch:
                print(core[j],"... here we go...")
                timer()
                print("great job... now the next one")
                time.sleep(5)
                print("\n"*45)
            condition=False


        elif choice==4:
            for i in range(0,len(full_body)):
                print(i,".",full_body[i])
            ch=Choice(full_body)
            for j in ch:
                print(full_body[j],"... here we go...")
                timer()
                print("great job... now the next one")
                time.sleep(5)
                print("\n"*45)
            condition=False



        elif choice==5:
            for i in range(0,len(flexibility)):
                print(i,".",flexibility[i])
            ch=Choice(flexibility)
            for j in ch:
                print(flexibility[j],"... here we go...")
                timer()
                print("great job... now the next one")
                time.sleep(5)
                print("\n"*45)
            condition=False


        elif choice==6:
            for i in range(0,len(endurance)):
                print(i,".",endurance[i])
            ch=Choice(endurance)
            for j in ch:
                print(endurance[j],"... here we go...")
                timer()
                print("great job... now the next one")
                time.sleep(5)
                print("\n"*45)
            condition=False


        elif choice==7:
            for i in range(0,len(glutes)):
                print(i,".",glutes[i])
            ch=Choice(glutes)
            for j in ch:
                print(glutes[j],"... here we go...")
                timer()
                print("great job... now the next one")
                time.sleep(5)
                print("\n"*45)
            condition=False


        else:
            print("invalid choice... enter a correct one")

        
        
        
    




def diet_plan(weight):

    def muscle_gain():
        print("Here is a diet plan for muscle gain")
        veg=['spirulina','kernels','peanut butter','beans','legumes','oats','tofu','tempeh']  
        nonveg=['chicken','steak','fish','salmon']
        c=True
        while c:
            food_type=input("Are you a vegetarian? Press v \n Are you a non vegetarian? Press n")
            if food_type=='n' or food_type=='N':
                print("Your vegetarian options are",veg)
                print("your non vegetarian options are",nonveg)
                c=False
            elif food_type=='v' or food_type=='V':
                print("Your vegetarian options are",veg)
                c=False
            else:
                print("Enter the correct choice")

                
    print("1.Weight Loss \n2.Weight gain \n3.Muscle gain")
    print("Set a target")
    
    cond=True
    while(cond==True):
        choice=int(input())

        if choice==1:
            weight_loss(weight)
            cond=False
        elif choice==2:
            weight_gain(weight)
            cond=False
        elif choice==3:
            muscle_gain()
            cond=False
        else:
            print("enter valid choice")


   




#weight loss
def weight_loss(w):
    target=float(input("Enter the target weight you want to lose:"))
    condition=True
    while condition:
        if target>=w:
            change=input("Do you want to apply for the weight gain program? \n If yes press(y) else press(n):")
            if change=='y' or change=='Y':
                print("We are shifting you to a weight gain program!")
                condition=False
                weight_gain(w)
                close()
            else:
                target=float(input(("Input the weight you would want to lose: ")))
                    
        else:
            condition=False        

    loss=w-target
    if loss>20:
        print("Lets start small")
    print("Here is a diet plan for upto 20kg weight loss")
    veg=['Whole egg',"leafy greens",'cruciferous vegetables','boiled potato','beans','legumes','cottage cheese','avocados','nuts','whole grains','fruits']    
    nonveg=['salmon','lean beef','chicken breast','tuna']
    c=True
    while c:
        food_type=input("Are you a vegetarian? Press v \n Are you a non vegetarian? Press n:")
        if food_type=='n' or food_type=='N':
            print("Your vegetarian options are ",veg)
            print("your non vegetarian options aren",nonveg)
            c=False
        elif food_type=='v' or food_type=='V':
            print("Your vegetarian options are ",veg)
            c=False
        else:
            print("Enter the correct choice:")



#weight gain
def weight_gain(w):
    target=float(input("Enter the target weight you want to gain:"))
    condition=True
    while condition:
        if target<=w:
            change=input("Do you want to apply for the weight loss program? \n If yes press(y) else press(n):")
            if change=='y' or change=='Y':
                print("We are shifting you to a weight loss program!")
                condition=False
                weight_loss(w)
                close()
            else:
                target=float(input(("Input the weight you would want to gain:")))
                    
        else:
            condition=False        

    gain=target-w
    if gain>20:
        print("Lets start small")
    print("Here is a diet plan for upto 20kg weight gain")
    veg=['nuts and nut butter','avocado','quinoa','tahini','olive oil','dried fruit','legumes','sweet potatoes','smoothies','rice','coconut oil']    
    nonveg=['chicken','steak','fish']
    c=True
    while c:
        food_type=input("Are you a vegetarian? Press v \n Are you a non vegetarian? Press n:")
        if food_type=='n' or food_type=='N':
            print("Your vegetarian options are ",veg)
            print("your non vegetarian options are ",nonveg)
            c=False
        elif food_type=='v' or food_type=='V':
            print("Your vegetarian options are ",veg)
            c=False
        else:
            print("Enter the correct choice:")





    


def fitness_tracker(ilist):
        h=ilist[2]
        w=ilist[3]
        bmi=(w*10000)/(h**2)
        print("Your BMI is ",bmi)
        if bmi<=18.5:
            print("You are underweight")
            print("We will redirict you to our weight gain plan")
            weight_gain(w)
        elif bmi>18.5 and bmi<=24.99:
            print("You are in normal range")
            print("Great going!! Maintain this range")
        elif bmi>=25.00 and bmi<30.00:
            print("You are overweight")
            print("We will redirict you to our weight loss plan")
            weight_loss(w)
        else:
            print("you are obese")
            print("we will redirict you to our weight loss plan \nfollow this plan more often to get into the normal range")
            weight_loss(w)
            
            

def close():
    import time
    time.sleep(7)
    print("\n"*45)
    choice=input("Well look at you all fit... Wanna go again? Press r \nIf you want a break see you tomorrow.Byeee.(Press any key now)")
    if choice=='r' or choice=='R':
        GetFit()
    else:
        exit()
                 
GetFit()



            
        
    
    
