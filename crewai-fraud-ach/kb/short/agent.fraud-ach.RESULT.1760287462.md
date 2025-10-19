```json
{
  "id": "54d5e26c9ad0409e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287462,
  "host_pid": "9e6742732c60:1",
  "hash": "b49ac580a1d8b71b253faa63f8dfda3664587993559175eb508057e0d1785e17",
  "cid": "QmV1b49ac580a1d8b71b253faa63f8dfda3664587993",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287462,
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
      "evaluated_at": 1760287462
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
  "sig": "44877b83013594af8b45df67fd518237074aa8314a9da130c2a88ca420d791dc"
}
```

Fraud detected: duplicate_transaction (score: 78)
Transaction: 121000247109361
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760285763, 'matching_hash': '3efad933d2b7f9bd'}}}een': 1760285764, 'matching_hash': '75b6b5cd12274a09'}}}