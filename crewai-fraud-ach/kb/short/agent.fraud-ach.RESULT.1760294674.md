```json
{
  "id": "f4db1b5a7b4c6ad8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294674,
  "host_pid": "9e6742732c60:1",
  "hash": "7b672e51aef7e6bc94ea13a46523480e54fe329d4a9c963d8c147c6d2ac4edc4",
  "cid": "QmV17b672e51aef7e6bc94ea13a46523480e54fe329d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294674,
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
      "evaluated_at": 1760294674
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
  "sig": "852084e5940a651fcebcef43545e0b5f7bfb43494ca19ea2a73ef5295c46a6c1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279407211
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 52621690, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285764, 'matching_hash': 'efd9a787beb40cb2'}}}