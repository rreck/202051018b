```json
{
  "id": "0e54b4387cd6002b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294224,
  "host_pid": "9e6742732c60:1",
  "hash": "f04da25ca602ab2f7d4fff7975b0cc67342cafe337b873fdfbfb9f2fc2410089",
  "cid": "QmV1f04da25ca602ab2f7d4fff7975b0cc67342cafe3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294224,
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
      "evaluated_at": 1760294224
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
  "sig": "75e36780b9c26483d8cb99f0f3c154ea6e1f0e486653692585ba26568c315bf6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030591378
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 68093064, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': 'a57eaa69ddfb92ca'}}}