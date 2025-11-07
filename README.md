
- **Backend**: Django REST Framework (DRF)
- **Frontend**: React + Vite
- **Container Orchestration**: Kubernetes (K8s)
- **Package Manager**: Helm


### 프로젝트 구조

```
2025_k8s/
├── backend/
├── frontend/
└── docs/
└── helm/
```

### Helm 차트 설치

1. Helm 차트 의존성 업데이트
```bash
cd helm
helm dependency update
```

2. Helm 차트 설치
```bash
helm install k8s-app . -n default
```

3. 설치 상태 확인
```bash
kubectl get pods
kubectl get services
kubectl get deployments
```

### API 엔드포인트

- `GET /api/names/` - 이름 목록 조회
- `POST /api/names/` - 이름 저장
  ```json
  {
    "name": "홍길동"
  }
  ```
- `GET /api/health/` - 헬스 체크 (liveness/readiness probe용)

### 아키텍처
<img width="1839" height="1648" alt="Image" src="https://github.com/user-attachments/assets/8830fb3b-f4ca-441e-ac4f-9c7b9d4a879e" />


### 참고 자료
- [Kubernetes 공식 문서](https://kubernetes.io/docs/)
- [Helm 공식 문서](https://helm.sh/docs/)
- [Django REST Framework 문서](https://www.django-rest-framework.org/)
- [React 공식 문서](https://react.dev/)
- [AWS EKS 문서](https://docs.aws.amazon.com/eks/)
