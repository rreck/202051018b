```json
{
  "id": "6ab3a6c3d5255b7c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292327,
  "host_pid": "9e6742732c60:1",
  "hash": "a2ac5bb1763d11896fec2688aaca8da05d3611c7abd617f5f4141bdae3d86c42",
  "cid": "QmV1a2ac5bb1763d11896fec2688aaca8da05d3611c7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292327,
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
      "evaluated_at": 1760292327
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
  "sig": "d80252028a395cafbb2847e5a695a2d3fb04f8e75a759d850f025e88b24d663a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029354583
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 15470910, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': 'dbced9ae96be05e0'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}