```json
{
  "id": "6ab7fc46387ddd76",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293919,
  "host_pid": "9e6742732c60:1",
  "hash": "4b3e7d547e8a5f230fca5b61f4b5072cc7616f69f7517c9d53b708148cedc7e8",
  "cid": "QmV14b3e7d547e8a5f230fca5b61f4b5072cc7616f69",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293919,
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
      "evaluated_at": 1760293919
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
  "sig": "e71091bbb934a466959acbc983ef0f09b905ef6fb8c128a7a6b5a1befd1d760f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026472141
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 46970736, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285764, 'matching_hash': 'c34da1cfbf75ff05'}}}