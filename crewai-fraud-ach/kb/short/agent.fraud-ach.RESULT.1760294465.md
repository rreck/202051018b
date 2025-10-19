```json
{
  "id": "c9d061678591547b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294465,
  "host_pid": "9e6742732c60:1",
  "hash": "42b83c8c4c690e97f74733086fdff3600846900a723a81da119c62fb76979a99",
  "cid": "QmV142b83c8c4c690e97f74733086fdff3600846900a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294465,
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
      "evaluated_at": 1760294465
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
  "sig": "01795507325e348db5d4c01e6cb33fc6db9ee22b656e5fe9628c10c9883f3a95"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039404283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 79581726, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285765, 'matching_hash': '11fbcf742e15d2b0'}}}