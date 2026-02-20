def analyze_log(log_content: str) -> str:
    # 임시 목업 응답 (API 키 준비되면 실제 AI로 교체)
    lines = log_content.splitlines()
    error_lines = [l for l in lines if "ERROR" in l or "CRITICAL" in l]
    
    if not error_lines:
        return """✅ 이상 패턴 없음
        
1. 에러 요약: 로그에서 특이사항이 발견되지 않았습니다.
2. 원인 추정: 서버가 정상적으로 운영 중입니다.
3. 해결 방안: 현재 조치 불필요합니다."""

    return f"""🚨 이상 패턴 감지됨

1. 에러 요약:
   - 총 {len(error_lines)}개의 에러/크리티컬 로그 발견
   - 주요 에러: {error_lines[0]}

2. 원인 추정:
   - 서버 또는 데이터베이스 연결 문제로 추정됩니다.
   - 반복적인 에러 패턴이 감지되었습니다.

3. 해결 방안:
   - 서버 연결 상태를 확인하세요.
   - 로그를 기반으로 해당 서비스를 재시작하세요.
   - 방화벽 및 네트워크 설정을 점검하세요.

⚠️ 감지된 에러 목록:
{chr(10).join(error_lines)}"""