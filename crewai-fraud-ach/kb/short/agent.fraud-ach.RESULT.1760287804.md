```json
{
  "id": "4311e6db9fb50248",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287804,
  "host_pid": "9e6742732c60:1",
  "hash": "d4e3ca7f855105c43ca3f50516d09c21238566c439968e524ade3f64129dfe57",
  "cid": "QmV1d4e3ca7f855105c43ca3f50516d09c21238566c4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287804,
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
      "evaluated_at": 1760287804
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
  "sig": "fff5a05a84dc8f7aea2c2318d4a09d0e0fb203f3829de26d2477042767a34216"
}
```

Fraud detected: duplicate_transaction (score: 90)
Transaction: 026009593273938
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 26593170, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285763, 'matching_hash': '9925ef3004078e34'}}}