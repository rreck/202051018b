```json
{
  "id": "8b905f06f2f398ee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286462,
  "host_pid": "9e6742732c60:1",
  "hash": "250422e286d44c017ee3db97e9c01947a0b50caa78667de8002d8040d271bb17",
  "cid": "QmV1250422e286d44c017ee3db97e9c01947a0b50caa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286462,
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
      "evaluated_at": 1760286462
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
  "sig": "c67be968a594b6bd0c053fd1e88042277f3ea5ae125eaeb551fba3c5cd817cdc"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000023924602
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10463778, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285764, 'matching_hash': '8a38ff5636f784bb'}}}760284979, 'matching_hash': '76eefa6b67e55304'}}}