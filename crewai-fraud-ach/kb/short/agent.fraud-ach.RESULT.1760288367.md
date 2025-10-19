```json
{
  "id": "6c91171cf6e693f1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288367,
  "host_pid": "9e6742732c60:1",
  "hash": "790b4858cb61b2410728855aa0b70e426e76642eb0fbc1d75b2b67d3c784b826",
  "cid": "QmV1790b4858cb61b2410728855aa0b70e426e76642e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288367,
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
      "evaluated_at": 1760288367
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
  "sig": "d846063dd72dbc1c8e704125dccdd4923e360f09ff846e81ff244423d2619c76"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272268645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 40068301, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285765, 'matching_hash': '088fbc730f5432fe'}}}