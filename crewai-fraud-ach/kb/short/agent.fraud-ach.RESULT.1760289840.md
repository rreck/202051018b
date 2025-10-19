```json
{
  "id": "8d3fc67135184ccd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289840,
  "host_pid": "9e6742732c60:1",
  "hash": "acc897c5f8999d9bd99c29a136a4fc537fcd0151f3f9bcb37d651107ffd8b60a",
  "cid": "QmV1acc897c5f8999d9bd99c29a136a4fc537fcd0151",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289840,
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
      "evaluated_at": 1760289840
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
  "sig": "61a1c264996039c5826f4b624c3056a558b962f3bc81cd9b7adc9a01d34d0f39"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028970082
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 38012450, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285765, 'matching_hash': 'a98af89fc7548453'}}}