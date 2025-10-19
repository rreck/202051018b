```json
{
  "id": "1ba3a03ceff9b035",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290021,
  "host_pid": "9e6742732c60:1",
  "hash": "1dcbcde2cb57364ff7c48561ecea80c03f9cdfa931701aab4fa2fc8f761f7977",
  "cid": "QmV11dcbcde2cb57364ff7c48561ecea80c03f9cdfa9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290021,
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
      "evaluated_at": 1760290021
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
  "sig": "14d2887a27b7c9213fd83a8d2a5f517955792e986db2333a3f559a5ba6dd45f0"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 021000026547506
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 139000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285764, 'matching_hash': 'e0a909ce459a76c8'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}