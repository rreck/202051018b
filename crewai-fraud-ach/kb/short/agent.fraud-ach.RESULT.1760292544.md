```json
{
  "id": "47a50fcc7dead722",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292544,
  "host_pid": "9e6742732c60:1",
  "hash": "076274741561305a1830ddcf2b590823f60054008feaad4a8712bef0dc09dd1e",
  "cid": "QmV1076274741561305a1830ddcf2b590823f6005400",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292544,
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
      "evaluated_at": 1760292544
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
  "sig": "dac1e4031ea86ab5b751c224080c7a2ea49d96b2842e0f513a8e76281a3d3734"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243028505
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 20622800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285763, 'matching_hash': '47e30fe250bb416c'}}}maly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 3.97, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7694908}}}