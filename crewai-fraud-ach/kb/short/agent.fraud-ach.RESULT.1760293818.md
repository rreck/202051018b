```json
{
  "id": "d90dbb43632edc47",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293818,
  "host_pid": "9e6742732c60:1",
  "hash": "b23291dc02b70fe29242f1b343ff1ab1b25bef4346582f47d03b038d9f57b1ca",
  "cid": "QmV1b23291dc02b70fe29242f1b343ff1ab1b25bef43",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293818,
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
      "evaluated_at": 1760293818
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
  "sig": "3e7510778625f9b0cfcca324c741743749014be58ebda97be07da6d62a9ce1d2"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 122105158962917
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 226000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': '11dc2cfd2eb8ef5d'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}