{{/*
공통 레이블
*/}}
{{- define "k8s-app.labels" -}}
app.kubernetes.io/name: {{ include "k8s-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
차트 이름
*/}}
{{- define "k8s-app.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
백엔드 선택자 레이블
*/}}
{{- define "k8s-app.backend.selectorLabels" -}}
app: {{ .Values.backend.name }}
{{- end }}

{{/*
프론트엔드 선택자 레이블
*/}}
{{- define "k8s-app.frontend.selectorLabels" -}}
app: {{ .Values.frontend.name }}
{{- end }}

