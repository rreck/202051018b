```json
{
  "id": "eee38a196d940986",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289536,
  "host_pid": "9e6742732c60:1",
  "hash": "602a0e954742d9f37acda7a5a6953dbdb69357dfdfbe75c64aea4da64edeec56",
  "cid": "QmV1602a0e954742d9f37acda7a5a6953dbdb69357df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289536,
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
      "evaluated_at": 1760289536
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
  "sig": "06e15e4d7204e934bba5f95fd979c3b4de431c9aa09989a177ceb434d9e81f46"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248255202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 50794506, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285764, 'matching_hash': 'c66fc0c5e7caab92'}}}