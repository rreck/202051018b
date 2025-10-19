```json
{
  "id": "1efbf9f99d976eaf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293836,
  "host_pid": "9e6742732c60:1",
  "hash": "d718ef32f82b11117a7e3abce5d7bf18772e73e64284268597bdbf61f090f34c",
  "cid": "QmV1d718ef32f82b11117a7e3abce5d7bf18772e73e6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293836,
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
      "evaluated_at": 1760293836
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
  "sig": "37dc1327d692ab884e12ccbf9042f78a40001ec33685062d873e5506cf105847"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152922139
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 45193672, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285765, 'matching_hash': '36c7f170a3aff02c'}}}