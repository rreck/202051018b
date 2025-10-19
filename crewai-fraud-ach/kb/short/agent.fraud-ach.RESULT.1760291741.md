```json
{
  "id": "13a4787fbef68be6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291741,
  "host_pid": "9e6742732c60:1",
  "hash": "3e60573eda6734a7f9d075811fe6d8126950373e26f1fda41a280e66ee1befed",
  "cid": "QmV13e60573eda6734a7f9d075811fe6d8126950373e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291741,
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
      "evaluated_at": 1760291741
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
  "sig": "5f1ba64cbd7992f7923e9cb6ecb04b2d7c6a2d94c6539b02aad0b5ff206f6819"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596363200
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 69472676, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285764, 'matching_hash': 'b9f8fedd6c477a32'}}}