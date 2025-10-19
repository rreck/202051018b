```json
{
  "id": "21ad3fb04f305305",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286182,
  "host_pid": "9e6742732c60:1",
  "hash": "b4e8fabb465cdd55bf08f4dcdb8358bc91c177b104b7cbd82ef3be080b076406",
  "cid": "QmV1b4e8fabb465cdd55bf08f4dcdb8358bc91c177b1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286182,
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
      "evaluated_at": 1760286182
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
  "sig": "e61aae7a70627a987e80eb1fc7a07744fea7fb04eb11f8192449a1a83e998230"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201467394934
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285763, 'matching_hash': '227a4380e23ca7de'}}}