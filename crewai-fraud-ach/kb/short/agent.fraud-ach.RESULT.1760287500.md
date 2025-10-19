```json
{
  "id": "b4dd71fe4c445217",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287500,
  "host_pid": "9e6742732c60:1",
  "hash": "138e764a484fed0c01176ecc694098e9712b2a1e93008d354151de650b5a5e39",
  "cid": "QmV1138e764a484fed0c01176ecc694098e9712b2a1e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287500,
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
      "evaluated_at": 1760287500
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
  "sig": "ef0e771f5134b0b75e5748c4082294eb8c566cc3f15487bab86bafe47934d3e8"
}
```

Fraud detected: duplicate_transaction (score: 79)
Transaction: 121000249867755
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760285765, 'matching_hash': '3e6b26eb59ce898a'}}}