<div align="center">
	<p>
		<img alt="Thoughtworks Logo" src="https://raw.githubusercontent.com/ThoughtWorks-DPS/static/master/thoughtworks_flamingo_wave.png?sanitize=true" width=200 />
    <br />
		<img alt="DPS Title" src="https://raw.githubusercontent.com/ThoughtWorks-DPS/static/master/EMPCPlatformStarterKitsImage.png?sanitize=true" width=350/>
		<br />
		<a href="https://aws.amazon.com"><img src="https://img.shields.io/badge/-deployed-blank.svg?style=social&logo=amazon"></a>
		<br />
		<h3>lab-platform-microservices-opa</h3>
		</a> <a href="https://app.circleci.com/pipelines/github/ThoughtWorks-DPS/lab-platform-microservices-opa"><img src="https://circleci.com/gh/ThoughtWorks-DPS/lab-platform-microservices-opa.svg?style=shield"></a>
		<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/github/license/ThoughtWorks-DPS/lab-platform-microservices-opa"></a>
	</p>
</div>


An implementation of opa as a microservice sidecar deployment for api authorization.

## Architectural assumptions and conventions included in this reference

**• Styra
**• opa injection is defined on a per-namespace level**  

The following configurations must be added to a namspace definition in order for deployments to the namespace to automatically pick up opa sidecars to perform the api authorizations.  

1. namespace annotation

Example:  
```yaml
---
apiVersion: v1
kind: Namespace
metadata:
  name: blue-dev
  labels:
    istio-injection: enabled
    thoughtworks-nonprod-manual-opa-injection: enabled  
```

; e.g., by including an annotation on a namespace, all deployments to the namespace will automatically have an opa sidecar included in the deployment. The annotation itself defines the SLP from which those sidecars will automatically pull their policy bundles.
• a dedicated namespace is defined for opa and styra related control-plane level components, such as SLPs and admission controllers.
