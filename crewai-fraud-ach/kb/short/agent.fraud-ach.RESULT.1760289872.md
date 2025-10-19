```json
{
  "id": "ad553671cbb29e8e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289872,
  "host_pid": "9e6742732c60:1",
  "hash": "97658e7f0fa3e34bef2133254867e475f22e12854f5167863a07dd477a6ee0e3",
  "cid": "QmV197658e7f0fa3e34bef2133254867e475f22e1285",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289872,
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
      "evaluated_at": 1760289872
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
  "sig": "13caad5069782c15b87a36016bacdef570b1f218fbe4c969e50754e4fddd64ac"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 683146203883533
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 50276970, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285764, 'matching_hash': '8f404d0fc37310f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '683146208', 'validation_error': 'Invalid routing number checksum'}}}