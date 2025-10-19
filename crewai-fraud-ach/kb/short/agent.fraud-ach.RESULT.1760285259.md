```json
{
  "id": "8472f23c6b610c30",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285259,
  "host_pid": "9e6742732c60:1",
  "hash": "5ec27572c5b16ce563aab292f5c330ba43ae6ec57247cdc83e63a97aa8a0036d",
  "cid": "QmV15ec27572c5b16ce563aab292f5c330ba43ae6ec5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285259,
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
      "evaluated_at": 1760285259
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "36f119fde077bde3b1c66679152c2fb5c6e8df79caceb439c5975117b6dc4542"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11799032, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}