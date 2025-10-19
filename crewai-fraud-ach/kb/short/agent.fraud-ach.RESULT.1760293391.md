```json
{
  "id": "7b4d668b41e9193c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293391,
  "host_pid": "9e6742732c60:1",
  "hash": "9957b7ecafb3ef0e21c7555bc408997375da35b4e96f3eea9e89d60cdc725b6b",
  "cid": "QmV19957b7ecafb3ef0e21c7555bc408997375da35b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293391,
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
      "evaluated_at": 1760293391
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
  "sig": "38717ab7e0980404da48d5f384df86354764a58a10b0a44a5d5cfe0ab15ac0f5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592654855
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 65521631, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285765, 'matching_hash': '0ed93ea6dd0046b6'}}}