```json
{
  "id": "f6080c71c7548061",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290389,
  "host_pid": "9e6742732c60:1",
  "hash": "138942f03471fa9dedcf2ddca9bce88d4ac8c93c5216d6d468588674cc81d662",
  "cid": "QmV1138942f03471fa9dedcf2ddca9bce88d4ac8c93c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290389,
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
      "evaluated_at": 1760290389
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
  "sig": "52bd2de7d0f6200dca06d9e0a4d40f36585d523dd71d756e90fcc0cbd3d1a041"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271528987
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 60645235, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285763, 'matching_hash': '52a7e62e45a672d0'}}}