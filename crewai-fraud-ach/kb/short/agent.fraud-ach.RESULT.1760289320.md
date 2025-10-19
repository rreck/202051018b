```json
{
  "id": "1a989461a3f6f845",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289320,
  "host_pid": "9e6742732c60:1",
  "hash": "12e73f9f748941e9f3dea516d3c0d76f97473c75cb749f090b84f26edcd7588d",
  "cid": "QmV112e73f9f748941e9f3dea516d3c0d76f97473c75",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289320,
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
      "evaluated_at": 1760289320
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
  "sig": "843736df8c8516c414ef5451361ae18bef4b749a953cad56f00aad8f4a131d9f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035229494
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 17347560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285763, 'matching_hash': '565398b77a50d0ac'}}}