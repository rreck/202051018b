```json
{
  "id": "af28f3bbfc304dbf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292022,
  "host_pid": "9e6742732c60:1",
  "hash": "a30e6a1460e9de2f4c551085af61156ac95fcfc5caf8b7962a0f621e3c03cc51",
  "cid": "QmV1a30e6a1460e9de2f4c551085af61156ac95fcfc5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292022,
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
      "evaluated_at": 1760292022
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
  "sig": "29c860258a5fe864ab25777582c0b99d6fb250cd2ce886bf0601943d1d1c6120"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 031201467532863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 1036695732, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285764, 'matching_hash': 'b320222423bba5e6'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5514339}}}