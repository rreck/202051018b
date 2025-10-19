```json
{
  "id": "0d1a94a67018dc1d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291276,
  "host_pid": "9e6742732c60:1",
  "hash": "cae89db05715f14ac30c175b8559e411016fabe02933a02b0b3b72f3c486def8",
  "cid": "QmV1cae89db05715f14ac30c175b8559e411016fabe0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291276,
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
      "evaluated_at": 1760291276
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
  "sig": "936fce38eba9a611b129f7c87268cb386a8a51d716358673982ac5922f5e8150"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240708140
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 18248607, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285763, 'matching_hash': 'e22b1a9baac54cae'}}}