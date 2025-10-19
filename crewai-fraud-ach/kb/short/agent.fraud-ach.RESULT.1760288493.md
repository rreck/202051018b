```json
{
  "id": "50bc253fd1447103",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288493,
  "host_pid": "9e6742732c60:1",
  "hash": "701c19c79d3322bcfd5daf3cd4c8f70135327a9f4734eecc960c8ed63c9ded8a",
  "cid": "QmV1701c19c79d3322bcfd5daf3cd4c8f70135327a9f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288493,
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
      "evaluated_at": 1760288494
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
  "sig": "96cf24d31262a6941736d526d4d0f7993f1fafe4320370dc6ecfb6a7e7669df7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276282888
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50, 'total_amount': 36282210, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285763, 'matching_hash': '2c6b6a2c3736dbce'}}}