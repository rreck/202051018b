```json
{
  "id": "e7215feb569b062e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289434,
  "host_pid": "9e6742732c60:1",
  "hash": "3e8cb6ebbb332f573697ef009a74d0c43c3a1c32115e9259f30891add965df91",
  "cid": "QmV13e8cb6ebbb332f573697ef009a74d0c43c3a1c32",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289434,
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
      "evaluated_at": 1760289434
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
  "sig": "5084f3c73b86c47314c5d5134350519d0f88bc4c5a539a6cae9e1909df04f255"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029233033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 51073782, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285763, 'matching_hash': 'f6bf3c76ea3935d9'}}}