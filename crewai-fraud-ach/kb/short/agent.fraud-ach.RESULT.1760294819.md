```json
{
  "id": "3d85a8b263690347",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294819,
  "host_pid": "9e6742732c60:1",
  "hash": "b446b0f90970d332d740d7ac769458da961fe0a94c9d15d4421fd0ca1ab43a0a",
  "cid": "QmV1b446b0f90970d332d740d7ac769458da961fe0a9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294819,
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
      "evaluated_at": 1760294819
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
  "sig": "3868cbac053a8a586a061731c64b98a992f5fc5037fad85865044bcec618454d"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 111000022304560
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 122500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': '2db1b4b6a652c406'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}57513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6892469}}}