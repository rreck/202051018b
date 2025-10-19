```json
{
  "id": "3160eb5a1c800652",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292481,
  "host_pid": "9e6742732c60:1",
  "hash": "fb9f75ec5054efaa3ae6c596ab7faa9c6764f4c7b6a50cf4a7eaf7a175ffa4e4",
  "cid": "QmV1fb9f75ec5054efaa3ae6c596ab7faa9c6764f4c7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292481,
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
      "evaluated_at": 1760292481
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
  "sig": "9a68bb711c177feb600fda28c4f36c802665d969a578e8df29f36d9cb0570933"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150171825
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 37217862, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285765, 'matching_hash': 'da3473f59eec3040'}}}