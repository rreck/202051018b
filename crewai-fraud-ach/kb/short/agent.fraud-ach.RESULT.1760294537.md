```json
{
  "id": "7fd920e71686e172",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294537,
  "host_pid": "9e6742732c60:1",
  "hash": "71801c5bbcadb24e0ea48bff52bbe02db85ad95f229b78c65c5e6d283dd6b748",
  "cid": "QmV171801c5bbcadb24e0ea48bff52bbe02db85ad95f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294537,
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
      "evaluated_at": 1760294537
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
  "sig": "9d31f332b856c5bdf9a206427fb78a1af409ab29cd0c372fd33c708da1f30253"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463831807
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 43266000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': 'ac2384e4a351cc1b'}}}