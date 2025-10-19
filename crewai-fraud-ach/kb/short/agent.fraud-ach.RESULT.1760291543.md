```json
{
  "id": "83f891e3a30881b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291543,
  "host_pid": "9e6742732c60:1",
  "hash": "301363a9be40a318d046dbc87021e74296c12506c98edc6a8a869e1e5d192968",
  "cid": "QmV1301363a9be40a318d046dbc87021e74296c12506",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291543,
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
      "evaluated_at": 1760291543
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
  "sig": "50bf2247605ab2cc28bec8d4e8b8820fbe4c108a3751a2e7531409cff9c3270e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039498282
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 88188834, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285765, 'matching_hash': 'dad018b424b66512'}}}