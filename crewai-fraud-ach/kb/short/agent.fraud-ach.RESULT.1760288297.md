```json
{
  "id": "51c92723357c864d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288297,
  "host_pid": "9e6742732c60:1",
  "hash": "23c1871d2b79988576d27556859229dfcdc422eee16d49034328d55360a250c1",
  "cid": "QmV123c1871d2b79988576d27556859229dfcdc422ee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288297,
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
      "evaluated_at": 1760288297
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
  "sig": "ca947273d2c88ec8cc6a0ece64b90c1ad4761ad9493521fee2ec092a309cb12d"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 122105150872647
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 641633574, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285763, 'matching_hash': 'f142eb53d77ea00a'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7209366}}}{'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9237211}}}