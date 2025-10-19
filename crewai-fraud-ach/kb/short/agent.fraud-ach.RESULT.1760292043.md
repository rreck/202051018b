```json
{
  "id": "a3bbf9993a094e98",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292043,
  "host_pid": "9e6742732c60:1",
  "hash": "92f9a542535233e30f968c07710efa579f57699b22191370e736535c4a731d1e",
  "cid": "QmV192f9a542535233e30f968c07710efa579f57699b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292043,
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
      "evaluated_at": 1760292043
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
  "sig": "04fc6f480f8b2a2ea6109d2bbf4fc7691fa5fcb74250126fb0d9b2c9990a82eb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247065619
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 75574863, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285763, 'matching_hash': '73a93f9011d99735'}}}