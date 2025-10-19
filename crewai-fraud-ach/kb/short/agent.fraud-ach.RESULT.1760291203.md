```json
{
  "id": "f1c7507dd63b64c3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291203,
  "host_pid": "9e6742732c60:1",
  "hash": "0cf2da31c1ea15d8a9c1339bb6c443c3b37e2ef2d303b934e12427d082fa6ad6",
  "cid": "QmV10cf2da31c1ea15d8a9c1339bb6c443c3b37e2ef2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291203,
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
      "evaluated_at": 1760291203
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
  "sig": "eb6aed9b8e00871896581a607519cbdda1d2bc56e4aa274123952db0f32c49e9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464250877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 63033451, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285765, 'matching_hash': '9a278d14d50dbff1'}}}