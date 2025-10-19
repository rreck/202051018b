```json
{
  "id": "ca7403f130eb1de4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294066,
  "host_pid": "9e6742732c60:1",
  "hash": "fc6f651f9ba99831c4d7738e200c790d0345f3ef33a1fc8accedb732175dc653",
  "cid": "QmV1fc6f651f9ba99831c4d7738e200c790d0345f3ef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294066,
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
      "evaluated_at": 1760294066
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "d7dcea1be6168f246612d6b813405630cfe8776405f90e0fe9d96c9442437e48"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 111000022758137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 115500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': '98fae2ebc6a98bc5'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}