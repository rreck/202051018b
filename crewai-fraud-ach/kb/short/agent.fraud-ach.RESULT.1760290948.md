```json
{
  "id": "a40eab1029183c68",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290948,
  "host_pid": "9e6742732c60:1",
  "hash": "adb173dda9dfdbe245ed155bb76a2c4179432fabe4c2a0be30c914d31db867ee",
  "cid": "QmV1adb173dda9dfdbe245ed155bb76a2c4179432fab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290948,
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
      "evaluated_at": 1760290948
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
  "sig": "ed1ed0e7f385709f4edc7172be775948d649b78ddeefd0f8555aa3710d5cdbc5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025262531
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 51930170, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285763, 'matching_hash': 'cd477724f7ce5ce7'}}}maly': {'fraud_detected': True, 'risk_score': 91, 'details': {'zscore': 5.16, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9795510}}}