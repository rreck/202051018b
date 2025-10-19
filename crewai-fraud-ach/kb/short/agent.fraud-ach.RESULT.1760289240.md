```json
{
  "id": "c571c9364c67d4e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289240,
  "host_pid": "9e6742732c60:1",
  "hash": "44bc4ec7fcc845814f6cf4492b4f8f530c05185ae1ea365e055df21190fde336",
  "cid": "QmV144bc4ec7fcc845814f6cf4492b4f8f530c05185a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289240,
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
      "evaluated_at": 1760289240
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
  "sig": "8693ceeef90688b2d9414204d871b8d3cfb8d297438883fab2fd77921344fa21"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 37235016, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}