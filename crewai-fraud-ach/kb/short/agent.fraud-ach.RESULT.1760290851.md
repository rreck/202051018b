```json
{
  "id": "169caace19b426bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290851,
  "host_pid": "9e6742732c60:1",
  "hash": "06363d9350024fedfc2bd9363f9674bfab2088f5db6ca59efbd1af5b049eea2f",
  "cid": "QmV106363d9350024fedfc2bd9363f9674bfab2088f5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290851,
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
      "evaluated_at": 1760290851
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
  "sig": "2b63c01b5d17dda611ec8240600ea21ab431e22ae8684c04119f75dade903a78"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274159227
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 20193264, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285763, 'matching_hash': 'c6403d45da933f2b'}}}