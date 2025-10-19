```json
{
  "id": "7ed0af52d01753f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289037,
  "host_pid": "9e6742732c60:1",
  "hash": "98787530ccade9041b83cf62b4f4fe2585325ce11e2cd0b0a69b58b17c383a7e",
  "cid": "QmV198787530ccade9041b83cf62b4f4fe2585325ce1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289037,
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
      "evaluated_at": 1760289037
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
  "sig": "5ab4761b6cd77872f4cfaa153eb3ceaf3cb9d703ccc7af39fc6baadd3d7c0200"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 35325528, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}