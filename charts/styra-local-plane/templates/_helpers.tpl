
{{- define "styra-local-plane.fullname" -}}
{{- printf "slp-%s-%s" .Values.tenant .Values.system | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "styra-local-plane.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "styra-local-plane.labels" -}}
helm.sh/chart: {{ include "styra-local-plane.chart" . }}
{{ include "styra-local-plane.selectorLabels" . }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "styra-local-plane.selectorLabels" -}}
app: {{ include "styra-local-plane.fullname" . }}
version: {{ .Chart.AppVersion }}
sytem-type: istio
app.kubernetes.io/name: {{ include "styra-local-plane.fullname" . }}
{{- end }}
