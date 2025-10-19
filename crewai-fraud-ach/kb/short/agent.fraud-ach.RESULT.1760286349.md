```json
{
  "id": "425fe331b1a6d94a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286349,
  "host_pid": "9e6742732c60:1",
  "hash": "cd16404c40ee902283d8d5a5c8f31418d52db04f7eb33d87405312a28fef141d",
  "cid": "QmV1cd16404c40ee902283d8d5a5c8f31418d52db04f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286349,
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
      "evaluated_at": 1760286349
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
  "sig": "b754c13f1129d8880b878f5d43a65be111bb1c874aa7d99609447caee23a22d5"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105150741223
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285765, 'matching_hash': '3a8aff16771fc05f'}}}