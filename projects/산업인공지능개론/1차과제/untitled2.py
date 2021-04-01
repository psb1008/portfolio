from durable.lang import *

s = 'H/W5'

with ruleset(s):
    @when_all(c.first << (m.predicate == '좋지않다') & (m.object == '포커스가'),
              (m.predicate == '문제가 해결된다') & (m.object == '디포커싱') & (m.subject == c.first.subject))
    def 워킹조절(c):
        c.assert_fact({ 'subject': c.first.subject, 'predicate': '조절한다', 'object': 'Working Distance를' })

    @when_all(c.first << (m.predicate == '어둡다') & (m.object == '영상밝기가'),
              (m.predicate == '문제가 해결된다') & (m.object == '영상밝기') & (m.subject == c.first.subject))
    def Gain조절(c):
        c.assert_fact({ 'subject': c.first.subject, 'predicate': '조절한다', 'object': 'Camera Gain 값을' })
    
    @when_all(c.first << (m.predicate == '어둡다') & (m.object == '영상밝기가'))
    def 컨트롤러조절(c):          
        c.assert_fact({ 'subject': c.first.subject, 'predicate': '조절한다', 'object': '조명값을' }) 
    
    @when_all(c.first << (m.predicate == '어둡다') & (m.object == '영상밝기가'))
    def 조리개조절(c):          
        c.assert_fact({ 'subject': c.first.subject, 'predicate': '조절한다', 'object': '조리개를' })    
              
    @when_all(c.first << (m.predicate == '고르지 않다') & (m.object == '포커스가'),
              (m.predicate == '심도가 커진다') & (m.object == '포커스') & (m.subject == c.first.subject))
    def 심도조절(c):
        c.assert_fact({ 'subject': c.first.subject, 'predicate': '조금 닫는다', 'object': '조리개를' })
    
    @when_all(c.first << (m.predicate == '이 되지 않는다') & (m.object == '장치인식'),
              (m.predicate == '문제가 해결된다') & (m.object == '장치인식') & (m.subject == c.first.subject))
    def 펌웨어확인(c):
        c.assert_fact({ 'subject': c.first.subject, 'predicate': '확인한다', 'object': '버전을' })
        
    @when_all((m.predicate == '이 되지 않는다') & (m.object == '장치인식'))
    def 전원확인(c):
        c.assert_fact({ 'subject': c.first.subject, 'predicate': '확인한다', 'object': '전원을' })
    
    @when_all(c.first << (m.predicate == '되지 않는다') & (m.object == '영상획득이'),
              (m.predicate == '문제가 해결된다') & (m.object == '영상획득') & (m.subject == c.first.subject))
    def 카메라전원(c):
        c.assert_fact({ 'subject': c.first.subject, 'predicate': '점등되어 있는지 확인', 'object': '카메라 전원 LED가' })
    
    @when_all((m.predicate == '되지 않는다') & (m.object == '영상획득이'))
    def 보드확인(c):
        c.assert_fact({ 'subject': c.first.subject, 'predicate': '인식 확인', 'object': 'FrameGrabber' })
    
    @when_all((m.predicate == '되지 않는다') & (m.object == '영상획득이'))
    def 카메라셋(c):
        c.assert_fact({ 'subject': c.first.subject, 'predicate': '확인 한다', 'object': '카메라 설정값' })
        
    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.object, c.m.predicate))


assert_fact(s, { 'subject': '디포커싱이슈:', 'predicate': '좋지않다', 'object': '포커스가' })
assert_fact(s, { 'subject': '디포커싱이슈:', 'predicate': '문제가 해결된다', 'object': '디포커싱' })
assert_fact(s, { 'subject': '영상불량이슈:', 'predicate': '어둡다', 'object': '영상밝기가' })
assert_fact(s, { 'subject': '영상불량이슈:', 'predicate': '문제가 해결된다', 'object': '영상밝기' })
assert_fact(s, { 'subject': '디포커싱이슈:', 'predicate': '고르지 않다', 'object': '포커스가' })
assert_fact(s, { 'subject': '디포커싱이슈:', 'predicate': '심도가 깊어진다', 'object': '포커스' })
assert_fact(s, { 'subject': 'FrameGrabber:', 'predicate': '이 되지 않는다', 'object': '장치인식' })
assert_fact(s, { 'subject': 'FrameGrabber:', 'predicate': '문제가 해결된다', 'object': '장치인식' })
assert_fact(s, { 'subject': '영상획득안됨:', 'predicate': '되지 않는다', 'object': '영상획득이' })
assert_fact(s, { 'subject': '영상획득안됨:', 'predicate': '문제가 해결된다', 'object': '영상획득' })

s = 'C/S5'

with ruleset(s):
    @when_all(c.first << (m.predicate == '접수한다') & (m.object == '이슈를'),
              (m.predicate == '해결한다') & (m.object == '이슈를') & (m.subject == c.first.subject))
    def 배포(c):
        c.assert_fact({ 'subject': c.first.subject + '에게', 'object': '신규버전을', 'predicate': '배포한다' })

    @when_all((m.object == '신규버전을') & (m.predicate == '배포한다'))
    def 테스트(c):
        c.assert_fact({ 'subject': '개발한', 'object': c.m.object, 'predicate': '테스트한다' })
    
    @when_all((m.object == '신규버전을') & (m.predicate == '테스트한다'))
    def 제작(c):
        c.assert_fact({ 'subject': '고객사가 요청한', 'object': '기능을', 'predicate': '개발한다' })
     
    @when_all((m.object == '기능을') & (m.predicate == '개발한다'))
    def 검토(c):
        c.assert_fact({ 'subject': c.m.subject, 'object': c.m.object, 'predicate': '검토한다' })
    
    @when_all((m.predicate == '테스트') & (m.object == '확인'))
    def 런테스트(c):
        c.assert_fact({ 'subject': c.m.subject + '을', 'object': '설비에 적용 후', 'predicate': '테스트한다' })
   
    @when_all((m.object == '기능을') & (m.predicate == '개발한다'))
    def 고객컨펌(c):
        c.assert_fact({ 'subject': c.m.subject + '대해서', 'object': '고객사에게', 'predicate': '컨펌을 받는다' })
        
    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.object, c.m.predicate))
        
assert_fact(s, { 'subject': '고객사', 'object': '이슈를', 'predicate': '접수한다' })
assert_fact(s, { 'subject': '고객사', 'object': '이슈를', 'predicate': '해결한다' })
assert_fact(s, { 'subject': 'A이슈에 대한', 'object': '기능을', 'predicate': '개발한다' })
assert_fact(s, { 'subject': '1.0.6의', 'object': '신규버전을', 'predicate': '테스트한다' })
assert_fact(s, { 'subject': '신규버전', 'object': '확인', 'predicate': '테스트' })