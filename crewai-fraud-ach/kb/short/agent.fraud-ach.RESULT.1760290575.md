```json
{
  "id": "81d812597b1d612f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290575,
  "host_pid": "9e6742732c60:1",
  "hash": "30ba17040178cf51e39d9108dfaea39ec267bc21099276652c3f8f280e7318a8",
  "cid": "QmV130ba17040178cf51e39d9108dfaea39ec267bc21",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290575,
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
      "evaluated_at": 1760290575
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
  "sig": "23793490516a24945a67526e736fcd18de4b69d41d161fea7d3370732485e53b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270157641
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 54984314, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285763, 'matching_hash': 'c979b8e092a32979'}}}