```json
{
  "id": "8c38bd10cb7b81dc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292008,
  "host_pid": "9e6742732c60:1",
  "hash": "f047431c8707de67d5e7e305e445295ba092a34dee45790a0a0ab5ba1fa20ed2",
  "cid": "QmV1f047431c8707de67d5e7e305e445295ba092a34d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292008,
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
      "evaluated_at": 1760292008
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
  "sig": "1434ada0a403ae7d319eebfe853dbf61182312e3391e7fa150454751b6a09a76"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035326391
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 70255224, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285763, 'matching_hash': '7c05ec5f373172f0'}}}