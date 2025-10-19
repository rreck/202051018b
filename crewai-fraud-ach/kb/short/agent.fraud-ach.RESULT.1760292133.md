```json
{
  "id": "2d8c968ae6b11dad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292133,
  "host_pid": "9e6742732c60:1",
  "hash": "8000d56ae160538cc98fdf4a239c5d6933c9e823e1158d915d3d0fd0d0b182fa",
  "cid": "QmV18000d56ae160538cc98fdf4a239c5d6933c9e823",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292133,
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
      "evaluated_at": 1760292133
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
  "sig": "fdcb8d1b6ed95337dab31a4b00cfb56cb9c9381681e5aa78ecbb7d39dc1fb2f6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025380503
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 15027116, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': '5a364e4e5c1e4dba'}}}