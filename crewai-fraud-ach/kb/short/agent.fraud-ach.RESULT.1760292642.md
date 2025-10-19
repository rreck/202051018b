```json
{
  "id": "acc8c9d94b6f0f74",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292642,
  "host_pid": "9e6742732c60:1",
  "hash": "846cda784c244bacc3a85817727cf2475e2ce84ac75a77239fb5b867840a363b",
  "cid": "QmV1846cda784c244bacc3a85817727cf2475e2ce84a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292642,
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
      "evaluated_at": 1760292642
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
  "sig": "f7f61a622542bc72967410cecbca5a1fab3efb350469b474d8b338ee17f9dd9f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030591378
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 58781192, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285763, 'matching_hash': 'a57eaa69ddfb92ca'}}}