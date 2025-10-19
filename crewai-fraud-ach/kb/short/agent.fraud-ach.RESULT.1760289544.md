```json
{
  "id": "d8d57678af78a282",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289544,
  "host_pid": "9e6742732c60:1",
  "hash": "4687544e17350467f76a04577def67b5fca1b9b185ed0535f1c9861af87cd5b8",
  "cid": "QmV14687544e17350467f76a04577def67b5fca1b9b1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289544,
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
      "evaluated_at": 1760289544
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
  "sig": "551d26023158e0bc82d990d31415035980a15e34cb9f43f750e6df5c82b365c5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156872006
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 10839402, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285763, 'matching_hash': '001baa6337a96952'}}}