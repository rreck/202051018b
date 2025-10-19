```json
{
  "id": "7816f6e6e1096921",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293716,
  "host_pid": "9e6742732c60:1",
  "hash": "7f8aaf36291b8c3e17f562ef386f4b21c412c0eab75709d5d4bcb88beedd027e",
  "cid": "QmV17f8aaf36291b8c3e17f562ef386f4b21c412c0ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293716,
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
      "evaluated_at": 1760293716
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
  "sig": "030201d3e03c2e71d371777c9eaf55407c565a2fd49176d89b37e09c98b5aeac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273021249
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 108022880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285764, 'matching_hash': '8f9c0aaacb6951b9'}}}