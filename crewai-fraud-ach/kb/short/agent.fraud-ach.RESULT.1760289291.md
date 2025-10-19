```json
{
  "id": "fc0c5607eb12dec6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289291,
  "host_pid": "9e6742732c60:1",
  "hash": "71df0954c383a6c019085072159b7869a0c349c78fd4b0a422e5e30dcd596d60",
  "cid": "QmV171df0954c383a6c019085072159b7869a0c349c7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289291,
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
      "evaluated_at": 1760289291
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
  "sig": "c25f9ee347ce03dc43594fbee3cfac102940aec1601ac555933552ff56591106"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240515775
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 28377573, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285763, 'matching_hash': 'c332d96fce6ec0fa'}}}aly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.15, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8018325}}}