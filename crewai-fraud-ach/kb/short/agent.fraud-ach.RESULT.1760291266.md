```json
{
  "id": "66bed8e33d0a26eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291266,
  "host_pid": "9e6742732c60:1",
  "hash": "01f159cd2d154423ae83b01884ffef024a5acf103686659e3940238ad0bb2148",
  "cid": "QmV101f159cd2d154423ae83b01884ffef024a5acf10",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291266,
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
      "evaluated_at": 1760291266
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
  "sig": "2a2a0becee4bfb93ee08cb743c9b0b02f4aca2b824d1a9fc75d5ed1e4e9e48aa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022959454
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 25720794, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285763, 'matching_hash': 'd9e1e1b77e5bc9b7'}}}