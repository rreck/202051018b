```json
{
  "id": "cff0d2624036cf02",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285867,
  "host_pid": "9e6742732c60:1",
  "hash": "402b9a6e385d6cc1d0407780d5e5332a031e651f8533a89167da6bd4ef746704",
  "cid": "QmV1402b9a6e385d6cc1d0407780d5e5332a031e651f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285867,
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
      "evaluated_at": 1760285867
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
  "sig": "81ebc47fc8c48d53916e7f1399b54577549a64dc45a94cfd68d7d4b9999f0873"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000028017264
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 5, 'first_seen': 1760285763, 'matching_hash': '707a4137bac9b143'}}}