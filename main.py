from module import physics

import multiprocessing
import time
import numpy as np
import msvcrt

frame_rate = 60
dt = 1/frame_rate

point_object = physics.Rigidbody(mass=1,fps=frame_rate)




def get_force(force_vector,force_q):
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if force_q.empty():
                if key == b'a':
                    force_vector = np.array([0.0,0.0,-1.0])
                    force_q.put(force_vector)
                if key == b'w':
                    force_vector = np.array([1.0,0.0,0.0])
                    force_q.put(force_vector)
                if key == b'd':
                    force_vector = np.array([0.0,0.0,1.0])
                    force_q.put(force_vector)
                if key == b's':
                    force_vector = np.array([-1.0,0.0,0.0])
                    force_q.put(force_vector)
                else: key = None
            
        
if __name__ == '__main__':
    force_q = multiprocessing.Queue()
    force_vector = np.array([0.0,0.0,0.0])
    
    p1 = multiprocessing.Process(target=get_force,args=(force_vector,force_q,)) 
    p1.start()       

    while True:
        t1 = time.time()
        
        if not force_q.empty():
            force_vector = force_q.get()
        point_object.update(force_vector)
        force_vector = np.array([0.0,0.0,0.0])
        
        print(point_object.position)
        
        # set delay for fps
        t = time.time() - t1
        time_delay = dt - t
        if time_delay > 0:
            time.sleep(time_delay)