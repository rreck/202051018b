```json
{
  "id": "63321261d212f5ae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286181,
  "host_pid": "9e6742732c60:1",
  "hash": "b93705b687bcf47f5bb114c96c8156edaf47d827f703c3628e85479d7b0f307b",
  "cid": "QmV1b93705b687bcf47f5bb114c96c8156edaf47d827",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286181,
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
      "evaluated_at": 1760286181
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
  "sig": "646bad18f077318231b81654a2d899e818ddf1635909e9687cf3690a2404b5fb"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000037000939
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285763, 'matching_hash': '56ce6d7e55b84807'}}}re': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285764, 'matching_hash': '37b4044b8dabc650'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6602570}}}