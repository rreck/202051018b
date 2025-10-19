```json
{
  "id": "63ca016a18cb2009",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287163,
  "host_pid": "9e6742732c60:1",
  "hash": "501f082c2ee2d032385d54379344814be1d0bd75917bc44a8dda1005d4460ef8",
  "cid": "QmV1501f082c2ee2d032385d54379344814be1d0bd75",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287163,
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
      "evaluated_at": 1760287163
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "4cd126736fc35e2d8bf94e6b374a295a08141e3350d69cd4b7d2f46b7f86fd78"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000029278927
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14448700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285765, 'matching_hash': '45338af8ff50831c'}}}