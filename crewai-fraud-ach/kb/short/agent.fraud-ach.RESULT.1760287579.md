```json
{
  "id": "30091480bfda9e39",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287579,
  "host_pid": "9e6742732c60:1",
  "hash": "f98867f6f2883ab7c2c45bd6b149e45db02ce13a1dfdaae046a6a6a83bf66ab9",
  "cid": "QmV1f98867f6f2883ab7c2c45bd6b149e45db02ce13a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287579,
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
      "evaluated_at": 1760287579
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
  "sig": "b321201ca04b507858dbabdae43cd10c9bee6baeb315e4d086e531b616927789"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 021000025260373
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50, 'total_amount': 20203950, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285765, 'matching_hash': '6c25bdeba85ae9df'}}}