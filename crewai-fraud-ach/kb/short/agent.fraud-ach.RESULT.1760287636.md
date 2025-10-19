```json
{
  "id": "54d7023e878496f2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287636,
  "host_pid": "9e6742732c60:1",
  "hash": "d11091f36d7102d5ba5e86bb9186bbc06de2d1a491b6976a158d03ef282a70f5",
  "cid": "QmV1d11091f36d7102d5ba5e86bb9186bbc06de2d1a4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287636,
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
      "evaluated_at": 1760287636
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
  "sig": "d986a48ddf34a8d366d0b136b4c75d0bcef92a4effab43d4f82c69b49766bd6a"
}
```

Fraud detected: duplicate_transaction (score: 84)
Transaction: 031201461869062
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50, 'total_amount': 33284595, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760285763, 'matching_hash': '24ed6b728fb62d75'}}}}}}