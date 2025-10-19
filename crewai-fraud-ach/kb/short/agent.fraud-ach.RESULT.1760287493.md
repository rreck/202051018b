```json
{
  "id": "a9359e0300a3bd60",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287493,
  "host_pid": "9e6742732c60:1",
  "hash": "bf4e60b8391e316c2e760c76f84dacb1d7f965544e9bcd149f80104baf5d6033",
  "cid": "QmV1bf4e60b8391e316c2e760c76f84dacb1d7f96554",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287493,
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
      "evaluated_at": 1760287493
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "d3eb2d3905b7aae5655dfacadbfa8b98a7f22a769508ab471f42775184b04a4f"
}
```

Fraud detected: duplicate_transaction (score: 79)
Transaction: 031201464346208
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760285763, 'matching_hash': 'be0548ed0e4f6107'}}}764, 'matching_hash': '3d8553245e7f2b19'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6481360}}}