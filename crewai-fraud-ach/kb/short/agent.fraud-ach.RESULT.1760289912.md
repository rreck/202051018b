```json
{
  "id": "d4fbc6dc54ad434d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289912,
  "host_pid": "9e6742732c60:1",
  "hash": "49b22531df3b2aadd6bcdd21d230ad15bbba4e6594bac8b7420a5fda551133f5",
  "cid": "QmV149b22531df3b2aadd6bcdd21d230ad15bbba4e65",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289912,
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
      "evaluated_at": 1760289912
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
  "sig": "cd7b98197c56ecddf1ac739ee98d0d5f5b0ef5410464e0ba7520b1451395c4b9"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 026009595707011
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 936443232, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285765, 'matching_hash': 'bce5819bd1402454'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.51, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6885612}}}