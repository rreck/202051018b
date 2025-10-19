```json
{
  "id": "d2a41296d6f2fac5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289255,
  "host_pid": "9e6742732c60:1",
  "hash": "3d0531075300a2dd14560e7c1d392d361ea9e3b89ba602e357b187a38f52e769",
  "cid": "QmV13d0531075300a2dd14560e7c1d392d361ea9e3b8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289255,
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
      "evaluated_at": 1760289255
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
  "sig": "9753e3efa7b316fc325376fb5b5f1d62bb978721a382e11cc922c794322f9067"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036907843
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 36373736, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285763, 'matching_hash': '5c57e03938e1b0ed'}}}