```json
{
  "id": "c64c7d9540e38e8d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289020,
  "host_pid": "9e6742732c60:1",
  "hash": "9f344825a28960580a538381200264e37b88cb2044af5023b339360dda2aa122",
  "cid": "QmV19f344825a28960580a538381200264e37b88cb20",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289020,
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
      "evaluated_at": 1760289020
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
  "sig": "4bf962099f554fd6cd69d6c44ce2a6ad80c659fb7e69e2f2385a56e70127c4dc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153839048
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 19302789, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285764, 'matching_hash': '20b3840d87952e5c'}}}