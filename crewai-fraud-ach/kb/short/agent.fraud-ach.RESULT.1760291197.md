```json
{
  "id": "c58663bd56716ffc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291197,
  "host_pid": "9e6742732c60:1",
  "hash": "8a13d45fe73311f77fb47537e79e8b3109698ebf754a6eea0878d10165636bee",
  "cid": "QmV18a13d45fe73311f77fb47537e79e8b3109698ebf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291197,
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
      "evaluated_at": 1760291197
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
  "sig": "ebe778332501fff77a8efa9c779b9300193ae299fdbc3d52456c6a956dc95ec5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598076965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 26501228, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285763, 'matching_hash': '05e01649c2d43b8b'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5062727}}}