```json
{
  "id": "9976fe2bec0061f7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294751,
  "host_pid": "9e6742732c60:1",
  "hash": "d03fb207bff7c29bb7518a7e7de1a3f354288bf2212745e12b3f484a12f928cc",
  "cid": "QmV1d03fb207bff7c29bb7518a7e7de1a3f354288bf2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294751,
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
      "evaluated_at": 1760294751
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
  "sig": "6700717cbb48d269d8706dee07f2ca5e1b275f8e4776122c6fbbdb2ddbb36226"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150868994
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 101117748, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': '612406b6271445a9'}}}