```json
{
  "id": "e96a66cb0ea35b8f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291372,
  "host_pid": "9e6742732c60:1",
  "hash": "93ac1786a4fa5dddd11628f9ff5e59b946f1699cfdad07a55ff44ccd646842d2",
  "cid": "QmV193ac1786a4fa5dddd11628f9ff5e59b946f1699c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291372,
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
      "evaluated_at": 1760291372
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
  "sig": "582528370748b4f83d0659f2687d55c4953ecb6a3aece5f88ffec6b78ecc5002"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 021000026312877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 975513957, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285764, 'matching_hash': 'b3443459d853f7b8'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5638809}}}