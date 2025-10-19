```json
{
  "id": "70c7fefb981b73b1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290707,
  "host_pid": "9e6742732c60:1",
  "hash": "75112ed28932c8031bd2f8f292bc735acf177aa3efcadf3b37230100f1d1a987",
  "cid": "QmV175112ed28932c8031bd2f8f292bc735acf177aa3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290707,
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
      "evaluated_at": 1760290707
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
  "sig": "1475f976fcff76b1f16d00697c6cc46f91e74f62e405661d16121d46ea830e12"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466272908
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 58769967, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285765, 'matching_hash': 'c5e3c9a8e5c19188'}}}