```json
{
  "id": "0adceb13573cba9f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294458,
  "host_pid": "9e6742732c60:1",
  "hash": "5eecd8090f4ee04cd0eb167377bc4b3d446de52860ff0b21b0507e256f6e62ff",
  "cid": "QmV15eecd8090f4ee04cd0eb167377bc4b3d446de528",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294458,
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
      "evaluated_at": 1760294458
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
  "sig": "4b4b13765d3cbae91fe4cdfb55cf1a6ca89be03829cc9f52dbec5020d26a09e4"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 121000247715779
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 238000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': 'e635467487b35661'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}