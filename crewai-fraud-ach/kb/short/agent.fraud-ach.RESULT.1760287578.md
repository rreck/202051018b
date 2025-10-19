```json
{
  "id": "89421cadb0fe12e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287578,
  "host_pid": "9e6742732c60:1",
  "hash": "21b48b9d37bc7ed2fb9d653d666ace0fc7a37489ca508b26e74bd938773b042d",
  "cid": "QmV121b48b9d37bc7ed2fb9d653d666ace0fc7a37489",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287578,
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
      "evaluated_at": 1760287578
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
  "sig": "6549345a63d1adcbf3f00fb99d9d64c77a6a3cdd243ded2d76830c83fefe9704"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 026009592616863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285764, 'matching_hash': '1f69fcd8882944a6'}}}een': 1760285763, 'matching_hash': '5c99a38661a1ddcd'}}}