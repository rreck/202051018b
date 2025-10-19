```json
{
  "id": "7239e63e0afb90ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292694,
  "host_pid": "9e6742732c60:1",
  "hash": "ad73de57258f68dd5c78298b83a4850e4e80f5060e1e76f731c063442fed0797",
  "cid": "QmV1ad73de57258f68dd5c78298b83a4850e4e80f506",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292694,
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
      "evaluated_at": 1760292694
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
  "sig": "1b1eef93b58a49b7412c863af6f2a70964205b7058ba71a7e447462a48f5d925"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154787030
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 89257070, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285764, 'matching_hash': '945ae0d1ce138c7f'}}}