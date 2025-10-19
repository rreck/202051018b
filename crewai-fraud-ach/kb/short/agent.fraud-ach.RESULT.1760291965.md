```json
{
  "id": "488f9853a53fcbd3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291965,
  "host_pid": "9e6742732c60:1",
  "hash": "b6fcc1dfdcb80eb4128b262865bd6bee1a4e507439090f7fde00929333452e01",
  "cid": "QmV1b6fcc1dfdcb80eb4128b262865bd6bee1a4e5074",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291965,
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
      "evaluated_at": 1760291965
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
  "sig": "12e74efc00bd8770c91e9ba97cd9d9fb5226fdc29a3ec5b9f1d3f8bf4e90e56f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240708140
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 19956079, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': 'e22b1a9baac54cae'}}}