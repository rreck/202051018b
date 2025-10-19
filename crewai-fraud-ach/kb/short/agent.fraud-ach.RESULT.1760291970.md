```json
{
  "id": "f7152f8ffa54e818",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291970,
  "host_pid": "9e6742732c60:1",
  "hash": "a07a05cb0ece579532156b061ccf03c0521b59509f3adc681563a67039392bc8",
  "cid": "QmV1a07a05cb0ece579532156b061ccf03c0521b5950",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291970,
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
      "evaluated_at": 1760291970
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
  "sig": "17c5532e25fa138f4a0284c4a92ee420f99c8630015df70a7394c5653d8f4200"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021708552
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 40296256, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': 'ae7eac3388a12cfd'}}}}