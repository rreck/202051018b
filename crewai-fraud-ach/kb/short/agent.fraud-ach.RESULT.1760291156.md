```json
{
  "id": "0ec3f11d615e502e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291156,
  "host_pid": "9e6742732c60:1",
  "hash": "f96080eda52a51d3379677eedf73c3d338b8776c022017423ea59a3b031cd4b3",
  "cid": "QmV1f96080eda52a51d3379677eedf73c3d338b8776c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291156,
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
      "evaluated_at": 1760291156
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
  "sig": "d8c4761c5329eef70cc1567ab88138fb4311c6b6b3138437aedae6fb614be4ac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023360084
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 30052512, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285763, 'matching_hash': 'bfec758d4b349e38'}}}