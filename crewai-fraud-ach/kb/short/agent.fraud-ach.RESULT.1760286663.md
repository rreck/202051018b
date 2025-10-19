```json
{
  "id": "dad48d17304decee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286663,
  "host_pid": "9e6742732c60:1",
  "hash": "c39423f8b7220045a894bc6d10b983c09d03012dec7b6cc218ec90ce184768fa",
  "cid": "QmV1c39423f8b7220045a894bc6d10b983c09d03012d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286663,
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
      "evaluated_at": 1760286663
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
  "sig": "6b62a7adeaad27f62620b5074e3ac391730944fcaedf4ffc026c144396c89ecc"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000025159939
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15570456, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285763, 'matching_hash': 'bd88da65ef85df29'}}}