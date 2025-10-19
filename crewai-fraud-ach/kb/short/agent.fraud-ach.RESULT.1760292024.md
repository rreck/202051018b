```json
{
  "id": "c2a19acaee313946",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292024,
  "host_pid": "9e6742732c60:1",
  "hash": "60396ea88943f9d06dc424fdba7cf4bac45fd844c5c9ec95771fc0312eaad931",
  "cid": "QmV160396ea88943f9d06dc424fdba7cf4bac45fd844",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292024,
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
      "evaluated_at": 1760292024
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
  "sig": "b0666f47963620b5407e6237f5e63641cd67d09bf3e57f5dd729d67bccbf37fd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463882943
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 23313504, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285765, 'matching_hash': '0eb18222520b1d39'}}}