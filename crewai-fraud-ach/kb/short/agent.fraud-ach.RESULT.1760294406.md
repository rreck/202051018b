```json
{
  "id": "ea1e76f108a47e86",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294406,
  "host_pid": "9e6742732c60:1",
  "hash": "536b10841e51e9196f324fa68dcd7166e6e4985b41e048b130aa7810a5663313",
  "cid": "QmV1536b10841e51e9196f324fa68dcd7166e6e4985b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294406,
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
      "evaluated_at": 1760294406
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
  "sig": "9afd7b2b15c119194e3bc86294894f643e1f6a26a01ed638c7e340ef5b44b644"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029265266
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 87001041, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285764, 'matching_hash': 'a9619dd56a360910'}}}