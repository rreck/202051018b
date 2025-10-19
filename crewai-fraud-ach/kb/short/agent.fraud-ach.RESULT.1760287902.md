```json
{
  "id": "9c3d05b9e3a57ecc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287902,
  "host_pid": "9e6742732c60:1",
  "hash": "aec81006796609adc020472471bbfadf7853944f951e9a3c67baa8ac38bc5a4a",
  "cid": "QmV1aec81006796609adc020472471bbfadf7853944f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287902,
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
      "evaluated_at": 1760287902
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
  "sig": "6b46cb699d6eb8093de11888d1656a52b783d117bbc373aa689dc94bc848767a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599876575
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50, 'total_amount': 23727808, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285764, 'matching_hash': '0131e24faef32fc6'}}}}}