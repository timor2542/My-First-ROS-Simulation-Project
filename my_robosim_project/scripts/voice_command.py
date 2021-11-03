#! /usr/bin/python3
from pickle import TRUE
import speech_recognition as sr
from subprocess import call
import actionlib
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

s = '-s 140'
g = '-g 0.8'
f = '-vf3'
a = '-a 150'

record = sr.Recognizer()

atKitchen = False
atRoom = False
task_completed = False


def movebasegoal_voicecommand():

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    txt_dat_read = ""
    place = ""

    if not task_completed:

        if not atKitchen:
            rospy.loginfo("Where should I go? Kitchen?")
            call(['espeak', s, g, f, a, "Where should I go? Kitchen?"])
        else:
            rospy.loginfo("Which room should I go?")
            call(['espeak', s, g, f, a, "Which room should I go?"])

        try:
            with sr.Microphone() as source:
                record.adjust_for_ambient_noise(source, duration=0.5)
                audio_listen = record.listen(source, timeout=10.0)

            txt_dat_read = record.recognize_google(audio_listen)
            txt_dat_read = txt_dat_read.lower()

            rospy.loginfo(txt_dat_read + " Confirmed!")
            call(['espeak', s, g, f, a, txt_dat_read + " Confirmed!"])

        except sr.WaitTimeoutError:
            rospy.loginfo("Oops! I will take a rest.")
            call(['espeak', s, g, f, a, "Oops! I will take a rest."])
            txt_dat_read = 'restroom'

        except sr.UnknownValueError:
            rospy.loginfo("Could not understand your command.")
            call(['espeak', s, g, f, a, "Could not understand your command."])

        except sr.RequestError as e:
            rospy.loginfo("Could not request results; {0}".format(e))
    else:
        rospy.loginfo("Task completed! I will go back to my station.")
        call(['espeak', s, g, f, a, "Task completed! I will go back to my station"])
        txt_dat_read = "restroom"

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    if task_completed:
        goal.target_pose.pose.position.x = -0.01456
        goal.target_pose.pose.position.y = 0.01456
        goal.target_pose.pose.orientation.z = 0.000000
        goal.target_pose.pose.orientation.w = 1.000000
        client.send_goal(goal)
        place = "restroom"
    else:
        if '101' in txt_dat_read:
            if not atKitchen:
                rospy.logerr("I don't get food yet.")
                call(['espeak', s, g, f, a, "I don't get food yet."])
                place = ""
            else:
                rospy.loginfo("I am going to room 101.")
                call(['espeak', s, g, f, a, "I am going to Room 101"])
                goal.target_pose.pose.position.x = 2.00000
                goal.target_pose.pose.position.y = 9.32772
                goal.target_pose.pose.orientation.z = 0.000000
                goal.target_pose.pose.orientation.w = 1.000000
                client.send_goal(goal)
                place = "101"

        elif '102' in txt_dat_read:
            if not atKitchen:
                rospy.logerr("I don't get food yet.")
                call(['espeak', s, g, f, a, "I don't get food yet."])
                place = ""
            else:
                rospy.loginfo("I am going to room 102.")
                call(['espeak', s, g, f, a, "I am going to Room 102"])
                goal.target_pose.pose.position.x = -2.91515
                goal.target_pose.pose.position.y = 9.51737
                goal.target_pose.pose.orientation.z = 0.000000
                goal.target_pose.pose.orientation.w = 1.000000
                client.send_goal(goal)
                place = "102"

        elif '103' in txt_dat_read:
            if not atKitchen:
                rospy.logerr("I don't get food yet.")
                call(['espeak', s, g, f, a, "I don't get food yet."])
                place = ""
            else:
                rospy.loginfo("I am going to room 103.")
                call(['espeak', s, g, f, a, "I am going to Room 103"])
                goal.target_pose.pose.position.x = -7.88505
                goal.target_pose.pose.position.y = 9.51737
                goal.target_pose.pose.orientation.z = 0.000000
                goal.target_pose.pose.orientation.w = 1.000000
                client.send_goal(goal)
                place = "103"

        elif '104' in txt_dat_read:
            if not atKitchen:
                rospy.logerr("I don't get food yet.")
                call(['espeak', s, g, f, a, "I don't get food yet."])
                place = ""
            else:
                rospy.loginfo("I am going to room 104.")
                call(['espeak', s, g, f, a, "I am going to Room 104"])
                goal.target_pose.pose.position.x = -13.0103
                goal.target_pose.pose.position.y = 9.37945
                goal.target_pose.pose.orientation.z = 0.000000
                goal.target_pose.pose.orientation.w = 1.000000
                client.send_goal(goal)
                place = "104"

        elif 'kitchen' in txt_dat_read:

            if atKitchen:
                rospy.loginfo("I already have food yet.")
                call(['espeak', s, g, f, a, "I already have food yet."])
                place = ""
            else:
                rospy.loginfo("I am going to kitchen.")
                call(['espeak', s, g, f, a, "I am going to Kitchen"])
                goal.target_pose.pose.position.x = -16.7755
                goal.target_pose.pose.position.y = 5.53971
                goal.target_pose.pose.orientation.z = 0.000000
                goal.target_pose.pose.orientation.w = 1.000000
                client.send_goal(goal)
                place = "kitchen"

        elif 'office' in txt_dat_read:
            if not atKitchen:
                rospy.logerr("I don't get food yet.")
                call(['espeak', s, g, f, a, "I don't get food yet."])
                place = ""
            else:
                rospy.loginfo("I am going to office.")
                call(['espeak', s, g, f, a, "I am going to Office"])
                goal.target_pose.pose.position.x = -9.02243
                goal.target_pose.pose.position.y = 1.146298
                goal.target_pose.pose.orientation.z = 0.000000
                goal.target_pose.pose.orientation.w = 1.000000
                client.send_goal(goal)
                place = "office"

        elif 'exit' in txt_dat_read:
            rospy.signal_shutdown("Exit voice command.")
            place = ""
        else:
            rospy.logerr("No goal!")
            call(['espeak', s, g, f, a, "No goal."])
            place = ""

    wait = client.wait_for_result()

    if not wait:
        return [False, place]
    else:
        return [client.get_result(), place]


if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')

        while not rospy.is_shutdown():
            [result, pl] = movebasegoal_voicecommand()

            if result:
                rospy.loginfo("Reached to " + pl)
                call(['espeak', s, g, f, a, "Reached to " + pl])

                if(pl.lower() == 'kitchen'):
                    atKitchen = True
                elif(pl.lower() == '101' or pl.lower() == '102' or pl.lower() == '103' or pl.lower() == '104' or pl.lower() == 'office'):
                    atRoom = True
                elif(pl.lower() == 'restroom'):
                    atKitchen = False
                    atRoom = False
                    task_completed = False

                if atKitchen and atRoom:
                    task_completed = True

    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
