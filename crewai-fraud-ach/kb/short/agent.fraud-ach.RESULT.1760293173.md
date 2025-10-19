```json
{
  "id": "252ff1819a14d175",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293173,
  "host_pid": "9e6742732c60:1",
  "hash": "1a0987dbb29bbba91788a5cd124d5bbc8c5a2d1255d14fb4120ece924d0ff7cb",
  "cid": "QmV11a0987dbb29bbba91788a5cd124d5bbc8c5a2d12",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293173,
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
      "evaluated_at": 1760293173
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
  "sig": "385a75510b6dd84de16380aee7415d6cbf0c9b7fea5d3c979764142cb5b68ca3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032435684
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 23689434, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': '191acc35d8c1baac'}}}