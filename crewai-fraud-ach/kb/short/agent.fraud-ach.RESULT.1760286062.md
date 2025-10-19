```json
{
  "id": "5c4ac384d032b6de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286062,
  "host_pid": "9e6742732c60:1",
  "hash": "5af993833467159b3a46c9bab85812130c4e2183fa2ecdd11e504c934ee83eaa",
  "cid": "QmV15af993833467159b3a46c9bab85812130c4e2183",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286062,
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
      "evaluated_at": 1760286062
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
  "sig": "8af1b265fb9dbf25e5220e26a5054a640fc76098cdc0576fdbe162e01b8d7997"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000036013549
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285763, 'matching_hash': 'f1471db42dbf1c81'}}}