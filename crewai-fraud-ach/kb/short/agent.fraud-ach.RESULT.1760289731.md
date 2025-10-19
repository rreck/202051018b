```json
{
  "id": "06395b948b30d29a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289731,
  "host_pid": "9e6742732c60:1",
  "hash": "d27154ab995b4a2dc420aec00a6a75524dc473c35d88c6381f44c63c6341b879",
  "cid": "QmV1d27154ab995b4a2dc420aec00a6a75524dc473c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289731,
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
      "evaluated_at": 1760289731
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
  "sig": "e1d1221ea9c49797857c5f9710c61db157ea855e0bdfa6869ac53cb2df5d8f36"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243970709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 11601884, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285765, 'matching_hash': '886d04c9297a738f'}}}