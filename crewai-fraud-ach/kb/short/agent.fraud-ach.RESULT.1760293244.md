```json
{
  "id": "c508bbdc836781b1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293244,
  "host_pid": "9e6742732c60:1",
  "hash": "152607eabd8f106fcf9a463370edd023d0407f0af8a8f476bd52439c35d531b3",
  "cid": "QmV1152607eabd8f106fcf9a463370edd023d0407f0a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293244,
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
      "evaluated_at": 1760293244
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
  "sig": "70e8160cc0ed471c3eb159cc6266228a1ad3c1454c84e694584dcfad26d0e28a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025824799
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 55693928, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285765, 'matching_hash': 'f20c8e7a7a7e0174'}}}