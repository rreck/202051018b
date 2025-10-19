```json
{
  "id": "651fa8d80c4f0a98",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293739,
  "host_pid": "9e6742732c60:1",
  "hash": "4556777527182be18bf0ee74694f10c31a8768c3d4e19f3747177673032deac0",
  "cid": "QmV14556777527182be18bf0ee74694f10c31a8768c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293739,
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
      "evaluated_at": 1760293739
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
  "sig": "219ae546b00269256b7ec4672cd65f4bfe3a9c89fca5ea1b7a240cbda9d53274"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 71287552, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}