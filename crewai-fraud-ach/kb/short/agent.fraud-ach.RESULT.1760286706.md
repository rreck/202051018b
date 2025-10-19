```json
{
  "id": "4b033cedfe200d96",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286706,
  "host_pid": "9e6742732c60:1",
  "hash": "b62f18e979849ab02c2b773e2e95614998136be821b5c2fb1795eef17ca695e2",
  "cid": "QmV1b62f18e979849ab02c2b773e2e95614998136be8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286706,
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
      "evaluated_at": 1760286706
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
  "sig": "bc69b4ecb4fe9fe82b2fbe092ca958dc441ea21aba4654f8675ed91df03a1236"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105154242410
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285765, 'matching_hash': '26a9af32f02bfdfc'}}}