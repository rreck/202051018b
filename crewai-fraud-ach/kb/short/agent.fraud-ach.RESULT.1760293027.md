```json
{
  "id": "9550e3654784f74f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293027,
  "host_pid": "9e6742732c60:1",
  "hash": "db9a891e3e87dccbc0f8521e030ce9190aef1dbbeff58b888328d3409bfd54c4",
  "cid": "QmV1db9a891e3e87dccbc0f8521e030ce9190aef1dbb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293027,
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
      "evaluated_at": 1760293027
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
  "sig": "64f57c61f6a92e91634b22bb6db74de49ca2f6f4202e1c6b55c524cf0ab23b0b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241012804
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 57991500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285763, 'matching_hash': 'ba9ba43773b08e05'}}}}