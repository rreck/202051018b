```json
{
  "id": "64d8b9d848645cfa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292184,
  "host_pid": "9e6742732c60:1",
  "hash": "bef76cff093c6a14187e59b462c25e00c616a3e07c236084cf52a3584bb2f6ec",
  "cid": "QmV1bef76cff093c6a14187e59b462c25e00c616a3e0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292184,
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
      "evaluated_at": 1760292184
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
  "sig": "5c94e49198cbf0863699d7e5adb335bf318f1bcd4b74d10bc444033e47b4cd60"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153448153
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 92781504, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285764, 'matching_hash': '55db9843fa0daece'}}}