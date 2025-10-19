```json
{
  "id": "2382b1ebede679a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292361,
  "host_pid": "9e6742732c60:1",
  "hash": "12b8eedf51126c8709f7120951409dba258131c8c3127b3354ccb956343635c5",
  "cid": "QmV112b8eedf51126c8709f7120951409dba258131c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292361,
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
      "evaluated_at": 1760292361
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "77c564fcbbb2db6583a464da0683997a34d8efdac7f1629c00498bd5960e2381"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 026009594828050
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 196000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285763, 'matching_hash': '3e77f188c48013ab'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}