```json
{
  "id": "d381b4187d189a54",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292497,
  "host_pid": "9e6742732c60:1",
  "hash": "dc3b68ca88c25f31629a771bb27536133baed62ac7e1d711edd8795813b58e79",
  "cid": "QmV1dc3b68ca88c25f31629a771bb27536133baed62a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292497,
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
      "evaluated_at": 1760292497
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
  "sig": "99f0b8d388fa4966b5c3051b26157d61594e8b7172f2ad715ba85d3885ec3fc0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023536829
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 27364291, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285763, 'matching_hash': 'cf71240b8169078c'}}}