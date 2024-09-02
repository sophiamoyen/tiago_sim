#!/usr/bin/env python3
import rospy
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose, Quaternion, Point
from tf.transformations import quaternion_from_euler


sdff="""
<?xml version='1.0' encoding='utf-8'?>
<sdf version="1.7">
    <model name="cabinet_with_drawer">
    <pose>0 0 0 0 0 0</pose>
    <static>true</static>

        <link name="cabinet">
            <pose>0 0 0 0 0 0</pose>
            <visual name="cabinet_visual">
                <geometry>
                    <mesh>
                     <uri>model://cabinet_drawer/meshes/cabinet.dae</uri>
                     <scale>1 1 1</scale>
                    </mesh>
                </geometry>
            </visual>
            <collision name="cabinet_collision">
                <geometry>
                    <mesh>
                     <uri>model://cabinet_drawer/meshes/cabinet.dae</uri>
                     <scale>1 1 1</scale>
                    </mesh>
                </geometry>
            </collision>
        </link>

        <link name="drawer1">
            <pose>0.013 -0.23 0.9 0 0 0</pose>
            <visual name="drawer_visual">
                <geometry>
                    <mesh>
                     <uri>model://cabinet_drawer/meshes/drawer.dae</uri>
                     <scale>1 1 1</scale>
                    </mesh>
                </geometry>
            </visual>
            <collision name="drawer_collision">
                <geometry>
                    <mesh>
                     <uri>model://cabinet_drawer/meshes/drawer.dae</uri>
                     <scale>1 1 1</scale>
                    </mesh>
                </geometry>
            </collision>
        </link>



        <joint name="drawer_joint1" type="prismatic">
        <child>drawer</child>
        <parent>cabinet</parent>
        <axis>
          <limit>
            <lower>-1</lower>
            <upper>1</upper>
          </limit>
          <xyz>0 1 0</xyz>
        </axis>
        <physics>
          <ode>
            <cfm_damping>1</cfm_damping>
          </ode>
        </physics>
       </joint>

        <link name="drawer2">
            <pose>0.013 -0.23 0.6 0 0 0</pose>
            <visual name="drawer_visual">
                <geometry>
                    <mesh>
                     <uri>model://cabinet_drawer/meshes/drawer.dae</uri>
                     <scale>1 1 1</scale>
                    </mesh>
                </geometry>
            </visual>
            <collision name="drawer_collision">
                <geometry>
                    <mesh>
                     <uri>model://cabinet_drawer/meshes/drawer.dae</uri>
                     <scale>1 1 1</scale>
                    </mesh>
                </geometry>
            </collision>
        </link>



        <joint name="drawer_joint2" type="prismatic">
        <child>drawer</child>
        <parent>cabinet</parent>
        <axis>
          <limit>
            <lower>-1</lower>
            <upper>1</upper>
          </limit>
          <xyz>0 1 0</xyz>
        </axis>
        <physics>
          <ode>
            <cfm_damping>1</cfm_damping>
          </ode>
        </physics>
       </joint>

        <link name="drawer3">
            <pose>0.013 -0.23 0.3 0 0 0</pose>
            <visual name="drawer_visual">
                <geometry>
                    <mesh>
                     <uri>model://cabinet_drawer/meshes/drawer.dae</uri>
                     <scale>1 1 1</scale>
                    </mesh>
                </geometry>
            </visual>
            <collision name="drawer_collision">
                <geometry>
                    <mesh>
                     <uri>model://cabinet_drawer/meshes/drawer.dae</uri>
                     <scale>1 1 1</scale>
                    </mesh>
                </geometry>
            </collision>
        </link>



        <joint name="drawer_joint3" type="prismatic">
        <child>drawer</child>
        <parent>cabinet</parent>
        <axis>
          <limit>
            <lower>-1</lower>
            <upper>1</upper>
          </limit>
          <xyz>0 1 0</xyz>
        </axis>
        <physics>
          <ode>
            <cfm_damping>1</cfm_damping>
          </ode>
        </physics>
       </joint>

    </model>
</sdf>
"""


rospy.init_node('insert_object',log_level=rospy.INFO)



position = [0,0,0]
orientation = [0,0,0]
cabinet_pose = Pose(Point(*position), Quaternion(*quaternion_from_euler(*orientation)))
rospy.wait_for_service('gazebo/spawn_sdf_model')
spawn_model_prox = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
spawn_model_prox("Cabinet", sdff, "", cabinet_pose, "world")
