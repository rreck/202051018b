```json
{
  "id": "604687a31671da29",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291238,
  "host_pid": "9e6742732c60:1",
  "hash": "d36d520c26d8bc7396d6510574647c589bce5f3e9e95ee370424470020dcb756",
  "cid": "QmV1d36d520c26d8bc7396d6510574647c589bce5f3e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291238,
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
      "evaluated_at": 1760291238
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
  "sig": "adc05872ff2130cda09f29f69718658f64793d90d686fa767b3a486d46f3a06f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035025346
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 27340930, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285763, 'matching_hash': 'a8a877b5861d69af'}}}