```json
{
  "id": "314a4aaf94f561ce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293295,
  "host_pid": "9e6742732c60:1",
  "hash": "084cabbc8cd3f2daefdb80bacc632847f6f2f73463d49acbb00b05c5700dae8c",
  "cid": "QmV1084cabbc8cd3f2daefdb80bacc632847f6f2f734",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293295,
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
      "evaluated_at": 1760293295
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
  "sig": "539c37422d9b9324ed3c58a8df59b7fecf4a5324dd2a60717056ac24ec8b0386"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 68423320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}