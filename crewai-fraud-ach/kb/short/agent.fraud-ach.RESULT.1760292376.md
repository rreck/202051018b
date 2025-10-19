```json
{
  "id": "64bd90db446487cf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292376,
  "host_pid": "9e6742732c60:1",
  "hash": "078ebf96592b24cb4a6fb0b7c6e3488e1f37424f4413647b86b6bd0bdc0e4665",
  "cid": "QmV1078ebf96592b24cb4a6fb0b7c6e3488e1f37424f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292376,
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
      "evaluated_at": 1760292376
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
  "sig": "d36f03f8b0f774d926d6ff0a5102e3c18eed4a76335fec4781a5f5920dd71fff"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272560065
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 272, 'threshold': 50, 'total_amount': 31082528, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 271, 'first_seen': 1760284979, 'matching_hash': 'aab4f056297a675d'}}}maly': {'fraud_detected': True, 'risk_score': 70, 'details': {'zscore': 3.08, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6131353}}}