```json
{
  "id": "6aab54a9e1cc19e8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292966,
  "host_pid": "9e6742732c60:1",
  "hash": "86981f4cc2ca8b63905a9e5822b4c0ef218b2c6ea501a1c653385f38b0adcd69",
  "cid": "QmV186981f4cc2ca8b63905a9e5822b4c0ef218b2c6e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292966,
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
      "evaluated_at": 1760292966
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
  "sig": "56bb37ec8908e60a50d1af7d2fd368401d78d23f7274ea7752132c3a448a40c2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599280040
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 101738274, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': '3242f38050bfb93d'}}}