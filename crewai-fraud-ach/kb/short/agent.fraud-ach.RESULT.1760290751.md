```json
{
  "id": "0f42857b167d5b11",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290751,
  "host_pid": "9e6742732c60:1",
  "hash": "afc84b2bf8644b9056f087fa748cc74c84b7129e94860985c1539cdfe6968e95",
  "cid": "QmV1afc84b2bf8644b9056f087fa748cc74c84b7129e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290751,
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
      "evaluated_at": 1760290751
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
  "sig": "ac1cb046bf8793cb9d22666f930e2c870bd9b32563b54811926c61e3a37dfaa8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469922578
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 19388970, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285763, 'matching_hash': '96901979868c282a'}}}