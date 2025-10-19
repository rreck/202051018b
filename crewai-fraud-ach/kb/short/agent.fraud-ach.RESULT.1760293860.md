```json
{
  "id": "807376c5be008d3c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293860,
  "host_pid": "9e6742732c60:1",
  "hash": "2f1a14607fc385db55a2e5b4ef084d69009af55ba1dba21fc835f7d59c959a5a",
  "cid": "QmV12f1a14607fc385db55a2e5b4ef084d69009af55b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293860,
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
      "evaluated_at": 1760293860
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
  "sig": "188c6471a0ffe9ef0b32237d436028757402766eca262ce5f161d9fbf6da7c87"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028116675
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 77269665, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': '276303153292771e'}}}