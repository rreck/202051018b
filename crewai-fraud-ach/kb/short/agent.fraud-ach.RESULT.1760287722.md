```json
{
  "id": "1a66bfc309094080",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287722,
  "host_pid": "9e6742732c60:1",
  "hash": "20ecb48860f59a10dfa943039edd69140372d6bcdb4dfb134d8f5cfd529cad12",
  "cid": "QmV120ecb48860f59a10dfa943039edd69140372d6bc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287722,
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
      "evaluated_at": 1760287722
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
  "sig": "cd6c317bbee8fa6ececdbe0f421d67e9bb5ea86edb5cff374b4772567bd35f97"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 026009595571766
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50, 'total_amount': 34410530, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285763, 'matching_hash': '7b9b43f48a0de4d3'}}}