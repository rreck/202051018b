```json
{
  "id": "94b90598dd87fa43",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294609,
  "host_pid": "9e6742732c60:1",
  "hash": "ef43738b27884bdec45b0b570466df89fa2fd8866c52720365f34841dd47e615",
  "cid": "QmV1ef43738b27884bdec45b0b570466df89fa2fd886",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294609,
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
      "evaluated_at": 1760294609
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
  "sig": "58e75736e5d6f6945e589d5a699d582d54ecd38ccc12f98563cffaf2b326db29"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021173532
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 74292829, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': 'a0cc7134a86fdd26'}}}