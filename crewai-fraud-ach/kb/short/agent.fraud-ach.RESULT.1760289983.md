```json
{
  "id": "cf3c6a67edee2a5b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289983,
  "host_pid": "9e6742732c60:1",
  "hash": "10841ccb3aded0dc6be5568605cfff555f966481d3c1118969542638d03c439f",
  "cid": "QmV110841ccb3aded0dc6be5568605cfff555f966481",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289983,
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
      "evaluated_at": 1760289983
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "205f8f5c2ae31859f7d4eeb658d387f0e4700c5703551f196d64dd0445480584"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 063100275328879
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 773452188, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285764, 'matching_hash': '9f5415d10b328afc'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5604726}}}