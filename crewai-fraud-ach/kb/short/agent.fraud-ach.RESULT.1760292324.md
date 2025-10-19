```json
{
  "id": "4fc11ba24a22823b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292324,
  "host_pid": "9e6742732c60:1",
  "hash": "c3bf0094a0a8a6a81ce6a9ac180ad4bef646607b22d3d4a2a64d304aec40ca17",
  "cid": "QmV1c3bf0094a0a8a6a81ce6a9ac180ad4bef646607b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292324,
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
      "evaluated_at": 1760292324
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
  "sig": "efa309b3a2841b9cd6adbbdd1e4cc610b8e6a853bc024a275c2bbb7bede01dc0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243604729
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 96861180, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': '930ed718dd68e21a'}}}