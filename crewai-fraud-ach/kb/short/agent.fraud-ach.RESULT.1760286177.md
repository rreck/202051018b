```json
{
  "id": "bee03dedf0ec8817",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286177,
  "host_pid": "9e6742732c60:1",
  "hash": "1927fe313c730fb4ce12097a95448f79718eb5a400cc34a92922473502eeaed1",
  "cid": "QmV11927fe313c730fb4ce12097a95448f79718eb5a4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286177,
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
      "evaluated_at": 1760286177
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "119603552384e251e3ad1faa0ebf5b10f6b510ab125a371917eba39f085e7f1c"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 021000025310959
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 129607592, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285763, 'matching_hash': 'c7c98ba146578274'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7623976}}}