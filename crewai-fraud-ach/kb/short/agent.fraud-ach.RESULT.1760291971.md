```json
{
  "id": "07341d839297bc6e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291971,
  "host_pid": "9e6742732c60:1",
  "hash": "37c89cbbd84e2c83220531480405ecdad4df0bfd6e35d9f5640fa05695527486",
  "cid": "QmV137c89cbbd84e2c83220531480405ecdad4df0bfd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291971,
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
      "evaluated_at": 1760291971
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
  "sig": "812368c6a4d8f6e4e66c8b6c719ce7dd9042c37d54aea08e59119bf2ab33ae62"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023553215
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 73229013, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': '85da211728f5a38f'}}}