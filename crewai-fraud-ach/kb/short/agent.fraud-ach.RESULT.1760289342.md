```json
{
  "id": "fdf8f4147009bd7d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289342,
  "host_pid": "9e6742732c60:1",
  "hash": "01f324b5e22aee086ca40b7c7344c05fd532f1bbf075f819a37527e57d3f5e35",
  "cid": "QmV101f324b5e22aee086ca40b7c7344c05fd532f1bb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289342,
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
      "evaluated_at": 1760289342
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
  "sig": "574c998864b0e535aa938cc19b30e199a127d3705d4a5f9795691872b764b2f4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274128098
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 49777920, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285765, 'matching_hash': 'e67ed82943972fb3'}}}