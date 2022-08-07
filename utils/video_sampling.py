import cv2

class VideoSampling:
    
    def __init__(self, dir_path, frame):
        
        self.dir = dir_path
        self.frame = frame
        # 비디오 로딩.
        self.vidcap = cv2.VideoCapture(self.dir)
        
        
    def sampling(self):

        cnt, num = 0, 1 # cnt는 Total frame 개수, num은 추출할 Frame 개수.

        total_length = int(self.vidcap.get(cv2.CAP_PROP_FRAME_COUNT)) # 총 비디오의 frame수.
        cycle = int(total_length / self.frame) # 주기 계산.
        
        while self.vidcap.isOpened():
            ret,image = self.vidcap.read()
            if num > res_cnt:
                break
            if ret and cnt % cycle == 0:  
                
                try:
                    cv2.imwrite(f"LLFF/yk_quarter_moving_150/images/frame{num}.jpg", image) # 경로랑 파일명 저장
                    num+=1
                except:
                    print("fail")
                    
            cnt += 1
            
        self.vidcap.release()
        
        
if __name__ == "__main__":
    
    # 비디오 경로 설정을 하고 추출하고 싶은 frame의 개수를 설정한다.
    dir_path = 'LLFF/yk_quarter_moving_150/video/20220707_131502.mp4'
    frame = 100
    
    exe = VideoSampling(dir_path, frame)
    exe.sampling()
