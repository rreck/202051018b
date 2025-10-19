```json
{
  "id": "b83b40da5a2b78bc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286374,
  "host_pid": "9e6742732c60:1",
  "hash": "2afcb4767e1622de5f3aa5b70a81ee015a39a8fc3f81f56f92dcd2432b21f959",
  "cid": "QmV12afcb4767e1622de5f3aa5b70a81ee015a39a8fc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286374,
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
      "evaluated_at": 1760286374
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
  "sig": "52375c6619717bd95e03421d9137dc7c09e872ea6b24f6bcd2543c8cd286436d"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 683146203883533
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285764, 'matching_hash': '8f404d0fc37310f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '683146208', 'validation_error': 'Invalid routing number checksum'}}}