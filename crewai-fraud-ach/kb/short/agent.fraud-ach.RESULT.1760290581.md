```json
{
  "id": "1a401dadc1ef544f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290581,
  "host_pid": "9e6742732c60:1",
  "hash": "f8e45b93cc8ca08fb8306afcecb7dbed279ee3ba89bf29008ecd8db670cb7b48",
  "cid": "QmV1f8e45b93cc8ca08fb8306afcecb7dbed279ee3ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290581,
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
      "evaluated_at": 1760290581
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
  "sig": "f10549138962477dda40794b00dca3440e2f568bd81ddcdff7413cf6ab5d0047"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021715081
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 35193004, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285764, 'matching_hash': '0ea9b1b5c7891ffe'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '498752220', 'validation_error': 'Invalid routing number checksum'}}}