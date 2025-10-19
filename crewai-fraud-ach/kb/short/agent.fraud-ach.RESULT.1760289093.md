```json
{
  "id": "0188af6f638ac4c7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289093,
  "host_pid": "9e6742732c60:1",
  "hash": "3f750b2a4cf2383a262aee89f5bab17d267a9dfcd4297e2d30c681024e6b45dc",
  "cid": "QmV13f750b2a4cf2383a262aee89f5bab17d267a9dfc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289093,
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
      "evaluated_at": 1760289093
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
  "sig": "225bbad46e3dde432bef6a70e1efd74d632c8ac942385d3c6982323c1d30b9a0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272268645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 49755143, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285765, 'matching_hash': '088fbc730f5432fe'}}}