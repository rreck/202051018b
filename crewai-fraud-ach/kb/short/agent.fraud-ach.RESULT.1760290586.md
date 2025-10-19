```json
{
  "id": "3aa1bf339722774b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290586,
  "host_pid": "9e6742732c60:1",
  "hash": "0b0628401cfd11c532195cdd7f33f5a1f10bc33439435f50547821cafa10bc5e",
  "cid": "QmV10b0628401cfd11c532195cdd7f33f5a1f10bc334",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290586,
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
      "evaluated_at": 1760290586
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
  "sig": "c6b6bea6cdcc9c01df672716723c3c131febd846ae9431b48cfddc3b3e5c5f4c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035410213
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 59285534, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285763, 'matching_hash': '3fae4375ff781af3'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}