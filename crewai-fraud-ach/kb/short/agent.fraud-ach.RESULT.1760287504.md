```json
{
  "id": "9fe3f5d04505ad3b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287504,
  "host_pid": "9e6742732c60:1",
  "hash": "684ad425ec858a89bfcad2df2df25c14b96aad7b91e9dce18ac08174b0d395bc",
  "cid": "QmV1684ad425ec858a89bfcad2df2df25c14b96aad7b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287504,
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
      "evaluated_at": 1760287504
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
  "sig": "5443e5aae2691a30c1558079076785d0b3edb3c431f88a19aa91fcb92add7ed9"
}
```

Fraud detected: duplicate_transaction (score: 79)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50, 'total_amount': 19731376, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}