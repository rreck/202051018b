```json
{
  "id": "a3bb8a4866438d37",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291039,
  "host_pid": "9e6742732c60:1",
  "hash": "2a0045975c5df59cadb16048cf0b5431784199a050ccc3486abf91513b84cab8",
  "cid": "QmV12a0045975c5df59cadb16048cf0b5431784199a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291039,
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
      "evaluated_at": 1760291039
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
  "sig": "c0ad76dd516202b2ee168574a7a272c71b94d7fa9c229e68f371993d90c34803"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025824799
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 42941580, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285765, 'matching_hash': 'f20c8e7a7a7e0174'}}}