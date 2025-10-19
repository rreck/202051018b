```json
{
  "id": "17f9bf1c07a01c82",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288376,
  "host_pid": "9e6742732c60:1",
  "hash": "8d123553891842ef7989bc80c08d1f2eb687cbe3d77c47c40605ce736e9cd93a",
  "cid": "QmV18d123553891842ef7989bc80c08d1f2eb687cbe3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288376,
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
      "evaluated_at": 1760288376
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
  "sig": "4d08cdc14ea8560b3d90b25a999f266e8a9a45cb3dc370f89709ed754487d5cb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466004729
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 25958387, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285765, 'matching_hash': '1e26fed2c08b1370'}}}