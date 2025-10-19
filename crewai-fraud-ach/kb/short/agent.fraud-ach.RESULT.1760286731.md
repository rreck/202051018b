```json
{
  "id": "8e52a6800aa993ff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286731,
  "host_pid": "9e6742732c60:1",
  "hash": "5dc305a10fc2f7e3e09a304643ba708f72b7ddfd3b4d98ac2efaf5e0616717fd",
  "cid": "QmV15dc305a10fc2f7e3e09a304643ba708f72b7ddfd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286731,
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
      "evaluated_at": 1760286731
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
  "sig": "21d09de1ab2ddec1d859deddfd8aa4e534e62b03e98c6346021eebbcd63404c0"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000023546405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15082445, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285763, 'matching_hash': '22f38bfa79b47563'}}}