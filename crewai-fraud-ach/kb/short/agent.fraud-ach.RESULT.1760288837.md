```json
{
  "id": "194d9f8f7c50015c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288837,
  "host_pid": "9e6742732c60:1",
  "hash": "d1e9e575689fe8f6928ec9168629b6f03962e88e88e659cd12c520fa9e708a4c",
  "cid": "QmV1d1e9e575689fe8f6928ec9168629b6f03962e88e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288837,
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
      "evaluated_at": 1760288837
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
  "sig": "e4e217fea8605db9c31143afd3b7d186fba0af5bf8cc05b1088603a901539121"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50, 'total_amount': 33416040, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}