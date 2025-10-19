```json
{
  "id": "52828bc84deb12b7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289273,
  "host_pid": "9e6742732c60:1",
  "hash": "eea41347a74adcb9a6c0722f36a01694c7a1be32ab6c8155e9b402a4ba6fe649",
  "cid": "QmV1eea41347a74adcb9a6c0722f36a01694c7a1be32",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289273,
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
      "evaluated_at": 1760289273
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
  "sig": "78eda0a96b7753a47c8fb60ba0ae2902ec0a349403f8d25cd2cd0964f4744951"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039495479
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 48090192, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285765, 'matching_hash': 'bbfd7bc59c80a282'}}}