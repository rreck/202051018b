```json
{
  "id": "5f44a660ec3c729a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288371,
  "host_pid": "9e6742732c60:1",
  "hash": "13c8a4a455b3c6b9fcf3e590bf8a2e37af86ea7bb3da39b751f6d98084231fff",
  "cid": "QmV113c8a4a455b3c6b9fcf3e590bf8a2e37af86ea7b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288371,
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
      "evaluated_at": 1760288371
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
  "sig": "08c29edb4407182b0f2d2a86a1722146875b968c8b32ca57878568d420057146"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021660412
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 29317561, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285764, 'matching_hash': '19be1dcf8b4c513c'}}}