```json
{
  "id": "1f1639207f57b160",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291051,
  "host_pid": "9e6742732c60:1",
  "hash": "b876858e9b5fb6f36aac6f9bf67fcf958e084d39ec401baceb04b7f6720e86d1",
  "cid": "QmV1b876858e9b5fb6f36aac6f9bf67fcf958e084d39",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291051,
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
      "evaluated_at": 1760291051
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
  "sig": "03237c5b4a444984f7e722c40346dc5fca0e68ff0b88de786b68327608c255ca"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595927429
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 24002438, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285763, 'matching_hash': 'ad7b7e4988d8fb8c'}}}