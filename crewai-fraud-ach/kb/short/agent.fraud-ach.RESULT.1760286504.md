```json
{
  "id": "675789e38957189e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286504,
  "host_pid": "9e6742732c60:1",
  "hash": "14136a718662df4e785580d6a22690e7cd738c93350d7e99c27582eb8e6b5801",
  "cid": "QmV114136a718662df4e785580d6a22690e7cd738c93",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286504,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760286504
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "644c3070e083c3e4b0a1b2d52792a63d831eb6808e3082746b847e25c0249cfd"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 272809904666410
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285765, 'matching_hash': 'b8be43189937b834'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '272809901', 'validation_error': 'Invalid routing number checksum'}}}