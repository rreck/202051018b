```json
{
  "id": "90a2dceb6cd88658",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293749,
  "host_pid": "9e6742732c60:1",
  "hash": "5e58e4d270abe3de616b436c0956d0b5518a334963569452ab0f525faa75b5c3",
  "cid": "QmV15e58e4d270abe3de616b436c0956d0b5518a3349",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293749,
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
      "evaluated_at": 1760293749
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "14e243b717fb3b29c90cb3149ab8f58d9d9db110d25bed1996a95f88f89199fe"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 021000021703881
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 1454719500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285763, 'matching_hash': '20cca8b4db3b5ffd'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 72, 'details': {'zscore': 3.27, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6465420}}}