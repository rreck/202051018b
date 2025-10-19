```json
{
  "id": "6d0ae2405dfbca02",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294046,
  "host_pid": "9e6742732c60:1",
  "hash": "b72e256b50785286da2ebd1d5cf5d1142a1bf33606dd42e6d34947ecbf028f04",
  "cid": "QmV1b72e256b50785286da2ebd1d5cf5d1142a1bf336",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294046,
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
      "evaluated_at": 1760294046
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
  "sig": "59814b3a465d5db031c4af1da1226a8ffadb5d86a231d60db06aea601c9c4edf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462408143
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 111833590, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285765, 'matching_hash': '36407d3e627869a5'}}}