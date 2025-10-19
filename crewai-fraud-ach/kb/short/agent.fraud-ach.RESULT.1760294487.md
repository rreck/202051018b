```json
{
  "id": "d26a74d86009c48d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294487,
  "host_pid": "9e6742732c60:1",
  "hash": "e1d93c8c68df7b51eef37ba03ea83a9a8825228f5143daa45f11dc8e33f89e39",
  "cid": "QmV1e1d93c8c68df7b51eef37ba03ea83a9a8825228f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294487,
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
      "evaluated_at": 1760294487
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
  "sig": "96c01b23bc3eebf8c1068ec9df387aec76e8198d88f10d62698f144035450ca9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249225817
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 56296211, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': 'b4dc0a1cb279f16e'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}