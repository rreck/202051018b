```json
{
  "id": "d085a17f231505f6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291141,
  "host_pid": "9e6742732c60:1",
  "hash": "b0920ad191746594779fdf26743e4e3a36212504c1e1fb82f6e2294b1767200b",
  "cid": "QmV1b0920ad191746594779fdf26743e4e3a36212504",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291141,
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
      "evaluated_at": 1760291141
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
  "sig": "95f4313dabada8c3bb70314a277f030f191f005c25213fb904b5d90a1b7748f2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021368470
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 29944656, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285763, 'matching_hash': 'a5ef2cf235167f67'}}}maly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.5, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6875376}}}