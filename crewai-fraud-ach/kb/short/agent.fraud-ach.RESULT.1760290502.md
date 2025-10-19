```json
{
  "id": "f96ac7cb83e5ce30",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290502,
  "host_pid": "9e6742732c60:1",
  "hash": "0f07ad41321751e15e09f3c541c23d7d13e5e3ea5f35ff2e5e0f1ae6dae2bfdb",
  "cid": "QmV10f07ad41321751e15e09f3c541c23d7d13e5e3ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290502,
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
      "evaluated_at": 1760290502
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
  "sig": "b9a4ff12a79f3419d181609e9fa8ccf70a7ffcf68ab2d808915236a869fc929a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274968720
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 56716368, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285763, 'matching_hash': '69fe72c937d65071'}}}