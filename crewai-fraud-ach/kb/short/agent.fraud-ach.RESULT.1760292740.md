```json
{
  "id": "f7ee39d82309f85f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292740,
  "host_pid": "9e6742732c60:1",
  "hash": "d78cf6ade5082a58a1b18f1954dda163a5518001c4fff435d099dc89604eca58",
  "cid": "QmV1d78cf6ade5082a58a1b18f1954dda163a5518001",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292740,
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
      "evaluated_at": 1760292740
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
  "sig": "01eff79ae10469ffbf843a448c0f11133a8c72c27f7724848e4db228f987ed9c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153776491
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 18052572, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285763, 'matching_hash': '94746339473c09ed'}}}