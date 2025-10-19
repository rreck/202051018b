```json
{
  "id": "23d215c4b7f3d840",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287109,
  "host_pid": "9e6742732c60:1",
  "hash": "462be499f4bb421327d5349e291dbef9f09ea0fedfdeda8ffc69ac3de2910502",
  "cid": "QmV1462be499f4bb421327d5349e291dbef9f09ea0fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287109,
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
      "evaluated_at": 1760287109
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
  "sig": "1b6f185f8dbdddf13001a87664dd1cb63aa3c1c955f4b24ce7811d15ac547827"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201469832017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15002448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760285765, 'matching_hash': '99e095073411ccc4'}}}