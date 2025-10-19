```json
{
  "id": "db50a42a5efa3ed3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286954,
  "host_pid": "9e6742732c60:1",
  "hash": "fb71911d3345382b304b5e57781b2cb362836d6bca9c101e6222355f171168bf",
  "cid": "QmV1fb71911d3345382b304b5e57781b2cb362836d6b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286954,
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
      "evaluated_at": 1760286954
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "26326edbe7ca58e977ec88e8a9f96be08b446e925e6923c19bc1ff5cc6c2e087"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100272276410
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760285764, 'matching_hash': '97f823784b1b19f6'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760285764, 'matching_hash': '0d940850b17c9224'}}}