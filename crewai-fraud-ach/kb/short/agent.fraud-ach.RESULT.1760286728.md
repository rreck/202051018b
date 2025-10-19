```json
{
  "id": "ad9f4abbf2079de6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286728,
  "host_pid": "9e6742732c60:1",
  "hash": "1027c4c4f70cb2a719ffbec1944e7845c3742fd3c589814b6d41260bbcb300df",
  "cid": "QmV11027c4c4f70cb2a719ffbec1944e7845c3742fd3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286728,
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
      "evaluated_at": 1760286728
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
  "sig": "ae56b5586354ca87624c75a30f883831c74d80568614d86142678351e4af3e84"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157375662
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 10948485, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760284979, 'matching_hash': '8218a7a652f8297c'}}}